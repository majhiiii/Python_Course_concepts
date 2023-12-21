import sys
x,y=10,20
print('before swap')
print('x value:',x,'address of x:',id(x),'type :',type(x),'size of x :',sys.getsizeof(x))
print('y value:',y,'address of y:',id(y),'type :',type(y),'size of y :',sys.getsizeof(y))
x,y=y,x # or y,x=x,y
print('after swap')
print('x value:',x,'address of x:',id(x),'type :',type(x),'size of x :',sys.getsizeof(x))
print('y value:',y,'address of y:',id(y),'type :',type(y),'size of y :',sys.getsizeof(y))
#sys is predefined module
