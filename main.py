import requests
import random
print("Welcome to Student Learning Game 🎮")
player_name=input("Enter your name: ")
print("Welcome " + player_name+"!"+"lets start your game")
print("Select your subject")
print("1:GK")
print("2:English")
print("3:Computer Science")
subject=int(input("Select your subject: "))
if subject == 1:
    category = 9

elif subject == 2:
    category = 10

elif subject == 3:
    category = 18
# DIFFICULTY SELECTION
print("Select difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = int(input("Select your difficulty level: "))

if difficulty == 1:
    difficulty_level = "easy"
elif difficulty == 2:
    difficulty_level = "medium"
elif difficulty == 3:
    difficulty_level = "hard"
else:
    print("Invalid difficulty")
    exit()

# API URL
url = f"https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty_level}&type=multiple"

response = requests.get(url)
data = response.json()

question_data = data["results"][0]

question = question_data["question"]
correct_answer = question_data["correct_answer"]
incorrect_answers = question_data["incorrect_answers"]

# Combine answers
options = incorrect_answers + [correct_answer]
random.shuffle(options)

print("Solve this to unlock the treasure door!\n")

print("Question:")
print(question)
print()

for i, option in enumerate(options):
    print(f"{i+1}. {option}")

answer = int(input("\nEnter your answer number: "))

if options[answer - 1] == correct_answer:
    print("\n✅ Correct! The treasure door opens.")
else:
    print("\n❌ Wrong answer!")
