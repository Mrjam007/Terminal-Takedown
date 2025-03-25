import time
import re
from textwrap import dedent

class CodingChallenge:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.challenges = [
            {
                "desc": "Fix the syntax errors in this function:\n",
                "code": dedent("""
                def add_numbers(a, b)
                    return a + b
                """),
                "tests": [
                    {"input": (2,3), "expected": 5},
                    {"input": (-1,5), "expected": 4}
                ],
                "hint": "Missing colon after parameters!"
            },
            {
                "desc": "Complete the factorial function:\n",
                "code": dedent("""
                def factorial(n):
                    # Your code here
                """),
                "tests": [
                    {"input": 5, "expected": 120},
                    {"input": 0, "expected": 1}
                ],
                "hint": "Use recursion: return n * factorial(n-1) if n > 0 else 1"
            }
        ]

    def run_tests(self, user_code, challenge):
        try:
            exec_scope = {}
            exec(user_code, exec_scope)
            func_name = 'add_numbers' if 'add_numbers' in user_code else 'factorial'
            func = exec_scope.get(func_name)
            
            for test in challenge["tests"]:
                result = func(*test["input"]) if isinstance(test["input"], tuple) else func(test["input"])
                if result != test["expected"]:
                    return False
            return True
        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            return False

    def display_code(self, code):
        print("\033[36m" + code + "\033[0m")

    def start(self):
        print("\033[1;32m=== PYTHON CODE WARRIOR ===\033[0m")
        
        for i, challenge in enumerate(self.challenges):
            print(f"\n\033[1mLEVEL {i+1}\033[0m")
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
                    if input("\033[90mHint? (y/n): \033[0m").lower() == 'y':
                        print(f"\033[93m💡 {challenge['hint']}\033[0m")
        
        print(f"\n\033[1;35m🏆 Final Score: {self.score}\033[0m")

if __name__ == "__main__":
    game = CodingChallenge()
    game.start()