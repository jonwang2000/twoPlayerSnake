import Tkinter as tk
import pygame
from pygame.locals import *


def singleplayerwindow():

    pygame.display.set_caption("Snake Singleplayer")


    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(20)

        import Singleplayer

        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                pygame.quit()




def multiplayerwindow():

    pygame.display.set_caption("Snake Multiplayer")

    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(30)

        import Multiplayer


        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                pygame.quit()

def leaderboardwindow():

    pygame.display.set_caption("High Scores!")


    clock = pygame.time.Clock()
    keep_going = True

    while keep_going:
        clock.tick(20)


        import HighScoresforSnake
        HighScoresforSnake.init()


        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                pygame.quit()



root = tk.Tk()
root.title("SNAKE")
root.geometry('900x800')
background=tk.PhotoImage(file="grass_tkinter.gif")
title = tk.Label(root, image=background)
title.pack(side='top')


leaderboard_button = tk.Button(root, bg = 'forest green', text='Leaderboard', width=25, command=leaderboardwindow, font= ('Comic Sans MS', 48))
leaderboard_button.pack(side='bottom')
multiplayer_button = tk.Button(root, bg = 'lime green', text='Multiplayer', width=25, command=multiplayerwindow, font=('Comic Sans MS', 48))
multiplayer_button.pack(side='bottom')
singleplayer_button = tk.Button(root, bg = 'green yellow', text='Singleplayer', width=25, command=singleplayerwindow, font=('Comic Sans MS', 48))
singleplayer_button.pack(side='bottom')






root.mainloop()
