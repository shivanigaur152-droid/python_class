#----------- File handling
#1.File handling in python means reading from and writing to files/folder stored on
# disk using python

#2. your python code can open a file, pull out data of it, put data into it and
#also close it properly

#----------- what is file
# files are store of data and information on the specific path of device.

# Types of file 
#1. text file(.txt,.csc,.json)
#2. Binary file (images,vedios,audio)


# Types of file path.
#1.Absolute path: The complete path from the root of the filesystem.
#2.Relative path: The path relative to where your current folder(current working dir)

#file mode
#1. a: append, a+ : append and read
#2. w: write , w+ : write and read
#3. r : read , r+ : read and write
#4. x : strictly create file

# python file handling methods.
# 1. open(file_name,mode) : opens file
# 2. close() : close file.
# 3. flush() : memory cleanup.

# 4. read() : file read.
# 5. readlines(): file read line by line.
# 6. write() : write data in file only take string.
#write data in file of any data types.

# 8. tail() : cursor move
# 9. seek() : specific position set of cursor


#1. create a file in strict mode
# file=open("strict.txt","x")
# file.write("this is python file handling...")
# print("file create..")

# file=open("strict.txt","x")
# file.write("this is python file handling...")
# file.flush()
# file.close()
# print("file create..")

# context manager
# with open("manage.txt","w+") as file:
#   file.write("this is completely python file handling...")
#   file.seek(0)
#   r=file.read(4)
#   print("file created and written...")
#   print(f"file content : {r}")

# with open(r"C:\Users\kumar\OneDrive\Desktop\Python_shivi\dictionary_lacture\demo.txt", "r") as f:
#     print(f.read())
  