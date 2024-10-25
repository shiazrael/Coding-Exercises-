# -*- coding: utf-8 -*-
"""
Exercise 4: Primitive Quiz - 30 Marks
"""
def france():
    questions = {"What is the capital of France?": "paris"}
    
    for question, correct_answer in questions.items():
        user_answer=input(question+"").strip().lower()
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong.The answer is {correct_answer.capitalize()}.")
# Run the quiz
if __name__ == "__main__":
    france()
 
    
              



    
