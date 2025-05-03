a=[1,2,3,4,5]
b=[5,4,3,2,1]

x=map(lambda x,y:x+y,a,b)
print(list(x))

def sq(a):
    return a*a

y=[45,332,23,92]

x1=map(sq,y)
print(list(x1))