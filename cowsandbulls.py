'''
Welcome to Cows and Bulls 
This is a number guessing game programmed by Mihir Chhiber, 1004359, F01.

This game makes use of turtle, random, libdw(state machines) and tkinter(GUI) libraries

There are 5 states provided by the state machine
- State 0 - Main page
- State 1 - Game is in progress
- State 2 - Game is over, user has won
- State 3 - Game is over, user has lost
- State 4 - User wants to quit

This is a number guessing game where the user has 10 tries to guess the number and help
is provided to the user by providing number of cows and bulls.

Number of cows = number of correct digits
Number of bulls = number of correct digits in the right position
'''

#all the required libraries
from libdw import sm  #helps in defining different state machine
import random  #helps in generating random numbers
import turtle  #helps in creating display for user
import tkinter as tk  #for GUI
from tkinter import messagebox  #for GUI
from tkinter import simpledialog  #for GUIfrom time import sleep 
from libdw import pyrebase   #for accessing database on firebase
application_window = tk.Tk()

#setup access to the database, used for keeping track of the new highscore
projectid = "dwcowsandbulls" 
dburl = "https://dwcowsandbulls.firebaseio.com/" 
authdomain = projectid + ".firebaseapp.com" 
apikey = "AIzaSyCYgvjtOxjd2qiz9rdNIFs9r9eYiP5RCpM" 
email = "mhhiber@gmail.com" 
password = "12345678" 
 
config = { 
    "apiKey": apikey, 
    "authDomain": authdomain, 
    "databaseURL": dburl, 
} 

firebase = pyrebase.initialize_app(config) 
auth = firebase.auth() 
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database() 

#this class respsonsible for initializing turtle
class turt:
    wn =turtle.Screen()
    wn.bgcolor('#465461')
    obj = turtle.Turtle()
    
#this class responsible for displaying the the main page and setting up the game background
class boot(turt): #this class inherits class turt to get turtle functionality
    
    #helps to draw lines
    def draw(self,dis,deg,x,y):
        self.obj.up()
        self.obj.goto(x,y)
        self.obj.down()
        self.obj.left(deg)
        self.obj.forward(dis)
        self.obj.right(deg)
        
    #helps to write
    def line(self,lin,x,y,font):
        self.obj.up()
        self.obj.goto(x,y)
        self.obj.down()
        self.obj.write(lin, font=font)
    
    #function to display the main page
    def main_page(self):
        self.obj.pensize(3)
        self.obj.color('#ecf3f4')
        font = ('Fixedsys',35,'bold')
        self.obj.up()
        self.obj.goto(-400,200)
        self.obj.down()
        self.obj.color('#ff893b')
        self.obj.write('Welcome to Cows and Bulls', font=font)
        font = ('System',20,'normal')
        self.obj.up()
        self.obj.goto(-275,130)
        self.obj.down()
        self.obj.write('Rules of this game:', font=font) 
        font = ('System',16,'normal')
        para = ['- System will generate a 4-digit number with no digits repeating','- Eg: 1234, 0283, 8402','- Your task is to guess the number','- You get 10 chances to guess','- After every guess, you will get to know how accurate is your ans','- Number of cows = number of correct digits','- Number of bulls = number of correct digits in the right position','- You can use number of cows and bulls to improve your guess']
        for i in range(len(para)):
            j = -i*25
            self.line(para[i],-275,100+j,font)
            
    #function to setup the background for the game        
    def setup(self):
        turtle.clearscreen()
        self.wn.bgcolor('#465461')
        self.obj.pensize(3)
        self.obj.color('#729ca2')
        self.draw(550,90,-150,-310)
        self.draw(550,90,-150,-310)
        self.draw(550,90,100,-310)
        self.draw(550,90,200,-310)
        for i in range(-310,290,50):
            self.draw(350,0,-150,i)
        self.obj.color('#729ca2')
        font = ('System',24,'normal')
        self.obj.up()
        self.obj.goto(-77,198)
        self.obj.down()
        self.obj.write('Number', font=font)
        self.obj.up()
        self.obj.goto(118,196)
        self.obj.down()
        self.obj.write('C   B', font=font)
        
#This class is responsible for displaying the game and to get/update the highscore
class game_dis(turt): #inherits class turt to get turtle funcitonality
    
    #function to display the input of user and the corresponding cows and bulls
    def display(self,row,n):
        self.obj.color('#c4dcdf')
        font = ('Arial',24,'normal')
        n = -(n-1)*50
        for i in range(len(row)):
            j=i*60
            self.obj.up()
            self.obj.goto(-125+j,150+n)
            self.obj.down()
            self.obj.write(row[i], font=font)
            
    #display function when the user wins, displays the number of tries
    def win(self,n,):
        self.obj.color('#ff893b')
        font = ('Fixedsys',60,'bold')
        self.obj.up()
        self.obj.goto(-300,200)
        self.obj.down()
        self.obj.write('Y', font=font)
        self.obj.up()
        self.obj.goto(-300,0)
        self.obj.down()
        self.obj.write('O', font=font)
        self.obj.up()
        self.obj.goto(-300,-200)
        self.obj.down()
        self.obj.write('U', font=font)
        self.obj.up()
        self.obj.goto(250,200)
        self.obj.down()
        self.obj.write('W', font=font)
        self.obj.up()
        self.obj.goto(250,0)
        self.obj.down()
        self.obj.write('I', font=font)
        self.obj.up()
        self.obj.goto(250,-200)
        self.obj.down()
        self.obj.write('N', font=font)
        font = ('Arial',24,'normal')
        self.obj.up()
        self.obj.goto(-125,260)
        self.obj.down()
        self.obj.color('#ff893b')
        self.obj.write('You won with '+str(n)+' moves', font=font)
        self.obj.up()
        self.obj.goto(-135,300)
        self.obj.down()
        hscore = db.child("Highscore").get(user['idToken'])  # to get the highscore from database
        hname = db.child("Name").get(user['idToken'])  # to get the name from database
        if hscore.val()>n:   #if the new score is better than the highscore
            inp = simpledialog.askstring("New Highscore!!!", 'Enter your name :',parent=application_window)
            db.child("Name").set(inp,user["idToken"])  # write the new name on database
            db.child("Highscore").set(n,user["idToken"])   #write the new highscore on database
            self.obj.write('Highscore: ' + inp + ' - ' + str(n), font=font)
        else:
            self.obj.write('Highscore: '+ hname.val() + ' - ' + str(hscore.val()), font=font)
    
    #display function when the user loses, displays the correct answer
    def lose(self,ans):
        self.obj.color('#ff893b')
        font = ('Fixedsys',60,'normal')
        self.obj.up()
        self.obj.goto(-300,200)
        self.obj.down()
        self.obj.write('Y', font=font)
        self.obj.up()
        self.obj.goto(-300,0)
        self.obj.down()
        self.obj.write('O', font=font)
        self.obj.up()
        self.obj.goto(-300,-200)
        self.obj.down()
        self.obj.write('U', font=font)
        self.obj.up()
        self.obj.goto(250,225)
        self.obj.down()
        self.obj.write('L', font=font)
        self.obj.up()
        self.obj.goto(250,75)
        self.obj.down()
        self.obj.write('O', font=font)
        self.obj.up()
        self.obj.goto(250,-70)
        self.obj.down()
        self.obj.write('S', font=font)
        self.obj.up()
        self.obj.goto(250,-215)
        self.obj.down()
        self.obj.write('E', font=font)
        font = ('Arial',24,'normal')
        self.obj.up()
        self.obj.goto(-125,260)
        self.obj.down()
        self.obj.color('#ff893b')
        self.obj.write('The number is '+str(ans[0])+str(ans[1])+str(ans[2])+str(ans[3]), font=font)
        hscore = db.child("Highscore").get(user['idToken'])  # to read the highscore from the database
        hname = db.child("Name").get(user['idToken'])  # to read the name from the database
        self.obj.up()
        self.obj.goto(-135,300)
        self.obj.down()
        self.obj.write('Highscore: '+ hname.val() + ' - ' + str(hscore.val()), font=font)
        
#This class inherits all the previous classes and provides user with the game
class CowsAndBulls(boot,game_dis,sm.SM):
    
    startState = 0 
    
    #to start state machine
    def start(self):
        self.state = self.startState
    
    #step function called to update the state and give an output using the old state and input
    def step(self, inp):
        (s, o) = self.get_next_state(self.state, inp)
        self.state = s
        return o
    
    #to check if the number entered by user can be used for playing the game
    def test(self,inp):
        if inp.isnumeric():   #if the input is numbers
            if len(inp)==4:   #if there are four numbers
                ls=[]
                for i in inp:
                    ls.append(int(i))
                if len(set(ls))==4:   #if there are four unique numbers
                    return True
        return False
    
    # helps state funciton to get the new state and output
    def get_next_state(self, state, inp):
        # 0 is start, 1 is during game, 2 is win , 3 is lose, 4 is quit
        ou = False
        if state == 0 or state == 2 or state == 3:
            if inp == True:
                state = 1
                self.n = 1
                self.setup()
                ou = True
            else:
                state = 4
                ou = False
        elif state == 1:
            if inp[5] == 4:
                state = 2
                ou = True
            else:
                if self.n == 10:
                    state = 3 
                else:
                    self.n += 1
                ou = False                
        return state, ou
    
    # function which starts the game and uses all the previous functions to make the game function
    def play(self):
        while True:
            if self.state == 0:     #State 0 is the main page
                super().main_page()
                ln = '''Welcome to Cows and Bulls,
        The instructions are displayed on the screen
                
                Do you want to start the game?'''
                inp = messagebox.askyesno("Cows and Bulls",ln)
                ou = self.step(inp)
                if ou:    #if the output is true, start new game
                    self.n = 1
                    ans = []    #code below helps to create a new number
                    for i in range(4):
                        a = random.randrange(0,10)
                        while a in ans:
                            a = random.randrange(0,10)
                        ans.append(a)
                else:
                    self.wn.bye()
                    break
            elif self.state == 1:     #State 1 is the game is going on
                inp = simpledialog.askstring("Cows and Bulls", "Enter the 4 digit number :",parent=application_window)
                ln='''Enter the 4 digit number as per the rules
- Should be 4 digits
- None of the digits repeat
- Number should not have space in between'''
                while not (self.test(inp)):  #to make sure the user input is usable
                    inp = simpledialog.askstring("Cows and Bulls", ln,parent=application_window)
                ls=[]
                for i in inp:
                    ls.append(int(i))
                cows = 0
                bulls = 0
                for i in range(len(ans)):   #to calculate number of cows and bulls
                    if ans[i] == ls[i]:
                        bulls += 1
                    if ls[i] in ans:
                        cows += 1
                ls.append(cows)
                ls.append(bulls)
                self.display(ls,self.n)  
                self.step(ls)
            elif self.state == 2:   #State 2 means the user has won
                self.win(self.n)
                inp = messagebox.askyesno("Winner","Do you want to play again?")
                ou = self.step(inp)
                if ou:   #if user says yes to another game, create a new random number
                    self.n = 1
                    ans = []
                    for i in range(4):
                        a = random.randrange(0,10)
                        while a in ans:
                            a = random.randrange(0,10)
                        ans.append(a)
            elif self.state == 3:   #State 3 means the user has lost
                self.lose(ans)
                inp = messagebox.askyesno("Loser","Do you want to play again?")
                ou = self.step(inp)
                if ou:    #if user says yes to another game, create a new random number
                    self.n = 1
                    ans = []
                    for i in range(4):
                        a = random.randrange(0,10)
                        while a in ans:
                            a = random.randrange(0,10)
                        ans.append(a)
            elif self.state == 4:   #State 4 means the user wants to quit
                self.wn.bye()  #closes the window
                break
                

fun = CowsAndBulls() #creates an object of the class
fun.start() #starts the state machine
fun.play() #starts the game