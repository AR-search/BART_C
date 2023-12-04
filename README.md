# BART_C

## Description

BART_C is a BART game developed in Python, using the Pygame library.
This game is designed to simulate the experience of inflating a balloon,
offering players a challenge in risk management and decision-making.
The game is optimized for launching and playing in the PyCharm integrated 
development environment.

## Prerequisites

- PyCharm (recommended IDE for running this application)
- Python 3.x
- Pygame
- Pandas

## Installation and Setup

1. Clone the BART_C repository or download the source code.
2. Open PyCharm and select `File > Open` to open the BART_C project folder.
3. Set up a Python virtual environment in PyCharm and install necessary dependencies with `pip install -r requirements.txt`.
4. Ensure all project settings are correctly configured in PyCharm, including paths to resource files (images, sounds).

## Launching BART_C in PyCharm

1. In PyCharm, ensure the correct Python interpreter is selected in project settings.
2. Navigate to the `main.py` file.
3. Right-click the file and select `Run 'main'` to start the game.


## Explanation of Main.py File

The `main.py` file serves as the entry point for the BART_C game.
It initializes the user interface and manages basic interactions before launching the main game.
The `main.py` file is the core of the BART_C game. 
It initiates Pygame, manages game display, user interactions, and game logic.

## Explanation of Expe.py File

`expe.py` is the file that contains the main gameplay logic for BART_C. This script is executed 
after the initial setup in `main.py` and is where players interact with the game. Key elements of 
this file include:

**Gameplay Mechanics**: This includes detailed implementation of the balloon inflation process,
  where players repeatedly inflate a virtual balloon to increase potential earnings.
  The risk calculation determines the likelihood of the balloon bursting, which is a critical
  part of the game's challenge.
  
**Player Interactions**: Players interact with the game primarily through keyboard inputs indicated 
  on the screen. These inputs are used to inflate the balloon (space bar), make decisions about cashing 
  out earnings skip to the next balloon (enter), and navigating through the game's interface.

**Game Loop**: The core loop of the game where the state is continuously updated based on player inputs and game rules. 
  This includes updating the size of the balloon on the screen, adjusting the risk level, and updating the player's current score.

**Graphics and Sound Management**: This involves handling the rendering of game graphics, 
  such as the dynamic changes in the balloon's size and the game's background, as well as 
  playing sounds like balloon inflating noises or the sound of the balloon bursting.

**Game State Management**:  This includes the size of the balloon, the player's accumulated score, the number of remaining tries, and whether the balloon 
  is intact or has burst.

**Player Feedback and Score**: The game provides immediate feedback to the player based on their actions, 
  such as visual and auditory cues when the balloon inflates or bursts. The player's score is also updated 
  in real-time, reflecting the earnings from successful balloon inflations.

## Data Exportation

The BART_C game records and exports session data to an Excel file.
This data includes the user's ID, age, number of popped balloons, saved money amount, and an indicator of whether money was cashed out or not. 
This information is useful for analyzing player performance and collecting game data.
