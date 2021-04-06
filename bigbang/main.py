import numpy as np
import math

def calculate_beggining(px,py,vx,vy):
    px=abs(px)
    py=abs(py)
    vx=abs(vx)
    vy=abs(vy)
    
    opt1=0
    opt2=0
    
    # For X
    print('part1')
    px_opt1=px//vx
    px_opt2=px//vx+1
    px_rez1=px-(px_opt1)*vx
    px_rez2=px-(px_opt2)*vx
    print(px_opt1,px_opt2)
    print(px_rez1, px_rez2)
    if abs(px_rez1) < abs(px_rez2):
        print(px_opt1)
        opt1=px_opt1
    else:
        print(px_opt2)
        opt1=px_opt2
        
    # For y
    print('part2')
    py_opt1=py//vy
    py_opt2=py//vy+1
    py_rez1=py-(py_opt1)*vy
    py_rez2=py-(py_opt2)*vy
    print(py_opt1,py_opt2)
    print(py_rez1, py_rez2)
    if abs(py_rez1) < abs(py_rez2):
        print(py_opt1)
        opt2=py_opt1
    else:
        print(py_opt2)
        opt2=py_opt2
    
    # This will generate 2 suggestions from which one has to be choosen by comparing 
    opt1_rezx=px-opt1*vx
    opt2_rezx=px-opt2*vx
    opt1_rezy=py-opt1*vy
    opt2_rezy=py-opt2*vy
    
    if (opt1_rezx + opt1_rezy) < (opt2_rezx + opt2_rezy):
        return opt1
    else:
        return opt2
    
        
    
def simulate_second(px,py,vx, vy, bound, debug=False):
    px_nb,py_nb=px+vx, py+vy
    vx_new=0
    vy_new=0
    
    hit_cnt=0
    
    if px_nb>bound:
        
        px_b= bound - (px_nb -bound)
        
        if debug:
            print(f'px > {bound}')
            print(px_nb)
            print(px_nb-10)
            print(px_b)
        vx_new=-vx
        hit_cnt+=1
    elif px_nb<-bound:

        px_b= -bound + (abs(px_nb) - abs(bound)) 
        
        if debug:
            print(f'px < {-bound}')
            print(px_nb)
            print(px_nb+10) 
            print(px_b)
        vx_new=-vx
        hit_cnt+=1
    else:
        px_b=px_nb
        vx_new=vx
    
    if py_nb>bound:

        py_b= bound - (py_nb -bound )
        
        if debug:
            print(f'py > {bound}')
            print(py_nb)
            print(py_nb-10)
            print(py_b)
        vy_new=-vy
        hit_cnt+=1
    elif py_nb<-bound:
        py_b= -bound + (abs(py_nb) - abs(bound))
        
        if debug:
            print(f'py < {-bound}')
            print(py_nb)
            print(py_nb-10)
            print(py_b)
        vy_new=-vy
        hit_cnt+=1
    else:
        py_b=py_nb
        vy_new=vy
        
    return px_b, py_b, vx_new, vy_new, hit_cnt


def read_file(fpth):
    with open(fpth, 'r') as f:
        lines=f.readlines()
    particle_cnt, bound, time_of_ref, ref_prob=(float(x) for x in lines[0].split(' '))
    
    particles=[]
    for i in range(int(particle_cnt)):
        particle=lines[i+1]
        px,py,vx,vy=(float(x) for x in particle.split(' '))
        particles.append((px,py,vx,vy))
    
    return particle_cnt, bound, time_of_ref, ref_prob, particles

def read_input():
    setting=input()
    particle_cnt, bound, time_of_ref, ref_prob=(float(x) for x in setting.split(' '))
    
    particles=[]
    for i in range(int(particle_cnt)):
        particle=input()
        px,py,vx,vy=(float(x) for x in particle.split(' '))
        particles.append((px,py,vx,vy))
    
    return particle_cnt, bound, time_of_ref, ref_prob, particles

def task_a(particles, particle_cnt):
    

    particles=np.array(particles)
    means=np.sum(particles,axis=0)
    x_sum=means[0]
    y_sum=means[1]
    vx_sum=means[2]
    vy_sum=means[3]
    aprox=int(((x_sum/particle_cnt)/(vx_sum/particle_cnt) + (y_sum/particle_cnt)/(vy_sum/particle_cnt)))/2
#     print('aprox',aprox)
    

    start_subs=aprox-3
    before_n_secs=start_subs
    
    min_x_std=np.std(particles[:,0]-start_subs*particles[:,2])
    min_y_std=np.std(particles[:,1]-start_subs*particles[:,3])
#     print('min ', min_x_std, min_y_std)
    
    for i in range(int(start_subs)+1, int(aprox)+5, 1):
#         print(i)
        x_std=np.std(particles[:,0]-i*particles[:,2])
        y_std=np.std(particles[:,0]-i*particles[:,2])

#         print('x_dif ',x_dif)
#         print('y_dif ',y_dif)
#         print('x_std', x_std)
#         print('y_std', y_std)
#         print()
        if (abs(x_std)+abs(y_std))<(abs(min_x_std)+abs(min_y_std)):
            min_x_std=x_std
            min_y_std=y_std
            before_n_secs=i
        else:
#             print('breaking')
            break
            
    return before_n_secs

def task_b_and_c(particles, bound, time, ref_prob):
#     print('bound ',bound)
    hit_result=0
    probas=[]
    
    for idx,particle in enumerate(particles):
#         print('particle ',idx)
        px,py,vx,vy= particle
#         print(f"{px:.2f}\t {py:.2f}\t {vx:.2f}\t {vy:.2f}")
        this_particle_hit=0
        for i in range(int(time)):
            px,py,vx,vy,hit_cnt=simulate_second(px,py,vx,vy,bound)
#             print(f"{px:.2f}\t {py:.2f}\t {vx:.2f}\t {vy:.2f}\t {hit_cnt:.2f}")
            this_particle_hit+=hit_cnt
            hit_result+=hit_cnt
#         print(this_particle_hit)
        proba=pow(ref_prob,this_particle_hit)
#         print(proba)
        probas.append(proba)
    return hit_result, sum(probas)


# Test public dataset
# for i in range(1,11,1):
#     if i < 10:
#         i_str='0'+str(i)
#     else:
#         i_str=str(i)
        
#     particle_cnt, bound, time_of_ref, ref_prob, particles=read_file(fpth=f'bigbang/data/{i_str}.in')
#     print(open(f'bigbang/data/{i_str}.out').read().strip())
#     A=task_a(particles, particle_cnt)
#     B,C=task_b_and_c(particles, bound, time_of_ref, ref_prob)
#     print(A,B,C)


if __name__=="__main__":
    particle_cnt, bound, time_of_ref, ref_prob, particles=read_input()
    A=task_a(particles, particle_cnt)
    B,C=task_b_and_c(particles, bound, time_of_ref, ref_prob)
    print(A,B,C)
