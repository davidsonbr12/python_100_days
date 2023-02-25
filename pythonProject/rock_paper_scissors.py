import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
running = True
while running:
    while True:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors:\n\n"))
        if user_choice < 0 or user_choice > 2:
            print('\nEnter a valid input\n')
            continue
        else:
            break

    print(f'\nPlayer chose:\n{game_images[user_choice]}')

    computer_choice = random.randint(0, 2)

    print(f'Computer chose:\n{game_images[computer_choice]}')

    # Logic to determine winner using handy Python lists
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 0:
        if computer_choice == 1:
            print('You lose.')
        if computer_choice == 2:
            print('**You win!**')
    elif user_choice == 1:
        if computer_choice == 2:
            print('You lose.')
        if computer_choice == 0:
            print('**You win!**')
    elif user_choice == 2:
        if computer_choice == 0:
            print('You lose.')
        if computer_choice == 1:
            print('**You win!**')
    if input('Do you want to play again?  Press "Y" or press "N" to quit\n').lower() == 'n':
        running = False