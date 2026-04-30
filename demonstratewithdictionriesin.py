dict1 = {'StdNo':'532','StuName': 'Naveen', 'StuAge': 21, 'StuCity': 'Hyderabad'}
print("\n Dictionary is :",dict1)
#Accessing specific values 
print("\n Student Name is :",dict1['StuName'])
print("\n Student City is :",dict1['StuCity'])
#Display all Keys
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
#Display all values
print("\n All Values in Dictionary ")
for x in dict1:
    print(dict1[x])
#Adding items
dict1["Phno"]=85457854
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Change values
dict1["StuName"]="Madhu"
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Removing Items
dict1.pop("StuAge");
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Length of Dictionary
