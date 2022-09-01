'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

x = 'amazing'
print(x[1:5])
'''
'''
sum = 0
for x in range(1, 5):
    result = 5 * x
    sum += result
print('Sum : ', sum)

n1 = int(input('Enter num 1 : '))
n2 = int(input('enter num 2 :'))

for val in range(n1, n2):
    print(val)
'''
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print('Total = ', sum)

#Data types
#x = 10
#x = 10.5
#is_male = True

print('-------------String------------------')
#for loop with strings
message = 'Hello World'
print(message)
for char in message:
    print(char)
print('End of the program')

number = '12345'
for num in number:
    print(num)
print('=======List====================')
# for loop with list
numbers = [1, 2, 3, 4, 5]
for value in numbers:
    print(value)
print('End for loop')

numbers = ['1', '2', '3', '4', '5',]
for value in numbers:
    print(value)
print(' end of loop')

numbers = (1, 2, 3, 4, 5)
print('====================Tuple===================')
for val in numbers:
    print(val)

print('===========Dictionary=======================')
emp_det = {'eid': 100, 'nam': 'Madhu', 'sal': 10000}
print('----Items-----')
for key, val in emp_det.items():
    print(key, ' : ', val)

print('----keys-----')
for key in emp_det.keys():
    print(key)

print('======values=========')
for val in emp_det.values():
    print(val)

print('=========Set==============')
emp_ids = {1, 2, 3, 4, 5, 6}
for eid in emp_ids:
    print(eid)

