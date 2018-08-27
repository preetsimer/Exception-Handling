#question 1
The exception is: ZeroDivisionError

#question 2
The exception is: IndexError -list index out of range

try:
    l=[1,2,3]
    print(l[3])
except:
    print("List index is out of range")


#question 3

Output:
    An exception
    An Exception NameError:Hi there will occur

#question 4
Output when (a,b)=(2.0,3.0):
    -5.0

Output when (a,b)=(3.0,3.0): as exception occured except block will execute
    a/b result in 0

#question 5

#1. import error
    try:
    import py #name of module that doesn't exist in python
except:
    print("So such module is present in python")
    
#2. value error
    try:
    n=int(input("Enter a number: "))
    print("you have entered ",n)
except:
    print("Nothing except integers is accepted")

#3. Index error
    try:
   l=[1,2,3,4,5,6]
   n=int(input("Enter index >0 and <6 to get it's value "))
   print(l[n])
except:
    print("Index range is out of bound : 0<index<6")





    
    
