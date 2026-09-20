try:
    a=b

except:
    print('the var has not been assigned')



try:
    a=b

except NameError as ne:
    print(ne)



#zerodiverror

try:
    res=1/0
except ZeroDivisionError as z:
    print(z)

#main except class
try:
    res=1/2
    a=b
except ZeroDivisionError as z:
    print(z)
    print('ignored')
except Exception as e:
    print(e)
    print('main exception caught here')


#try except else
try:
    res=1/2

except ZeroDivisionError as z:
    print(z)
    print('ignored')
except Exception as e:
    print(e)
else:
    print(f'result is {res}') # must be executed if no exception

#try except else finally
try:
    res=1/2
    a=b

except ZeroDivisionError as z:
    print(z)
    print('ignored')
except Exception as e:
    print(e)
else:
    print(f'result is {res}')
finally:
    print('execution complete') # even in case of error execute..always execute



# file handling nd exception hndling


try:
    file=open('example1.txt')
    content=file.read()
    print(content)
except FileNotFoundError as f:
    print(f)
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('file closed')

try:
    file=open('justAisehi.txt')
    content=file.read()
    print(content)
except FileNotFoundError as f:
    print(f)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file closed')