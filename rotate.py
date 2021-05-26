def rotate(l, n):
    return l[n:] + l[:n] # forward direction
    #return l[-n:] + l[:-n] #reverse direction

l = [1,2,3,4,5,6,7,8]
r=int(input("enter no of elements to rotate"))
print (l[:r])  # print first r elements
print (l[r:])  # skip first r elements

print (l[r:] + l[:r]) 
print (rotate(l,r))
