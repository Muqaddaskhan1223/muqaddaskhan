
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print("welcome to the game")
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    # Add your code here
    #------------------------
    print("Choose a category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    while True:
        try:
            choice = int(input("Enter the number of the category you want to choose: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and", len(categories), ".")
        except ValueError:
            print("Invalid input. Please enter a number.")
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Score: {score} | Round: {round_number}")
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Game over! Your final score is: {score}")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    for round_number in range(1, 6):
     print(f"Round {round_number}...")
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    if player_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    # Add your code here
    #------------------------
point_per_question = 10
score = 0

def reward_points(points):
    """Reward points for a correct answer."""
    global score
    score += points
    print(f"You earned {points} points! Your new score is {score}.")

def validate_answer(answer, correct_answer):
    """Validate the player's answer as correct or incorrect."""
    global score
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        reward_points(point_per_question)
        return True
    else:
        print("Incorrect.")
        return False
    correct_answer = "Python"
    player_answer = input("What is the name of the programming language we are using? ")
    is_correct = validate_answer(player_answer, correct_answer)
    #------------------------
    
#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    # Add your code here
    #------------------------
    
    round_number += 1
    print(f"Round {round_number}...")
    ound_number = 1
while True:
    # Your game logic goes here
    #increase_round_number()
    if round_number > 5:
        break
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    max_incorrect_answers = 3
incorrect_answers = 0

def game_over():
    """End the game if the player makes 3 incorrect answers."""
    global incorrect_answers
    incorrect_answers += 1
    if incorrect_answers >= max_incorrect_answers:
        print(f"Game over! You made {incorrect_answers} incorrect answers.")
        exit()

def validate_answer(answer, correct_answer):
    """Validate the player's answer as correct or incorrect."""
    global incorrect_answers
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        reward_points(point_per_question)
    else:
        print("Incorrect.")
        game_over()
    correct_answer = "Python"
player_answer = input("What is the name of the programming language we are using? ")
validate_answer(player_answer, correct_answer)
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    while True:
        answer = input("Do you want to restart the game or exit? (yes/no) ")
        if answer.lower() == "yes":
            # Reset the game state
            global score, incorrect_answers, round_number
            score = 0
            incorrect_answers = 0
            round_number = 1
            # Restart the game
            main()
        elif answer.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
game_over()
restart_or_exit()
    #------------------------

#---------------------------------------
