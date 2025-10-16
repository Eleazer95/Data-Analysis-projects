'''
name="Jack"
print(name)
'''
'''
name = "Jack"
print(Name)
'''

"""#changing case in a string with methods
info="iNfOrMaTiOn"

#using title()
print(info.title())

#using upper()
print(info.upper())

#using lower()
print(info.lower())
"""

"""#String formatting
name="Alex"
age=34

#f-string
print(f"Hello there {name} you are {age}")

#format method()
print("Hello there {} you are {}".format(name,age))

#c-style string
print("Hello there %s you are %d"%(name,age))
"""

#Adding whitespaces to strings with tabs ("\t") or newline ("\n")
name2="\tAdam"
name3="\nJonathan\n"
"""print(name2)
print(name3)
"""

"""#removing whitespaces using lstrip()
print(name2.lstrip())
print(name3.lstrip())
"""
'''#removing whitespaces using rstrip()
print(name3.rstrip())
print(name3.strip())
'''

#Numbers
#integers
num1=34
#print(num1)


#floats
num2=44.22
#print(num2)

"""#convert to integer using int() function
print(int(num2))
"""

"""#convert to float using float() function
print(float(num1))
"""

"""#Simple Arithmetics
number1=52
number2=37
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(number1%number2)
print(number1**number2)
"""

"""#Underscore in numbers
oneMillion=1_000_000
print(oneMillion)
"""

"""#multiple assignment
name,course,age="Adam","Physics",34
print(name)
print(course)
print(age)"""

"""#Constants
NAME="Jade"
print(NAME)"""

"""#Introduction to list
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
print(namesList)
"""

#index position and accessing elements in a list
#namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
#print(namesList[-5])
#Using individual values from a list
#print(f"Hey there Mr. {namesList[3]}")

"""#Changing
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList[0]="Gabriel"
print(namesList)
"""

"""#Adding using append()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.append("Maverick")
print(namesList)
"""

"""#Adding Using insert()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.insert(4,"Allen")
print(namesList)
"""

"""#Removing using pop()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.pop(2)
namesList.pop()
print(namesList)
"""

"""namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.remove("Anthony")
print(namesList)

"""

"""#Removing using del
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
del namesList[1]
print(namesList)
"""

"""#with sort()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.sort()
print(namesList)"""

"""#with sorted()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
print(sorted(namesList))
print(namesList)
"""

"""#with reverse()
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.reverse()
print(namesList)"""

"""#reversing a sorted() list
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
namesList.sort()
namesList.reverse()
print(namesList)
"""

"""#len()
numberList=[23,24,31,37,15,17]
print(len(numberList))
"""

"""#sum()
numberList=[23,24,31,37,15,17]
print(sum(numberList))
"""

"""#min()
numberList=[23,24,31,37,15,17]
print(min(numberList))
"""

"""#max()
numberList=[23,24,31,37,15,17]
print(max(numberList))
"""

"""#Working with list
#Looping through a list
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
for name in namesList:
    print(name)
"""

"""#Doing more work withing a loop
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
for name in namesList:
    print(name)
    print(f"Hello there {name}")
"""

"""#Doing something after looping
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
for name in namesList:
    print(name)
    print(f"Hello there {name}")

print("That is all")
"""

"""#Avoiding Indentation error
namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
for name in namesList:
print(name)
print(f"Hello there {name}")
"""

"""#Using the range() function
#First variant
for n in range(10):
    print(n)
print("\n")
#Second Variant
for n in range(0,10):
    print(n)
print("\n")
#Third Variant
for n in range(0,10,1):
    print(n)
"""

"""#using range() to make a List of numbers
oneHundred=list(range(1,101))
print(oneHundred)
"""

#Simple statistics with a list of numbers
numbers=[23,22,21,19,4]
"""plusTwo=[]

for numb in numbers:
    add=numb**2
    plusTwo.append(add)
print(plusTwo)
"""

"""#List Comprehension
newPlusTwo=[(add**2) for add in numbers]
print(newPlusTwo)
"""

#Working with parts of a List
#Slicing a List
#namesList=["James","Samuel","Scott","Lucas","David","Anthony","Jeffrey"]
#print(namesList[2:5])
#Looping through a slice
"""for name in namesList[:4]:
    print(name)
"""

"""#Copying a List
copiedList=namesList[:]
print(copiedList)
"""

"""#Tuples
names=("Adam","Bryan","Shane","Joseph","Airvin")
print(names)
"""

"""#Looping through all values in a tuple
names=("Adam","Bryan","Shane","Joseph","Irvin")
for name in names:
    print(name)
"""

"""#writing over a value in a tuple
tupleContain=("Adam","Rufus","Shane","Rahul","Rupert")
print(tupleContain)

tupleContain=("Shelock","Robert","Anthony","Marshal")
print(tupleContain)

print("hello there {}".format(tupleContain[1]))"""

"""#Checking for equality
nameEql="Alex"
print(nameEql=="Alex")
"""

"""#Ignoring case when checking for equality
nameEql="Alex"
print(nameEql=="alex")
"""


"""#Checking for inequality
nameIneq="Anthony"
print(nameIneq!="Bryan")
"""

"""#Numerical Comparison
num1=43
print(num1==43)
"""

"""#Checking multiple conditions
numComp1=47
numComp2=51
numComp3=55
numComp4=57
print(numComp1<numComp2 and numComp3<=numComp4)
"""

"""#Checking whether a value is in a list
checkList1=[23,41,78,32,15,17]
print(41 in checkList1)
"""

"""#Checking whether a value is not in a list
checkList1=[23,41,78,32,15,17]
print(47 not in checkList1)
"""

"""#boolean expressions
first=True
second=False
print(f"First value is {first}")
print(f"Second value is {second}")
"""

"""#if statements
#Simple If statements
ifname="Adam"
if(ifname=="Adam"):
    print(f"Greetings {ifname}")
"""

"""#if-else statements
ifnameElse="Hey there"

if(ifnameElse=="Greetings"):
    print(f"Greetings {ifnameElse}")
else:
    print(f"{ifnameElse}, Mr. Alex")
"""

"""#if-elif-else chain
ifElifElse="Maybe tomorrow"
if(ifElifElse=="Today"):
    print(f"I would see you {ifElifElse}")

elif(ifElifElse=="Maybe tomorrow"):
    print(f"We would meet {ifElifElse}")

else:
    print("We would see")
"""
"""#Using multiple elif blocks
mult="What is 2 and 2"

if(mult=="2 plus 2"):
    print(f"{mult} = 8")

elif(mult=="2 times 4"):
    print(f"{mult} = 10")

elif(mult=="What is 2 and 2"):
    print(f"{mult} = 4")

else:
    print("No chance")
"""

"""#Checking whether a value is not in a list
checkList1=[23,41,78,32,15,17]
print(47 not in checkList1)"""

"""#boolean expressions
first=True
second=False
print(f"First value is {first}")
print(f"Second value is {second}")
"""

"""#Omitting the else block
mult="2 plus 2"
if(mult=="2 plus 2"):
    print(f"{mult} = 4")

elif(mult=="2 times 4"):
    print(f"{mult} = 10")

elif(mult=="What is 2 and 2"):
    print(f"{mult} = 4")
"""

"""#Testing multiple conditions
firstCon="Allen"
secondCon="Jason"
thirdCon="Ralph"

if(firstCon=="Allen"):
    print(f"Hello {firstCon}")

if(secondCon=="Jason"):
    print(f"Greetings there {secondCon}")

if(thirdCon=="Ralph"):
    print(f"Hi there {thirdCon}")
"""

"""#Checking for special items
ifList=["Adam","Thomas","Anthony","Mark","Allen","Sinath"]
for ifi in ifList:
    if ifi==ifList[0]:
        print(f"Hello there {ifi}")
    else:
        print(f"Greetings {ifi}")
"""

"""emptyList=[]
if emptyList:
    for empty in emptyList:
        print(empty)

else:
    create=["James","Adam","Jerry","Gerrald"]
    for crea in create:
        emptyList.append(crea)

    for empty in emptyList:
        print(empty)
"""

"""#Dictionaries
#A simple dictionary
dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
print(dictInfo)
"""

"""#Accessing values in a dictionary
dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
print(dictInfo["Name"])
"""

"""#Adding New Key value Pairs
dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

dictInfo["Score"]=88
print(dictInfo)
"""


"""#Starting with an empty dictionary
emptyDict={}
emptyDict["Name"]="Richard"
emptyDict["Course"]="Biology"
emptyDict["School"]="Yale"
print(emptyDict)
"""

"""#Modifying values in a dictionary
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
emptyDict["Name"]="Augustus"
print(emptyDict)
"""


"""#Removing key-Value Pairs
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

del emptyDict["Course"]
print(emptyDict)
"""

"""#Using get() to access unavailable values
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

strange=emptyDict.get("Age","Age not Available")
print(strange)
"""

"""#Looping through a dictionary
#Looping through all key-value pairs
dictLoop={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
for k,v in dictLoop.items():
    print(f"Key: {k}")
    print(f"Value: {v}")
    print("\n")
"""

"""#Looping through all the keys
dictLoop={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
for k in dictLoop.keys():
    print(f"Key: {k}")
    print("\n")
"""

"""#Looping through all the keys in a particular order
dictLoop={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
for k in sorted(dictLoop.keys()):
    print(f"Key: {k}")
    print("\n")
"""

"""#Looping through all values
dictLoop={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
for v in dictLoop.values():
    print(f"Value: {v}")
    print("\n")
"""

"""#nested For Loop
#7 and 8 times table
sevenAndEight=[7,8]
twelve=[1,2,3,4,5,6,7,8,9,10,11,12]
print("7 times")
for outV in sevenAndEight:
    for inV in twelve:
        print(f"{outV} x {inV} = {outV*inV}")
    print("\n8 times")
"""

"""#list in a list
innerList1=["Jack","Adam","Luke","David"]
innerList2=["Aaron","Thomas","Anthony","Mark"]

outerList=[innerList1,innerList2]
print(outerList)
for outV in outerList:
    for inV in outV:
        print(inV)
"""

"""#List in a Tuple
innerList1=["Jack","Adam","Luke","David"]
innerList2=["Aaron","Thomas","Anthony","Mark"]

outerTuple=(innerList1,innerList2)
print(outerTuple)

for outV in outerTuple:
    for inV in outV:
        print(inV)
"""

"""#List in a dictionary
dictList1=[12,25,22,23,28,31,30]
dictList2=[39,42,17,19,27,23,24]

dictNest={

    "First List":dictList1,
    "Second List":dictList2
}
print(dictNest)
for f,s in dictNest.items():
    print(f"Key: {f}")
    for sVal in s:
        print(f"Value: {sVal}")
    print("\n")
"""

"""#Tuple in List
tupleList1=(12,25,22,23,28,31,30)
tupleList2=(39,42,17,19,27,23,24)

listNest=[tupleList2,tupleList2]
print(listNest)
for tup in listNest:
    for t in tup:
        print(t)
"""

"""#Tuple in tuple
tupleList1=(12,25,22,23,28,31,30)
tupleList2=(39,42,17,19,27,23,24)

tupleNest=(tupleList1,tupleList2)
print(tupleNest)
for tup in tupleNest:
    for t in tup:
        print(t)"""

"""#Tuple in Dictionary
tupleList1=(12,25,22,23,28,31,30)
tupleList2=(39,42,17,19,27,23,24)

dictNest2={
    "First Tuple":tupleList1,
    "Second Tuple":tupleList2
}
print(dictNest2)

for f,s in dictNest2.items():
    print(f"key:{f}")
    for sVal in s:
        print(sVal)
"""

"""#Dictionary in List
dict1={
    "Name":"David",
    "Age":37,
    "Course":"Physics"
}
dict2={
    "Name":"Jerry",
    "Age":31,
    "Course":"Biology"
}

listDict=[dict1,dict2]
print(listDict)

for item in listDict:
    for it1,it2 in item.items():
        print(f"Key:{it1}")
        print(f"Value: {it2}")
    print("\n")
"""

"""#Dictionary in a tuple
dict1={
    "Name":"David",
    "Age":37,
    "Course":"Physics"
}
dict2={
    "Name":"Jerry",
    "Age":31,
    "Course":"Biology"
}

tupleDict=(dict1,dict2)
print(tupleDict)

for item in tupleDict:
    for it1,it2 in item.items():
        print(f"Key:{it1}")
        print(f"Value: {it2}")
    print("\n")
"""

#Dictionary in a Dictionary



"""dictHold={
    "Hold1":{
        "Name":"Jerry",
        "Age":31,
        "Course":"Biology"
    },
    "Hold2":{
        "Name":"David",
        "Age":37,
    "Course":"Physics"
    }
}
print(dictHold)

for firstDict,secondDict in dictHold.items():
    print(f"first Key: {firstDict}")
    for sec1,sec2 in secondDict.items():
        print(f"second Key: {sec1}")
        print(f"second Value: {sec2}")
    print("\n")
"""

"""#Writing clear prompts
name=input("Enter your Name: ")
print(f"Hello there {name}")
"""

"""#using int() to accept numerical inputs
nameValR=input("Enter Name: ")
ageValR=int(input("Enter Age: "))
print(f"Hello {nameValR} you are {ageValR} years old")
"""

"""#Modulo Operator
print(17%9)
"""


"""#While loops
#The while loop in action
num=1
while(num<=10):
    print(num)
    num=num+1
"""

"""#Letting the user choose when to quit
name=""
while name!="Stop":
    name=input("Enter Name: ")
    print(f"Greetings {name}")
"""

"""#using a Flag
run=True
name="Josh"

while run:
    name=input("Enter Name: ")
    if(name=="stop" or name=="Stop"):
        print("Exiting program")
        run=False
    else:
        print(f"Hello there {name}")
"""

"""#Using break to exit the loop
run=True
name="Josh"

while run:
    name=input("Enter Name: ")
    if(name=="stop" or name=="Stop"):
        #run=False
        break
    else:
        print(f"Hello there {name}")
"""


#using continue

"""num=1

while num<=10:
    num=num+1
    if(num==5):
        continue
    else:
        print(num)
"""

"""num=1

while num<=10:
    print(num)
"""


#Moving items from one list to another

"""listHold=[1,2,3,4,5]
newList=[]

while listHold:
    num=listHold.pop(0)
    newList.append(num)

print(newList)
print(listHold)"""


"""#Removing all instances of specific values from a list
listItems=["Cat","Dog","Rat","Fox","Rat","Rat"]

while "Rat" in listItems:
    listItems.remove("Rat")

print(listItems)
"""

#Filling a Dictionary with user input

"""containDict={}
run=True

while run:
    key=input("Enter Key: ")
    value=input("Enter value: ")

    containDict[key]=value

    repeat=input("Do you want to repeat?(yes/no): ")
    if(repeat=="no" or repeat=="No"):
        run=False

print(containDict)"""

"""def first(name):
    print(f"Hello there {name}")


first('Alex')"""


"""# Arguments and Parameters
def argFunct(name):
    print(f"Hello there {name}")

argFunct("James")
"""

"""# Passing Arguments
# Positional Arguments
def posFunct(name, age):
    print(f"Hello there {name}")
    print(f"You are {age} years")

posFunct("Adam", 34)
"""

"""# Key-word Argument
def keyFunc(score=84):
    print(f"You had a score of {score}")

keyFunc()"""


"""# Default Values
def defFunc(school, course='Physics'):
    print(f"I go to {school}, and I study {course}")

defFunc("Oxford")
"""

# Equivalent function Call

"""def defFunc(school, course='Physics'):
    print(f"I go to {school}, and I study {course}")


defFunc("Oxford")
defFunc(school="Oxford")
"""


# Return Values

"""def message(cgpa):
    msg = f"I have a CGPA of {cgpa}"
    return msg


print(message(4.23))
"""

# Making an Argument Optional

"""def initials(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"Hello there {first_name} {middle_name} {last_name}"
        return full_name
    else:

        full_name = f"Hello there {first_name} {last_name}"
        return full_name


print(initials("Jack", "Alex", "Smith"))
"""


# Returning a Dictionary

"""def dictFunc(name, nameVal, age, ageVal):
    hold = {}
    hold[name] = nameVal
    hold[age] = ageVal
    return hold


print(dictFunc("Name", "Alex", "Age", 34))
"""

"""# using a Function with a while loop

def names(first_name, second_name):
    return f"{first_name} {second_name}"


while True:

    first = input("Enter first Name: ")
    if first == "quit":
        break
    second = input("Enter second Name: ")
    if second == "quit":
        break

    print(f"Hello there {names(first, second)}")
"""

# passing a list
# Modifying a list in a function

"""def modFunct(valList, empList):
    while valList:
        val = valList.pop(0)
        empList.append(val)
        if val==3:
            break
    return empList


valueList = [1, 2, 3, 4, 5]
emptyList = []
print(modFunct(valueList, emptyList))
print(valueList)"""


"""# preventing a function from modifying a list
def modFunct(valList, empList):
    while valList:
        val = valList.pop(0)
        empList.append(val)
    return empList


valueList = [1, 2, 3, 4, 5]
valueListCopy = valueList[:]
emptyList = []
print(modFunct(valueListCopy, emptyList))
print(valueList)"""


"""# Passing an Arbitrary number of arguments
def arbFunct(*names):
    return names

print(arbFunct("Alex", "Jones", "Sam", "Adam"))
"""

"""# Mixing Positional and Arbirary arguments
def mixFunct(name, *courses):
    print(f"{name} offers the following courses below:")
    for course in courses:
        print(f"Course: {course}")


mixFunct("Adam", "Chemistry", "Biology", "Psychology", "Physics")
"""

# Using Arbitrary keyword arguments

"""def arbKeyWordFunct(name, age, nameVal, ageVal, **Data):
    Data[name] = nameVal
    Data[age] = ageVal
    return Data


print(arbKeyWordFunct("Name", "Age", "Alex", 34, Course="Physics", School="Harvard"))
"""
#Number 1
"""def run(first,second="Alex",*list_):
    print(f"You are {first} years old")
    print("Hello there {}".format(second))
    for val in list_:
        if val==list_[0]:
            print("Hello there {}".format(val))
        elif val==list_[1]:
            print("Greetings to you {}".format(val))
        elif val==list_[2]:
            print("Hi {} how are you?".format(val))
        elif val==list_[3]:
            print("Hey there {}".format(val))

run(34,"David","James","Sam","John","Anthony")"""

#Number 3
"""def returnDict(name,age,course):
    hold={
        "Name":name,
        "Age":age,
        "Course":course,
        "Number":2348053321187,
        "Address":"G.R.A Benin City, Edo State"
    }
    return hold

print(returnDict("Alex",34,"Physics"))"""

#Number 4

"""def merge(list_,dict_):
    return list_,dict_

listData=[]
dictData={}
listInd=0
listCount=5

while True:
    if listInd<listCount:
        listVal=input("Enter list Value: ")
        listData.append(listVal)
        key=input("Enter Key: ")
        keyVal=input("Enter key Value: ")
        dictData[key]=keyVal
        listInd=listInd+1
    else:
        break

print(merge(listData,dictData))"""

"""def argMix(course="Physics",**studentData):
    print("So, you study {}".format(course))
    studentData["Course"]=course
    print(studentData)

argMix("Physics",Name="Alex",Age=34,Score=89,)"""

"""first=lambda name,age:f"Hello there {name} you are {age}"

print(first("Alex",34))
"""

"""def embed(course):

    contain=lambda name,age:f"Greetings to you {name}, you are {age} you offer {course}"

    return contain

hold=embed("Physics")

print(hold("David",37))
"""

# Classes
# Creating a class
"""class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return f"Hello {self.name} you are {self.age}"


print(Test("Alex", 34).run())
"""

# Making an Instance of a class
"""class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return f"Hello {self.name} you are {self.age}"


test = Test("Alex", 34)
print(test.run())

"""

"""# Setting a Default Value for an Attribute
class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age} you scored {self.score}"

    def scoreReport(self):
        return f"You had a score of {self.score}"


test = Test("Alex", 34)
print(test.run())
print(test.scoreReport())
"""

"""# Modifying an attribute value through a function
class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"

    def scoreUpdate(self, newScore):
        self.score = newScore


test = Test("Alex", 34)
print(test.run())
test.scoreUpdate(90)
print(test.scoreReport())
"""

"""# Incrementing an attribute value Directly
class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"


test = Test("Alex", 34)
print(test.run())
test.score = test.score + 12
print(test.scoreReport())

"""

"""# Incrementing an Attribute Value through a function
class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"

    def incScore(self, inc):
        self.score = self.score + inc


test = Test("Alex", 34)
print(test.run())
test.incScore(12)
print(test.scoreReport())
"""

"""# Inheritance

class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"


class ChildTest(Test):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(name,age)


childTest = ChildTest("Alex", 34)
print(childTest.run())
print(childTest.scoreReport())
"""

"""#Attributes and Methods for Child class
class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"


class ChildTest(Test):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course="Physics"

        super().__init__(name,age)

    def courseDesc(self):
        return f"So you offer {self.course}"

childTest = ChildTest("Alex", 34)
print(childTest.run())
print(childTest.scoreReport())
print(childTest.courseDesc())
"""


#Overriding methods from the parent class
"""class Test:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 84

    def run(self):
        return f"Hello {self.name} you are {self.age}"

    def scoreReport(self):
        return f"You had a score of {self.score}"


class ChildTest(Test):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course="Physics"

        super().__init__(name,age)

    def courseDesc(self):
        return f"So you offer {self.course}"

    def scoreReport(self):
        childTest.score=82
        return f"Score now seems to be {self.score}"

childTest = ChildTest("Alex", 34)
print(childTest.run())
print(childTest.scoreReport())
print(childTest.courseDesc())
"""


#instance as an attribute

"""class FirstProg:
    school=None
    course=None
    def __init__(self,school,course):
        self.school=school
        self.course=course

    def message(self):
        return f"You attend {self.school} and you study {self.course}"

class SecondProg:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.first=FirstProg("Harvard","Biology")

    def reveal(self):
        return f"Hello there {self.name} you are {self.age} years"

second=SecondProg("Alex",33)
print(second.reveal())

print(second.first.message())
"""

"""#0 dimensional Array
import numpy

con=numpy.array(47)
print(con)
"""

"""#1 dimensional Arrays
import numpy

con=numpy.array([33,37,48,23])
print(con)"""

"""#2 Dimensional Arrays
import numpy

con=numpy.array([[33,37,48,23],[21,27,33,45]])
print(con)"""

"""#3 Dimensional Arrays
import numpy

con=numpy.array([[[33,37,48,23]],[[21,27,33,45]],[[22,43,32,41]]])
print(con)"""

"""#Checking Dimensions of Arrays
import numpy

con=numpy.array([[[33,37,48,23]],[[21,27,33,45]],[[22,43,32,41]]])
print(con.ndim)
"""

"""#1 Dimensional Arrays
#index position
import numpy

con=numpy.array([33,37,48,23])
print(con[2])"""

#2 Dimensional Arrays
#index position
"""import numpy

con=numpy.array([[33,37,48,23],[21,27,33,45]])
print(con[1,2])
"""


"""#3 Dimensional Arrays
#index position
import numpy

con=numpy.array([[[33,37,48,23]],[[21,27,33,45]],[[22,43,32,41]]])
print(con[1,0,3])
"""

"""#1 dimension Array
#Array Slicing
import numpy

con=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(con[::2])



#2 Dimensional Arrays
#Array Slicing
import numpy

con=numpy.array([[33,37,48,23],[21,27,33,45]])
print(con[1,0::2])
"""

"""#Data Type
import numpy

con=numpy.array(['101','121','131','141','151','161','171','181','191','201'])
print(con.dtype)
"""

"""#Data Type
import numpy

con=numpy.array(['101','121','131','141','151','161','171','181','191','201'])
print(con.dtype)


con=numpy.array([101,121,131,141,151,161,171,181,191,201])
print(con.dtype)"""

"""#Data Type Conversion
import numpy

con=numpy.array(['1','2','3','4','5','6','7','8','9','10'])
#print(con.dtype)

floating=con.astype(float)
print(floating)


integer=con.astype(int)
print(integer)


con=numpy.array([1,2,3,4,5,6,7,8,9,10])

stringVal=con.astype(str)
print(stringVal)
"""

#Numpy Array Copy and View
#Copy
import numpy

con=numpy.array([1,2,3,4,5,6,7,8,9,10])
conCopy=con.copy()
conCopy[4]=12
"""print(conCopy)
print(con)

print("\n")
"""

#View
import numpy

con=numpy.array([1,2,3,4,5,6,7,8,9,10])
conView=con.view()
conView[2]=11
"""print(conView)
print(con)
"""

"""print(conCopy.base)
print(conView.base)
"""

"""import numpy

con=numpy.array([[33,37,48,23],[21,27,33,45]])
print(con.shape)"""

"""#Reshaping
import numpy

con=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(con.reshape(2,5))



con=numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(con.reshape(2,3,2))

"""


"""#Flattening Arrays
import numpy

data=numpy.array([[2,3,4],[5,7,1],[7,7,1],[2,3,1]])
print(data.reshape(-1))
"""

"""#Iterating
import numpy

data=numpy.array([[2,3,4],[5,7,1],[7,7,1],[2,3,1]])
for x in numpy.nditer(data):
    print(x)
"""

"""#Iterating with different step sizes
import numpy

valz=numpy.array([[1,2,3,4],[5,6,7,8]])

for v in numpy.nditer(valz[:,::2]):
    print(v)
"""

#ndenumerate

import numpy

"""data=numpy.array([[2,3,4],[5,7,1],[7,7,1],[2,3,1]])

for n,x in numpy.ndenumerate(data):
    print(n,x)
"""

#Joining
#Concatenate
import numpy

"""arr1=numpy.array([1,2,3])
arr2=numpy.array([4,5,6])

join=numpy.concatenate((arr1,arr2))
print(join)
"""

"""first=numpy.array([[1,2,3],[4,5,6]])
second=numpy.array([[7,8,9],[10,11,12]])

combine=numpy.concatenate((first,second),axis=1)
print(combine)
"""

"""arr1=numpy.array([1,2,3])
arr2=numpy.array([4,5,6])

v=numpy.stack((arr1,arr2),axis=0)
print(v)
"""

"""arr1=numpy.array([1,2,3])
arr2=numpy.array([4,5,6])

v=numpy.stack((arr1,arr2),axis=1)
print(v)
"""

"""first=numpy.array([[1,2,3],[4,5,6]])
second=numpy.array([[7,8,9],[10,11,12]])

combine=numpy.stack((first,second),axis=1)
print(combine)
"""

#Vstack
"""import numpy

first=numpy.array([[1,2,3],[4,5,6]])
second=numpy.array([[7,8,9],[10,11,12]])

combine=numpy.vstack((first,second))
print(combine)
"""

#Hstack
import numpy

"""first=numpy.array([[1,2,3],[4,5,6]])
second=numpy.array([[7,8,9],[10,11,12]])

combine=numpy.hstack((first,second))
print(combine)"""

"""res1=numpy.array([2,4,6,8])
res2=numpy.array([1,1,3,4])

join=numpy.hstack((res1,res2))
print(join)"""

"""#dstack
first=numpy.array([[1,2,3],[4,5,6]])
second=numpy.array([[7,8,9],[10,11,12]])

combine=numpy.dstack((first,second))
print(combine)"""

"""#splitting
import numpy

arr=numpy.array([1,2,3,4,5,6])

val=numpy.array_split(arr,4)
print(val)




con=numpy.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])

vor=numpy.array_split(con,3)
print(vor)



con=numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

vor=numpy.array_split(con,3,axis=1)
print(vor)
"""

#Searching
#where()

import numpy

cont=numpy.array([12,13,15,16,18])

res=numpy.where(cont==15)
#print(res)


even=numpy.where(cont%2==0)
#print(even)


#Searchsorted
"""val=numpy.searchsorted(cont,11)
print(val)




enum=numpy.searchsorted(cont,[10,14,17])
print(enum)
"""

#Sorting
"""data=numpy.array([[12,15,11],[8,12,10]])

print(numpy.sort(data))
"""

#Filtering Arrays

"""import numpy

valz=numpy.array([22,37,42,88,36,77])

compare=numpy.array([True,False,True,False,True,False])

new=valz[compare]
print(new)
"""

#Random Numbers
#Random integers from 30 to 100
"""import numpy

number=numpy.random.randint(-30,100)
print(number)
"""

"""#Random Decimal numbers from 12 to 80
import numpy

number3=numpy.random.uniform(12,80)
print(number3)
"""

"""#2 dimensional array having two 1 dimensional arrays having three random decimal numbers ranging from 0 to 12
import numpy

number5=numpy.random.uniform(12,size=(2,3))
print(number5)
"""

#A 3 dimensional array having two 2 dimensional arrays with three 1 dimensional arrays which have 4 random whole numbers
#ranging from 0 to 27
"""import numpy

number6=numpy.random.randint(27,size=(2,3,4))
print(number6)
"""

"""#Choice
res=numpy.random.choice(numpy.array(["Jack","Alex","Bryan","Lucas"]),size=(3,2))
print(res)
"""

"""import matplotlib.pyplot as plt
xV=numpy.random.normal(18,10,100)
print(xV)

plt.hist(xV)
plt.show()
"""

"""import numpy
data=numpy.array([27,33,21,26,32])
print(numpy.mean(data))
"""

"""import numpy
data=numpy.array([27,33,21,26,32])
print(numpy.median(data))
"""

"""import numpy
data=numpy.array([27,33,21,26,32])
print(numpy.std(data))
"""

"""import numpy

def mode1(con):
    hold={}
    for a in con:
        if not a in hold:
            hold[a]=1
        else:
            hold[a]=hold[a]+1
    return [first for first,val in hold.items() if val==max(hold.values())]
data=numpy.array([27,33,21,26,32,27,33,27])
print(mode1(data))
"""

#Pandas
#Series

"""import numpy
import pandas

data=numpy.array([12,15,18,27,81])

reveal=pandas.Series(data)
print(reveal)"""

"""import numpy
import pandas

data=numpy.array([12,15,18,27,81])

reveal=pandas.Series(data)
print(reveal[0])
print(pandas.Series(data)[0])"""

#Creating Labels
"""import numpy
import pandas

data=numpy.array([12,15,18,27,81])

reveal=pandas.Series(data,index=['a','b','c','d','e'])
print(reveal)"""

#Key Value Object as Series
"""import pandas

cont={
    "One":"James",
    "Two":"Alex",
    "Three":"Samuel",
    "Four":"Gabriel"
}

viewer=pandas.Series(cont)
print(viewer)
"""

"""#Create a Series using only a specified key-value pair
import pandas

cont={
    "One":"James",
    "Two":"Alex",
    "Three":"Samuel",
    "Four":"Gabriel"
}

viewer=pandas.Series(cont,index=["One","Three"])
print(viewer)
"""

"""import pandas

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

result = pandas.DataFrame(data)
print(result)"""


"""import pandas

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

result = pandas.DataFrame(data)

print(result.loc[1])
print("\n")
print(result.loc[[0, 1]])
"""

"""# Naming Indexes
import pandas

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

result = pandas.DataFrame(data, index=["first", "Second", "Third", "Fourth", "Fifth"])
print(result)"""

"""# Locate Named Indexes
import pandas

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

result = pandas.DataFrame(data, index=["first", "Second", "Third", "Fourth", "Fifth"])
print(result.loc["Second"])
"""

"""import pandas

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

result = pandas.DataFrame(data)

print(result.iloc[0:2, 0:2])
print("\n")
print(result.iloc[[0, 1], [0, 1]])

"""

"""import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\testData.csv")
print(dataSet)
"""

import pandas
pandas.options.display.max_rows=100

pandas.options.display.max_columns=100


# Reading Json Files
"""import pandas

contain = {

    "Names": {
        0: "Jack",
        1: "Alen",
        2: "Jason",
        3: "Gabriel",
        4: "Anthony"
    },
    "Course": {
        0: "Physics",
        1: "Biology",
        2: "Mathematics",
        3: "Chemistry",
        4: "BioChemistry",
    }
}

reveal = pandas.DataFrame(contain)
print(reveal)
"""

#head() function
"""import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\testData.csv")
print(dataSet.head())"""


#tail() function
"""import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\testData.csv")
print(dataSet.tail())"""

#info() function
"""import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\testData.csv")
print(dataSet.info())
"""

import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\rawsets.csv")
#print(dataSet)

#removing empty rows temporarily
"""print(dataSet.dropna())
print("\n")
print(dataSet)
"""

#removing empty rows permanently
#dataSet.dropna(inplace=True)
#print(dataSet)
#print(dataSet)

"""dataSet.fillna('2020/12/22',inplace=True)
print(dataSet)
"""

"""dataSet['Date'].fillna('2020/12/22',inplace=True)
print(dataSet)
"""

#print(dataSet)
"""x=dataSet["Duration"].mean()
dataSet['Date'].fillna(x,inplace=True)
print(dataSet)
"""

"""dataSet["Date"]=pandas.to_datetime(dataSet["Date"])
#print(dataSet)
dataSet['Date'].fillna('2020/12/22',inplace=True)
#print(dataSet)"""

#dataSet.dropna(subset=['Date'],inplace=True)
#print(dataSet)
"""meanVal=dataSet["Duration"].mean()

for x in dataSet.index:
    if dataSet.loc[x,"Duration"]>120:
        dataSet.loc[x,"Duration"]=meanVal
"""
#print(dataSet)

"""for x in dataSet.index:
    if dataSet.loc[x,"Duration"]>120:
        dataSet.drop(x,inplace=True)
"""
"""#print(dataSet)
#print(dataSet.duplicated())
print(dataSet.drop_duplicates())"""

#Correlation
import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\rawsets.csv")
newDataSet=dataSet[["Duration","Pulse"]]
#print(dataSet)
#print(newDataSet.corr())

import pandas
"""from matplotlib import pyplot as plt

#dataSet=pandas.read_csv("C:\\Users\\Eleazer\\Desktop\\Mikon_Data_Analysis_Data\\rawsets.csv")

dataSet.plot(kind='line',x='Duration',y='Pulse',marker='o')
plt.show()"""

"""#Data manipulation using pandas
import pandas

table={
    "S/N":[1,2,3,4,5,6,7,8],
    "Name":["James","Bryan","Alex","Greg","David",
           "Daniel","Kenneth","Jude"],
    "Course":["Physics","Biology","Chemistry","Chemistry",
             "Physics","Biology","Chemistry","Physics"],
    "Score":[82,83,84,81,80,92,91,87]
}

contain=pandas.DataFrame(table)
print(contain)
print("\n")

print(contain["Course"]=="Chemistry")
print("\n")

chemistry=contain["Course"]=="Chemistry"

physics=contain["Course"]=="Physics"

print(contain[chemistry|physics])
print("\n")
score_84=contain["Score"]>84
#print(contain[score_84])
print("\n")
containedValue=(contain["Score"]==82) | (contain["Score"]==83) | (contain["Score"]==84)

newData=contain[containedValue]
newData.to_csv("C:\\Users\\user\\Desktop\\newUpdate.csv")"""

# MatplotLib
# pyplot
"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

data1=pandas.DataFrame(data)
dataX = data1["Names"]
dataY = data1["Age"]

plt.plot(dataX, dataY, marker='o')
plt.show()
"""

"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
con

dataX = con["Names"]
dataY = con["Age"]
plt.plot(dataX, dataY, marker='o', ms=10, mfc='green', mec='red')
plt.show()
"""

# Lines
"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
print(con)

dataX = con["Names"]
dataY = con["Age"]

plt.plot(dataX, dataY, ls='dotted', marker='o', lw=1, color='green')
plt.show()"""

"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
print(con)

dataX = con["Names"]
dataY = con["Age"]

data1 = {
    'family': 'arial',
    'color': 'red',
    'size': 20
}

data2 = {
    'family': 'times new roman',
    'color': 'blue',
    'size': 20
}

plt.plot(dataX, dataY, marker='o', color='green')
plt.xlabel("Names Data", fontdict=data1)
plt.ylabel("Age Data", fontdict=data2)

plt.title("Plotting Age Data against Name Data", loc='center')
plt.show()"""

# Grid Lines
"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
con

dataX = con["Names"]
dataY = con["Age"]

data1 = {
    'family': 'arial',
    'color': 'red',
    'size': 20
}

data2 = {
    'family': 'times new roman',
    'color': 'blue',
    'size': 20
}

plt.plot(dataX, dataY, ls='dotted', lw=1, marker='o', color='green')
plt.xlabel("Names Data", fontdict=data1)
plt.ylabel("Age Data", fontdict=data2)

plt.title("Plotting Age Data against Name Data", loc='center')

plt.grid()
plt.show()
"""


"""# Grid Lines X-axis
import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

data1 = {
    'family': 'arial',
    'color': 'red',
    'size': 20
}

data2 = {
    'family': 'times new roman',
    'color': 'blue',
    'size': 20
}

plt.plot(dataX, dataY, ls='dotted', lw=1, color='green', marker='o')
plt.xlabel("Names Data", fontdict=data1)
plt.ylabel("Age Data", fontdict=data2)

plt.title("Plotting Age Data against Name Data", loc='center')

plt.grid(axis='x')
plt.show()
"""

"""# Grid Lines Y-axis
import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

data1 = {
    'family': 'arial',
    'color': 'red',
    'size': 20
}

data2 = {
    'family': 'times new roman',
    'color': 'blue',
    'size': 20
}

plt.plot(dataX, dataY, ls='dotted', lw=1, color='green', marker='o')
plt.xlabel("Names Data", fontdict=data1)
plt.ylabel("Age Data", fontdict=data2)

plt.title("Plotting Age Data against Name Data", loc='center')

plt.grid(axis='y')
plt.show()
"""

# Grid Lines Color Red
"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

data1 = {
    'family': 'arial',
    'color': 'red',
    'size': 20
}

data2 = {
    'family': 'times new roman',
    'color': 'blue',
    'size': 20
}

plt.plot(dataX, dataY, ls='dotted', lw=1, color='green', marker='o')
plt.xlabel("Names Data", fontdict=data1)
plt.ylabel("Age Data", fontdict=data2)

plt.title("Plotting Age Data against Name Data", loc='center')

plt.grid(color='red',axis='y')
plt.show()
"""

# Subplot
"""import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"],
    "Score": [88, 76, 80, 81, 82]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

plt.subplot(1, 2, 1)
plt.plot(dataX, dataY, marker='o')
plt.title("First Plot")

dataX = data["Names"]
dataY = data["Score"]

plt.subplot(1, 2, 2)
plt.plot(dataX, dataY, marker='o')
plt.title("Second Plot")

plt.suptitle("Diagram Holding two graphs")
plt.show()
"""

"""# Scatter Plot
import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"],
    "Score": [88, 76, 80, 81, 82]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

plt.scatter(dataX, dataY)
plt.show()
"""

"""#Scatter Plot
import pandas
import numpy
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]
contain=numpy.array(["red","green","yellow","pink","blue"])


plt.scatter(dataX,dataY,c=contain)
plt.show()
"""

"""#Scatter Plot
import pandas
import numpy
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]
contain=numpy.array(["red","green","yellow","pink","blue"])
change=numpy.array([40,80,130,150,200])


plt.scatter(dataX,dataY,c=contain,s=change)
plt.show()
"""


"""#Scatter Plot
import pandas
import numpy
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]
contain=numpy.array(["red","green","yellow","pink","blue"])
change=numpy.array([40,80,130,150,200])
contain=numpy.array([20,30,40,50,70])


plt.scatter(dataX,dataY,c=contain,s=change,cmap='viridis')
plt.colorbar()
plt.show()
"""

# Scatter Plot
"""import pandas
import numpy
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"],
    "Score": [88, 76, 80, 81, 82]
}

con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]
contain = numpy.array(["red", "green", "yellow", "pink", "blue"])
change = numpy.array([40, 80, 130, 150, 200])
contain = numpy.array([20, 30, 40, 50, 70])

plt.scatter(dataX, dataY, c=contain, s=change, cmap='viridis', alpha=0.5)
plt.colorbar()
plt.show()
"""

# Matplotlib Bars
"""import numpy
import pandas
from matplotlib import pyplot as plt

data = {

    "Names": ["James", "Alex", "Sam", "Gabriel", "Bryan"],
    "Courses": ["Physics", "Chemistry", "Biology", "Mathematics", "Biochemistry"],
    "Age": [27, 33, 31, 30, 29],
    "School": ["Harvard", "Yale", "Oxford", "Stanford", "Machussette"],
    "Score": [88, 76, 80, 81, 82]
}

contain = numpy.array([20, 30, 40, 50, 70])
con = pandas.DataFrame(data)
dataX = con["Names"]
dataY = con["Age"]

plt.bar(dataX, dataY, width=0.5)

plt.show()
"""

"""#Matplotlib Bars
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

contain=numpy.array([20,30,40,50,70])
con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]


plt.barh(dataX,dataY,height=0.5,color='red')

plt.show()
"""

#Histogram

"""import numpy
from matplotlib import pyplot as plt

valz=numpy.random.normal(60,12,100)
print(valz)
plt.hist(valz)
plt.grid()
plt.show()
"""

"""from matplotlib import pyplot as plt
contain=numpy.array([23,14,15,19,57,88,19,22,19,27,22,21,20,13,14,16,11,19,21,27,23,24])
plt.hist(contain)
plt.show()
"""

"""#piechart
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

#contain=numpy.array([20,30,40,50,70])


con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY)

plt.show()
"""


#Piechart with labels

"""import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

#contain=numpy.array([20,30,40,50,70])

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY,labels=dataX)

plt.show()
"""

"""#Piechart start Angle
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

contain=numpy.array([20,30,40,50,70])

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY,labels=dataX,startangle=90)

plt.show()
"""

"""#Piechart Explode
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

contain=numpy.array([0.20,0.30,0.40,0.50,0.70])

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY,labels=dataX,startangle=90,explode=contain)

plt.show()
"""

"""#Piechart Colors
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

contain=numpy.array([0.20,0.30,0.40,0.50,0.70])

c=numpy.array(["green","yellow","black","orange","blue"])

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY,labels=dataX,startangle=90,explode=contain,colors=c)

plt.show()
"""

"""#Piechart legend
import numpy
import pandas
from matplotlib import pyplot as plt

data={

    "Names":["James","Alex","Sam","Gabriel","Bryan"],
    "Courses":["Physics","Chemistry","Biology","Mathematics","Biochemistry"],
    "Age":[27,33,31,30,29],
    "School":["Harvard","Yale","Oxford","Stanford","Machussette"],
    "Score":[88,76,80,81,82]
}

contain=numpy.array([0.20,0.30,0.40,0.50,0.70])

c=numpy.array(["green","yellow","black","orange","blue"])

con=pandas.DataFrame(data)
dataX=con["Names"]
dataY=con["Age"]

plt.pie(dataY,labels=dataX,startangle=90,explode=contain,colors=c)

plt.legend(title="Pie Chart Detail")

plt.show()
"""

#Dictionaries
#A simple dictionary
"""dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
print(dictInfo)
"""

#Accessing values in a dictionary
"""dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
print(dictInfo["Name"])
"""

"""#Adding New Key value Pairs
dictInfo={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

dictInfo["Score"]=88
print(dictInfo)
"""

"""#Starting with an empty dictionary
emptyDict={}
emptyDict["Name"]="Richard"
emptyDict["Course"]="Biology"
emptyDict["School"]="Yale"
print(emptyDict)
"""

"""#Modifying values in a dictionary
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}
emptyDict["Name"]="Augustus"
print(emptyDict)
"""

"""#Removing key-Value Pairs
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

del emptyDict["Course"]
print(emptyDict)
"""

"""#Using get() to access unavailable values
emptyDict={
    "Name":"Alex",
    "Course":"Physics",
    "Age":37,
    "School":"Oxford"
}

strange=emptyDict.get("Age","Age not Available")
print(strange)
"""

import pandas
pandas.options.display.max_rows=888

pandas.options.display.max_columns=888


"""# Reading Json Files
import pandas

contain = {

    "Names": {
        0: "Jack",
        1: "Alen",
        2: "Jason",
        3: "Gabriel",
        5: "Anthony"
    },
    "Course": {
        0: "Physics",
        1: "Biology",
        2: "Mathematics",
        3: "Chemistry",
        4: "BioChemistry",
    }
}

reveal = pandas.DataFrame(contain)
print(reveal)
"""
"""
#tail() function
import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\testData.csv")
#print(dataSet.head())

print(dataSet.info())"""

import pandas

dataSet=pandas.read_csv("C:\\Users\\user\\Desktop\\Lecture Notes\\rawsets.csv")
"""print(dataSet)

#removing empty rows temporarily
print(dataSet.dropna())
print("\n")
print(dataSet)
"""

#removing empty rows permanently
"""dataSet.dropna(inplace=True)
print(dataSet)
"""

"""dataSet.fillna('2020/12/22',inplace=True)
print(dataSet)"""


"""dataSet['Date'].fillna('2020/12/22',inplace=True)
print(dataSet)"""

"""x=dataSet["Duration"].mean()
dataSet.fillna(x,inplace=True)
print(dataSet)
"""

"""dataSet["Date"]=pandas.to_datetime(dataSet["Date"])
dataSet['Date'].fillna('2020/12/22',inplace=True)
print(dataSet)"""

"""dataSet.dropna(subset=['Date'],inplace=True)
print(dataSet)"""

meanVal=dataSet["Duration"].mean()

"""for x in dataSet.index:
    if dataSet.loc[x,"Duration"]>120:
        dataSet.loc[x,"Duration"]=meanVal

print(dataSet)
"""

"""for x in dataSet.index:
    if dataSet.loc[x,"Duration"]>120:
        dataSet.drop(x,inplace=True)

print(dataSet)"""

"""print(dataSet.duplicated())
print("\n")
print(dataSet.drop_duplicates())
"""



"""import os
import pandas as pd

pd.options.display.max_rows = 888
pd.options.display.max_columns = 888

# Path to Downloads folder
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Original file path
original_filename = "oecd_bli_2015.csv"
original_path = os.path.join(download_folder, original_filename)

# Read directly with proper encoding and delimiter
df = pd.read_csv(original_path, encoding='utf-8-sig')

# Display the DataFrame
print(df)
"""


"""#Peceptron
import pandas
import matplotlib.pyplot as plt

data={
    "x1":[0,0,1,1],
    "x2":[0,1,0,1],
    "y":[-1,-1,-1,1]
}


contain=pandas.DataFrame(data,index=['a','b','c','d'])
#print(contain)
w1=0
w2=0
b=0
n=1.0

x1=contain["x1"]
x2=contain["x2"]
y=contain["y"]

def step(z):
    return 1 if z>=0.5 else -1

trainingCount=0
epoch=0
while True:

    total_error=0
    for i in range(len(x1)):

        z = w1*x1[i]+w2*x2[i]+b

        pred=step(z)

        error=y[i]-pred

        total_error=total_error+abs(error)

        if error!=0:

            w1=w1+n*(y[i]-pred)*x1[i]
            w2=w2+n*(y[i]-pred)*x2[i]

            b=b+n*(y[i]-pred)
    trainingCount=trainingCount+1
    print(f"Training {trainingCount} complete with error: {total_error}")

    epoch=epoch+1

    if total_error==0:
        print(f"Training converged at {epoch}")
        break

def predict(newX1,newX2):
    z = w1 * newX1 + w2 * newX2 + b

    prediction=step(z)
    return f"The prediction for {newX1} and {newX2} is {prediction}"

print(predict(0,1))
"""


"""#Updated Perceptron
import pandas as pd
import numpy as np

# Input data — add more features (x3, x4...) if needed
data = {
    "x1": [0, 0, 1, 1],
    "x2": [0, 1, 0, 1],
    "y":  [0, 0, 0, 1]
}

df = pd.DataFrame(data, index=["a", "b", "c", "d"])

# Separate features and target
X = df.drop(columns="y").values  # All columns except 'y'
y = df["y"].values               # Target labels
n_features = X.shape[1]          # Automatically detects number of features

# Initialize weights and bias
weights = np.zeros(n_features)
bias = 0
learning_rate = 1.0

def step(z):
    return 1 if z >= 0.5 else -1

epoch = 0
while True:
    total_error = 0
    for xi, target in zip(X, y):
        z = np.dot(weights, xi) + bias
        pred = step(z)
        error = target - pred
        total_error += abs(error)

        if error != 0:
            weights += learning_rate * error * xi
            bias += learning_rate * error

    epoch += 1
    print(f"Epoch {epoch} complete. Total error: {total_error}")
    if total_error == 0:
        print(f"Training converged at epoch {epoch}")
        break

# General prediction function for any number of features
def predict(new_input):
    new_input = np.array(new_input)
    z = np.dot(weights, new_input) + bias
    prediction = step(z)
    return f"The prediction for {new_input.tolist()} is {prediction}"

# Example predictions
print(predict([0, 1]))
print(predict([1, 1]))
"""

"""import numpy as np
X=np.array([2,3,4,5])
random_state=1
rgen = np.random.RandomState(random_state)
w_ = rgen.normal(loc=0.0, scale=0.01,
size=1 + X.shape[1])
print(w_)"""
###############################
##############################
import numpy as np
class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,size=1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):

        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):

        return np.where(self.net_input(X) >= 0.0, 1, -1)

ppn = Perceptron(eta=0.1, n_iter=10)
################################
###############################
class OneVsRestClassifier:
    def __init__(self, base_classifier):
        self.base_classifier = base_classifier
        self.classifiers = {}

    def fit(self, X, y):
        self.unique_classes = np.unique(y)
        for cls in self.unique_classes:
            y_binary = np.where(y == cls, 1, -1)
            clf = self._clone_classifier()
            clf.fit(X, y_binary)
            self.classifiers[cls] = clf
        return self

    def _clone_classifier(self):
        return Perceptron(
            eta=self.base_classifier.eta,
            n_iter=self.base_classifier.n_iter,
            random_state=self.base_classifier.random_state
        )

    def predict(self, X):
        scores = {}
        for cls, clf in self.classifiers.items():
            scores[cls] = clf.net_input(X)  # raw scores

        # Transpose to shape (n_samples, n_classes)
        score_matrix = np.column_stack(list(scores.values()))

        # Pick class with max score per sample
        predictions = np.argmax(score_matrix, axis=1)
        return self.unique_classes[predictions]
##################################
#################################


'''import numpy as np
random_state=1
rgen = np.random.RandomState(random_state)
value=rgen.random()
print(value)'''

import os
import pandas

pandas.options.display.max_rows=9999
pandas.options.display.max_columns=9999
data=pandas.read_csv("C:\\Users\\user\\desktop\\machine learning lectures\\iris.data")
#print(data.head(5))

data.columns=["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)","class (or species)"]

data.to_csv("C:\\Users\\user\\desktop\\machine learning lectures\\iris2.data")

"""import matplotlib
import numpy as np

y=data.iloc[0:100,4]
y=numpy.where(y=="Iris-setosa",-1,1)
#print(y)


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([-1, -1, -1, 1])  # AND gate


ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)"""


"""X_new = np.array([[1, 1], [0, 0], [1, 0]])
predictions = ppn.predict(X_new)
#print(predictions)
"""

##########################################
#########################################
########################################

import pandas as pd
df = pd.read_csv('C:\\Users\\user\\Desktop\\machine learning lectures\\iris.data',header=None, encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np

# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values

ppn.fit(X,y)
# plot data points
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# Plot decision boundary if the Perceptron model is already trained:
x_values = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
y_values = -(ppn.w_[0] + ppn.w_[1] * x_values) / ppn.w_[2]
plt.plot(x_values, y_values, color='green')

# Show the plot
plt.show()

#########################################################
########################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('C:\\Users\\user\\Desktop\\machine learning lectures\\iris.data', header=None, encoding='utf-8')

# Select only setosa and versicolor (first 100 samples)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# Extract features: sepal length (column 0) and petal length (column 2)
X = df.iloc[0:100, [0, 2]].values

# Shuffle the data manually
np.random.seed(42)  # for reproducibility
indices = np.arange(100)
np.random.shuffle(indices)

X = X[indices]
y = y[indices]

# Manual split: 80% train, 20% test
split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Fit model on training set
ppn.fit(X_train, y_train)

# Plot training data points
plt.scatter(X_train[y_train == -1, 0], X_train[y_train == -1, 1], color='red', marker='o', label='setosa')
plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# Plot decision boundary
x_values = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
y_values = -(ppn.w_[0] + ppn.w_[1] * x_values) / ppn.w_[2]
plt.plot(x_values, y_values, color='green')

plt.title('Perceptron Decision Boundary (Manual Split)')
plt.show()

# Predict on test set
y_pred = ppn.predict(X_test)

# Accuracy
accuracy = np.mean(y_pred == y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

########################################################
#######################################################




"""ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1),
ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()"""

################################################
################################################
"""from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')


plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
"""


import numpy as np
import matplotlib.pyplot as plt

"""def plot_decision_boundary(X, y, classifier):
    # Plot the data points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k')

    # Plot the decision boundary (a straight line)
    x_values = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
    # Decision boundary equation: x2 = (-w0 - w1*x1) / w2
    y_values = -(classifier.w_[0] + classifier.w_[1] * x_values) / classifier.w_[2]
    plt.plot(x_values, y_values, color='green')

    plt.xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
    plt.ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)
    plt.show()

ppn1 = Perceptron(eta=0.1, n_iter=10).fit(X,y)

plot_decision_boundary(X,y,ppn1)
"""
######################################
#####################################
####################################

import numpy as np
from matplotlib import pyplot as plt

"""x=[2,3,4]
y=[3,4,5]

xx,yy=np.meshgrid(x,y)

print(xx.shape)
plt.scatter(xx,yy)
plt.show()"""

"""x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.02),
np.arange(x2_min, x2_max, 0.02))

print(xx1)"""



"""xx1,xx2=np.meshgrid(np.arange(2,5,0.5),np.arange(2,5,0.5))
print(xx1)"""


class AdalineGD(object):

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
    def fit(self, X, y):

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,
                              size=1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):

        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):

        return X

    def predict(self, X):

        return np.where(self.activation(self.net_input(X))
                    >= 0.0, 1, -1)
############################################################
############################################################
"""fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
ax[0].plot(range(1, len(ada1.cost_) + 1),
np.log10(ada1.cost_), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline - Learning rate 0.01')
ada2 = AdalineGD(n_iter=1000, eta=0.0001).fit(X, y)
ax[1].plot(range(1, len(ada2.cost_) + 1),
ada2.cost_, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaline - Learning rate 0.0001')
plt.show()"""

############################################################
###########################################################
"""X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()
ada_gd = AdalineGD(n_iter=15, eta=0.01)
ada_gd.fit(X_std, y)

#plot_decision_regions(X_std, y, classifier=ada_gd)

plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
plt.plot(range(1, len(ada_gd.cost_) + 1),
ada_gd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.tight_layout()
plt.show()"""
#######################################################
#######################################################
"""import matplotlib.pyplot as plt
import numpy as np

# Standardize features
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

# Train Adaline using gradient descent
ada_gd = AdalineGD(n_iter=15, eta=0.01)
ada_gd.fit(X_std, y)

# Plot data points
plt.scatter(X_std[y == -1, 0], X_std[y == -1, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X_std[y == 1, 0], X_std[y == 1, 1],
            color='blue', marker='x', label='versicolor')

# Plot decision boundary
x_values = np.linspace(X_std[:, 0].min() - 1, X_std[:, 0].max() + 1, 100)
# Using the equation: w0 + w1*x1 + w2*x2 = 0 → solve for x2
y_values = -(ada_gd.w_[0] + ada_gd.w_[1] * x_values) / ada_gd.w_[2]
plt.plot(x_values, y_values, color='green', label='decision boundary')

# Label and show plot
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.title('Adaline - Gradient Descent')
plt.tight_layout()
plt.show()

# Plot cost over epochs
plt.plot(range(1, len(ada_gd.cost_) + 1), ada_gd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.title('Adaline - Learning rate 0.01')
plt.tight_layout()
plt.show()
"""
##############################
##############################
class AdalineSGD(object):

    def __init__(self, eta=0.01, n_iter=10,
        shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        self.random_state = random_state

    def fit(self, X, y):

        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self

    def partial_fit(self, X, y):

        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self

    def _shuffle(self, X, y):


        r = self.rgen.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):

        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01,
                                   size=1 + m)
        self.w_initialized = True

    def _update_weights(self, xi, target):

        output = self.activation(self.net_input(xi))
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error ** 2
        return cost

    def net_input(self, X):

        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):

        return X

    def predict(self, X):

        return np.where(self.activation(self.net_input(X))
                    >= 0.0, 1, -1)
##################################
#################################
import matplotlib.pyplot as plt
import numpy as np

# Standardize features
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()


# Train Adaline using stochastic gradient descent
ada_sgd = AdalineSGD(n_iter=15, eta=0.01,random_state=1)
ada_sgd.fit(X_std, y)

# Plot data points
plt.scatter(X_std[y == -1, 0], X_std[y == -1, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X_std[y == 1, 0], X_std[y == 1, 1],
            color='blue', marker='x', label='versicolor')

# Plot decision boundary
x_values = np.linspace(X_std[:, 0].min() - 1, X_std[:, 0].max() + 1, 100)
# Using the equation: w0 + w1*x1 + w2*x2 = 0 → solve for x2
y_values = -(ada_sgd.w_[0] + ada_sgd.w_[1] * x_values) / ada_sgd.w_[2]
plt.plot(x_values, y_values, color='green', label='decision boundary')

# Label and show plot
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.title('Adaline - Stochastic Gradient Descent')
plt.tight_layout()
plt.show()

# Plot cost over epochs
plt.plot(range(1, len(ada_sgd.cost_) + 1), ada_sgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')
plt.title('Adaline - Learning rate 0.01')
plt.tight_layout()
plt.show()


##################################################
##################################################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
print('Class labels:', np.unique(y))
#Class labels: [0 1 2]
##################################################
#################################################
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=1, stratify=y)
################################################
################################################
import random

# Step 1: Combine X and y into pairs
data = list(zip(X, y))

# Step 2: Shuffle the data randomly (for mixing the order)
random.seed(1)  # Ensures same shuffle every time
random.shuffle(data)

# Step 3: Split the data into training and testing
split_index = int(len(data) * 0.7)  # 70% train, 30% test

train_data = data[:split_index]  # First 70%
test_data = data[split_index:]   # Remaining 30%

# Step 4: Separate features and labels again
X_train1 = [x for x, y in train_data]
y_train1 = [y for x, y in train_data]

X_test1 = [x for x, y in test_data]
y_test1 = [y for x, y in test_data]
#######################################
#######################################
####USING THE IRIS DATASET####
from sklearn import datasets
import random

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]  # use petal length and petal width
y = iris.target           # class labels (0, 1, 2)

# Step 1: Combine X and y into pairs
data = list(zip(X.tolist(), y.tolist()))  # convert NumPy arrays to lists

# Step 2: Shuffle the data randomly
random.seed(1)  # makes shuffle consistent every run
random.shuffle(data)

# Step 3: Split the data into training and testing
split_index = int(len(data) * 0.7)  # 70% train, 30% test
train_data = data[:split_index]
test_data = data[split_index:]

# Step 4: Separate features and labels again
X_train2 = [x for x, y in train_data]
y_train2 = [y for x, y in train_data]

X_test2 = [x for x, y in test_data]
y_test2 = [y for x, y in test_data]

# Optional: Show sizes
print(f'Training samples: {len(X_train2)}')
print(f'Testing samples: {len(X_test2)}')
#########################################
########################################
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
#################################
################################
from sklearn.linear_model import Perceptron
ppn = Perceptron(eta0=0.1, random_state=1)
ppn.fit(X_train_std, y_train)
##############################
#############################
y_pred = ppn.predict(X_test_std)
print('Misclassified examples: %d' % (y_test != y_pred).sum())
#############################
#############################
from sklearn.metrics import accuracy_score
print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
#Accuracy: 0.978
#############################
#############################
"""# Let's say these are your actual and predicted labels
y_test = [0, 1, 2, 1, 0, 2]      # true labels
y_pred = [0, 0, 2, 1, 0, 1]      # predicted labels

# Step 1: Count how many predictions are correct
correct = 0
for true, pred in zip(y_test, y_pred):
    if true == pred:
        correct += 1

# Step 2: Calculate accuracy = correct / total
total = len(y_test)
accuracy = correct / total

# Step 3: Print with 3 decimal places
print('Accuracy: %.3f' % accuracy)"""
##################################
#################################
print('Accuracy: %.3f' % ppn.score(X_test_std, y_test))
#Accuracy: 0.978
################################
###############################
"""from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
def plot_decision_regions(X, y, classifier, test_idx=None,
resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
        alpha=0.8, c=colors[idx],
        marker=markers[idx], label=cl,
        edgecolor='black')

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1],
                    c='', edgecolor='black', alpha=1.0,
                    linewidth=1, marker='o',
                    s=100, label='test set')

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X=X_combined_std,
y=y_combined,
classifier=ppn,
test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()"""
######################################
#####################################
import matplotlib.pyplot as plt
import numpy as np
"""from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Load dataset (Iris: petal length & petal width)
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]  # petal length and petal width
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

# Standardize features
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Train Perceptron model
ppn = Perceptron(eta0=0.1, random_state=1)
ppn.fit(X_train_std, y_train)

# Predict and show accuracy
y_pred = ppn.predict(X_test_std)
print('Misclassified examples:', (y_test != y_pred).sum())
print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
"""
#####################################
####################################
# Scatter plot of training data (without loop)
plt.scatter(X_train_std[y_train == 0, 0], X_train_std[y_train == 0, 1],
            color='red', marker='o', label='Class 0')
plt.scatter(X_train_std[y_train == 1, 0], X_train_std[y_train == 1, 1],
            color='blue', marker='x', label='Class 1')
plt.scatter(X_train_std[y_train == 2, 0], X_train_std[y_train == 2, 1],
            color='green', marker='s', label='Class 2')

# Plot decision boundaries manually (3 OvR classifiers)
x_values = np.linspace(X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1, 100)

# Class 0 vs Rest
w0 = ppn.coef_[0]
b0 = ppn.intercept_[0]
y0 = -(w0[0] * x_values + b0) / w0[1]
plt.plot(x_values, y0, linestyle='--', color='red', label='Boundary for class 0')

# Class 1 vs Rest
w1 = ppn.coef_[1]
b1 = ppn.intercept_[1]
y1 = -(w1[0] * x_values + b1) / w1[1]
plt.plot(x_values, y1, linestyle='--', color='blue', label='Boundary for class 1')

# Class 2 vs Rest
w2 = ppn.coef_[2]
b2 = ppn.intercept_[2]
y2 = -(w2[0] * x_values + b2) / w2[1]
plt.plot(x_values, y2, linestyle='--', color='green', label='Boundary for class 2')

# Labels and formatting
plt.xlabel('Petal length [standardized]')
plt.ylabel('Petal width [standardized]')
plt.title('Perceptron Decision Boundaries (Explicit Version)')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
#############################
############################
import matplotlib.pyplot as plt
import numpy as np
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))
z = np.arange(-7, 7, 0.1)
phi_z = sigmoid(z)
plt.plot(z, phi_z)
plt.axvline(0.0,color='black')
plt.xlabel("z",loc='center')
plt.ylabel("Phil",loc='center')
plt.show()

print(z)
#print(z)
#print(phi_z)
#print("\n\n")
############################
############################
def cost_1(z):
    return - np.log(sigmoid(z))
def cost_0(z):
    return - np.log(1 - sigmoid(z))
z = np.arange(-10, 10, 0.1)
phi_z = sigmoid(z)
c1 = [cost_1(x) for x in z]
plt.plot(phi_z, c1, label='J(w) if y=1')
c0 = [cost_0(x) for x in z]
plt.plot(phi_z, c0, linestyle='--', label='J(w) if y=0')
plt.ylim(0.0, 5.1)
plt.xlim([0, 1])
plt.xlabel('Phil')
plt.ylabel('J(w)')
plt.legend(loc='upper center')
plt.tight_layout()
plt.show()

#print(cost_1(z))
#print(cost_0(z))
print(np.round(phi_z,4))
print("\n")
print(c0)
print("\n")
print(c1)
############################
###########################
class LogisticRegressionGD(object):

    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
    def fit(self, X, y):

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,
                              size=1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()

            cost = (-y.dot(np.log(output)) -
                    ((1 - y).dot(np.log(1 - output))))
            self.cost_.append(cost)
        return self

    def net_input(self, X):

        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, z):

        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):

        return np.where(self.net_input(X) >= 0.0, 1, 0)
        # equivalent to:
        # return np.where(self.activation(self.net_input(X))
        # >= 0.5, 1, 0)

############################################
###########################################
import numpy as np

class LogisticRegressionGDReg(object):

    def __init__(self, eta=0.05, n_iter=100, lambda_=0.01, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.lambda_ = lambda_
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,
                              size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)

            # Weight update with L2 regularization (skip bias term)
            self.w_[1:] += self.eta * (X.T.dot(errors) - self.lambda_ * self.w_[1:])
            self.w_[0] += self.eta * errors.sum()  # no reg for bias

            # Compute regularized cost
            cost = (-y.dot(np.log(output)) -((1 - y).dot(np.log(1 - output)))) + (self.lambda_ / 2.0) * np.sum(self.w_[1:] ** 2)
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, z):
        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)

##########################################
#########################################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

X_train_01_subset = X_train_std[(y_train == 0) | (y_train == 1)]
y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]
lrgd = LogisticRegressionGD(eta=0.05,
    n_iter = 1000,
    random_state = 1)

lrgd.fit(X_train_01_subset,y_train_01_subset)

plt.scatter(X_train_01_subset[y_train_01_subset == 0, 0], X_train_01_subset[y_train_01_subset == 0, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X_train_01_subset[y_train_01_subset == 1, 0], X_train_01_subset[y_train_01_subset == 1, 1],
            color='blue', marker='x', label='versicolor')

# Plot decision boundary
x_values = np.linspace(X_train_01_subset[:, 0].min() - 1, X_train_01_subset[:, 0].max() + 1, 100)
# Using the equation: w0 + w1*x1 + w2*x2 = 0 → solve for x2
y_values = -(lrgd.w_[0] + lrgd.w_[1] * x_values) / lrgd.w_[2]
plt.plot(x_values, y_values, color='green', label='decision boundary')

# Label and show plot
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.title('Logistic Regression - Stochastic Gradient Descent')
plt.tight_layout()
plt.show()

# Plot cost over epochs
plt.plot(range(1, len(lrgd.cost_) + 1), lrgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')
plt.title('Logistic regression - Learning rate 0.05')
plt.tight_layout()
plt.show()
##########################################
#########################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('C:\\Users\\user\\Desktop\\machine learning lectures\\iris.data', header=None, encoding='utf-8')

# Select only setosa and versicolor (first 100 samples)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# Extract features: sepal length (column 0) and petal length (column 2)
X = df.iloc[0:100, [0, 2]].values

# Shuffle the data manually
np.random.seed(42)  # for reproducibility
indices = np.arange(100)
np.random.shuffle(indices)

X = X[indices]
y = y[indices]

# Manual split: 80% train, 20% test
split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test3 = y[:split_idx], y[split_idx:]

# Standardize features
X_train_std = np.copy(X_train)
X_train_std[:, 0] = (X_train[:, 0] - X_train[:, 0].mean()) / X_train[:, 0].std()
X_train_std[:, 1] = (X_train[:, 1] - X_train[:, 1].mean()) / X_train[:, 1].std()

X_train_01_subset = X_train_std[(y_train == 0) | (y_train == 1)]
y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]
lrgd = LogisticRegressionGD(eta=0.05,
    n_iter = 1000,
    random_state = 1)

lrgd.fit(X_train_01_subset,y_train_01_subset)

plt.scatter(X_train_01_subset[y_train_01_subset == 0, 0], X_train_01_subset[y_train_01_subset == 0, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X_train_01_subset[y_train_01_subset == 1, 0], X_train_01_subset[y_train_01_subset == 1, 1],
            color='blue', marker='x', label='versicolor')

# Plot decision boundary
x_values = np.linspace(X_train_01_subset[:, 0].min() - 1, X_train_01_subset[:, 0].max() + 1, 100)
# Using the equation: w0 + w1*x1 + w2*x2 = 0 → solve for x2
y_values = -(lrgd.w_[0] + lrgd.w_[1] * x_values) / lrgd.w_[2]
plt.plot(x_values, y_values, color='green', label='decision boundary')

# Label and show plot
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.title('Logistic Regression - Stochastic Gradient Descent')
plt.tight_layout()
plt.show()

# Plot cost over epochs
plt.plot(range(1, len(lrgd.cost_) + 1), lrgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')
plt.title('Logistic regression - Learning rate 0.05')
plt.tight_layout()
plt.show()
#########################################
########################################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=100.0, random_state=1,
solver='lbfgs', multi_class='ovr')
lr.fit(X_train_std, y_train)

# Scatter plot of training data (without loop)
plt.scatter(X_train_std[y_train == 0, 0], X_train_std[y_train == 0, 1],
            color='red', marker='o', label='Class 0')
plt.scatter(X_train_std[y_train == 1, 0], X_train_std[y_train == 1, 1],
            color='blue', marker='x', label='Class 1')
plt.scatter(X_train_std[y_train == 2, 0], X_train_std[y_train == 2, 1],
            color='green', marker='s', label='Class 2')

# Plot decision boundaries manually (3 OvR classifiers)
x_values = np.linspace(X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1, 100)

# Class 0 vs Rest
w0 = lr.coef_[0]
b0 = lr.intercept_[0]
y0 = -(w0[0] * x_values + b0) / w0[1]
plt.plot(x_values, y0, linestyle='--', color='red', label='Boundary for class 0')

# Class 1 vs Rest
w1 = lr.coef_[1]
b1 = lr.intercept_[1]
y1 = -(w1[0] * x_values + b1) / w1[1]
plt.plot(x_values, y1, linestyle='--', color='blue', label='Boundary for class 1')

# Class 2 vs Rest
w2 = lr.coef_[2]
b2 = lr.intercept_[2]
y2 = -(w2[0] * x_values + b2) / w2[1]
plt.plot(x_values, y2, linestyle='--', color='green', label='Boundary for class 2')

# Labels and formatting
plt.xlabel('Petal length [standardized]')
plt.ylabel('Petal width [standardized]')
plt.title('Logistic Regression Decision Boundaries For Training Datasets (Explicit Version)')
plt.legend(loc='upper left')
plt.show()
############################
############################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=100.0, random_state=1,
solver='lbfgs', multi_class='ovr')
lr.fit(X_train_std, y_train)

# Scatter plot of training data (without loop)
plt.scatter(X_test_std[y_test == 0, 0], X_test_std[y_test == 0, 1],
            color='red', marker='o', label='Class 0')
plt.scatter(X_test_std[y_test == 1, 0], X_test_std[y_test == 1, 1],
            color='blue', marker='x', label='Class 1')
plt.scatter(X_test_std[y_test == 2, 0], X_test_std[y_test == 2, 1],
            color='green', marker='s', label='Class 2')

# Plot decision boundaries manually (3 OvR classifiers)
x_values = np.linspace(X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1, 100)

# Class 0 vs Rest
w0 = lr.coef_[0]
b0 = lr.intercept_[0]
y0 = -(w0[0] * x_values + b0) / w0[1]
plt.plot(x_values, y0, linestyle='--', color='red', label='Boundary for class 0')

# Class 1 vs Rest
w1 = lr.coef_[1]
b1 = lr.intercept_[1]
y1 = -(w1[0] * x_values + b1) / w1[1]
plt.plot(x_values, y1, linestyle='--', color='blue', label='Boundary for class 1')

# Class 2 vs Rest
w2 = lr.coef_[2]
b2 = lr.intercept_[2]
y2 = -(w2[0] * x_values + b2) / w2[1]
plt.plot(x_values, y2, linestyle='--', color='green', label='Boundary for class 2')

# Labels and formatting
plt.xlabel('Petal length [standardized]')
plt.ylabel('Petal width [standardized]')
plt.title('Logistic Regression Decision Boundaries for Test Datasets (Explicit Version)')
plt.legend(loc='upper left')
plt.show()
####################################
###################################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=100.0, random_state=1,
solver='lbfgs', multi_class='ovr')
lr.fit(X_train_std, y_train)

print(lr.predict_proba(X_test_std[:3, :]).sum(axis=1))
print(lr.predict_proba(X_test_std[:3, :]).argmax(axis=1))
print(lr.predict(X_test_std[:3, :]))
lr.predict(X_test_std[0, :].reshape(1, -1))
#########################################
#########################################
weights, params = [], []
for c in np.arange(-5, 5):
    lr = LogisticRegression(C=10.**c, random_state=1,solver='lbfgs', multi_class='ovr')
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10.**c)
weights = np.array(weights)
plt.plot(params, weights[:, 0],label='petal length')
plt.plot(params, weights[:, 1], linestyle='--',label='petal width')
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.legend(loc='upper left')
plt.xscale('log')
plt.show()
################################
###############################
class LinearSVM:
    def __init__(self, learning_rate=0.001, C=1.0, n_iters=1000):
        self.lr = learning_rate
        self.C = C
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        y_ = np.where(y <= 0, -1, 1)
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) + self.b) >= 1
                if condition:
                    dw = self.w
                    db = 0
                else:
                    dw = self.w - self.C * y_[idx] * x_i
                    db = -self.C * y_[idx]

                self.w -= self.lr * dw
                self.b -= self.lr * db

    def predict(self, X):
        return np.where(np.dot(X, self.w) + self.b >= 0, 1, -1)

###############################
###############################
# Hybrid SVM implementation (linear + RBF kernel)
# Supports binary classification, vectorized, and includes plotting

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class HybridSVM:
    def __init__(self, C=1.0, kernel='rbf', gamma=0.1, tol=1e-3, max_passes=5):
        self.C = C
        self.kernel = kernel
        self.gamma = gamma
        self.tol = tol
        self.max_passes = max_passes
        self.alphas = None
        self.b = 0
        self.X = None
        self.y = None

    def _kernel_matrix(self, X):
        if self.kernel == 'linear':
            return X @ X.T
        elif self.kernel == 'rbf':
            X_norm = np.sum(X**2, axis=-1)
            return np.exp(-self.gamma * (X_norm[:, None] + X_norm[None, :] - 2 * X @ X.T))
        else:
            raise ValueError(f"Unsupported kernel: {self.kernel}")

    def _kernel_function(self, x1, x2):
        if self.kernel == 'linear':
            return np.dot(x1, x2)
        elif self.kernel == 'rbf':
            return np.exp(-self.gamma * np.linalg.norm(x1 - x2)**2)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.X = X
        self.y = np.where(y == 0, -1, 1)
        self.alphas = np.zeros(n_samples)
        self.b = 0
        K = self._kernel_matrix(X)

        passes = 0
        while passes < self.max_passes:
            alpha_changed = 0
            for i in range(n_samples):
                Ei = self._decision_function_single(X[i]) - self.y[i]

                if (self.y[i]*Ei < -self.tol and self.alphas[i] < self.C) or (self.y[i]*Ei > self.tol and self.alphas[i] > 0):
                    j = np.random.choice([x for x in range(n_samples) if x != i])
                    Ej = self._decision_function_single(X[j]) - self.y[j]

                    alpha_i_old = self.alphas[i]
                    alpha_j_old = self.alphas[j]

                    if self.y[i] != self.y[j]:
                        L = max(0, self.alphas[j] - self.alphas[i])
                        H = min(self.C, self.C + self.alphas[j] - self.alphas[i])
                    else:
                        L = max(0, self.alphas[i] + self.alphas[j] - self.C)
                        H = min(self.C, self.alphas[i] + self.alphas[j])

                    if L == H:
                        continue

                    eta = 2 * K[i, j] - K[i, i] - K[j, j]
                    if eta >= 0:
                        continue

                    self.alphas[j] -= self.y[j] * (Ei - Ej) / eta
                    self.alphas[j] = np.clip(self.alphas[j], L, H)

                    if abs(self.alphas[j] - alpha_j_old) < 1e-5:
                        continue

                    self.alphas[i] += self.y[i]*self.y[j]*(alpha_j_old - self.alphas[j])

                    b1 = self.b - Ei - self.y[i]*(self.alphas[i] - alpha_i_old)*K[i, i] - self.y[j]*(self.alphas[j] - alpha_j_old)*K[i, j]
                    b2 = self.b - Ej - self.y[i]*(self.alphas[i] - alpha_i_old)*K[i, j] - self.y[j]*(self.alphas[j] - alpha_j_old)*K[j, j]

                    if 0 < self.alphas[i] < self.C:
                        self.b = b1
                    elif 0 < self.alphas[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2) / 2

                    alpha_changed += 1

            passes = passes + 1 if alpha_changed == 0 else 0

    def _decision_function_single(self, x):
        result = 0
        for i in range(len(self.alphas)):
            if self.alphas[i] > 0:
                result += self.alphas[i] * self.y[i] * self._kernel_function(self.X[i], x)
        return result + self.b

    def predict(self, X):
        return np.where(np.array([self._decision_function_single(x) for x in X]) >= 0, 1, 0)

    def plot_decision_boundary(self, X, y, resolution=0.02):
        markers = ('s', 'x')
        colors = ('red', 'blue')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        grid = np.array([xx1.ravel(), xx2.ravel()]).T
        Z = self.predict(grid)
        Z = Z.reshape(xx1.shape)

        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolors='k')
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title(f'SVM Decision Boundary ({self.kernel} kernel)')
        plt.show()

###############################
###############################
import numpy as np

class SVM:
    def __init__(self, kernel='linear', C=1.0, gamma=0.1, degree=3, tol=1e-3, max_iter=1000):
        self.kernel = kernel
        self.C = C
        self.gamma = gamma
        self.degree = degree
        self.tol = tol
        self.max_iter = max_iter

    def _kernel_func(self, X, Y=None):
        if self.kernel == 'linear':
            return X @ Y.T if Y is not None else X @ X.T
        elif self.kernel == 'rbf':
            if Y is None: Y = X
            sq_dists = np.sum((X[:, np.newaxis] - Y[np.newaxis, :]) ** 2, axis=2)
            return np.exp(-self.gamma * sq_dists)
        elif self.kernel == 'poly':
            return (X @ Y.T + 1) ** self.degree if Y is not None else (X @ X.T + 1) ** self.degree
        else:
            raise ValueError(f"Unknown kernel type: {self.kernel}")

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = y.astype(np.float64)
        y[y == 0] = -1

        K = self._kernel_func(X)
        alpha = np.zeros(n_samples)
        b = 0

        for _ in range(self.max_iter):
            alpha_prev = np.copy(alpha)
            for i in range(n_samples):
                j = np.random.randint(0, n_samples)
                while j == i:
                    j = np.random.randint(0, n_samples)
                xi, xj = X[i], X[j]
                yi, yj = y[i], y[j]
                kii, kij, kjj = K[i, i], K[i, j], K[j, j]

                eta = 2 * kij - kii - kjj
                if eta >= 0:
                    continue

                alpha_j_new = alpha[j] - (yj * (self._decision(X[i], X, y, alpha, b, K) -
                                                self._decision(X[j], X, y, alpha, b, K))) / eta

                L = max(0, alpha[j] - alpha[i]) if yi != yj else max(0, alpha[i] + alpha[j] - self.C)
                H = min(self.C, self.C + alpha[j] - alpha[i]) if yi != yj else min(self.C, alpha[i] + alpha[j])
                alpha_j_new = np.clip(alpha_j_new, L, H)
                alpha_i_new = alpha[i] + yi * yj * (alpha[j] - alpha_j_new)

                alpha[i], alpha[j] = alpha_i_new, alpha_j_new

                b1 = b - (self._decision(X[i], X, y, alpha, b, K) - yi)
                b2 = b - (self._decision(X[j], X, y, alpha, b, K) - yj)
                b = (b1 + b2) / 2

            diff = np.linalg.norm(alpha - alpha_prev)
            if diff < self.tol:
                break

        self.alpha = alpha
        self.b = b
        self.X = X
        self.y = y
        self.support_ = alpha > 1e-4

    def _decision(self, x, X, y, alpha, b, K):
        idx = np.where(alpha > 1e-4)[0]
        return np.sum(alpha[idx] * y[idx] * K[idx, np.where((X == x).all(1))[0][0]]) + b

    def project(self, X):
        K = self._kernel_func(X, self.X)
        return (self.alpha[self.support_] * self.y[self.support_]) @ K[:, self.support_].T + self.b

    def predict(self, X):
        return np.sign(self.project(X))

class MultiClassSVM:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.classifiers = {}

    def fit(self, X, y):
        self.labels = np.unique(y)
        for label in self.labels:
            binary_y = np.where(y == label, 1, -1)
            clf = SVM(**self.kwargs)
            clf.fit(X, binary_y)
            self.classifiers[label] = clf

    def predict(self, X):
        scores = {label: clf.project(X) for label, clf in self.classifiers.items()}
        return np.array([max(scores, key=lambda k: scores[k][i]) for i in range(X.shape[0])])

##############################
##############################
import numpy as np

class KernelSVM:
    def __init__(self, C=1.0, kernel='rbf', gamma=0.1, tol=1e-3, max_passes=5):
        self.C = C
        self.kernel = kernel
        self.gamma = gamma
        self.tol = tol
        self.max_passes = max_passes
        self.alphas = None
        self.b = 0
        self.X = None
        self.y = None

    def _kernel_function(self, x1, x2):
        if self.kernel == 'linear':
            return np.dot(x1, x2)
        elif self.kernel == 'rbf':
            return np.exp(-self.gamma * np.linalg.norm(x1 - x2)**2)
        else:
            raise ValueError(f"Unsupported kernel: {self.kernel}")

    def _compute_kernel_matrix(self, X):
        n_samples = X.shape[0]
        K = np.zeros((n_samples, n_samples))
        for i in range(n_samples):
            for j in range(n_samples):
                K[i, j] = self._kernel_function(X[i], X[j])
        return K

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.X = X
        self.y = np.where(y == 0, -1, 1)  # Convert 0 to -1
        self.alphas = np.zeros(n_samples)
        self.b = 0

        K = self._compute_kernel_matrix(X)

        passes = 0
        while passes < self.max_passes:
            alpha_changed = 0
            for i in range(n_samples):
                Ei = self._decision_function(X[i]) - self.y[i]

                if (self.y[i] * Ei < -self.tol and self.alphas[i] < self.C) or (self.y[i] * Ei > self.tol and self.alphas[i] > 0):
                    j = np.random.choice([x for x in range(n_samples) if x != i])
                    Ej = self._decision_function(X[j]) - self.y[j]

                    alpha_i_old = self.alphas[i]
                    alpha_j_old = self.alphas[j]

                    if self.y[i] != self.y[j]:
                        L = max(0, self.alphas[j] - self.alphas[i])
                        H = min(self.C, self.C + self.alphas[j] - self.alphas[i])
                    else:
                        L = max(0, self.alphas[i] + self.alphas[j] - self.C)
                        H = min(self.C, self.alphas[i] + self.alphas[j])

                    if L == H:
                        continue

                    eta = 2 * K[i, j] - K[i, i] - K[j, j]
                    if eta >= 0:
                        continue

                    self.alphas[j] -= self.y[j] * (Ei - Ej) / eta
                    self.alphas[j] = np.clip(self.alphas[j], L, H)

                    if abs(self.alphas[j] - alpha_j_old) < 1e-5:
                        continue

                    self.alphas[i] += self.y[i] * self.y[j] * (alpha_j_old - self.alphas[j])

                    b1 = self.b - Ei - self.y[i]*(self.alphas[i]-alpha_i_old)*K[i, i] - self.y[j]*(self.alphas[j]-alpha_j_old)*K[i, j]
                    b2 = self.b - Ej - self.y[i]*(self.alphas[i]-alpha_i_old)*K[i, j] - self.y[j]*(self.alphas[j]-alpha_j_old)*K[j, j]

                    if 0 < self.alphas[i] < self.C:
                        self.b = b1
                    elif 0 < self.alphas[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2) / 2.0

                    alpha_changed += 1

            passes = passes + 1 if alpha_changed == 0 else 0

    def _decision_function(self, x):
        result = 0
        for i in range(len(self.alphas)):
            if self.alphas[i] > 0:
                result += self.alphas[i] * self.y[i] * self._kernel_function(self.X[i], x)
        return result + self.b

    def predict(self, X):
        return np.where(np.array([self._decision_function(x) for x in X]) >= 0, 1, 0)

###############################
###############################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class SVMFull:
    def __init__(self, kernel='linear', C=1.0, gamma=0.1, degree=3, tol=1e-3, max_iter=1000):
        self.kernel = kernel
        self.C = C
        self.gamma = gamma
        self.degree = degree
        self.tol = tol
        self.max_iter = max_iter

    def _kernel_func(self, X, Y=None):
        if self.kernel == 'linear':
            return X @ Y.T if Y is not None else X @ X.T
        elif self.kernel == 'rbf':
            if Y is None: Y = X
            sq_dists = np.sum((X[:, np.newaxis] - Y[np.newaxis, :]) ** 2, axis=2)
            return np.exp(-self.gamma * sq_dists)
        elif self.kernel == 'poly':
            return (X @ Y.T + 1) ** self.degree if Y is not None else (X @ X.T + 1) ** self.degree
        else:
            raise ValueError(f"Unknown kernel type: {self.kernel}")

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = y.astype(np.float64)
        y[y == 0] = -1

        K = self._kernel_func(X)
        alpha = np.zeros(n_samples)
        b = 0

        for _ in range(self.max_iter):
            alpha_prev = np.copy(alpha)
            for i in range(n_samples):
                j = np.random.randint(0, n_samples)
                while j == i:
                    j = np.random.randint(0, n_samples)

                xi, xj = X[i], X[j]
                yi, yj = y[i], y[j]
                kii, kij, kjj = K[i, i], K[i, j], K[j, j]

                eta = 2 * kij - kii - kjj
                if eta >= 0:
                    continue

                alpha_j_new = alpha[j] - (yj * (self._decision(X[i], X, y, alpha, b, K) -
                                                self._decision(X[j], X, y, alpha, b, K))) / eta

                L = max(0, alpha[j] - alpha[i]) if yi != yj else max(0, alpha[i] + alpha[j] - self.C)
                H = min(self.C, self.C + alpha[j] - alpha[i]) if yi != yj else min(self.C, alpha[i] + alpha[j])
                alpha_j_new = np.clip(alpha_j_new, L, H)
                alpha_i_new = alpha[i] + yi * yj * (alpha[j] - alpha_j_new)

                alpha[i], alpha[j] = alpha_i_new, alpha_j_new

                b1 = b - (self._decision(X[i], X, y, alpha, b, K) - yi)
                b2 = b - (self._decision(X[j], X, y, alpha, b, K) - yj)
                b = (b1 + b2) / 2

            diff = np.linalg.norm(alpha - alpha_prev)
            if diff < self.tol:
                break

        self.alpha = alpha
        self.b = b
        self.X = X
        self.y = y
        self.support_ = alpha > 1e-4

    def _decision(self, x, X, y, alpha, b, K):
        idx = np.where(alpha > 1e-4)[0]
        return np.sum(alpha[idx] * y[idx] * K[idx, np.where((X == x).all(1))[0][0]]) + b

    def project(self, X):
        K = self._kernel_func(X, self.X)
        return (self.alpha[self.support_] * self.y[self.support_]) @ K[:, self.support_].T + self.b

    def predict(self, X):
        return np.sign(self.project(X))

    def plot_decision_boundary(self, X, y, resolution=0.02):
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'green', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        grid = np.array([xx1.ravel(), xx2.ravel()]).T
        Z = self.predict(grid)
        Z = Z.reshape(xx1.shape)

        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolors='k')
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title(f'SVM Decision Boundary ({self.kernel} kernel)')
        plt.show()


class MultiClassSVM:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.classifiers = {}

    def fit(self, X, y):
        self.labels = np.unique(y)
        for label in self.labels:
            binary_y = np.where(y == label, 1, -1)
            clf = SVM(**self.kwargs)
            clf.fit(X, binary_y)
            self.classifiers[label] = clf

    def predict(self, X):
        scores = {label: clf.project(X) for label, clf in self.classifiers.items()}
        return np.array([max(scores, key=lambda k: scores[k][i]) for i in range(X.shape[0])])

    def plot_decision_boundary(self, X, y):
        for label, clf in self.classifiers.items():
            print(f"Plotting for class: {label}")
            clf.plot_decision_boundary(X, y)

###############################
##############################
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)


from sklearn.svm import SVC
svm = SVC(kernel='linear', C=1.0, random_state=1)
svm.fit(X_train_std, y_train)

# Scatter plot of training data (without loop)
plt.scatter(X_test_std[y_test == 0, 0], X_test_std[y_test == 0, 1],
            color='red', marker='o', label='Class 0')
plt.scatter(X_test_std[y_test == 1, 0], X_test_std[y_test == 1, 1],
            color='blue', marker='x', label='Class 1')
plt.scatter(X_test_std[y_test == 2, 0], X_test_std[y_test == 2, 1],
            color='green', marker='s', label='Class 2')

# Plot decision boundaries manually (3 OvR classifiers)
x_values = np.linspace(X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1, 100)

# Class 0 vs Rest
w0 = svm.coef_[0]
b0 =svm.intercept_[0]
y0 = -(w0[0] * x_values + b0) / w0[1]
plt.plot(x_values, y0, linestyle='--', color='red', label='Boundary for class 0')

# Class 1 vs Rest
w1 = svm.coef_[1]
b1 = svm.intercept_[1]
y1 = -(w1[0] * x_values + b1) / w1[1]
plt.plot(x_values, y1, linestyle='--', color='blue', label='Boundary for class 1')

# Class 2 vs Rest
w2 = svm.coef_[2]
b2 = svm.intercept_[2]
y2 = -(w2[0] * x_values + b2) / w2[1]
plt.plot(x_values, y2, linestyle='--', color='green', label='Boundary for class 2')


plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
######################################
#####################################
from sklearn.linear_model import SGDClassifier
ppn = SGDClassifier(loss='perceptron')
lr = SGDClassifier(loss='log')
svm = SGDClassifier(loss='hinge')
###################################
##################################
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
X_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(X_xor[:, 0] > 0,
X_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)
plt.scatter(X_xor[y_xor == 1, 0],
X_xor[y_xor == 1, 1],
c='b', marker='x',
label='1')
plt.scatter(X_xor[y_xor == -1, 0],
X_xor[y_xor == -1, 1],
c='r',
marker='s',
label='-1')
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc='best')
plt.tight_layout()
plt.show()
#############################
##############FIRST ONE USING LIBRARY##############
svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(X_xor, y_xor)
#plot_decision_regions(X_xor, y_xor, classifier=svm)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
#############################
##############SECOND ONE WITHOUT LIBRARY##############
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define XOR dataset used in Sebastian Raschka’s book
np.random.seed(1)
X_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)

# Step 2: Set hyperparameters
gamma = 0.10  # same as in SVC
b = 0.0       # bias term (assumed for now)

# Step 3: Manually assign alphas (in reality, you’d solve QP to get these)
# For simplicity, we'll just assign small nonzero alphas to mimic influence
alpha = np.ones(len(X_xor)) * 0.5

# Step 4: Define RBF kernel manually
def rbf_kernel(x, xi, gamma):
    diff = x - xi
    return np.exp(-gamma * np.dot(diff, diff))

# Step 5: Define decision function from scratch
def decision_function(x):
    total = 0
    for i in range(len(X_xor)):
        total += alpha[i] * y_xor[i] * rbf_kernel(x, X_xor[i], gamma)
    return total + b

# Step 6: Create mesh grid
x0_range = np.linspace(X_xor[:, 0].min() - 1, X_xor[:, 0].max() + 1, 300)
x1_range = np.linspace(X_xor[:, 1].min() - 1, X_xor[:, 1].max() + 1, 300)
xx0, xx1 = np.meshgrid(x0_range, x1_range)

Z = np.zeros_like(xx0)

for i in range(xx0.shape[0]):
    for j in range(xx0.shape[1]):
        point = np.array([xx0[i, j], xx1[i, j]])
        Z[i, j] = decision_function(point)

# Step 7: Plot decision boundary (f(x) = 0)
plt.contour(xx0, xx1, Z, levels=[0], colors='black', linewidths=2)

# Step 8: Plot original points
plt.scatter(X_xor[y_xor == -1][:, 0], X_xor[y_xor == -1][:, 1], color='red', marker='o', label='Class -1')
plt.scatter(X_xor[y_xor == 1][:, 0], X_xor[y_xor == 1][:, 1], color='blue', marker='x', label='Class +1')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Non-linear SVM (RBF Kernel) - From Scratch (XOR)')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
##################################
##########SVM####################
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load iris dataset
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]  # petal length and petal width
y = iris.target           # classes: 0, 1, 2

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

# Standardize
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)

# Use entire training data
X_data = X_train_std
y_data = y_train

# Step 2: Hyperparams
gamma = 0.10
b = 0.0
alpha = np.ones(len(X_data)) * 0.5  # Fake alphas

# Step 3: RBF kernel
def rbf_kernel(x, xi, gamma):
    diff = x - xi
    return np.exp(-gamma * np.dot(diff, diff))

# Step 4: OvR decision functions (one per class)
def decision_function_class(x, target_class):
    total = 0
    for i in range(len(X_data)):
        y_binary = 1 if y_data[i] == target_class else -1
        total += alpha[i] * y_binary * rbf_kernel(x, X_data[i], gamma)
    return total + b

# Step 5: Meshgrid for plotting
x0_range = np.linspace(X_data[:, 0].min() - 1, X_data[:, 0].max() + 1, 300)
x1_range = np.linspace(X_data[:, 1].min() - 1, X_data[:, 1].max() + 1, 300)
xx0, xx1 = np.meshgrid(x0_range, x1_range)
Z = np.zeros_like(xx0)

# Step 6: Predict class at each grid point using OvR
for i in range(xx0.shape[0]):
    for j in range(xx0.shape[1]):
        point = np.array([xx0[i, j], xx1[i, j]])
        scores = [
            decision_function_class(point, class_label)
            for class_label in np.unique(y_data)
        ]
        Z[i, j] = np.argmax(scores)

# Step 7: Plot decision regions
from matplotlib.colors import ListedColormap
colors = ('#FFAAAA', '#AAFFAA', '#AAAAFF')
cmap = ListedColormap(colors[:len(np.unique(y_data))])
plt.contourf(xx0, xx1, Z, alpha=0.3, cmap=cmap)

# Step 8: Plot training points
markers = ('o', 's', '^')
for idx, cl in enumerate(np.unique(y_data)):
    plt.scatter(X_data[y_data == cl, 0], X_data[y_data == cl, 1],
                c=colors[idx], marker=markers[idx], label=f'Class {cl}',
                edgecolor='black')

plt.xlabel('Petal length (std)')
plt.ylabel('Petal width (std)')
plt.title('Multiclass SVM Decision Boundary (Manual RBF, OvR)')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
