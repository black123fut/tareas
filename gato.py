from tkinter import *
from tkinter import messagebox


def tic_tac_toe():
    ventana = Toplevel()
    ventana.title("Tic Tac Toe Deluxe")

main = Tk()

contenedor = Canvas(main, width=600, height=600, bg="#8c6586")
contenedor.pack()

contenedor.create_line(0, 200, 600, 200, width=5, fill="black")  # x1, y1, x2, y2
contenedor.create_line(0, 400, 600, 400, width=5, fill="black")

contenedor.create_line(200, 600, 200, 0, width=5, fill="black")
contenedor.create_line(400, 600, 400, 0, width=5, fill="black")

shape = "O"

grid = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8"]


def click(event):
    global shape, grid
    across = int(contenedor.canvasx(event.x) / 200)
    down = int(contenedor.canvasy(event.y) / 200)

    square = across + (down * 3)

    if grid[square] == "X" or grid[square] == "O":
        return

    if shape == "O":
        contenedor.create_oval(across * 200, down * 200,
                               (across + 1) * 200, (down + 1) * 200,
                               width=15, fill="#8c6586")
        grid[square] = "O"
        shape = "X"
    else:
        contenedor.create_line(across * 200, down * 200,
                               (across + 1) * 200, (down + 1) * 200, width=10)
        contenedor.create_line(across * 200, (down + 1) * 200,
                               (across + 1) * 200, down * 200, width=10)
        grid[square] = "X"
        shape = "O"
    winner()


def winner():
    if grid[0] == "X" and grid[1] == "X" and grid[2] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[3] == "X" and grid[4] == "X" and grid[5] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[6] == "X" and grid[7] == "X" and grid[8] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[0] == "X" and grid[3] == "X" and grid[6] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[1] == "X" and grid[4] == "X" and grid[7] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[2] == "X" and grid[5] == "X" and grid[8] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[0] == "X" and grid[4] == "X" and grid[8] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[2] == "X" and grid[4] == "X" and grid[6] == "X":
        messagebox.showinfo("WINNER", "Winner is X")
    elif grid[0] == "O" and grid[1] == "O" and grid[2] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[3] == "O" and grid[4] == "O" and grid[5] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[6] == "O" and grid[7] == "O" and grid[8] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[0] == "O" and grid[3] == "O" and grid[6] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[0] == "O" and grid[3] == "O" and grid[6] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[1] == "O" and grid[4] == "O" and grid[7] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[2] == "O" and grid[5] == "O" and grid[8] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[0] == "O" and grid[4] == "O" and grid[8] == "O":
        messagebox.showinfo("WINNER", "Winner is O")
    elif grid[2] == "O" and grid[4] == "O" and grid[6] == "O":
        messagebox.showinfo("WINNER", "Winner is O")


contenedor.bind("<Button-1>", click)

mainloop()
