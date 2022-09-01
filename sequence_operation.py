# SEQUENCE OPERATIONS
message = 'HELLO WORLD'
print('-----------1. Indexing --------------')

print("4th index : ", message[4])
print("5th index : ", message[5])
print("7th index : ", message[7])
print("9th index : ", message[9])
print("9th index : ", message[-2])
print("10th index : ", message[10])
print("10th index : ", message[-1])
print('============================================')
l = ['ekm', 'bbb', 'ccc']
n = []
for i in l:
    n.append(i[1:2])

print(n)
print('********************************************')
print('----------- 2. Slicing ------------------')
message  = 'Hello-World'
print('o to 5 : ', message[0:5])
print('2 to5 : ', message[2:5])
print('3 to 7 :', message[3:7] )
print('-9 to 5:', message[-9:5])

print('----------- 3. Adding -------------')
str1 = 'Hello'
str2 = 'World'
print('Addition1 :', str1 + str2)
print('Addition 2 :', str1 + ' ' + str2)

print('====== 4. Multiplication =========')
print('Multiplication : ', str1 * 4)

print('----------- 5. Membership -----------')
print('H : ', 'H' in 'HELLO-PYTHON')
print('L : ', 'L' in 'HELLO-PYTHON')
print('LL : ', 'LL' in 'HELLO-PYTHON')
print('PH :', 'PH' in 'HELLO-PYTHON')
print('- :', '-' not in 'HELLO-PYTHON')
print('Space :', ' ' not in 'HELLO-PYTHON')
print('B :', 'B' not in 'HELLO-PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)

str1 = 'Hello-World'
print('--------- 6. Length --------')
print('Length of string : ', len(str1))

print('======= 7. Max =============')
print('Max of string : ', max(str1))
print('**********')
