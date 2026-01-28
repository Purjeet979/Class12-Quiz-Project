# 🧠 Python Quiz Game Project

A console-based quiz application developed as a Class 12 project. This application uses Python and the **Pandas** library to manage question databases, track user sessions, and generate a real-time leaderboard.

## 📋 Project Overview
This project demonstrates the use of data manipulation in Python to create an interactive user experience. Unlike simple hard-coded quizzes, this application loads data dynamically from external files and persists user performance data.

### Key Features
* [cite_start]**Dynamic Data Loading:** Uses Pandas to read quiz questions and options from an external CSV file (`ioo.csv`)[cite: 1].
* [cite_start]**Randomized Questions:** Utilizing the `random` module to select 5 unique questions every time the game is played, ensuring no two sessions are exactly the same[cite: 2].
* [cite_start]**Score Persistence:** Automatically appends the user's name and score to a results file (`scores.csv`) after every game[cite: 5].
* [cite_start]**Real-time Leaderboard:** Sorts the user data in descending order to display the player's current rank and a global ranking of all users immediately after finishing the quiz[cite: 6, 7].
* [cite_start]**Input Validation:** Handles user input to ensure answers are processed correctly regardless of case (A/B/C/D)[cite: 2].

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:**
    * `pandas` (for CSV handling and data sorting)
    * `random` (for question sampling)
    * `os` (for file path management)

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies**
    You need the `pandas` library to run this project.
    ```bash
    pip install pandas
    ```

3.  **Prepare the Data**
    Ensure the `ioo.csv` file is in the same directory as the script. The CSV should contain the following columns:
    * `Question`
    * `A`, `B`, `C`, `D` (Options)
    * `Answer` (Correct option key)

4.  **Run the Quiz**
    ```bash
    python main.py
    ```

## 📂 File Structure
* `main.py`: The core application logic.
* `ioo.csv`: The source database containing the question pool.
* `scores.csv`: (Auto-generated) Stores the history of player names and scores.

## 🚀 Future Improvements
* Add a Graphical User Interface (GUI) using Tkinter.
* Support multiple categories of questions.
* Implement a timer for each question.

---
*Created by Purjeet Shahu*
