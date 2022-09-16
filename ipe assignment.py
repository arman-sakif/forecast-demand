A = [1200,1285,1350,1575,1660,1700,1825,1920,2180]

F = [0]*10
T = [0]*10
fitt = [0]*10

alpha=0.4
beta = 0.8


F[0] = 985
T[0] = 256
fitt[0] = 985+256


for i in range(9):
    f0 = F[i]
    t0 = T[i]
    
    f1 = alpha*A[i] + (1-alpha)*(F[i]+T[i])
    t1 = beta*(f1-f0) + (1-beta)*t0
    
    F[i+1] = f1
    T[i+1] = t1
    fitt[i+1] = f1+t1

for i in range(10):
    print(i+1,F[i],T[i],fitt[i], sep='\t')
    print()
    