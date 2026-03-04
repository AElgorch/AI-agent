Adversarial Search:  Minimax AI

A Python-based AI agent that uses the Minimax algorithm with Alpha-Beta Pruning to play a game of Tic-Tac-Toe. This agent evaluates all possible future states to ensure it never loses, achieving a draw at worst and a win at best.
Overview

This project demonstrates the application of adversarial search in a zero-sum game environment. By treating Tic-Tac-Toe as a state-space search problem, the AI explores the game tree to make mathematically optimal decisions.
Key Features

    Alpha-Beta Pruning: Optimized search efficiency by eliminating branches that do not influence the final decision, reducing the number of states evaluated.

    Recursive Game Theory: Implements the core principles of the Minimax algorithm, recursively alternating between maximizing and minimizing players.

    Robust Logic: Includes deep copying of board states and custom exception handling for invalid actions.

How It Works

The AI views the game as a tree of possibilities:

    Minimax Algorithm: The X player attempts to maximize its score, while the O player is trying to minimize the score.

    State Evaluation: Terminal states are assigned values: +1 (Max), -1 (Min), or 0 (Draw).

    Alpha-Beta Pruning: Two variables, α (the best value Max can guarantee) and β (the best value Min can guarantee), are used to stop evaluating branches that are guaranteed to be worse than previously explored options.

Technical Implementation

The core logic is contained within several modular functions:

    player(board): Tracks whose turn it is based on the current board state.

    actions(board): Returns a set of all legally available coordinates.

    result(board, action): Returns a new board state without modifying the original (Deep Copy).

    winner(board): Uses geometric checks for rows, columns, and diagonals.

    minimax(board): The entry point for the AI's decision-making process.
