# control statements : break continue pass
# con stat in while/ for
# print 1st 25 even nums without 10 multiplier values between 1 to 100
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        if i % 10 == 0:
            continue
        print(i)
        count += 1
        if count == 25:
            break
print('------------End of progrqam-----------------------')

count = 0
for val in range(1, 101):
    if val % 2 == 0:
        print(val)
        count += 1
        if count ==7:
            break

# REQ: Print first 7 even numbers between 1 to 100
count = 0
for val in range(0, 101):
    if val % 2 == 0:
        print(val)
        count += 1
        if count == 7:
            break
print('-----------end of the program---------------')

st = int(input('Enter st value '))
end = int(input('ender end value'))
counter = 0
# add validation
for val in range(st, end+1):
    if val % 2 == 0:
        print(val)
        counter += 1
        if counter == 7:
            break
print(' end of loop')

print("----Print only first 7 numbers-------")
count = 0
for val in range(1, 101):
    if val % 2 == 0:
        count += 1
        print(val)
        if count == 7:
            break
print("After for loop break")
num = 1
counter = 0
while num <=100:
    if counter > 7:
        break
    if num % 2 == 0:
        print(num)
        counter += 1
    num += 1
print('Exited while loop')
print('=========Using for loop============')
counter = 0
for val in range(1, 101):
    if val % 2 == 0:
        print(val)
        counter += 1
        if counter == 7:
            break
print('End of loop$$$$$$$$$$$$$$$$$$$$')

print("----Other program-------")
# Print even numbers between 50 to 80
for val in range(1, 101):
    if val >= 50 and val <= 80:  # val > 49 and val < 81
        if val % 2 == 0:
            print(val)
    elif val > 80:
        break
print("End of for loop")

print("--------For loop with String-------")
msg = 'Hello World'

for char in msg:
    print("Character : ", char)

for element in msg:
    print("Character : ", element)








