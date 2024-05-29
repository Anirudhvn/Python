# l1=[1,2,3,4,5,6]
# l2=[x**2 for x in l1]
# print(l2)

# friuts=['apple','banana','cherry','blueberry','mango','orange']
# new=[i for i in friuts if 'a' in i]
# print(new)

# friuts=['apple','banana','cherry','blueberry','mango','orange']
# new=[len(i) for i in friuts if 'a' in i]
# print(new)

# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[i for i in l1 if i%2==0]
# print(l2)

# def squre(x):
#     return x**2

# l1=[1,2,3,4,5,6]
# l2=[squre(x) for x in l1]
# print(l2)


# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# flattened=[num for row in matrix for num in row]
# print(flattened)

# l1=[1,2,3,4,5,6,7,8,9]
# l2=["even" if x%2==0 else "odd" for x in l1]    #first condtion then for loop
# print(l2)

# l1=["apple", "banana", "cherry", "date"]
# l2=[i.upper() for i in l1 if len(i)>4]
# print(l2)

# l1=["apple", "banana", "cherry", "date"]
# l2=[i[0] for i in l1 ]
# print(l2)

#zip

# l1=[1,2,3]
# l2=[4,5,6]
# # l3=zip(l1,l2)
# # print(list(l3))
# l3=[x*y for x,y in zip(l1,l2)]
# print(l3)

# l1=[1,2,3,4,5,6,7,8,9]
# l2=[(x,x**2) for x in l1 if x%2==0]
# print(l2)


