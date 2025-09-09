#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print("👋 Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🖥️ Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("🤝 It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

# Run the game
play_game()


# In[4]:


# UPDATED CODE WITH SCORE TRACKING.........


# In[6]:


import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    win, lose, draw = 0, 0, 0  # Score tracking
    
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print(f"\n🏆 Final Score: Wins - {win}, Losses - {lose}, Draws - {draw}")
            print("👋 Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🖥️ Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("🤝 It's a draw!")
            draw += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
            win += 1
        else:
            print("😢 You lose!")
            lose += 1
        
        # Display score after each round
        print(f"📊 Score: Wins - {win}, Losses - {lose}, Draws - {draw}")

# Run the game
play_game()


# In[ ]:




