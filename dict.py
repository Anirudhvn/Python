# capital={"Kerala":"Thiruvananthapuram","TN":"Chennai"}
# print("initian dictionary",capital)
# capital["Telengana"]="Hydrabad"
# print (capital)


a={1:"Apple",2:"Banana",3:"Carrot"}
a[4]="JackFruit" #adding element
print(a)

a[2]="Pineapple" #changing element
print(a)

print(a[4]) #calling element

del (a[1]) #removing element
print(a)

#nested dictionary
family={"child1":{"name":"emi","year":2004},"child2":{"name":"este","year":2005}}
print(family)

q=a.copy() #copy a dictionary
print(q)