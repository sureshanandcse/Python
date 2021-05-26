n=int(input("enter a number to find square root"))
h=int(input("enter no of approximation iterations"))
approx = 0.5 * n
for i in range(h):
  betterapprox = 0.5 * (approx + n/approx)
  approx = betterapprox

print(approx)

print("another way")
n=int(input("enter a number to find square root"))

approx = 0.5 * n
better = 0.5 * (approx + n/approx)
while better != approx:
    approx = better
    better = 0.5 * (approx + n/approx)
print(approx)

