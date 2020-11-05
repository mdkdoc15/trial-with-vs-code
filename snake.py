import random
# import keyboard

game_over = False
window_height = 20
window_width = 20
x = window_width/2
y = window_height/2
fruitX = 15
fruitY = 5
speed = 0


def setup():
    global game_over
    global speed
    global window_width
    global window_height
    global x 
    global y
    global fruitY
    global fruitX
    global speed
    global game_over
    game_over = False
    speed = 0
    window_width = 20
    window_height = 20
    x = window_width/2
    y = window_height/2
    fruitY = random.randint(1,window_height-1)
    fruitX = random.randint(1, window_width-1)
    speed = 0

def draw():
    for i in range(0, window_width):
        print("#", end = "")

    print()
    for i in range(0, window_height):
        for j in range(0, window_width):
            if(j == 0):
                print("#", end = "")
            elif(j == window_width-1):
                print("#", end = "")
            elif(i == x and j == y):
                print("O", end = "")
            elif(i == fruitY and j == fruitX):
                print("F", end = "")
            else:
                print(" ", end = "")
        print()

    for i in range(0, window_width):
        print("#", end="")

# def input():
#     while(True):
#         try:
#             if keyboard.is_pressed('a'):   
#                 print("a was pressed")
#             if keyboard.is_pressed('q'):
#                 break
#         except:
#             print("nothing was pressed")
        
    


# def logic():

def main():
   setup()
   global game_over
#    input()
#    TODO: write out keyboard pressses, write out logic
#    while(not game_over):
#        draw()
#        input()
#        logic()



if __name__ == "__main__":
    main()