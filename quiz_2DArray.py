question = ("Which is the largest desert in the world?",
            "What is the capital city of Australia?",
            "Which planet is known as the Morning Star or Evening Star?",
            "Which is the largest ocean on Earth?")

options = (("A) Sahara Desert","B) Arabian Desert","C) Antarctic Desert","D) Gobi Desert"),
           ("A) Sydney","B) Melbourne","C) Perth","D) Canberra"),
           ("A) Mars","B) Venus","C) Jupiter","D) Mercury"),
           ("A. Atlantic Ocean","B. Indian Ocean","C. Arctic Ocean","D. Pacific Ocean"))


ans = ("C","C","B","D")

guesses=[]
score = 0
que_num = 0

for i in question:
    print("------------------")
    print(i)

    for j in options[que_num]:
        print(j)
    guess = input("Enter the option(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == ans[que_num]:
        print("CORRECT!")
        score+=1
    else:
        print("INCORRECT!!")
        print(f"The correct ans is {ans[que_num]}")
    que_num+=1

    print(f"Your score is {score}")