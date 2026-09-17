#map(function,iterable)

nums=[1,2,3,4,5]
mp_list=list(map(lambda x:x**2,nums))
print(mp_list)



def even(x):
    if x%2==0:
        return True
    return False

mp_dynamic=list(map(even,nums))
print(mp_dynamic) #[False, True, False, True, False]


#mutliple iterables
l1=[1,2,3,4]
l2=[4,5,6]

mp_add=list(map(lambda x,y:x+y,l1,l2))
print(mp_add)  #[5,7,9]

str_nums=['1','2','3','4']
int_nums=list(map(int,str_nums))
print(int_nums)


str='1 2 3 4 5 6 7 8 9'
ls=str.split(' ')
ins=list(map(int,ls))
print(ins)
for x in ins:
    print(type(x),end=' ')

