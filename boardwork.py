#print("Sam Cusick: \music, video games, working out")

#animal = input("Name an animal: ")
#place = input("Name a place: ")
#verb = input("Name a verb: ")

#print(f"The {animal} went to the {place} and {verb} my hat")

#base = int(input("What is the base?: "))
#height = int(input("What is the height?: "))
#area = base*height*0.5
#print("The area is:",area)

#winner = input("Who is going to win the superbowl?: ")
#if winner == "KC":
#    print("That's so true!")
#else:
#    print('WRONG!')

#grade = int(input("What is your grade?: "))
#if grade >= 90:
#    print("You have an A")
#elif grade >= 80:
#    print("You have an B")
#elif grade >= 70:
#    print("You have an C")
#elif grade >= 60:
#    print("You have an D")
#elif grade >= 0:
#    print("You have an F")

#grade = float(input("What is your grade?: "))
#if grade >= 90:
#   print("A")
#if grade < 90 and grade >= 80:
#    print("B")
#if grade < 80 and grade >= 70:
#    print("C")
#if grade < 70 and grade >= 60:
#    print("C")
#if grade < 60 and grade >= 50:
#    print("D")
#if grade < 50:
#    print("F")

#for i in range(100,201):
#    print(i)
#for i in range(100, -101, -1):
#    print(i)
#for i in range(7, 78, 7):
#    print(i)

#answer = "q"
#guess = ''
#while guess != 'q':
#    guess = input("Guess a letter: ")
#    if guess == "Q":
#        guess = "q"
#if guess == "q":
#    print("You got it!")

#for i in range(100, -101, -1):
#    print(i)
#for i in range(5, 56, 5):
#    print(i)
#for i in range(1000):
#    print("A")

#total = 0
#for i in range(6):
#    total = total + i
#print(total)

#word = input("What's a word?")
#dog = word.count("g")
#print(dog)

#num_list = []
#while len(num_list) < 10:
#    add = int(input("What do number do you want to add? "))
#    num_list.append(add)
#threshold = int(input("What is your threshold? "))
#for num in num_list:
#    if num_list[num] >= threshold:
#        print(num_list[num])

num_list = []
counter = 0
while len(num_list) < 10:
    add = float(input("What do number do you want to add? "))
    num_list.append(add)
threshold = float(input("What is your threshold? "))
for num in num_list:
    spot = num_list[num-1]
    if spot >= threshold:
        counter = counter + 1

print(counter)