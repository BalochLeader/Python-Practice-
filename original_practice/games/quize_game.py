
questions = (
    "What Is Python?",
    "Do You Like Me?",
    "Do You Use TikTok?",
    "Do You Know I am Coder?"
)

options = (
    ("A: Language", "B: No", "C: Yes"),
    ("A: Yes", "B: Yeah", "C: Yupp"),
    ("A: No", "B: Cringe", "C: Yeah"),
    ("A: Yupp", "B: Hmm", "C: Ahh"),
)

answer= ("A", "B", "A", "A")
 
 
guesses = []
 
score = 0
 
questions_num = 0
 
 
for question in questions:
 	print("-----------------------------------")
 	print(question)
 	for option in options[questions_num]:
 		print(option)
 	guess = input("Enter Your Answer  (A / B / C / D ) : ").upper()
 	guesses.append(guess)
 	
 	if guess == answer[questions_num]:
 		print("CORECT ! ")
 		score += 1 
 	else:
 		print("INCORRECT !")
 		print(f"{answer[questions_num]} is Correct Answer")
 	questions_num +=1 
 		
print("------------------------------")
print("       RESULT             ")
print("-------------------------------")
 
print("answer : " , end=" ")
for an in answer:
 	print(an, end=" ")
 
 
print("guess :" , end=" ")
for gu in guesses:
	print(gu , end=" ")
	

score = int(score / len(questions)*100 )
print("----------------------------------------------")
print(f"Here Is Your Score : {score} %")
 
  #45 min To write This Shit 