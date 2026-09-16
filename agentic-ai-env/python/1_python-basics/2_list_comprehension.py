l=[1,2,3,4,5]

l2=[x*x for x in l]
print(l)
print(l2)

#comditional list comprehension

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

even=[x for x in nums if x%2==0]
print(even)

odd=[x for x in nums if x%2!=0]
print(odd)

num_less_ten=[x for x in nums if x<10]
print(num_less_ten)


# n=[1,2,4,[1,2,3],'num','nums',False, True]
# n1=[x for x in n if x%2==0]
# print(n1)

a1=[1,2,3,4,5,6,7,8]
a2=[9,8,7,6,5,4,3,2,1,0]

p=[[i,j] for i in a1 for j in a2]
print(p)


#list comprehension with function calls
wrd=['hdhdhd','qwerty', 'mnbvcx','aa','bb','bbb']
list_lrn=[len(x) for x in wrd]
print(list_lrn)