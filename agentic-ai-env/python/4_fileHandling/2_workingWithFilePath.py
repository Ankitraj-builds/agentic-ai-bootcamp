#create new dir
import os
new_dir='package'

# os.mkdir(new_dir)
# print(f'Directory {new_dir} created')


#ListingFilesAndDir
items=os.listdir('.')
print(items)


#joining paths
dir_name='folder'
file_name='file.txt'
full_path=os.path.join(os.getcwd(),dir_name,file_name)

print(full_path)

#finding path
path='example.txt'
if os.path.exists(path):
    print(f'path - {path} exists')
else:
    print(f'path - {path} dont exists')

path1='example1.txt'
if os.path.exists(path1):
    print(f'path - {path1} exists')
else:
    print(f'path - {path1} dont exists')


# checking if path is file or directory
path='example.txt'

if os.path.isfile(path):
    print(f'path {path} is file')
elif os.path.isdir(path):
    print(f'path {path} is dir')

path='package'

if os.path.isfile(path):
    print(f'path {path} is file')
elif os.path.isdir(path):
    print(f'path {path} is dir')
else:
    print('file not found')



#getting relative path

rp='example.txt'
abs_path=os.path.abspath(rp)
print(abs_path)