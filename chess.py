import tkinter as tk
from tkinter import messagebox

class ChessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")
        self.canvas = tk.Canvas(master, width=640, height=640)
        self.canvas.pack()
        self.board = self.initialize_board()
        self.draw_board()

    def initialize_board(self):
        board = []
        for i in range(8):
            row = [' '] * 8
            board.append(row)
        return board

    def draw_board(self):
        colors = ["white", "gray"]
        for i in range(8):
            for j in range(8):
                color = colors[(i + j) % 2]
                x0, y0 = j * 80, i * 80
                x1, y1 = x0 + 80, y0 + 80
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        # Draw pieces
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != ' ':
                    self.canvas.create_text(j * 80 + 40, i * 80 + 40, text=piece, font=("Arial", 36))

    def play(self):
        self.canvas.bind("<Button-1>", self.click_square)

    def click_square(self, event):
        col = event.x // 80
        row = event.y // 80
        piece = self.board[row][col]
        messagebox.showinfo("Square Clicked", f"Piece: {piece}, Row: {row}, Column: {col}")

def main():
    root = tk.Tk()
    chess_game = ChessGame(root)
    chess_game.play()
    root.mainloop()

if __name__ == "__main__":
    main()
