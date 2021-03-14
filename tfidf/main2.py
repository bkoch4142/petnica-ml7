from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import math
import nltk
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')


def preprocessor(txt):
    tokens=[stemmer.stem(token.lower()) for token in tokenizer(txt) if token.isalnum()]
    return tokens

def tfidf(tok_doc, tok_corpus):
    doc_length=len(tok_doc)
    corpus_length=len(tok_corpus)

    #tf
    term_count=Counter(tok_doc)
    
    #idf
    tfidf={}
    for key in tok_doc:
        doc_frequency=0
        for doc in tok_corpus:
            if key in doc:
                doc_frequency+=1
        inverse_doc_frequency=math.log(corpus_length/doc_frequency)

        tfidf[key]= (term_count[key]/doc_length) * inverse_doc_frequency
    
    return tfidf

def task1(tok_text, tfidf_scores):
    
    # extract top 10
    top_10=[(k,v) for k, v in sorted(tfidf_scores.items(), key=lambda item: item[1], reverse=True)][:10]
    
    #print top 10
    print(', '.join([k for k,v in top_10]))

def task2(text,tfidf_scores):
    sentences=sent_tokenize(text)
    if len(sentences)<6:
        return text # da li treba spojit s razmakom ili samo text vratit 
    
    sent_scores=[]
    tok_text=preprocessor(text)
    
    for sent in sentences:
        tok_sent=preprocessor(sent)
        tfidfs=[tfidf_scores[tok] for tok in tok_sent]
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


# setup 
corpus_pth='data\\corpus'
input_pth='data\\corpus\\goose\\Chinese goose.txt'

tokenizer=word_tokenize
stemmer=SnowballStemmer(language='english', ignore_stopwords=False)

corpus_string=''
for root, dirs, files in os.walk(corpus_pth, topdown=False):
   for name in files:
      corpus_string+=str(
              open(os.path.join(root, name),'r', encoding='UTF-8').read()
        )

tok_corpus=preprocessor(corpus_string)

input_text=open(input_pth,'r', encoding='UTF-8').read()
tok_text=preprocessor(input_text)
tfidf_scores=tfidf(tok_text,tok_corpus)

# task 1
task1(tok_text, tfidf_scores)

# task 2
task2(input_text, tfidf_scores)  