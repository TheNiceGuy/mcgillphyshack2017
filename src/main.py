import numpy as np
print('yo')
print("Hello World!")
print(2+2)
m=np.zeros((100,100))
#m[0][0]=1
for i in range(0,100):
        for j in range(0,100):
                    m[i][j]=min(i+1,j+1)/max(i+1,j+1)
                    print( m )
