Tic-Tac-Toe AI using Minimax Algorithm

Project Overview
This project is a simple implementation of the classic Tic-Tac-Toe game integrated with an Artificial Intelligence agent. The AI uses the Minimax algorithm, a fundamental concept in AI and Game Theory, to make optimal decisions.
The game allows a human player to compete against an unbeatable AI opponent in a console-based environment.

Concepts Used
Artificial Intelligence (AI)
Minimax Algorithm
Game Theory  
Recursion
Decision Making

Features
Human vs AI gameplay
AI always plays optimally (cannot be defeated)
Simple command-line interface
Input validation for user moves
Detects win, loss, and draw conditions

Technologies Used
Python 3
Built-in libraries (math)

Project Structure
TIC-TAC-TOE/
│── tic_tac_toe.py
│── README.md

How to Run the Project
Install Python (if not already installed)
Download or clone this repository
Navigate to the project folder
Run the following command:
Bash
python tic_tac_toe.py

How the AI Works
The AI uses the Minimax algorithm, which:
Simulates all possible moves
Evaluates each move based on outcomes
Chooses the best possible move to maximize its chances of winning
AI = Maximizing player (O)
Human = Minimizing player (X)

Game Rules
The board has positions from 0 to 8
Players take turns:
Human → X
AI → O
First to align 3 symbols wins
If all positions are filled → Draw

Example Gameplay

|   |  
--+---+--
 |   |  
--+---+--
 |   |  

Enter your move (0-8): 0
X |   |  
--+---+--
 |   |  
--+---+--
 |   |  

AI chooses: 4

Author
Sonali
B.Tech CSE (AI & ML)
VIT Bhopal

Learning Outcome
Through this project, I learned:
How AI makes decisions in games
Implementation of recursive algorithms
Problem-solving using logic and optimization

Future Improvements
Add GUI using Tkinter or Pygame
Add difficulty levels
Multiplayer mode
Web-based version

Source Code
Main implementation file:  
TIC TAC TOE.py 