easy_questions = [
{
"question": "What is the capital of India?",
"options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
"answer": "A"
},
{
"question": "How many days in a week?",
"options": ["A. 5", "B. 6", "C. 7", "D. 8"],
"answer": "C"
}
]

medium_questions = [
{
"question": "Which language is used in Data Science?",
"options": ["A. Python", "B. HTML", "C. CSS", "D. JavaScript"],
"answer": "A"
},
{
"question": "Which planet is called Red Planet?",
"options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
"answer": "B"
}
]

hard_questions = [
{
"question": "Who invented Python?",
"options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Elon Musk"],
"answer": "B"
},
{
"question": "Which company developed Windows?",
"options": ["A. Apple", "B. Google", "C. Microsoft", "D. IBM"],
"answer": "C"
}
]

print('''1.Easy level\n
2. Medium level \n 
3. Hard level ''')

choice = input('Choose option as mentione above: ')

if choice == '1':
        quiz = easy_questions
elif choice == "2":
        quiz = medium_questions
elif choice == '3':
        quiz = hard_questions
else:
        print('Invalid option')
        exit()

score =0

while True:

        for q in quiz:
                print('\n'+ q['question'])
                for a in q['options']:
                        print(a)

                answer = input('Enter answer: ').upper()

                if answer == q['answer']:
                        print(f'Your answer {answer} is correct')
                        score +=1

                else:
                        print("Invalid answer")
        
        repeat = input("Are u play again y/n: ")

        if repeat == 'n':
                print(f'Your score is {score}')
                break