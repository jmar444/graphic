import r
import matrix
import drw

x = 1
y = 1
empty = dict(zip(list(r.c2(i, j) for i in range(x) for j in range(y)), [[0,0,0] for k in range(x*y)]))
full  = dict(zip(list(r.c2(i, j) for i in range(x) for j in range(y)), [[1,1,1] for k in range(x*y)]))
a = drw.layer(1, 1, full)
b = drw.layer(1, 1, empty)
c = a*b
d = a+b
print('summ',d.lyr)
print('mul',c.lyr)