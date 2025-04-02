
import math
from PIL import Image
import numpy as np
import time
s = time.time()
W = 2001
L = 2001
frac = Image.new('RGB',(W,L))
px = frac.load()
n_iter = 60

palette = []
for i in range(n_iter):
    palette.append((int(255*i/n_iter +60),int(i/n_iter ),0))
    #print(M)

def norm(a,b):
    a = 3*(a-(W+1)/2+1)/W-0.3
    b = 3*(b-(L+1)/2+1)/L
    return complex(a,b)

for x in range(W):
    for y in range((L+1)//2):
        p = np.sqrt((x-1/4)**2+y*y)
        if x<p - 2*p**2+1/4 or (x+1)**2+y**2<16:
            px[x,y] = (0,0,0)
        else:
            z = norm(x,y)
            z0 = z
            #print(z)
            px[x,y] = (0,0,0)
            #px[W-x,L-y] =(0,0,0)
            for j in range(n_iter):
                z = z**2 + z0
                if abs(z) > 2:
                    px[x,y] = palette[j]
                    px[x,L-y-1] = palette[j]
                    break
print(time.time()-s)
frac.show()
