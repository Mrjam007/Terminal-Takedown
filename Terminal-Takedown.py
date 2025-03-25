import time
import random
from textwrap import dedent

class CodingChallenge:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.challenges = self.generate_challenges()

    def generate_challenges(self):
        challenges = []

        # ===== TIER 1: Syntax Fixes (10 levels) =====
        for i in range(1, 11):
            challenges.append({
                "desc": f"Level {i}: Fix the syntax errors",
                "code": dedent(f"""
                def multiply_{i}(a, b)
                    return a * b
                """),
                "tests": [{"input": (2,3), "expected": 6}, {"input": (-1,5), "expected": -5}],
                "hint": "Missing colon after parameters!"
            })

        # ===== TIER 2: Basic Algorithms (15 levels) =====
        algorithms = [
            ("Fibonacci", "def fib(n):\n    # Return nth Fibonacci number", 
             [(0, 0), (1, 1), (5, 5)], "Use fib(n-1) + fib(n-2) with base cases"),
            ("Prime Check", "def is_prime(n):\n    # Return True if prime", 
             [(2, True), (4, False), (9, False)], "Check divisibility up to sqrt(n)"),
            ("String Reverse", "def reverse_str(s):\n    # Return reversed string", 
             [("hello", "olleh"), ("world", "dlrow")], "Use slicing [::-1]"),
            ("List Sum", "def list_sum(nums):\n    # Return sum of list", 
             [([1,2,3], 6), ([], 0)], "Initialize total and iterate"),
            ("Count Vowels", "def count_vowels(s):\n    # Return vowel count", 
             [("hello", 2), ("xyz", 0)], "Check for 'aeiou' in lowercase")
        ]
        for name, code, tests, hint in algorithms:
            for v in range(3):
                challenges.append({
                    "desc": f"Level {len(challenges)+1}: {name}",
                    "code": dedent(code),
                    "tests": [{"input": t[0], "expected": t[1]} for t in tests],
                    "hint": hint
                })

        # ===== TIER 3: OOP Challenges (10 levels) =====
        oop_problems = [
            ("BankAccount class", "class BankAccount:\n    def __init__(self):\n        # Add code", 
             [("deposit(100)", 100), ("withdraw(50)", 50)]),
            ("Rectangle class", "class Rectangle:\n    # Add width/height\n    def area(self):", 
             [(5, 4, 20), (3, 7, 21)])
        ]
        for desc, code, tests in oop_problems:
            for v in range(5):
                challenges.append({
                    "desc": f"Level {len(challenges)+1}: {desc}",
                    "code": dedent(code),
                    "tests": tests,
                    "hint": "Use __init__ and instance variables"
                })

        # ===== TIER 4: Recursion/Advanced (10 levels) =====
        advanced = [
            ("Binary Search", "def binary_search(arr, target):\n    # Return index", 
             [([1,3,5,7,9], 5, 2)], "Check mid-point recursively"),
            ("Tower of Hanoi", "def hanoi(n):\n    # Return moves needed", 
             [(3, 7)], "Formula: 2^n - 1")
        ]
        for name, code, tests, hint in advanced:
            for v in range(5):
                challenges.append({
                    "desc": f"Level {len(challenges)+1}: {name}",
                    "code": dedent(code),
                    "tests": [{"input": t[0], "expected": t[1]} for t in tests],
                    "hint": hint
                })

        # ===== TIER 5: Code Golf (5 levels) =====
        golf_challenges = [
            ("FizzBuzz", "def fizzbuzz(n):\n    # Return 'Fizz'/'Buzz'"),
            ("Factorial", "def fact(n):\n    # One-line solution")
        ]
        for desc, code in golf_challenges:
            challenges.append({
                "desc": f"Level {len(challenges)+1}: {desc}",
                "code": dedent(code),
                "tests": [{"input": 15, "expected": "FizzBuzz"}],
                "hint": "Use list comprehensions!"
            })

        return challenges[:50]  # Force exactly 50 levels

    def run_tests(self, user_code, challenge):
        try:
            exec_scope = {}
            exec(user_code, exec_scope)
            
            # Detect function/class name
            func_name = next((name for name in ['multiply', 'fib', 'is_prime', 'reverse_str', 
                                              'list_sum', 'count_vowels', 'binary_search',
                                              'hanoi', 'fizzbuzz', 'fact'] if name in user_code), None)
            
            # Class detection
            if 'class' in user_code:
                test_obj = exec_scope.get('BankAccount')() if 'BankAccount' in user_code else exec_scope.get('Rectangle')(5,4)
                for test in challenge["tests"]:
                    if 'BankAccount' in user_code:
                        eval(f"test_obj.{test[0]}")
                        return test_obj.balance == test[1]
                    elif 'Rectangle' in user_code:
                        return test_obj.area() == test[2]
            else:
                func = exec_scope.get(func_name)
                for test in challenge["tests"]:
                    result = func(test["input"]) if not isinstance(test["input"], tuple) else func(*test["input"])
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