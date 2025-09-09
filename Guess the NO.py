#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))  # Get user input
            attempts += 1  # Count attempts

            if guess < secret_number:
                print("Too low! Try again. ⬆️")
            elif guess > secret_number:
                print("Too high! Try again. ⬇️")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit loop if correct guess

        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the game
number_guessing_game()


# In[4]:


import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    
    # Select difficulty level
    print("\nChoose a difficulty level:")
    print("1️⃣ Easy (1-50, 10 attempts)")
    print("2️⃣ Medium (1-100, 7 attempts)")
    print("3️⃣ Hard (1-200, 5 attempts)")

    while True:
        try:
            difficulty = int(input("Enter 1, 2, or 3: "))
            if difficulty == 1:
                max_number, max_attempts = 50, 10
            elif difficulty == 2:
                max_number, max_attempts = 100, 7
            elif difficulty == 3:
                max_number, max_attempts = 200, 5
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number (1-3).")

    secret_number = random.randint(1, max_number)  
    attempts = 0  

    print(f"\n🔢 Guess a number between 1 and {max_number}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))  
            attempts += 1  

            if guess < secret_number:
                print(f"⬆️ Too low! {max_attempts - attempts} attempts left.")
            elif guess > secret_number:
                print(f"⬇️ Too high! {max_attempts - attempts} attempts left.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        
    if attempts == max_attempts:
        print(f"😢 Game Over! The correct number was {secret_number}.")

# Run the game
number_guessing_game()


# In[ ]:




