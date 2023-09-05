a = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
import random 
def printBoard():
  print(f'{a[0]} | {a[1]} | {a[2]}')
  print("--|---|--")
  print(f'{a[3]} | {a[4]} | {a[5]}')
  print("--|---|--")
  print(f'{a[6]} | {a[7]} | {a[8]}')

all = []
dct = {"O":[],"X":[]}
check = True
play = ["O","X"]
start = 1
win = False
whowin = None
wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

while check:
  printBoard()
  if start == 1:    
      print("X's chance")
      try:
        value = int(input("Enter the position: "))
        a[value] = "X"
        if value>8 and value in all:
          break
      except:
        continue
  else:  
      randNums = [num for num in range(9) if num not in all]
      value = random.choice(randNums)
      print(f"O's chance, CPU chose {value}")
      a[value] = "O"
  all.append(value)
  dct[play[start]].append(value)
  print(dct)
  print(all)
  count = 0
  if len(all)>5:
    for i in wins:
      for j in i:
        for k in dct["O"]:
          if j==k:
            count+=1
        if count>=3:
          check=False
          win=True
          whowin="O"
          break
        else:
          count=0
        for k in dct["X"]:
          if j==k:
            count+=1
        if count>=3:
          win=True
          check=False
          whowin="X"
          break
        else:
          count=0
  elif len(all)==8:
    check=False
  if start==0:start+=1
  else:start=0
printBoard()
if win == True:
  print(f"Game WON BY {whowin}")
else:
  print("Game Tie")