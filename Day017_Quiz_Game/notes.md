# Day 17 - Quiz Game (OOP)

## What I Built

A CLI true/false quiz game built across four files using OOP. Question data lives in `data.py`, the `Question` class models each question, `QuizBrain` drives the game logic, and `main.py` wires everything together — building the question bank and running the loop until questions run out.

## Project Structure

```
day-17/
├── main.py
├── data.py
├── question_model.py
└── quiz_brain.py
```

## Concepts Used

- **List of dictionaries** — `question_data` stores each question as a dict with keys like `"question"` and `"correct_answer"`; `main.py` loops over it to build objects
- **Class instantiation in a loop** — `Question(question_text, question_answer)` is called once per dict entry, and each object is appended to `question_bank`
- **`self.question_number` as both a counter and an index** — incremented before `check_answer()` is called, so it always reflects the human-readable question number (1-based) while the list access uses it before incrementing
- **`still_has_questions()`** — returns a boolean by comparing `self.question_number` to `len(self.question_list)`; the `while` loop in `main.py` uses this directly as its condition
- **`.lower()` on both sides** — `user_answer.lower() == correct_answer.lower()` makes the comparison case-insensitive so `"true"`, `"True"`, and `"TRUE"` all count
- **Separation of concerns** — `Question` only holds data; `QuizBrain` owns all game logic; `main.py` only handles setup and the loop; `data.py` is purely a data source

## Code

### main.py

```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```

### data.py

```python
question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    # ... (full list of 10 questions)
]
```

### question_model.py

```python
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### quiz_brain.py

```python
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
```

## Sample Output

```
Q.1: The HTML5 standard was published in 2014. (True/False): True
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: The first computer bug was formed by faulty wires. (True/False): True
That's wrong.
The correct answer was: False.
Your current score is: 1/2

...

You've completed the quiz
Your final score was: 7/10
```

## What I Learned

- `question_number` is doing two jobs at once — it's used as a 0-based list index _before_ incrementing, then immediately incremented to serve as the 1-based display number. It works, but if you ever called `next_question()` and `check_answer()` separately in a different order, it would break silently
- `still_has_questions()` returning a boolean expression directly (`return self.question_number < len(self.question_list)`) is cleaner than `if ... return True else return False` — worth internalizing as a habit
- `data.py` stores keys like `"category"`, `"type"`, `"difficulty"`, and `"incorrect_answers"` that `main.py` never uses — they're just ignored. This is intentional: the data is shaped like an API response (from Open Trivia DB), so it carries extra fields. Knowing which fields to extract and which to skip is a real-world skill
- `Question` is a minimal class — just `__init__` with two attributes, no methods. This is valid OOP; not every class needs behavior. It exists to give data a named structure so you access `question.text` instead of `question["question"]`, which is cleaner and less error-prone
- The `question_data` list could be replaced with a live API call to `https://opentdb.com/api.php` and `main.py` wouldn't need to change at all — that's the payoff of separating data from logic
