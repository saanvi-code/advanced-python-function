x={100,200,300,400}
y={"ha","va","sa"}
xy=zip(y,x)
print(list(xy))

c=[100,200,400]
l=[900,800,700]

for x,y in zip(c,l[::-1]):
    print(x,y)

d=["infosis","bmw","amazon"]
v=[1000,3000,2000]
dict={d:v for d,v in zip(d,v)}
print(dict)