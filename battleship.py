import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

board_size = 10
num_ships = 5
board = [['O' for _ in range(board_size)] for _ in range(board_size)]
ships = []

def generate_ships():
    for _ in range(num_ships):
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)
        ships.append([ship_row, ship_col])

@app.route('/', methods=['GET', 'POST'])
def play_battleship():
    if request.method == 'POST':
        row = int(request.form['row'])
        col = int(request.form['col'])

        if [row, col] in ships:
            board[row][col] = 'X'
            ships.remove([row, col])
        else:
            board[row][col] = 'M'

        if len(ships) == 0:
            return render_template('game_over.html', message='Congratulations! You sunk all the ships.')

    return render_template('index.html', board=board)

@app.route('/play_again', methods=['POST'])
def play_again():
    global board, ships
    board = [['O' for _ in range(board_size)] for _ in range(board_size)]
    ships = []
    generate_ships()
    return redirect('/')

@app.route('/exit', methods=['POST'])
def exit_game():
    return render_template('game_over.html', message='Thanks for playing! Goodbye.')

if __name__ == '__main__':
    generate_ships()
    app.run(debug=True)
