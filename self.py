'''x = 10
y = 20
result = x+y
res = 10 + 20
print(10+20)

print(x+y)

# Add 2 numbers  SC 1: Add directly and print the result
print(10 + 20) #worked

# SC 2: Add 2 numbers and give output value to a variable and print the result

res = 10+20
print(res)'''
'''
#SC 3: Give values to 2 references
x = 10
y = 20
   #Repeat above 2 scenarios
print(x+y)

res = x+y
print(res)

#1. Arithmetic:
#==================
x = 20
y = 3
print("Addition:",x+y)

print("Subtraction:", x-y)
print("Mulitplication:", x*y)
print("Division :", x/y)
print("Floor Division :", x//y)
print("Modulus :", x/y)
print("Modulus :", x%y)
print("Exponential :", x**y)


# comparison or relational

print(10<20)

print("Lessthan :", 10<20)
10>20

print("Greaterthan:", 10>20)
'''
'''
x = 10
y = 10
print("Both equals :", x==y)
print(x != y)

x = 10
y = 20
print(x >= y)
print( x <= y)

# assignment operator
x = 10
sal = 1000.4
name = 'Madhu.N'
is_active = True


X=y=10
print(id(X))
print(id(y))

x=10
y=20
print(id(x))
print(id(y))
a="apple"
b="apple"
print(id(a))
# print(id(b))
#id(x)=356843EE
#X=10
#Id(x)=46886
#X=10
'''

# oTHER OPERATORS
'''
print(10+20)
# Type2
x = 10
y = 20
print(x+y)

# Type3
x = 10
y = 20
result = x+y
print(result)
'''
'''
# Assignment opeartors
x = 10  # We are assiging value 10 to variable x
y = 20
res = x+y
x = x+y
# # x = +y  x += y
x += y
print(x)

x = 10
y = 20
y = y+x
print(y)
y += x
print(y)

# internal external- OR , AND

'''
'''
x = 10
y= 20
print(x+y)
print (x-y)

#print(10+20)
print(x*y)

result = x*y
print(result)

result = x+y
print(result)

mul = x*y
print(mul)

div = x/y
print(div)

fdiv = x//y
print(fdiv)

print(20/3)

print(20//3)

print(10**2)

print(10.5+2)

print(10+True)
print(10+False)

print(12+True)

print(int(True))

print(int(False))

#print(12+ '10')

print(10+20+30)

# Relational comparison

print(10==10)

print(10==5+5)

print(10==10.0)

print(10==20)

print(5!=20)

print(5!=5)

print(10>5)

x = 10
y = 20
print(x>y)
print(x<y)

print(10<=10)

print(10<=12)

print(10<=5)

print(10>=10)

print(10>=6)

print(10>=20)
'''
# Assignment operator
'''
x = 10
print(x)

x=20
print(x)

result = 10+20+30

result = 10 <=20
print(result)

result = 10 == 10
#print(resukt)
print(result)

result = 10 != 10
print(result)

print(10 + True)  # int + boolean ==> int+int(bool)

# We dont have increment, decrement ++ -- pre incr post incr pre decr post decr

x = 10
print(x)

y = x+10
print(y)

x = x+5
print(x)

x=x-5
print(x)
x=x*5
print(x)
x=x/5
print(x)
x=x//5
print(x)
x=x%5
print(x)
print(2%5)
x = 10
x = x + 3
print(x)
x=12
x +=3 #x=x+3
print(x)

x -= 2 # x= x-2
print(x)
x *= 4 # x= x*4
print(x)
x /= 3 # x= x/3
print(x)
x //= 2 # x = x//2
print(x)
x **=4 # x = x ** 4
print(x)
x %= 100 # x=x%100
print(x)
'''
#print(10 + 20 + 30)
#print(10*20)

''''
#print(x = 10)   # note ******************************************************
print('x = 10')

x = 10
result = x * 2
print(result)

print(x, result)
print(x + 20)

print(x-5)
print(result + 100)

#####print(x = 30+100) ############
x= 30 +100
print(x)

x= 1
x += 10
print(x)

print(x+2)
y = 1
print(x , y)

x= 1
y = x + 1
print(x, y)

x = x + 1
print(x)

x = 1 , 2
print(x)

x = 10
y = 10
print(x != y)

'''

# Numbers
 # int
 # float
 # complex

'''
x = 10 # int
print('Value of x: ', x)

x = 10.4 # float
print('Value of x: ', x)

x = 10
 # Convert to float
x = float(x)
print('Value of x: ', x)
'''
# Boolean
    #True
    #False

is_present = True
is_active = False
is_exists = True
is_completed = False
is_leap = True

is_val = 0
is_val2 = 1
# 0 - False
# 0 - True

# non zero = True
#zero      = False
'''
x= 10
print('Vaalue of x: ', x)
x = bool(x)
print('Value of x:', x)

res = 10-10
print('Value of x: ', res, bool(res))
'''
'''
str1 = ''
print('Bool of string ', bool(str1))
val = None
print('Value ', val, bool(val))

str1 = 'hello'
print("Bool string ", bool(str1))
val = [1,2,3] # # 10,10.5,'hello', [1,2,3], (1,2,3), {1:1},{1,2,3}
print('Value ', val, bool(val))
'''
'''
Datatypes/Structures: STATE
Functions           : BEHAVIOR

Functions:
-----------
print()
type()  id()
int()   float() complex() bool()
'''
'''
# float x = 10+20-30/54*23
x = 10+20-30/54*23
print('Value of x: ', x)
print('Type of x: ', type(x))
print('Address of x: ', id(x))

print('----------------------------')
sal = 10000.32
print("Value of sal: ", sal)
print('Type of sal :', type(sal))
print('Adress of sal: ', id(sal))

print('--------------------------------')
is_active = True
print('Status of active : ', is_active)
print('Type of active : ', type(is_active))
print('Address of active :', id(is_active))
print('----------------------------------')

print('-----------Type of values---------------')

# Type convertions int() float() bool()

#float to int
print('====float to int====')

x= 100.42
print('Value of x : ', x, type(x))
#Convert above number to integer

x = int(x) #here python creates new value 100
print('Value of x : ', x, type(x))

print('======int to float=======')
# int to float
x= 10
print('value of x:', x, type(x))
x= float(x)
print('Value of x:', x, type(x))

# Convert bool and viceversa
print('=========bool to ind and viceversa==============')
# boolean
# Boolean
'''
'''
True   - True
         non 0
         not None

False  - False
         0
         None

0 vs None

'''
'''
x = 100
print("value of x: ", x, type(x))
x = bool(x)
print('Value of x : ', x, type(x))

x=0
print("Value of x:",x, type(x))
x = bool(x)
print('value of x:', x, type(x))

# None  not none

x = 'hello' # not non
print(type(x))
x = bool(x)
print('hello ---> ', x, type(x))

x = '' # None
print(type(x))
x = bool(x)
print('Empty str --->', x, type(x))

x = [] #list
x = () #tuple
x = {} # dictionary
x = set({}) # set
'''

'''

Data types: Numbers : int float
            Boolean : True Fals
            String  : 'hello' 'madhu' "VN2"
            
            
'''
'''
print('------------String---------------')
#String ==> Collection of charecters
x = 'Hello World '  # left to right indexing
    #012345678910
print('value of : ', x, id(x), type(x))

name ='Akshay'
print("name is : ", name, type(name))

passw = '@#@$32424SDFDSFfdsdf'
print('Name is : ', passw, type(passw))

print('--------------CRUD Operations----------------')
x = 10   # CREATE
print(x) # RETRIEVE
x = 20   # UPDATE
del x    # DELETE

#CRUD
# 1. CREATE
str1 = 'Hellow World'
    #   01234567890
# 2.  Retrieve
print('Message : ', str1)
print('Message : ', str1[0]) #Indexing
print('Message : ', str1[4])
print('Message : ', str1[0:5]) # Slicing
print('Message : ', str1[2:9])

#UPDATE
str1 = str1 + ' Welcome'
print('Message : ', str1)

# DELETE
del str1

#LIST
print('-----------------LIST-------------------')

list1 = [13, 22, 43, 24, 55]
      #  0    1   2   3   4
print('List1 : ', list1)
print("List1 : ", list1[0])  #indexing
print("List1 : ", list1[2])
print(('List! : ', list1[1:3])) #Slicing  prints from 1 to 2 indexes

print('Before udadate :', list1)
#UPDATE
list1[2] = 44  # number in position 2 changed
print('After update : ',list1)

del list1[4]
#dele list1
print('List1 : ', list1)

list1 = [1.3, 2.2, 3.6, 4.7, 5.4]
print('list1 :', list1)
list1 = [True, False, True, False, True]
print('List1 :', list1)
list1 = ['hello', 'world', 'madhu']
print('list 1 : ', list1)
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('list1 : ', list1)
print('list1 : ', list1[1])
print('list1 : ', list1[1][2])   # o/p = 6

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(list1)
print(list1[1])
print(list1[1][2])
print(list1[0][1])


list1 = [{'id': 100}, {'name': 'Madhu'}]
print(list1)
print(list1[1])
print(list1[0])
#print(list1[0][1])    # won't work bcos dictionary

print(list1[0]['id'])
print(list1[1]['name'])


list1 = [{1, 2, 3}, {4, 5, 6}]   # Set
print(list1)
print(list1[1])
print(list1[0])
# print(list1[0][1])   ============== won't work bcos set is not subscriptable

list1 = [1.1, 3, 4.2, True, False, 0, None, 'Hello', [1, 2, 3]]
print('List1 : ', list1)

######################################
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('Adding lists : ', list1+list2)
##########################################
print('---------------Tuple-----------------')
tup1 = (1, 2, 3, 4, 5)
print('Tuple1 : ', tup1)
tup1 = (1.3, 2.2, 3.6, 4.7, 5.4)
print('Tuple1 :' , tup1)
tup1 = (True, False, True, False, True)
print('Tuple1 :', tup1)
tup1 = ('hello', 'world', 'madhu')
print('Tuple1 : ', tup1)

tup1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print('tuple1 : ', tup1)
print('tuple! :', tup1[1]) # indexing, slicing is possible in python
print('Tuple1 :', tup1[1][2])
print((tup1[2][1]))
del tup1

print('------------Dictionary------------------')

emp_details = [100, 'Madhu nateem', 20000, 'Bangalore', 'Oracle', 'M']

order_details = [12345, 54324, 432, 43, 3, 'Samsung S13', 'Banglore']

# key value pair association
emp_details = {'eid': 100,
               'name': 'Madhu nateem',
               'sal': 20000,
               'loc': 'Banglore',
               'office': 'Oracle',
               'gender': 'M'
               }
# key value pair association
# dict key : # int, float, bool, string, tuple

ord_details = {'order_n0': 12345,
               'ref_no': 534324,
               'price': 432,
               'tax': 43,
               'quantity': 3,
               'prod_desc': 'Samsung S13',
               'del_loc': 'Banglore'
               }
'''
#key = eid
#value = 100
#'eid':100 --> Item i.e, key:value
'''

print('Dictionary :', emp_details)
print('Dictionar keys :', emp_details.keys())
print('Dictionary keys : ', list(emp_details.keys()) ) # list of keys
print('Dictionary values :', list(emp_details.values()))
print('Dictionary values - ', list(emp_details.items())) # list of tuples

print('===============SET====================')
set1 = set({})
print('Set1 :', set1)
set1 = {1, 2, 3, 4, 5, 6}
print('set1 ; ', set1)

#indexing is not allowed in set and dict
# print('Set1 ; ', set1[2])
# Inside set, dict, list are not allowed.

'''
'''
x = 'abcd'
print(id(x))

marks = int(input("Enter marks :"))
if marks >= 0:
    print('number is positive')
else:
    print('number is negative')

k = 10
p = 1
k , p = p,k
print(k, p)
'''
'''
count = 0
while (count < 9):
    print('The count is', count)
    count = count + 1
print('Good bye')
i = 1
while i<= 10:
    print(' value is',  i)
    i += 1

st = int(input('Enter start value :  '))
end = int(input('Enter the end value : '))

if st < end:
    print('input data is valid')
    i = 1
    while i <= 10:
        if i % 2 == 0:
            print('Value is : ', i)
        i += 1
else:
    print(' invalid data is entered')

while st <= end:
    print('Value is : ', st)
    st += 1

print('----------Result with class---------------')

marks = int(input('Enter exam exam mark : '))

#Validation
if marks >= 0 and marks <=100:
    if marks >= 35:
        print('Result : PASS')
        if marks >= 60:
            print('---first class-----')
            if marks == 100:
                print(' cent percent')
            elif marks >= 90:
                print('Distinction')
            elif marks >= 80:
                print('----------First class--------')
        elif marks >= 70:
            print('second class')
        elif marks >= 50:
            print('Trird class -------')
    else:
        print('Result ; Fail- Better luck next time')
else:
    print('Enter valid marks')
print('================================================')
'''
'''
marks = int(input("Enter exam marks  :"))
if marks >= 0 and marks <= 100:
    # print("Valid input")
    if marks >= 35:
        print("RESULT : PASS")
        if marks == 100:
            print("---PERFECT----")
        elif marks >= 90:
                print("-----Good-----")
        elif marks >= 60:
                print("----FIRST CLASS----------")
        elif marks >= 50 and marks < 60:
            print("---SECOND CLASS----")
        elif marks >= 35 and marks < 50:
            print("----THIRD CLASS----")
    else:
        print("RESULT : FAIL")
else:
    print("Invalid marks")

print("--------------------------------------")
'''
'''
print('---------whileloop-------')
i = 1
while i <=10:
    print(i)
    i += 1
print(' End of the program')
print('------numbs from 1 to 10 except 5')
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i += 1

print('----Even nos b/w 1 to 10-----')
i = 1
while i <= 10:
    if i % 2 == 0 :
        print(i)
    i += 1

print('--------- numbers b/w 1 - 30 divisible by 3 & 5')
i = 1
while i <=30:
    if i % 3 == 0 and i % 5 == 0: # AND gate
        print('Value', i)
    i += 1

print('---- numbers b/w 1 - 100 divisible by 4 or 5 0r 7-- modified for printing 1st 10 outputs')
i = 1
count=0
while i <= 100:
    if i % 4 == 0 or i % 5 == 0 or i % 7 == 0:
        count = count + 1
        if count <= 10:
            print('count=', count,'|', i)



    i += 1
print('==this code ends====')
#g = [1,23,edkskdh jm lkcj klh lc klch jhcgb j j,gc gnkcj n , k cgbct c lcsjh ]
#for i in g:
#   print(g[1])

# reverse printing
x = 10
while x >= 1:
    print(x)
    x -= 1

a = [1, 2, 3, 4, 5]
print(a[::-1])
print(a[::1])
print(a[-1::])

print('--------while 15 to 30---------')
print('--------Without Validation------')

start = int(input('Enter num 1 :'))
end = int(input('enter num 2 : '))
while start <= end:
    print(start)
    start += 1
print('=====this program ends======')

print('====updated======')
start = int(input('Enter num 1 :'))
end = int(input('Enter num 2 : '))
if start <= end:
    while start <= end:
        print(start)
        start += 1
else:
    print('#### start value should be less than end value ###')
print('**** End of the program****')
'''
'''
# Even numbers printing
n1 = int(input('Enter no 1 :'))
n2 = int(input('enter num 2 : '))
while n1 <= n2:
    if n1 % 2 == 0:
        print(n1)
    n1 += 1

#print numbers from 500 to 600 divisible by 9

n1 = 500
n2 = 600
if n1 <= n2:
    while n1 <= n2:
        if n1 % 9 == 0:
            print(n1)
        n1 += 1
else:
    print(' Invalid input data')
# Print numbers between 1 to 100 which are divisible by 5 and 3
n1 = 1
n2 = 100
if n1 <= n2:
    while n1 <= n2:
        if n1 % 5 == 0 and n1 % 3 == 0:
            print(n1)
else:
    print('Invalid i/p data')
'''
'''
print('---odd nos------')
n1 = 1
n2 = 21
while n1 <= n2:
    if n1 % 2 == 1:
        print(n1)
    n1 += 1

print('-------- Divisible by 3 and 5------------')
num1 = 1
num2 = 100
while num1 <= num2:
    if num1 % 3 == 0 and num1 % 5 == 0:
        print(num1)
    num1 += 1
print('code ends------------')

print('=====Even numbers b/w 1 - 20 =====')
x = 1
li = []
while x <=20:
    if x % 2 == 0:
        li.append(x)
    x += 1
print('Even numbers: ', li)

# print numbers divissible by 5 b/w 1 to 100
print('Divisible by 5======')
n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 5 == 0:
        print(n1)
    n1 += 1
print('code ended')

print('====Divisible by 3 and 7 ========')
n1 = 1
n2 = 120

while n1 <= n2:
    if n1 % 3 == 0 and n1 % 7 == 0:
        print(n1)
    n1 += 1
print(' code ends here')

print('============ Divisible by 5 or 6')
n1 = 100
n2 = 150
while n1 <= n2:
    if n1 % 5 == 0 or n1 % 6 ==0:
        print(n1)
    n1 += 1
print('Section ends here$$$$$$$$$$$')

print(' ---------- Numbers ending with 0 -------------')
n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 10 == 0:
        print(n1)
    n1 += 1
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

print(' nos 1 to 10')
num = 1
while num <= 10:
    print(num)
    num = num + 1
print(' end of pgm')

num = 1
while num <= 20:
    if num < 10:
        print(num, end='-')  # print ln # \n
    else:
        print(num)
    num += 1

print('---- Print even numbers------')
#State
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# Print nos from 2 to 100 divisibleby 3 & 4
print('------divisible by 3 and 4 -------')
num = 2
while num <= 100:
    if num % 3 == 0 and num % 4 == 0:
        print(num)
    num += 1

print('====== print odd numbersw =======')
num = 10
while num <= 20:
    if num % 2== 1:
        print(num)
    num += 1

# numbers b/w 500 and 600 and divisible by 5
print('====numbers divisible by 5========')
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1

# Print numbers b/w 500 and 1000. It should be divisibe by 5 and 8
print('--Numbers divisible with 5 & 8')
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# print nos b/w 500 to 1k. it should be divisible by 5 or 9
print('numbers divisible by 5 or 9******')
num = 500
while num <= 1000:
    if num % 5 == 0 or num % 9 ==0:
        print(num)
    num += 1
'''
# prit 0 to 100 and divisible by 4
print('========== numbs b/w 0 to 100===========')
x = 0
while x <= 100:
    if x % 4 == 0:
        print(x)
    x += 1

#print no which are divisible by either 3 or 8 b/w 1 to 1000
print('====== either 3 or 8 between 1 to 1k=======')
x = 1
while x <=1000:
    if x % 3 == 0 or x % 8 == 0:
        print(x)
    x += 1


def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(0, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


# Driver function to check the above function
a =  (-10, 2, 3, -2, 0, 5, -15)
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))

print("++++++++++++++++++++++++++++++++++++")
A = [1, 2, 3, 'a']
B = [1, 1, 'a', 'e']


print(len(A))
#A = [1, 2, 3, 'ae']
#B = [1, 1, 'b', 6]
C = []
#C = [sum(i) for i in zip(A, B )]
for i in range(0, len(A)):
    if (type(A[i]) == str or type(B[i]) == str) or ((A[i] + B[i]) % 2 == 1):
        C.append(0)
    else:
        C.append(A[i] + B[i])
print(C)
def most_frequent(C):
    return max(set(C), key = C.count)
print(most_frequent(C))
print('============================================================')
a = [['A','Laptop'],['A','Laptop'],['A','Mouse'],['B','Laptop'],['A','Headset'],['B','Headset']]
A = ['Laptop', 'Mouse', 'Headset']
B = ['Laptop', 'Headset']
D = []
if A[0]==B[0] or A[0] == B[1]:
    D.append(A[0])
    #if A[1]== B[0] or A[1] == B[1]:
            #D.append(A[1])
    if A[2] == B[0] or A[2] == B[1]:
        D.append(A[2])
E = ['A','B', D]
print(E)


#for i in range(0, len(A)):
#    if A[i] == B[i]:
#        print(D, i)

count_A = 0
count_B = 0
count_H = 0
count_L = 0
temp = []
o3 = []
for l in a:
    if l not in a:
        o3.append(l)
print(o3)
for i in a:
    if i[0] == 'A':
        count_A += 1
    if i[0] == 'B':
        count_B += 1
    if i[0] == 'Laptop':
        count_L += 1
    if i[0] == 'Headset':
        count_H += 1
    if count_A and count_B and count_L and count_H >= 2:
        o3.append([['A', 'B', 'Laptop', 'Headset']])
temp.append([['A',count_A],['B',count_B]])
print(temp)
print(o3)
print([['A', 'Laptop',a.count(['A','Laptop'])],['A','Mouse',a.count(['A','Mouse'])],
      ['B','Laptop',a.count(['B','Laptop'])],['A','Headset',a.count(['A','Headset'])],
      ['B','Headset',a.count(['B','Headset'])]])



if count_A and count_B and count_L and count_H >=2:
    o3.append(['A', 'B', ['Laptop', 'Headset']])
#        break
#    if count_B >= 2:
#       o3.append(['B'])
#    if count_L and count_H >=2:
#       o3.append([['Laptop', 'Headset']])

print(o3)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


# Returns floor of square root of x
def floorSqrt(x):
    # Base cases
    if (x == 0 or x == 1):
        return x

    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1;
    result = 1
    while (result <= x):
        i += 1
        result = i * i

    return i - 1


# Driver Code
x = 27
print(floorSqrt(x))

list_of_lists = [['a', 1], ['b', 2], ['a', 1], ['b', 2], ['c', 3]]


new_list = []

for l in list_of_lists:
    if l not in new_list:
        new_list.append(l)
print(new_list)
##################################################################################################################

class newNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class newNode:
    def _init_(self, data):
        self.data = data
        self.left = self.right = None
# A utility function to print inorder
# traversal of a Binary Tree
def printInorder(node):
    if (node == None):
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)
# A recursive function to construct Full
# binary tree from pre[] and preM[].
# preIndex is used to keep track of index
# in pre[]. l is low index and h is high
# index for the current subarray in preM[]
def constructBinaryTreeUtil(pre, preM, preIndex, l, h, size):
    # Base case
    if (preIndex >= size or l > h):
        return None, preIndex
    # The first node in preorder traversal
    # is root. So take the node at preIndex
    # from preorder and make it root, and
    # increment preIndex
    root = newNode(pre[preIndex])
    preIndex += 1
    # If the current subarray has only
    # one element, no need to recur
    if (l == h):
        return root, preIndex
    # Search the next element of
    # pre[] in preM[]
    i = 0
    for i in range(l, h + 1):
        if (pre[preIndex] == preM[i]):
            break
    # construct left and right subtrees
    # recursively
    if (i <= h):
        root.left, preIndex = constructBinaryTreeUtil(pre, preM, preIndex, i, h, size)
        root.right, preIndex = constructBinaryTreeUtil(pre, preM, preIndex, l + 1, i - 1, size)
    # return root
    return root, preIndex
# function to construct full binary tree
# using its preorder traversal and preorder
# traversal of its mirror tree
def constructBinaryTree(root, pre, preMirror, size):
    preIndex = 0
    preMIndex = 0

    root, x = constructBinaryTreeUtil(pre, preMirror, preIndex, 0, size - 1, size)
    printInorder(root)
# Driver code
if _name_ == "_main_":
    preOrder = [4, 7, 9, 6, 2, 3, 1]
    preOrderMirror = [4, 2, 1, 3, 7, 9, 6]
    size = 7
    root = newNode(0)
    constructBinaryTree(root, preOrder, preOrderMirror, size)