s=set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1)
s.add(2)
s.add(6)
s.add(9)
print(s)

# s.add((11,12,14,10,1,2,1111,12))
# print(s)


for x in s:
    print(x)


s1=set([1,2,3,4,5,'mango','kiwi'])
print(s1)



#set ops
##1. add
s1.add(7)
print(s1)

#remove
s1.remove(3)
print(s1)

s1.discard(10) # no error
print(s1)

#pop
s1.pop()
print(s1)


#in
if 'kiwi' in s1:
    print('healthy')

#maths
s1={12,13,14,15,155,13333,1111222,45666}
s2={12,13,14,9099090,98889,99090,7373783}

#union
union_set=s1.union(s2)
print(union_set)

#intersection
intersection_set=s1.intersection(s2)
print(intersection_set)

#difference
dif_set=s1.difference(s2)
print(dif_set)

dif_set1=s2.difference(s1)
print(dif_set1)

#symmetric difference
sdif_set=s1.symmetric_difference(s2)
print(sdif_set)

#intersection_update
print(s1)
s1.intersection_update(s2)
print(s1)


#set methods
#1. issubset()

s1={1,2,3,4,5,6,7}
s2={11,1,13,14,15}
s3={1,2,3,4,5,6,7,8,9}

print(s1.issubset(s2))
print(s1.issubset(s3))
print(s2.issubset(s1))
print(s2.issubset(s3))
print(s3.issubset(s1))

#2 superset
print(s3.issuperset(s1))