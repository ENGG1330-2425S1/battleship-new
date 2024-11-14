# Battleship Python Game

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Game Modes](#game-modes)
- [Running Tests](#running-tests)

## Introduction

Welcome to the **Battleship Python Game**! This is a console-based implementation of the classic Battleship game where you can play against the computer. Strategize your attacks, place your ships wisely, and sink your opponent's fleet to win the game.

## Features

- **Multiple Game Modes**:
  - **Attack Mode**: Take turns attacking the computer's grid.
  - **Defense Mode**: Defend against the computer's attacks.
  - **Combine Mode**: A mix of both attack and defense strategies.
  
- **User-Friendly CLI**: Clear and interactive command-line interface for an enjoyable gaming experience.

- **Ship Placement**:
  - **Manual Placement**: Place your ships manually with coordinates and directions.
  - **Random Placement**: Let the computer place ships randomly.

- **Attack Methods**:
  - **Horizontal Bomb**
  - **Vertical Bomb**
  - **Cross Bomb**
  - **Common Bomb**

- **Visual Grid Representation**: Easily view your grid and track hits/misses.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/battleship.git
   cd battleship
   ```

## Usage

Run the main game script using Python:

```bash
python main.py
```

**Alternatively**, you can select different game modes:

```bash
python game_logic/selectmode.py
```

Follow the on-screen prompts to place your ships and start battling the computer!

## Directory Structure

```
battleship/
├── .gitignore
├── constants.py
├── matrix.py
├── cli.py
├── main.py
├── README.md
├── game_logic/
│   ├── __init__.py
│   ├── attackmode.py
│   ├── battle.py
│   ├── combinemode.py
│   ├── defensemode.py
│   ├── helper.py
│   ├── place_ship.py
│   ├── selectmode.py
│   ├── welcome.py
│   └── test.py
└── tests/
    ├── test_battle.py
    ├── test_cli.py
    ├── test_helper.py
    ├── test_matrix.py
    └── test_place_ship.py
```

- **`constants.py`**: Defines ship types and labels.
- **`matrix.py`**: Handles matrix creation and manipulation.
- **`cli.py`**: Manages command-line interface functions.
- **`main.py`**: Entry point for the standard game mode.
- **`game_logic/`**: Contains modules for different game functionalities and modes.
- **`tests/`**: Contains unit tests for the project.

## Game Modes

1. **Standard Mode (`main.py`)**:
   - Classic Battleship experience where you place your ships and take turns attacking the computer.

2. **Combine Mode (`game_logic/combinemode.py`)**:
   - A hybrid mode that combines attack and defense strategies for a more challenging gameplay.

3. **Attack Mode (`game_logic/attackmode.py`)**:
   - Focuses on the offensive aspect, allowing multiple players to attack the computer's grid.

4. **Defense Mode (`game_logic/defensemode.py`)**:
   - Concentrates on defending your grid against the computer's attacks.

5. **Select Mode (`game_logic/selectmode.py`)**:
   - Choose between available game modes at the start of the game.

## Running Tests

Ensure you have `unittest` installed (it's included in the Python standard library).

Navigate to the `tests/` directory and run the test modules:

```bash
python -m unittest discover tests
```

This command will discover and run all tests in the `tests/` directory.