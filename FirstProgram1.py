import time

time.sleep(5)

print("Welcome")
print()
print()
time.sleep(3)
print("How Andrey are you? A quiz, made by daddy")
time.sleep(3)
print()
print()
a = input("Do you like Putin: ")
b = input("Do you have a maid or a driver at home: ")
c = input("Do you pop your collar: ")
d = input("Is Ponch better than you at FIFA: ")
e = input("Were u mad about Miracle On Ice: ")
f = input("Should gays have rights: ")
g = input("Should transgenders have rights: ")
h = input("Do you have a fucking insatiable desire to annex Crimea: ")
i = input("Were u mad when Reagan shoved his cock down Gorbachevs throat: ")
j = input("Can your girlfriend talk: ")

response = [a, b, c, d, e, f, g, h, i, j]

print()
print()
print()

if response.count('yes') < 5:
	print("More than half of your answers were different from Andrey's. This gives me significant statistical evidence to conclude that you are NOT a flaming douche.")

elif response.count('yes') == 5:
        print("Half of your answers matched Andrey's. Typically, a 50% matching rate would not be conclusive,\
but the fact that you shared even one answer with Andrey is a damn embarassment to you and your family")

elif response.count('yes') > 5:
        print("A majority of your answers matched Andreys. This gives me significant statistical evidence to determine that you are indeed a Grade A piece of shit. Fuck you and fuck Andrey.")
print()
print()
time.sleep(3)
print("Thank you for participating in Ponchs first dabble at computer science.")
time.sleep(3)
print()
print("Look forward for more programs, as Ponch will be restarting college in an attempt to actually pass one class and hopefully become wikileaks one day.")
time.sleep(3)
print()
print("this is Seargant Chris Kyle, signing off")
print()
time.sleep(3)
print("HOORAH")












