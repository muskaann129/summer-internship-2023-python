import random
a=[]
inp = input("Enter name: ")
while inp.lower()!="exit":
    inp = str(input("Enter name: "))
    if inp.lower()=='exit':
        break
    a.append(inp)
guess = random.randint(0,len(a))
print(f'{a[guess]} wins the lottery!!')