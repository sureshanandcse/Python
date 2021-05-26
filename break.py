for i in range(10):
    if i == 5:
        break    # terminate loop
    print(i)
print("out side the loop")
  
for i in range(10):
    if i == 5:
        continue    # skip the current iteration
    print(i)
print("out side the loop")

for i in range(10):
    if i == 5:
        pass    # null operation NOP
    print(i)
print("out side the loop")
