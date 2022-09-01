from sys import getsizeof

mess = 'hello world '
print('====== message 1======== ', mess)
mess2 = 'PYTHON PROGRAMING'
print('-------- message 2 ------', mess2)

# Indexing
print('----- 1st index in message 1 ----', mess[4])
print('====== 4th index in message 1 ===== Positive :', mess[1],' Negative : ', mess[-11])

# Slicing
print('Slicing positive : ', mess[6:11])
print('slicing megative : ', mess[-6:-1])
print('Sicing with start stop step :', mess2[0:13:1], '==', mess2[0:13], ' ', mess2[0:13:2]," ",mess2[0:13:3])
print("Slicing without any positions + :",mess2[::],"  ",mess2[2::]," ",mess2[:8:]," ",mess2[::2]," ",mess2[::3])
print('Slicing without any positions - :', mess2[::], ' ', mess2[-2::], ' ', mess2[:-8:], '  ', mess2[::-2], '  ', mess2[::-3])


# Adding Concattination
final_message = mess + ' Welcome to ' + mess2
print('Concatenation :: ', final_message)

# Multiplying
print("Multiplivation :", mess*4)
print('Multiplicaation :: ', final_message*4)

# Checking for Membership
print('-- Membership --- :', 'PYTHON' in mess2)

#Built in String methods
print('-- Capitalize ---', mess.capitalize())
print('Count---------- ', mess2.count('O'), ' ', mess2.count('O', 6, 15))

#String formating Operators
print('My name is %s and weight is %d kg!' % ('Zara', 21))

# ASCII Unicode
str1 = 'Akshay'
str2 = u'Akshay'
print(str1, ' ', len(str1), ' ', len(str2))
print(getsizeof(str1), ' ', getsizeof(str2))