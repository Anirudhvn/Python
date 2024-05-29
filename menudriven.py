# #simple calculator


# def add(a,b):
#     c=a+b
#     print(c)

# def sub(a,b):
#     c=a-b
#     print(c)

# def mul(a,b):
#     c=a*b
#     print(c)

# def div(a,b):
#     c=a/b
#     print(c)

# while True:
#     print("Menu")
#     print("1. add")
#     print("2. sub")
#     print("3. mul")
#     print("4. div")
#     print("5. exit")
#     choise=int(input("eneter the choise"))

#     if choise==1:
#         a=int(input("1st no. "))
#         b=int(input("2nd no. "))
#         add(a,b)

#     elif choise==2:
#         a=int(input("1st no. "))
#         b=int(input("2nd no. "))
#         sub(a,b)

#     elif choise==3:
#         a=int(input("1st no. "))
#         b=int(input("2nd no. "))
#         mul(a,b)

#     elif choise==4:
#         a=int(input("1st no. "))
#         b=int(input("2nd no. "))
#         div(a,b)

#     elif choise==5:
#         break


#banking system

account={}

def create_acc(account):
    acc=int(input("enter acc no."))
    amt=float(input("enter initial amt"))
    account[acc]=amt
    print("balance:",account[acc])
    print("amt added successfuly")

def deposit_amt(account):
    acc=int(input("enter account no."))
    amt=float(input("enter amt to deposit"))
    if acc in account:
        account[acc] += amt
        print("amt deposited successfully")
        print("balance:",account[acc])
    else:
        print("acc not found")

    
def withdraw_amt(account):
    acc=int(input("enter acc no."))
    if acc in account:
        amt=float(input("enter amt to withdraw"))
        if amt <= account[acc]:
            account[acc] -= amt
            print("balance:",account[acc])
        else:
            print("insufficient balance")
    else:
        print("acc not found")

def delete_acc(account):
    acc=int(input("enter acc no."))
    if acc in account:
        account.pop(acc)
        print("account deleted successfully")
    else:
        print("acc not found")


while True:
    print("menu:")
    print("1. create acc")
    print("2. deposite amt")
    print("3. withdraw amt")
    print("4. delete acc")
    print("5. exit")
    ch=int(input("enter your choise"))

    if ch==1:
        create_acc(account)
    elif ch==2:
        deposit_amt(account)
    elif ch==3:
        withdraw_amt(account)
    elif ch==4:
        delete_acc(account)
    elif ch==5:
        break
    else:
        print("not a choise")
