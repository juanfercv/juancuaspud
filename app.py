from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <title>Juego del Gato</title>
            <style>
                body { 
                    background-color: #f0f8ff; 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    margin-top: 50px;
                }
                h1 { color: #2e8b57; }
                #board {
                    display: grid;
                    grid-template-columns: repeat(3, 100px);
                    grid-template-rows: repeat(3, 100px);
                    gap: 5px;
                    justify-content: center;
                    margin-top: 20px;
                }
                .cell {
                    background: #fff;
                    border: 2px solid #2e8b57;
                    font-size: 2em;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                }
                #status {
                    margin-top: 20px;
                    font-size: 18px;
                    color: #333;
                }
                button {
                    margin-top: 15px;
                    padding: 10px 20px;
                    font-size: 16px;
                    background: #2e8b57;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Hola Juan Fernando Cuaspud Velasco 👋</h1>
            <p>¡Bienvenido a tu aplicación Flask!</p>

            <div id="board"></div>
            <div id="status">Turno de X</div>
            <button onclick="resetGame()">Reiniciar</button>

            <script>
                let board = ["", "", "", "", "", "", "", "", ""];
                let currentPlayer = "X";
                let gameActive = true;

                const boardElement = document.getElementById("board");
                const statusElement = document.getElementById("status");

                function renderBoard() {
                    boardElement.innerHTML = "";
                    board.forEach((cell, index) => {
                        const cellElement = document.createElement("div");
                        cellElement.classList.add("cell");
                        cellElement.textContent = cell;
                        cellElement.addEventListener("click", () => makeMove(index));
                        boardElement.appendChild(cellElement);
                    });
                }

                function makeMove(index) {
                    if (board[index] === "" && gameActive) {
                        board[index] = currentPlayer;
                        if (checkWinner()) {
                            statusElement.textContent = "¡Ganó " + currentPlayer + "!";
                            gameActive = false;
                        } else if (board.every(cell => cell !== "")) {
                            statusElement.textContent = "¡Empate!";
                            gameActive = false;
                        } else {
                            currentPlayer = currentPlayer === "X" ? "O" : "X";
                            statusElement.textContent = "Turno de " + currentPlayer;
                        }
                        renderBoard();
                    }
                }

                function checkWinner() {
                    const winPatterns = [
                        [0,1,2],[3,4,5],[6,7,8], // filas
                        [0,3,6],[1,4,7],[2,5,8], // columnas
                        [0,4,8],[2,4,6]          // diagonales
                    ];
                    return winPatterns.some(pattern => 
                        pattern.every(index => board[index] === currentPlayer)
                    );
                }

                function resetGame() {
                    board = ["", "", "", "", "", "", "", "", ""];
                    currentPlayer = "X";
                    gameActive = true;
                    statusElement.textContent = "Turno de X";
                    renderBoard();
                }

                renderBoard();
            </script>
        </body>
    </html>
    """



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2407)