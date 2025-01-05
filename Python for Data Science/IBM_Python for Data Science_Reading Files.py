with open('C:/Users/M-TT/Code/Example1.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )



#copy file to another

with open("C:/Users/M-TT/Code/Example1.txt", "r") as readfile:
       with open("C:/Users/M-TT/Code/Example3.txt", "w") as writefile:
              for line in readfile:
                     writefile.write(line)


with open("C:/Users/M-TT/Code/Example3.txt", "r") as new_file:
       for line in new_file:
              print("new_file:", line)

              

       