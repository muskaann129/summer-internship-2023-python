# Calculator
# a = int(input("Enter first number: \n"))
# b = int(input("Enter Second number: \n"))
# c = str(input("Enter the operation!: \n"))
# def calc(a,b,c):
#     if c=="+":
#         return a+b
#     elif c=="-":
#         return a-b
#     elif c=="*":
#         return a*b
#     elif c=="/":    
#         try:
#             return a/b
#         except:
#             print("0 can not be divided by 0")
#     elif c=="//":
#         return a//b
#     elif c=="%":
#         return a%b
#     else:
#         return "Invalid input !!"

# print(calc(a,b,c))

# Stone Paper siccor
# import random

# def stonePaperSiccor():
#     inp = int(input("Enter 1(for stone), 2(for paper), 3(scissor): \n"))
#     a = random.randint(1,3)
#     if a==1:
#         comp = "Stone"
#     elif a==2:
#         comp = "Paper"
#     else:
#         comp = "Scissor"

#     print("computer choose", comp)
    
#     if inp == 1 and comp == "Stone":
#         return("Computer wins!!")
#     elif inp == 1 and comp == "Scissor":
#         return("You win!!")
#     elif inp == 2 and comp == "Stone":
#         return("You win!!")
#     elif inp == 2 and comp == "Scissor":
#         return("Computer wins!!")
#     elif inp == 3 and comp == "Stone":
#         return("Computer wins!!")
#     elif inp == 3 and comp == "Paper":
#         return("You win!!")
#     else:
#         return("Game tie!!")

# print(stonePaperSiccor())

# tareeka 2

import random
lst=["rock", "paper", "Scissor"]
a=input("Enter yout choise: ").lower()
rno = random.choices(lst)
print(f'CPU choose {rno}')
print(f'you chosoe {a}')
if a==rno:
    print("Game tie")
elif (a==lst[1] and rno==lst[1]) or(a==lst[2] and rno==lst[1]) or(a==lst[0] and rno==lst[2]):
    print("You won!!")
else:
    print("CPU won!!")


# class className:
#       def run(self):
#         return("hello")

# a = className()
# a.run()



# array of random num
# import random
# b=[]
# def randomNum():
#     for i in range(4):
#         a = random.randint(1,100)
#         b.append(a)
#     return b
# return(randomNum())



# Multiple
# def mul(value):
#     count = 0
#     for i in range(1,value+1):
#         if value%i==0:
#             count+=1;
#     return count

# print(mul(125))





# a = "sh2973sgh28"

# countInt = 0
# countStr = 0
# for i in a:
#     try:
#         int(i)
#         countInt+=1
#     except:
#         countStr+=1

# print(f"integer are {countInt} and string are {countStr}")

       
