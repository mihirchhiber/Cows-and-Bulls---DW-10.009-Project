# Cows and Bulls

A number guessing game. User needs to guess a 4-digit number which has no repeating numbers. User gets 10 tries to guess the number. After each try, the user gets help in the form cows and bulls. Cows is number of correct digits and bulls is number of correct digits in the right position. 

## How to play

Run the python program. Read the rules of the game provided on the main page and proceed to the game. 

User gets 10 turns to guess the number. A table will be displayed with all the guesses, cows and bulls. GUI dialog box will ask you for your 4-digit number guess. You need to submit your answer in the dialogue box and it will display it on the table. 

If you guess the number within ten tries, the game will end and 'YOU WIN' will be displayed on your screen. If you are not able to guess the number within the ten tries, the game will end and it will display the number and 'YOU LOSE' message.

Highscore and name be displayed after the game is over. If the user beats the old highscore, the program will ask for the users name and the highscore will be updated with his/her name.

(Highscore is the lowest number of moves)

After the game is over, a dialogue box will ask you if you want to play again or quit.

## Describing the Code

### Libraries required

- turtle - for display
- libdw - for state machine and firebase
- random - to generate random numbers
- tkinter - for GUI

### Classes
 - Class turt - responsible for initializing turtle functions
 - Class boot - responsible for displaying the main pages and setting up the game board
		-	inherits class turt
 - Class game_dis - responsible for displaying the game and to get/update the highscores
		 - inherits class turt
 - Class CowsAndBulls - this is the  main class which helps in combining all the class functions to provide the game
			 - MAIN CLASS
		 - inherits class boot, game_dis and sm.SM
### Funcitons

-	Main Function  - play() - Responsible for calling all the functions from its own class and inherited classes to help the game run
-	Display functions
		-	draw(), line(), main_page(), setup() - Responsible for displaying the main page and to setup the grid for the game. draw() and line() helps by reducing the number of lines of code and making it more readable.
		-	display(), win(), lose() - Responsible for displaying the game based on the users input. display() is called every time the user enters a new input. win() and lose() are called if the user wins or loses. These functions also retrieve highscore and name from the database and set a new highscore and name.
-	State machine functions
		-	start() - sets up the state machine, needs to be called before play()
		-	step() and get_next_state() - responsible for updating the state value based on the users input and give an output
-	Input check function - test() - it checks if the users input is valid or not. If not, it guides the user and gets a valid input for the game to function without encountering any errors.

### State machine
There are 5 states provided by the state machine 
- State 0 - Main page
- State 1 - Game is in progress
- State 2 - Game is over, user has won
- State 3 - Game is over, user has lost
- State 4 - User wants to quit

The default value of the state is set by using function start(). Function step() updates the state and gives an output with the help of function get_next_state().

### Turtle and tkinter

Turtle helps in setting up user display and tkinter provides GUI for the user to interact with. 

### Firebase

Stores the highscore and name of the user. This is retrieved to display in the game and updated if the user sets a new highscore.


## Contributor

**Mihir Chhiber** - 1004359 - F01


## Acknowledgments

* SUTD 10.009 DW course material 
* Professor Oka, Kenny, Simon and Siyong for helping me in DW module and in this project.
* [https://stackedit.io/app#](https://stackedit.io/app#) to guide me in writing ReadMe file
