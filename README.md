
# Crow and Vulture Game

## Introduction
This game is a strategic board game played between Crows (represented as skyblue coins) and a Vulture (represented as a yellow coin). The game is coded in Python using object-oriented programming principles. The objective varies based on which side you play:

- **Crows' Objective:** Surround and block the Vulture so it cannot move.
- **Vulture's Objective:** Jump over Crows to eliminate them until only one Crow remains or it reaches a winning condition.

## Game Instructions
1. **Starting the Game:**
   - Run the command:
     ```bash
     python3 kaooa.py
     ```
   - The game board will be displayed, showing initial positions for Crows and the Vulture.

2. **Placing and Moving Coins:**
   - **Placing a Coin:** Click on an empty spot on the board to place a Crow.
   - **Selecting a Coin to Move:** Click on a Crow to turn it green, indicating it's selected for movement.
   - **Moving a Crow:** After selecting a Crow, click on an adjacent empty spot to move it, following the movement rules.
   - **Moving the Vulture:** Click on the Vulture to select it, then click on an adjacent empty spot to move it or jump over a Crow to eliminate it and move to the next spot in a straight line.

3. **Movement Rules:**
   - **Crow Movement:** Can only move to adjacent empty spots until there are 7 Crows, after which they can move to any adjacent empty spot.
   - **Vulture Movement:** Can move to any adjacent empty spot or jump over a Crow to eliminate it if there's a vacant spot directly after the Crow in a straight line.

4. **Winning Conditions:**
   - **Vulture Wins:** If it eliminates 4 Crows.
   - **Crows Win:** If they surround the Vulture so it cannot move.

5. **Interface:**
   - The current state of the game, instructions, and prompts are displayed in the center of the board.
   - Colors of coins and birds are shown on the top-right corner of the board for easy reference.

6. **Gameplay:**
   - Follow on-screen prompts and instructions for the next steps and moves.
   - The game interface is GUI-based, ensuring a user-friendly experience.

7. **Ending the Game:**
   - When a winning condition is met, the board resets, and the winner (Crows or Vulture) is announced.
