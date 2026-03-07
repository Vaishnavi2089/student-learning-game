print("Welcome to Student Learning Game 🎮")
player_name=input("Enter your name: ")
print("Welcome " + player_name+"!"+"lets start your game")
print("Select your subject")
print("1:GK")
print("2:English")
print("3:Computer Science")
subject=int(input("Select your subject: "))
if subject==1:
    print("GK quiz starting.....")
elif subject==2:
    print("English quiz starting.....")
elif subject==3:
    print("Computer Science quiz starting.....")
else:
    print("Invalid choice🫣")
print("select difficulty level:")
print("1:Easy")
print("2:Medium")
print("3:Hard")
difficulty=int(input("Select your difficulty level: "))
if difficulty==1:
    print("Easy starting.....")
elif difficulty==2:
    print("Medium starting.....")
elif difficulty==3:
    print("Hard starting.....")
else :
    print("Invalid choice🫣")