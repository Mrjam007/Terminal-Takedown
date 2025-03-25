import time
import random
from textwrap import dedent

class CodingChallenge:
    # ... [keep previous methods unchanged] ...

    def show_tutorial(self):
        print("\033[1;36m" + "="*40 + "\033[0m")
        print("\033[1;36m        HOW TO PLAY\033[0m")
        print("\033[1;36m" + "="*40 + "\033[0m")
        print("\n\033[96mWelcome to Python Code Warrior!\033[0m")
        print("You'll be given coding challenges to solve.")
        print("Here's what you need to know:\n")
        
        print("\033[93m1. Challenge Types:\033[0m")
        print("- 🛠️  Fix syntax errors (missing colons, brackets)")
        print("- 🧩 Complete functions/algorithms")
        print("- 🏗️  Build classes and objects")
        
        print("\n\033[93m2. Game Flow:\033[0m")
        print("- You'll see a code snippet with a problem")
        print("- Type your solution directly in Python")
        print("- We'll test it automatically")
        print("- Earn points for speed and accuracy!")
        
        print("\n\033[93m3. Example Challenge:\033[0m")
        print("\033[90m# Fix this function:\033[0m")
        print("\033[36mdef add(a, b)")
        print("    return a + b\033[0m")
        print("\033[92m# Correct answer:\033[0m")
        print("\033[36mdef add(a, b):")
        print("    return a + b\033[0m")
        
        print("\n\033[93m4. Scoring:\033[0m")
        print("- Base 100 points per challenge")
        print("- -1 point per second taken")
        print("- -10 points per failed attempt")
        print("- Bonus for first-try success!")
        
        print("\n\033[93m5. Controls:\033[0m")
        print("- Type code directly when prompted")
        print("- Use proper Python syntax")
        print("- Ask for hints if stuck (costs points)")
        
        print("\n\033[95mPress Enter to try a practice challenge...\033[0m")
        input()
        
        # Practice challenge
        print("\n\033[1mPRACTICE CHALLENGE\033[0m")
        print("Fix this function:")
        print("\033[36mdef subtract(a, b)")
        print("    return a - b\033[0m")
        
        while True:
            answer = input("\nYour solution:\n")
            if ":" in answer and "def subtract(a, b):" in answer:
                print("\033[92m✔ Correct! You're ready!\033[0m")
                break
            else:
                print("\033[91m✘ Almost! Add the missing colon\033[0m")
        
        print("\n\033[95mProceeding to main game...\n\033[0m")
        time.sleep(1)

    def start(self):
        print("\033[1;32m=== PYTHON CODE WARRIOR ===\033[0m")
        if input("Show tutorial? (y/n): ").lower() == 'y':
            self.show_tutorial()
        self.choose_difficulty()
        # ... [rest of start method unchanged] ...

if __name__ == "__main__":
    game = CodingChallenge()
    game.start()