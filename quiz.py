import pgzrun

WIDTH = 800
HEIGHT = 700

TITLE = "Quiz Game"
marque_box = Rect(0,0 , 800,60)
#Rect(x,y , W,H)
question_box = Rect(20,80 , 500,100)
timer_box = Rect(660,80 , 250,100)
#skip_box = 
#ans_box1 =
#ans_box2 = 
#ans_box3 = 
#ans_box4 = 

#answer_boxes = [ans_box1 , ans_box2 , ans_box3 , ans_box4]




def draw():
    screen.fill("black")
    screen.draw.filled_rect(marque_box,"blue")
    screen.draw.filled_rect(question_box,"white")
    screen.draw.filled_rect(timer_box, "green")
    
    

    



pgzrun.go()