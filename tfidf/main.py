from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import math
import string 
import nltk
nltk.download('stopwords')
nltk.download('punkt')

corpus_pth='data/corpus'
input_pth='data/corpus/goose/Chinese goose.txt'


tokenizer=word_tokenize
stemmer=SnowballStemmer(language='english', ignore_stopwords=False)



import os
txt_file_pths=[]
for root, dirs, files in os.walk(corpus_pth, topdown=False):
   for name in files:
      txt_file_pths.append(os.path.join(root, name))

texts=[open(pth,'r').read() for pth in txt_file_pths]


def preprocessor(txt):
    tokens=[stemmer.stem(token.lower()) for token in tokenizer(txt) if token.isalnum()]
    return tokens

def tfidf(tok_doc, tok_corpus):
    doc_length=len(tok_doc)
    corpus_length=len(tok_corpus)

    #tf
    term_count=Counter(tok_doc)
    term_frequency={key:value/doc_length for key, value in term_count.items()}
    
    #idf
    inverse_doc_frequency={}
    for key in tok_doc:
        doc_frequency=0
        for doc in tok_corpus:
            if key in doc:
                doc_frequency+=1
        inverse_doc_frequency[key]=math.log(corpus_length/doc_frequency)
    
    #tfidf
    tfidf={}
    for key in tok_doc:
        tfidf[key]=term_frequency[key] * inverse_doc_frequency[key]
        
    return tfidf

def task1(corpus_pth, input_pth):
    
    #find all txt files
    txt_file_pths=[]
    for root, dirs, files in os.walk(corpus_pth, topdown=False):
       for name in files:
          txt_file_pths.append(os.path.join(root, name))
    
    #read them
    texts=[open(pth,'r').read() for pth in txt_file_pths]
    
    #preprocess them
    tok_corpus=[preprocessor(text) for text in texts]
    
    #read input doc
    tok_text=preprocessor(open(input_pth,'r').read())
    
    #calculate tfidf for each term
    tfidf_scores=tfidf(tok_text,tok_corpus)
    
    # extract top 10
    top_10=[(k,v) for k, v in sorted(tfidf_scores.items(), key=lambda item: item[1], reverse=True)][:10]
    
    #print top 10
    print(', '.join([k for k,v in top_10]))


def task2(text,tok_corpus):
    sentences=sent_tokenize(text)
    if len(sentences)<6:
        return text # da li treba spojit s razmakom ili samo text vratit 
    
    sent_scores=[]
    tok_text=preprocessor(text)
    tfidf_score=tfidf(tok_text, tok_corpus)
    
    for sent in sentences:
        tok_sent=preprocessor(sent)
        tfidfs=[tfidf_score[tok] for tok in tok_sent]
        tfidfs_top_10=sorted(tfidfs,reverse=True)[:10]
        sent_score=sum(tfidfs_top_10)

        sent_scores.append((sent,sent_score))
    
    sentences_result=[]
    for sent,val in sorted(sent_scores, key=lambda item: item[1], reverse=True)[:5]:
        sentences_result.append(sent)

    sentences_sorted=[]
    for sent in sentences:
        if sent in sentences_result:
            sentences_sorted.append(sent)
        
    print(' '.join(sentences_sorted))
    


tok_corpus=[preprocessor(text) for text in texts]
tfidf_scores=task1(corpus_pth,input_pth)
task2(open(input_pth,'r').read(), tok_corpus)   
