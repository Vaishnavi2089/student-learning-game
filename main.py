print("Welcome to Student Learning Game 🎮")
player_name=input("Enter your name: ")
print("Welcome " + player_name+"!"+"lets start your game")
print("Select your subject")
print("1:GK")
print("2:English")
print("3:Computer Science")
subject=input(int("Select your subject: "))
if subject==1:
    print("GK quiz starting")
elif subject==2:
    print("English quiz starting")
elif subject==3:
    print("Computer Science quiz starting")
else
    print("Invalid choice")
