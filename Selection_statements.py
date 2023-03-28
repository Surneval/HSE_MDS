#user enters a number, we check is it even or odd
# number = int(input('your number'))
# if number % 2 == 0:
#     print('even')
# else:
#     print('odd')
# isEven = number % 2 == 0
# print("Is even?:", isEven)

##comparison operators
# x = int(input('First number:'))
# y = int(input('Second number:'))
# print(x > y)
# print(x < y)

#comparing strings
# password = input("Enter your password: ")
# isCorrect = password == "Qwerty"
# print('Is correct?: ', isCorrect)
# print(ord('Q'))
# print(ord("q"))

### identity operators
# is and is not

# a = int(input())
# b = int(input())
#
# print(id(a))
# print(id(b))
# print(id(a) == id(b))
# print(a is b)
# print(a is not b)

###if statement
# age = int(input('How old are you? '))
# eligibility = False
# if age >= 18:
#     eligibility = True
#     print("Eligible! you can proceed! ")

### if else statement
# num = int(input())
# if num > 0:
#     print('positive')
# else:
#     print('negative or zero')

##traffic estimation
# traffic_fration = float(input())
# if traffic_fration > 0.5:
#     print('High traffic!')
# else:
#     print('Low traffic!')

###If-Elif-Else Statement Practice
# num = int(input())
#
# if num > 0:
#     print('positive')
# elif num < 0:
#     print("negative")
# else:
#     print( 'number equals to zero')

### users classification

# light User 1-2 visits
# medium user 2-10 visits
# heavy user 10+ visits
numVisits = int(input())
# if numVisits >= 10:
#     print('Heavy user')
# elif 2 < numVisits < 10:
#     print('medium user')
# else:
#     print('light user')

## nested condition
if numVisits > 2:
    if numVisits < 10:
        print('medium user')
    else:
        print('Heavy user')
else:
    print('light user')