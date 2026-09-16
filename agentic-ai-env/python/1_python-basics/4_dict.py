dict1={}
dict2=dict()
dict3={1:'name',2:'age'}
print(dict1)
print(dict2)
print(dict3)


print(dict3[1])
# print(dict3[4])
print(dict3.get(2))
print(dict3.get(4)) # none ---> no error
print(dict3.get(4,'not available'))

print(dict3)
del dict3[1] # delete key value pair
print(dict3)

data={

    'name':"Ankit",
    'age':8,
    'height':5.7,
    'weight': 68
}
print(data.keys())
print(data.values())
print(data.items())


#shallow and deep copy

#deep
data_cpy=data
print(data)
print(data_cpy)
data['age']=11
print(data)
print(data_cpy)


#shallow
d_cpy=data.copy()  #diff memory allocated
print(d_cpy)
data['age']=19
print(data)
print(d_cpy)

#dictionary comprehension

sq={x:x**2 for x in range(5)}
print(sq)


esq={x:x**2 for x in range(5) if x%2==0}
print(esq)