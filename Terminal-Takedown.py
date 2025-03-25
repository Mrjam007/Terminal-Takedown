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
        choice = input("Enter choice (1-3): ").strip()
        self.difficulty = ['easy', 'medium', 'hard'][int(choice)-1] if choice in ['1','2','3'] else 'easy'
        self.generate_challenges()

    def generate_challenges(self):
        base_challenges = []
        
        # ===== EASY CHALLENGES =====
        for i in range(1, 21):
            base_challenges.append({
                "difficulty": "easy",
                "desc": f"Fix Syntax Errors {i}",
                "code": dedent(f"""
                def task_{i}(a, b)
                    return a + b
                """),
                "tests": [{"input": (2,3), "expected": 5}],
                "hint": "Missing colon after parameters!"
            })

        # ===== MEDIUM CHALLENGES =====
        oop_problems = [
            ("Bank Account Class", "self.balance += amount", [100, 50]),
            ("Rectangle Area", "return width * height", [(5,4)])
        ]
        for name, sol, tests in oop_problems:
            for v in range(12):
                base_challenges.append({
                    "difficulty": "medium",
                    "desc": f"OOP: {name} {v+1}",
                    "code": f"class Solution:\n    def __init__(self):\n        {sol}",
                    "tests": tests,
                    "hint": "Use proper class structure"
                })

        # ===== HARD CHALLENGES =====
        advanced = [
            ("Recursive Fibonacci", "return fib(n-1) + fib(n-2)", [5, 7]),
            ("Binary Search", "mid = (low + high) // 2", [([1,3,5], 3)])
        ]
        for name, sol, tests in advanced:
            for v in range(12):
                base_challenges.append({
                    "difficulty": "hard",
                    "desc": f"Advanced: {name} {v+1}",
                    "code": f"def solution():\n    {sol}",
                    "tests": tests,
                    "hint": "Mind the base cases!"
                })

        # Filter based on difficulty
        self.challenges = [c for c in base_challenges if 
                          (self.difficulty == 'easy' and c['difficulty'] == 'easy') or
                          (self.difficulty == 'medium' and c['difficulty'] in ['easy', 'medium']) or
                          (self.difficulty == 'hard')]
        random.shuffle(self.challenges)
        self.challenges = self.challenges[:50]

    def display_code(self, code):
        print("\033[36m" + code + "\033[0m")

    def run_tests(self, user_code, challenge):
        try:
            exec_scope = {}
            exec(user_code, exec_scope)
            
            if 'class' in user_code:
                test_obj = exec_scope['Solution']()
                return test_obj.balance == challenge["tests"][0]
            else:
                func = exec_scope.get('task') or exec_scope.get('solution')
                return func(*challenge["tests"][0]["input"]) == challenge["tests"][0]["expected"]
        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
            return False

    def start(self):
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
                    if input("\033[90mHint? (y/n): \033[0m").lower() == 'y':
                        print(f"\033[93m💡 {challenge['hint']}\033[0m")
        
        print(f"\n\033[1;35m🏆 Final Score: {self.score}\033[0m")

if __name__ == "__main__":
    game = CodingChallenge()
    game.start()