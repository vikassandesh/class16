import pgzrun

WIDTH = 800
HEIGHT = 700

TITLE = "Quiz Game"
marque_box = Rect(0,0 , 800,60)
#Rect(x,y , W,H)
question_box = Rect(20,80 , 500,100)
timer_box = Rect(560,80 , 250,100)
skip_box = Rect(600,215 , 150,300)
ans_box1 = Rect(20,200 , 250,150)
ans_box2 = Rect(290,200 , 250,150)
ans_box3 = Rect(20,400 , 250,200)

ans_box4 = Rect(290,400 , 250,200)

answer_boxes = [ans_box1 , ans_box2 , ans_box3 , ans_box4]


#variables
score = 0
time_left = 10
is_game_over = False
marque_message = ""
question_file_name = "Quiz master\\questions.txt"
questions = []
question_count = 0
question_index = 0 

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marque_box,"black")
    screen.draw.filled_rect(question_box,"white")
    screen.draw.filled_rect(timer_box, "green")
    #screen.draw.filled_rect(ans_box1, "grey")
    #screen.draw.filled_rect(ans_box2, "grey")
    #screen.draw.filled_rect(ans_box3, "grey")
    #screen.draw.filled_rect(ans_box4, "grey")
    screen.draw.filled_rect(skip_box, "yellow")
    
    #instead of 4 lines of code use a list and the for loop
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "grey")
    
    #marque_box- msg & Que with ques no.
    marque_message = "Welcome To Quiz Master... "
    marque_message += f"Q:{question_index} of {question_count}"

    #display marque text
    screen.draw.textbox(marque_message, marque_box, color="white")
    
    #displaw timer text
    screen.draw.textbox(
        str(time_left), timer_box,
        color="white", shadow = (0.5,0.5),
        scolor = "dim grey")

    #skip box text
    screen.draw.textbox("SKIP", skip_box, color="black", 
                         angle =-90, 
                         shadow =(-1,-1), scolor="dim grey")
    
    #display qusestion text
    screen.draw.textbox(question[0].strip(), question_box, color="black", 
                        shadow=(0.5,0.5), scolor = "dim grey")
    
    #display answer text
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color="purple")
        index += 1
        
def update():
    move_marque()
    
    
def move_marque(): 
    marque_box.x -= 2
    if marque_box.right < 0:
        marque_box.left = WIDTH
        
    
def read_question_file():
    global question_count, questions 
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()
    

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()
        
        index = index +1
    if skip_box.collidepoint(pos):  
        skip_question()
        
              

def correct_answer():
    global questions, time_left, question, score
    score += 1
    if questions: 
        question = read_next_question()
        time_left = 10
    else:
        game_over()


def game_over():
    global time_left, question, is_game_over
    message = f"GAME OVER\n You got {score} questions correct!"
    question = [message," "," "," "," ",5]
    time_left = 0
    is_game_over = True
    
    
    
def skip_question():
    global question, time_left
    if questions and not is_game_over:     #if more questions are left in the questions list and game is yet not over the restore it to the question()
        question =read_next_question()
        time_left = 10
    else:
        game_over()
        

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()
        

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)

pgzrun.go()
