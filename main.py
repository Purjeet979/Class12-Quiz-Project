import pandas as pd
import random

questions_df = pd.read_csv("C:/Users/LENOVO/Desktop/ioo.csv")

def ask_question(question_row):
    print(question_row["Question"])
    options = ["A", "B", "C", "D"]
    for option in options:
        option_column = f"{option}"
        if option_column in question_row:  # Check if the column exists
            print(f"{option}. {question_row[option_column]}")
        else:
            print(f"Option {option} not found in the CSV.")
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    return user_answer

def main():
    print("Welcome to the Quiz!")
    print()
    name = input("Enter Your name: ")
    print(f"Hello, {name}!\n")
    
    playagain = True 
    
    while playagain:
        num_questions = 5
        selected_questions = random.sample(range(len(questions_df)), num_questions)
        score = 0

        for i in selected_questions:
            print(f"\nQuestion {i + 1}:")
            question_row = questions_df.iloc[i]
            user_answer = ask_question(question_row)
            correct_answer = question_row["Answer"].strip().upper()  
            
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer is {correct_answer}.\n")

        print(f"Quiz completed, {name}! Your score: {score}/{num_questions}")
        
        # Save user data to CSV
        result_df = pd.DataFrame({'Name': [name], 'Score': [score]})
        result_df.to_csv('C:/Users/LENOVO/Desktop/.output.csv', mode='a', header=False, index=False)  

        # Ask the user if they want to play again
        pl = input("Do you want to play again? (yes/no): ").strip().lower()
        if pl != 'yes':
            playagain = False  

    # Load user data from CSV
    userdata = pd.read_csv('C:/Users/LENOVO/Desktop/.output.csv')

    # Sort the CSV file in descending order of scores and reset the index
    userdata = userdata.sort_values(by='Score', ascending=False).reset_index(drop=True)

    # Display the user's rank
    userrank = userdata[userdata['Name'] == name].index[0] + 1
    print(f"Your rank is: {userrank}")

    # Display the sorted CSV file with ranks
    print("\nRanking of all users:")
    userdata['Rank'] = userdata.index + 1
    print(userdata[['Rank', 'Name', 'Score']])

if __name__ == "__main__":
    main()
