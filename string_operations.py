#string operation in python
name = "Suresh Anand M" 

fullname = name 
name = str("Suresh Anand M") 
#indexing
 #name[4]='s' #throws error bcos string is immutable
print(name[0])
print(name[5])
print(name[-1])
for i in name:
      print(i,end="")
#slicing  name[start:end]
print(name[0:10])
print(name[0:])
print(name[:10])
print(name[:])
s1="sri"
s2="sairam"
s3=s1+s2  #concatenation
print(s3)
s3+="Engineering college" #appending
print(s3)
print(s1*5)  #multiplication
