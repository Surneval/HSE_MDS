# print('Hello user')
#
# #Input part
# username = input("Input your username \n")
# password = input("input your password \n")
#
# #Output part
# print("Username", username, sep=": ", end="\n")
# print("Password", password, sep=": ")

# #math task
# part1 = int(input())
# part2 = int(input())
# part3 = int(input())
# part4 = int(input())
#
# print("Your grade: ", 0.25 * part1 + 0.25 * part2 + 0.25 * part3 + 0.25 * part4)

# name = input('What is your name? ')
# print('Hello ', name, "!", sep= "")

# expression = '2 + 2 ='
# res = 2+2
# print(expression, str(res), sep= " ")
# username = input()
# print('Hello, ', username, "!", sep= "")


# number = int(input())
# h = "/\___/\    "
# m = "(=^o^=)    "
# l = '(") (")__/ '
# print(number * h)
# print(number * m)
# print(number * l)

# num = float(input())
# print(int(num))

# a = int(input())
# b = int(input())
# c = (a * a + b * b) ** 0.5
# print(c)

# number = int(input())
# third_digit = number % 10
# number //= 10
# second_digit = number % 10
# number //= 10
# first_digit = number % 10
#
# sum = first_digit + second_digit + third_digit
# print(sum)


# n = int(input())
# k = int(input())
# for i in range(k):
#     n = n // 10
#
# print(n)

# cel = float(input())
# far = cel * 1.8 + 32
# print(cel, "°C is equal to ", far, "°F", sep="")

# n = int(input())
# lives = 256
# result = n % lives
# print(result)

n = int(input())
sec = n % 60
min = n // 60
m = min % 60
h = min // 60
if sec < 10 and m < 10:
    print(h,":", '0',str(m),":", "0", str(sec), sep="")
elif sec < 10 and m > 10:
    print(h, ":", str(m), ":", "0", str(sec), sep="")
elif sec > 10 and m < 10:
    print(h,":", '0',str(m),":", str(sec), sep="")
else:
    print(h,":",m,":", sec, sep="")