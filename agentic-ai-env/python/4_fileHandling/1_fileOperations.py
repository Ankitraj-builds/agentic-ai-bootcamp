#read the whole file
with open('example.txt','r') as file:
    content=file.read()
    print(content)

#read line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip())


#write with overriding content
with open('example.txt','w') as file:
    file.write("hello this is ankit\n")
    file.write('welcome!!')

#reading to see content
with open('example.txt','r') as file:
    content=file.read()
    print(content)

#write without overriding content
with open('example.txt','a') as file:
    file.write("well i am writing again!!")

#writing a list of lines to a file

lines=['first line\n','second line\n',"third line\n"]

with open('example.txt','a') as file:
    file.writelines(lines)


#Binary files

bData=b'\x00\x01\x02\x03\x04'

with open('ex.bin','wb') as file:
    file.write(bData)

with open('ex.bin','rb') as file:
    print(file.read())



#read from src and write to dest
with open('example.txt','r') as src_file:
    content=src_file.read()

with open('destination.txt','w') as dest_file:
    dest_file.write(content)


#writing then reading the file after that

# w+ -> write then read 
# if no file then create, if exits then override


with open('example.txt','w+') as file:
    file.write('newly written\n')
    file.write('newly written1\n')
    file.seek(0)
    content=file.read()
    print(content)
