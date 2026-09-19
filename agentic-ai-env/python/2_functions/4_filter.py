l=[1,2,3,4,5]
f=list(filter(lambda x:x%2==0,l))
print(f)


f1=list(filter(lambda x:x>2,l))
print(f1)

l1=[1,2,3,4,5,6,7,8,9,10,11,12,3222,999]

greaterThanFiveAndEven=list(filter(lambda x:x>5 and x%2==0,l1))
print(greaterThanFiveAndEven)

#filter in dictionary

people=[
    {
        'name':'Ankit', 'age':11
    },
    {'name':'Raj', 'age':14},
    {'name':'Rahul', 'age':38},
    {'name':'Rajeev', 'age':19},
    {'name':'Ram', 'age':17},
    {'name':'shyam', 'age':18}
]

def ageGreater15(people):
    return people['age']>17

nameListOfAge=list(filter(ageGreater15,people))
print(nameListOfAge)