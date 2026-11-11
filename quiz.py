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
    screen.draw.filled_rect(marque_box,"blue")
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
    pass

def read_question_file():
    pass

def read_next_question():
    pass

        
        


pgzrun.go()
