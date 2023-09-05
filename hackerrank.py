# s = "hello world"
# new = s.split(" ")
# ss=[]
# for i in range(len(new)):
#     word = new[i].capitalize()
#     ss.append(word)
#     line = " ".join(ss)
# print(line)


# set 
arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
arr = set(arr)
add = 0
for i in arr:
    add = add + i 
avg = add/len(arr)
print(avg)
