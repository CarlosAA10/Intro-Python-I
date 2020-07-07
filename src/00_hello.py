# Print "Hello, world!" to your terminal

print('Hello World')

def double(x):
    return x * 2

lis = [10,11,12,13,14]

#another list to store doubled values 

# doubled = []

# call our double function on every element in the list 
# for x in lis:
#     d = double(x)
#     doubled.append(d) 

doubled = [double(x) for x in lis]

#List comprehension to copy the elements of lis 
# and populate another list with them 
copy_of_lis = [x for x in lis]

#List comprehension to copy the even elements of lis 
# and populate another list with them 

evens_of_lis = [x for x in lis if x % 2 == 0]

# List comprehension format 
# [
#   `return `
# 
# 
# 
# ]

evens_of_lis = []

#looping through each element of lis
for x in lis:
    # check if the element is even
    if x % 2 == 0:
        #if it is, append it to evens_of_lis
        evens_of_lis.append(x)

# the loop part where we're accessing "outside"
# the initial part says how we want to treat that element
# the fact that spelled this out between brackets means we 
# want all these elements in a list 

print(doubled)
print(evens_of_lis)