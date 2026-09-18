# [Do you know your Beyonce?]
# Author: [Omarai Williams]
# A quiz/questionnaire program built for CS 104 Project 1

# TODO: Define your variables here.
score = 0

# TODO: Print a welcome message introducing your program.
print("Welcome to the Beyonce quiz that got everyone buzzin")
print()
# TODO: Write your questions and conditional logic here.
birthplace = input("Where was Beyonce born? (Enter 1-3) Houston, Tx, 2. Little Rock, Ar, 3. New York City, NY ")

if birthplace == "1":
    print("correct")
    score += 1

else:
    print()
    print("wrong")
    print("correct answer: 1. Houston, Tx")

girl_group = input("What Girl Group was Beyonce in? (Enter 1-3) Pussycat Dolls, 2. Destiny's Child, 3. SWV ")

if girl_group == "2":
    print("correct")
    score += 1

else:
    print()
    print("wrong")
    print("correct answer: 2. Destiny's Child")

husband = input("What is Beyonce's husband name? (Enter 1-3) 1. Jay Z, 2. Curtis, 3. Kanye West ")

if birthplace == "1":
    print("correct")
    score += 1

else:
    print()
    print("wrong")
    print("correct answer: 1. Jay Z")

album = input("What was Beyonce's first solo album? (Enter 1-3) 1. Channel Orange, 2. Dangerously in Love, 3. Pink Friday ")

if album == "2":
    print("correct")
    score += 1

else:
    print()
    print("wrong")
    print("correct answer: 2. Dangerously in Love")

grammy = input("Bonus: How many Grammys does Beyonce have? (Enter 1-3) 1. 12 grammys, 2. 28 grammys, 3. 35 grammys ")

if grammy == "3":
    print("correct")
    score += 3

else:
    print()
    print("wrong")
    print("correct answer: 3. 35")

print()
# Follow the outline you planned in your README.

# TODO: Display the final results to the user.
if score == 7:
  print("THEE BUG A BOO")
elif score < 7 and score > 3:
  print("Barely Buzzin")
else: 
    print("Not a Bee at all")
