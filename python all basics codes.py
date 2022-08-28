#!/usr/bin/env python
# coding: utf-8

# # variable

# In[1]:


print('Abir')


# In[2]:


x = 2
y = 'abir'
print(x)
print(y)


# In[3]:


x=7
print(x)


# In[4]:


x=2

X=5
print(x)


# In[5]:


print(X)


# In[6]:


name = 'Abir'
print(name)


# In[7]:


name_Abir = 23
print(name_Abir)


# # Assign value to a multiple variable

# In[8]:


a1,a2,a3= 1,2,3
print(a1,a2,a3)


# In[9]:


print(a1)


# # Memory Management

# In[10]:


x=10
y=90
z=10+90
a='abir'


# In[11]:


print(id(x)) #find the memory address


# In[12]:


print(id(y))


# In[13]:


print(id(100))


# In[14]:


print(id(z))


# In[15]:


print(id(a))


# # comments

# In[16]:


#x = 'abir' #single line comment
"""
p='abir'
q='anu'
print(p)

"""


# # Escape sequence

# In[17]:


a='Abir\'s cat' #single quote
print(a)


# In[18]:


a='Abir\'s \tcat' #tab
print(a)


# In[19]:


a='Abir\'s \"cat"' #double quote
print(a)


# # data type

# # numeric

# In[20]:


x=7
result=type(x)
print(result)


# In[21]:


x=7.7
result=type(x)
print(result)


# In[22]:


x=7+8j
result=type(x)
print(result)


# In[23]:


x=5
y=6
result=type(x==y)
print(result)


# # sequence

# In[24]:


x="I AM ABIR"
r=type(x)
print(r)


# In[25]:


x=[1,2,23,3,3]
result=type(x)
print(result)


# In[26]:


x=(1,2,3,3,3,3)
result=type(x)
print(result)


# In[27]:


x={1,2,2,2,2,2}
result=type(x)
print(result)


# In[28]:


x=range(6)
result=type(x)
print(result)


# # user input in python

# In[29]:


x=input('Enter any number:')
y=input('Enter any number:')
z=x+y


# In[30]:


print(z)


# In[31]:


type(z)


# ## x=int(input('Enter any number:'))
# y=int(input('Enter any number:'))
# z=x+y

# In[33]:


print(z)


# In[34]:


type(z)


# # operators

# In[ ]:


# Arithmetic


# In[35]:


a=20
b=3


# In[36]:


print(a+b)


# In[37]:


print(a-b)


# In[38]:


print(a*b)


# In[39]:


print(a/b)


# In[40]:


print(a%b)


# In[41]:


print(a**b)


# In[42]:


print(a//b)


# # assignment

# In[43]:


p=10
q=20
r=p+q
r+=p     #r=r+p


# In[44]:


print(r)


# In[45]:


r-=p
print(r)


# In[46]:


r*=p
print(r)


# In[47]:


r/=p
print(r)


# # relational

# In[48]:


a=10
b=4


# In[49]:


print(a>b)


# In[50]:


print(a<b)


# In[51]:


print(a>=b)


# In[52]:


print(a<=b)


# In[53]:


print(a==b)


# # logical

# In[54]:


a=10
b=2
c= a>3 or b<1  #one condition is true


# In[55]:


print(c)


# In[56]:


c= a>3 and b>1  #both condition is true
print(c)


# # unary

# In[57]:


a =10
b=1
c=5
a=-a
a=-a
print(a)


# # Strings

# In[406]:


a = '  Data Science  '
print(a)


# In[59]:


print(a[2])


# In[ ]:


print(a[5:8])


# In[ ]:


print(a[-9:-6]) #reverse


# In[62]:


print(len(a))


# In[63]:


print(a.strip()) #space remove 


# In[64]:


print(a.upper())


# In[65]:


print(a.lower())


# In[66]:


p='As Abir'
print(p)


# In[67]:


print(p.replace('As','Md'))


# In[407]:


print(a.split())


# # Arrays

# In[69]:


from array import *
salary=array('i',[1200,2200,2100,2300])
print(salary)


# In[70]:


print(salary[0])


# In[71]:


for i in range(4):
    print(salary[i])


# In[72]:


print(salary.buffer_info())


# In[73]:


print(salary.append(4500))
print(salary)


# In[74]:


print(salary.remove(4500))
print(salary)


# In[75]:


print(salary.pop(2))
print(salary)


# In[76]:


print(salary.reverse())
print(salary)


# # Difference between Tuple and list

# In[77]:


import sys
Tuple = (12,1,2,2,21,3,2)
List = [12,2,3,455,5,7,79]
#Tuple[3]=3 #unchanged value
List[3]=80  #changed value
print('Tuple',sys.getsizeof(Tuple))
print('List',sys.getsizeof(List))
print(Tuple)
print(List)


# In[78]:


Tuple.remove(Tuple[1]) #not work


# In[79]:


del Tuple


# In[80]:


print(Tuple)


# In[81]:


List.remove(List[0])


# In[82]:


print(List)


# In[83]:


del List


# # Set

# In[84]:


a=set([1,2,3,4,5])
print(a)


# In[85]:


a1={1,2,3,4,5,1,2}
a2={8,10,12}
a1.add(6)
a1.update([7,8],a2)
a1.remove(4)
a1.discard(15)
print(a1)


# In[86]:


s1={1,2,23,34,4,44,38}
s2={1,2,2,3,4,5,6,6,6}
s3={1,2,22,2,3,4,4,4,4}


# In[87]:


s4=s1.intersection(s2,s3)
print(s4)


# In[88]:


s4=s1.difference(s2,s3)
print(s4)


# In[89]:


s4=s1.symmetric_difference(s2)
print(s4)


# In[90]:


p1=[1,2,2,2,33,3,4,4,4]
result=list(set(p1))
#result=set(p1)
print(result)


# In[91]:


s5=s1.union(s2,s3)
s6=s1|s2|s3
print(s6)
print(s5)




# # Dictionaries

# In[98]:


d1={'Name':'Abir','Age':24,'Bday':1998}

d2={'True':'True',10:10,10.5:11}
print(d1)
print(d1['Name'])
print(d1['Age'])
print(d1['Bday'])
print(d2)
print(d2['True'])
print(d2[10])
print(d2[10.5])


# In[94]:


d3=d2.copy()
print(d3)
 


# In[95]:


d3=len(d2) 
print(d3) 


# In[96]:


d3=len(d1)
print(d3) 


# In[106]:


d1={'Name':'Abir','Age':24,'Bday':1998}
d1['university']='AIUB'
d1.pop('Age')
print(d1)


# In[107]:


d1.clear()
#del d1
print(d1)


# In[347]:


f={1:'Abir',2:'Anu',3:'Anik'}
print(f)
print(f.get(2))
print(f.items())
print(f.keys())


# # nested dictionaries

# In[115]:


student={
         1:{'sex':'male','name':'abir','age':28},
         2:{'sex':'male','name':'anu','age':22},
         3:{'sex':'male','name':'anik','age':30}
        }
print(student)


# In[117]:


print(student[1]['name'])
print(student[2]['age'])
print(student[3]['sex'])


# In[132]:


#add in sets
student[4]={}
student[4]['sex']='male'
student[4]['name']='adil'
student[4]['age']=30
print(student[4])


# In[133]:


print(student)


# In[134]:


del student[4]['age']
print(student[4])

del student[4]
print(student)


# # if else elif

# In[143]:


x=20
y=20
z=30
if x>y:
    print('x is less than y' )
elif x<y:
    print('x is greater than y')
else:
    print('x is equal to y')


# # even or odd

# In[147]:


number=int(input('Enter any value:'))
n = number%2
if n==0:
    print('the value is even')
else:
    print('the value is odd')


# # negative or positive

# In[150]:


n=int(input('Enter any value:'))
if n<0:
    print('the value is negative')
elif n>0:
    print('the value is positive')
else:
    print('the value is zero')


# # nested if

# In[159]:


n=float(input('Enter any value:'))
if n<0:
    print('the number is negative')
else:
    print('the numberr is postive')
    if (n%2)==0:
        print('the number is even')
    else:
        print('the number is odd')


# # find max number out of three number

# In[161]:


x = int(input('Enter 1st number:'))
y = int(input('Enter 2nd number:'))
z = int(input('Enter 3rd number:'))

if x>y:
    if x>z:
        print('x is greater than y,z')
    else:
        print('x is less than y,z')
elif y>x:
    if y>z:
        print('y is greater than x,z')
    else:
        print('y is less than x,z')


# # ternary operator

# In[164]:


a,b=12,13
c=a if a<b else b
print(c)


# In[166]:


num=int(input('Enter any value:'))
a='value is even' if num%2==0 else 'value is odd'
print(a)


# # swapping

# In[169]:


a=10
b=20
temp=a
a=b #20
b=temp  #10
print('a =',a)
print('b =',b)


# In[170]:


a=1
b=2
a=a+b #3
b=a-b #1
a=a-b #2



print('a =',a)
print('b =',b)


# In[172]:


a=7
b=4
a,b=b,a
print('a =',a)
print('b =',b)


# # assertion

# In[179]:


def MySalary(salary):
    assert salary>0,'salary can not less than zero'
    print('my salary is:',salary)
MySalary(60000)


# # for loop and range

# In[180]:


a=['abir','anu','anik','adil']
for name in a:
    print(name)


# In[183]:


p=[1,2,2,2,3,3,3]
total= 0
for element in p:
    #total +=element 
    total=total+element
    print(total)


# In[189]:


#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
c=list(range(1,16))
print(c)


# In[196]:


total=0
for i in range(1,17):
   
        if(i%2==0):
            total+=i
    
print(total)


# # prime num find out

# In[217]:


num = int(input('Enter any value:'))
for i in range(2,num):
    if num%2==0:
        print('it,s not a prime number')
        break
else:
    print('oh,its a prime number')


# # while loop

# In[208]:


n=10
while n>=1:
    print('abir',n)
    n=n-1
    


# In[207]:


n=1
while n<10:
    print('abir',n)
    n=n+1
    


# # Break statement

# In[215]:


n=int(input('how many phone do yo want to sell: '))
i=1
available = 10
while i<=n:
    if i>available:
        print('sorry,stock out')
        break
    print('iphone',i)
    i+=1
print('OK!Thank you.')
    


# # continue statement

# In[226]:


for i in range(1,40):
    if i%2==1:
        continue
    print(i)


# # pass statement

# In[243]:


for i in range(1,40):
    if i%2!=0:
        pass
    
    else:
        print(i)


# # functions

# In[246]:


def function1():
    print("Abir")
    print("good boy")
function1()
print("done!")
#function1()


# In[253]:


def abir(age):
    return age*2
result=abir(20)
print(result)


# In[265]:


def anu(x,y):
    return x*y
p = anu(20,20)
print(p)
p = anu(20,25)
print(p)
p = anu(20,30)
print(p)


# # non keyword argument 

# In[280]:


def  p(*num):
    result=0
    for i in num:
        result=result+i
    
    print('result: ',result)
p(7,9,8)


# In[281]:


def name(*argv):
    for i in argv:
        print(i)
name("hi","He","is","Anik")


# In[314]:


def name(argv1, *argv):
    print("1st argument: ",argv1)
    
    for i in argv:
        print("next argument:",i)

name("Abir","Bir","Cat","Doll")


# In[332]:


def a(num1,*num):
    result=1
    for i in num:
        result=result*i
    print('resut is :',result)
a(12,2,8,7)


# # keyword argument

# In[340]:


def myself(**others):
    print(others)
  
myself(name="abir",age=24)


# In[339]:


def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# # zip function

# In[343]:


name=['Abir','Anik','Anu']
varsity=['AIUB','DIU','EWU']
zipped = list(zip(name,varsity))
print(zipped)


# In[344]:


zipped = tuple(zip(name,varsity))
print(zipped)


# In[345]:


zipped = dict(zip(name,varsity))
print(zipped)


# # Unzip function

# In[350]:


name=['Abir','Anik','Anu']
varsity=['AIUB','DIU','EWU']
zipped = list(zip(name,varsity))
print(zipped)


# In[351]:


name1,varsity1 = zip(*zipped)


# In[352]:


name1


# In[353]:


varsity1


# In[449]:


all_info=list(zip(*zipped))
print(all_info)


# In[450]:


name1=all_info[0]
print(name1)


# In[451]:


varsity1=all_info[1]
print(varsity1)


# # fibonacci series

# In[394]:


def fibo(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        
        print(c)
fibo(10)


# # Factorial Number

# In[386]:


def num(n):
    initial =1
    for i in range(1,n+1):
        initial=initial*i
    return initial
result=num(5)
print(result)


# In[390]:


#or
n=int(input('Enter any number: '))
f=1
for i in range(1,n+1):
    f=f*i
print(f)


# In[396]:


#or
import math
#f=5
f=int(input('Enter any num:'))
r=math.factorial(f)
print(r)


# # python list vs Numpy array

# In[402]:


#python list
list1=[1,2,3,4]
list2=[1,2,3,4]

result=list1[2] * list2[2]
print(result)


# In[397]:


#numpy array
import numpy as np
list1=np.array([1,2,3,4])
list2=np.array([1,2,3,4])

result=list1*list2
print(result)


# # multidimentional array

# In[411]:


from numpy import *

array1 = array([
    [1,2,3,4,5,6],
    [9,8,7,5,3,2]
])

print(array1)


# In[415]:


print(array1.dtype)
print(array1.ndim)
print(array1.shape)
print(array1.size)


# In[428]:


from numpy import *

array1 = array([
    [1,2,3,4,5,6],
    [9,8,7,5,3,2]
])
#print(array1)
array2 = array1.flatten() #two dimentional array convert to one dimentional array
print('1D: ',array2)

array3=array2.reshape(3,4) #one dimentional array convert to two dimentional array
print('2D:',array3)

array4=array2.reshape(2,2,3) #one dimentional array convert to three dimentional array
print('3D: ',array4)

print(array4.ndim)
print(array4.shape)


# # Matrix

# In[443]:


import numpy as np

a1 = (
       [1,2,3],
       [2,3,4],
       [3,4,5]
     )
a2 = (
       [8,6,4],
       [2,3,4],
       [1,2,5]
     )
"""
print(a1)
print(a2)
"""
result=np.add(a1,a2) #addition
print(result)


# In[446]:


result=np.subtract(a1,a2) #substract
print(result)


# In[445]:


result=np.multiply(a1,a2) #index multiplication
print(result)


# In[444]:


result=np.dot(a1, a2) #matrix multiplication
print(result)


# # Lambda Function 

# In[452]:


def num(p,q,r):  #function using
    return p*q*r
result=num(1,2,3)
print(result)


# In[453]:


result=(lambda p,q,r : p*q*r) (1,2,3)   #using lambda function
print(result)


# # Map Function

# In[464]:


def mul_five(number):
    return number*5
result =[]
number = [1,23,4,44,5,6]
for i in number:
    result.append(mul_five(i))
print(result)


# In[484]:


#or  using map function
def mul_five(number):
    return number*5
number = [1,23,4,44,5,6]
result=list(map(mul_five,number))
print(result)


# # Filter function

# In[481]:


num=[1,2,2,3,3,5,5,6,7,8,8,8,8,9]

result=list(filter((lambda n:n%2),num))
print(result)
result1=list(filter((lambda n:n<4),num))
print(result1)


# # Reduce Function

# In[485]:


import functools
def add_two(num1,num2):
    return num1+num2
list1=[1,2,3,3,4,4,5]
result=functools.reduce(add_two,list1)
print(result)


# # local variable vs global variable

# In[489]:


x=5 #global
def function1():
    x=10 #local
    print('inside func:',x)

function1()
print("outside func:",x)


# In[500]:


x=5 #global
def function1():
    global y
    y=x+30 #local
    print('inside func:',y)
    print(id(y))

function1()
print("outside func:",x)
print(id(x))

def function2():
    x=10
    print('another func:',x)
    print(id(x))
function2()


# # Default arguments

# In[507]:


def my_pow(a,b=5):   #default parameter
    return pow(a,b)
result=my_pow(2,3)
print(result)


# In[509]:


def my_name(x='Abir'):    #default parameter
    print('I am Abusufiun',x)
my_name('(Abir)')


# # Recursion limit

# In[517]:


import sys
print("limit: ",sys.getrecursionlimit())
sys.setrecursionlimit(1500)
count =0
def myfunction():
    global count
    count=count+1
    print("Abir",count)
    myfunction()
#myfunction()


# In[520]:


def myfact(x):
    if x==0:
        return 1
    return x*myfact(x-1)
result=myfact(5)
print(result)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




