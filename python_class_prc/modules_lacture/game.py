# rock,paper,sessior Game
# import random
# user_score=0
# computer_score=0

# system_choose=["rock","paper","scissor"]
# user_input=input(f'select:["rock","paper","scissor"]')
# if user_input==random.choice(system_choose):
#   print("TIE")
# elif.user_input=="rock".and,system_choose==paper
#   print(paper won)

import random
max_attempt=3
user_score = 0
computer_score = 0
attempt=0

choices = ["rock", "paper", "scissor"]

while attempt< max_attempt:
  user_input = input("\nSelect (rock/paper/scissor) or 'quit' to exit: ").lower()

  if user_input == "quit":
    break

  if user_input not in choices:
    print("Invalid Choice!")
    continue

  computer_choice = random.choice(choices)

  print("Computer chose:", computer_choice)

  if user_input == computer_choice:
    print("TIE")

  elif (
    (user_input == "rock" and computer_choice == "scissor") or
    (user_input == "paper" and computer_choice == "rock") or
    (user_input == "scissor" and computer_choice == "paper")
    ):
    print("You Win!")
    user_score += 1

  else:
    print("Computer Wins!")
    computer_score += 1

    print("User Score:", user_score)
    print("Computer Score:", computer_score)
  attempt+=1  
print("\nGame Over!")
print("Final User Score:", user_score)
print("Final Computer Score:", computer_score)

if user_score > computer_score:
    print("🏆 You won the game!")
elif computer_score > user_score:
    print("💻 Computer won the game!")
else:
    print("🤝 Match Draw!")
