from tkinter import *
import random, time

def check_win(n):
    global game
    if ((game[0] == n and game[1] == n and game[2] == n) \
        or (game[3] == n and game[4] == n and game[5] == n) \
        or (game[6] == n and game[7] == n and game[8] == n) \
        or (game[0] == n and game[3] == n and game[6] == n) \
        or (game[1] == n and game[4] == n and game[7] == n) \
        or (game[2] == n and game[5] == n and game[8] == n) \
        or (game[0] == n and game[4] == n and game[8] == n) \
        or (game[2] == n and game[4] == n and game[6] == n)):
        return True
              
def stop_game():
    global game_left
    for i in game_left:
        button[i].config(state='disabled')

def click(a):
    global game
    global game_left
    global count
    game[a] = 'X'
    button[a].config(text='X', state='disabled')
    game_left.remove(a)
    if a == 4 and count == 0:
        b = random.choice(game_left)
    elif a != 4 and count == 0:
        b = 4
    if count > 0:
        b = 8 - a
    if b not in game_left:
        try:
            b = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена!'
            stop_game()
    game[b] = '0'
    time.sleep(0.5)
    button[b].config(text='0', state='disabled')
    if check_win('X'):
        label['text'] = 'Вы победили!'
        stop_game()
    elif check_win('0'):
        label['text'] = 'Вы проиграли!'
        stop_game()
    else:
        if (len(game_left)>1):
            game_left.remove(b)
        else:
            label['text'] = 'Игра окончена!'
            stop_game()
        count += 1


game = [None] * 9
game_left = list(range(9))
count = 0

window = Tk()
label = Label(width=18, text = 'TicTacToe', font=('Arial', 15, 'bold'))

button = [Button(width=5, height=2, font=('Arial', 12, 'bold'), command = lambda x=i: click(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
row = 1; col = 0
for i in range(9):
    button[i].grid(row=row,column=col)
    col +=1
    if col == 3:
        row +=1
        col = 0

window.mainloop()