tup=()
tup1=tuple()
print(tup)
print( type(tup))
print(tup1)
print( type(tup1))


l=[1,23,4,5,6,66]

t=tuple(l)
print(t)
print(type(t))

print(l)
l1=list(t)
print(l1)
print(type(l1))


#mixed tuple
tup1=(1,2,False,3.14,'hello')
print(tup1)


#indexing and slicing just like list

#tuple operations
tup2=(1,101,'jhygxukhj')
t_concat=tup1+tup2
print(t_concat)

#multiply
tx=tup2*3
print(tx)

l=[1,2,3,4,5]
print(l*3)


#tuple meothods
tupp=(1,2,3,4,5,1,1,1,11,3,3,3,3,3,1,1,23,3,3)
print(tupp.count(1))
tupp.index(3) #first index of value


#packing and unpacking tuples

packed_tuples=1,2,3,'hello',3.13,False
print(packed_tuples)

a,b,c,d,e,f=packed_tuples
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#unpacking with *
numbers=(1,2,3,4,5,6)
f,*mid,l=numbers
print(f,' ',mid,' ',l)