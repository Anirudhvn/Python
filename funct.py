# def jagan(a):
#     print(a)





# jagan(123)
# print("-------------------------------------------------------")
# jagan(234)


# def square(num):
#     b=num**2
#     return b

# a=int(input())
# print(square(a))

# def function(n1,n2=20):
#         sub=n1-n2
#         return sub


# a=function(30)
# print(a)

# a=function(50)
# print(a)

# def func(a,b):
#     print("value of a:",a)
#     print("value of b:",b)

# a=int(input("Enter value of a:"))
# b=int(input("Enter the value of b:"))
# func(b,a)


# def add(a,b):
#     c=a+b
#     return c
# a=int(input("enter value of a"))
# b=int(input("enter value of b"))
# print(add(a,b))


# def fact(a):
#     if a==1:
#         return 1
#     else:
#         return a*fact(a-1)

# a=int(input("enter the value of a:"))
# b=fact(a)
# print(b)

# def add(x,y):
#     return x+y
# print(add(6,5))


# a=lambda x,y : x*y 
# print(a(6,5))



# d=lambda a: a%2==0
# print(d(6))

# def add(a,b,c):
#     return a+b+c
# print(add(2,3,4))

# q=lambda a,b,c: a+b+c
# print(q(2,3,4))


# a=10
# b=20
# c=30
# # print(f" the digit {a} is even")

# print("the digit is {} , {} and {} is even".format(a,b,c))


# def even(a):
#     if a%2==0:
#         return "{} is even".format(a)
#     else:
#         return "{} is odd".format(a)
# list1=[1,2,3,4,5,6,7,8,9,10]
# x=map(even,list1)
# print(list(x))

# def even(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# list1=[1,2,3,4,5,6,7,8,9,10]
# x=filter(even,list1)
# print(list(x))

# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda n: n%2==0 , list1)))
