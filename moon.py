myString= "This is a string"
print(myString)
print(type(myString))

print(myString + " is the data type " + str(type(myString)))

# Concatonating

FirstString = "Water"
secondstring = 'Fall'
thirdstring = FirstString +  secondstring
print(thirdstring)

# name = input("What is your name?")
# color = input("What is your favorite color?")
# animal = input("What is your favorite animal?")
# print("{}, you like a {} {}!" .format(name, color, animal))

myFruitList = ["apple", "pineapple", "banana"]

myFruitList[1] = "orange"
print(myFruitList)

favoriteRestaraunts = ("Bojangles", "Mcdonalds", "Popeyes")
print(favoriteRestaraunts[0])
print(favoriteRestaraunts[2])

print(f"My favorite restaraunt is {favoriteRestaraunts[0]}")

myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)