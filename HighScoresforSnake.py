import tkinter as tk


highscore = open("Highscore.txt", "r")
read_highscore=highscore.read()

highscores_split=read_highscore.split()
sorted_highscore=sorted(highscores_split, key=int, reverse=True)



root = tk.Tk()
root.title("SNAKE")
root.geometry('900x800')

HighScoreTitle = tk.Label(root, bg = 'DarkOliveGreen1',  text='High Scores', width=100, font= ('Comic Sans MS', 110))
HighScoreTitle.pack(side='top')

HighScore4 = tk.Label(root, bg = 'SpringGreen2',  text=str(sorted_highscore[3]), width=50, font=('Comic Sans MS', 76))
HighScore4.pack(side='bottom')
HighScore3 = tk.Label(root, bg = 'green yellow',  text=str(sorted_highscore[2]), width=50, font=('Comic Sans MS', 76))
HighScore3.pack(side='bottom')
HighScore2 = tk.Label(root, bg = 'lime green', text=str(sorted_highscore[1]), width=50, font=('Comic Sans MS', 76))
HighScore2.pack(side='bottom')
HighScore1 = tk.Label(root, bg = 'forest green', text=str(sorted_highscore[0]), width=50, font= ('Comic Sans MS', 76))
HighScore1.pack(side='bottom')

root.mainloop()
