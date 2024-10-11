# for x in range(1,11):
#     print(f"hello who are you {x}")



# #Q. To display numbers from 21 to 1 in descending order:
#     for x in range(11,1,-2):
#             print(x)

# #Q. To print the sum of numbers in the given list:

# list = eval(input("Enter the list: "))
# sum = 0
# for x in list:
#       sum = sum + x 
# print(sum)

#Q. Write a program to display the characteristics of given string index wise (both positive and negative)

s = input('Enter the str:')
i=0
for x in s:
    print('The Character present at +v index: {} and -ve index: {} is: {}'.format(i, i-len(s), x))
    i=i+1