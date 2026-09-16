def sayHi():
    print("Hi")

sayHi()

#default params

def greet(name='mr x'):
    name=name.capitalize()
    print(f"Hi, {name}!! Nice to meet you ")


greet('ankit')
greet()


def players(*args):
    for n in args:
        print(n)

players('mahi','vk','hitman','mr 360')


def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"key={key}:value={value}")


print_details(name="ankt",age=21)