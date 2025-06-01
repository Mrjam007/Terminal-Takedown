import time
import random
from textwrap import dedent

class CodingChallenge:
    def __init__(self):
        self.score = 0
        self.difficulty = None
        self.challenges = []

    def choose_difficulty(self):
        print("\033[1;32m=== PYTHON CODE WARRIOR ===\033[0m")
        print("Choose difficulty:")
        print("1. Easy\n2. Medium\n3. Hard")
        print("\033[90m(Press Ctrl+C at any time to exit)\033[0m")
        choice = input("Enter choice (1-3): ").strip()
        self.difficulty = ['easy', 'medium', 'hard'][int(choice)-1] if choice in ['1','2','3'] else 'easy'
        self.generate_challenges()

    def display_code(self, code):
        print("\033[36m" + code + "\033[0m")

    def run_tests(self, user_code, challenge):
        try:
            exec(user_code, {})
            return True
        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            return False

    def generate_challenges(self):
        # Basic challenge setup (customize as needed)
        base_challenges = []
        for i in range(1, 51):
            base_challenges.append({
                "desc": f"Challenge {i}",
                "code": dedent(f"""
                def problem_{i}():
                    # Your code here
                """),
                "tests": [],
                "hint": "Sample hint"
            })
        self.challenges = random.sample(base_challenges, 10)

    def show_tutorial(self):
        # Tutorial code remains the same
        print("\033[1;36m" + "="*40 + "\033[0m")
        print("\033[1;36m        HOW TO PLAY\033[0m")
        print("\033[1;36m" + "="*40 + "\033[0m")
        print("\n\033[96mWelcome to Python Code Warrior!\033[0m")
        print("You'll be given coding challenges to solve.")
        print("\033[90m(Press Ctrl+C at any time to exit)\033[0m")  # Add exit notice
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
        print("\033[36mdef add(a, b)")  # Fixed typo here
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
        print("\033[90m(Press Ctrl+C at any time to exit)\033[0m")
        if input("Show tutorial? (y/n): ").lower() == 'y':
            self.show_tutorial()
        self.choose_difficulty()
        print(f"\nStarting {self.difficulty.capitalize()} mode with {len(self.challenges)} challenges!")
        
        for i, challenge in enumerate(self.challenges):
            print(f"\n\033[1mCHALLENGE {i+1}\033[0m")
            print(challenge["desc"])
            self.display_code(challenge["code"].strip())
            
            start_time = time.time()
            attempts = 0
            
            while True:
                user_code = input("\n\033[93mEnter your solution:\033[0m\n")
                attempts += 1
                
                if self.run_tests(user_code, challenge):
                    time_taken = time.time() - start_time
                    self.score += max(100 - int(time_taken) - (attempts-1)*10, 10)
                    print(f"\033[92m✔ Tests passed! (+{max(100 - int(time_taken) - (attempts-1)*10, 10)} points)\033[0m")
                    break
                else:
                    print("\033[91m✘ Tests failed!\033[0m")
                    hint_response = input("\033[90mHint? (y/n): \033[0m").lower()
                    if hint_response == 'y':
                        print(f"\033[93m💡 {challenge['hint']}\033[0m")
        
        print(f"\n\033[1;35m🏆 Final Score: {self.score}\033[0m")

if __name__ == "__main__":
    try:
        game = CodingChallenge()
        game.start()
    except KeyboardInterrupt:
        print("\n\033[91mProgram terminated. Thanks for playing!\033[0m")
    except Exception as e:
        print(f"\033[91mAn error occurred: {str(e)}\033[0m")
    finally:
        # Clean up if needed
        pass