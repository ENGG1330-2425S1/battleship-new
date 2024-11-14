# Battleship

## Introduction

Welcome to **Battleship**, a Python-based implementation of the classic naval combat game. Challenge the computer or your friends in various game modes, strategically place your ships, and aim to sink your opponent's fleet!

## Features

- **Multiple Game Modes**:
  - **Attack Mode**: Focus on offensive strategies against the computer.
  - **Defense Mode**: Emphasize defending your own fleet.
  - **Classic Mode**: Enjoy traditional Battleship gameplay between players.

- **Ship Placement**: Choose to place ships manually or have them randomly arranged by the computer.

- **Interactive Command-Line Interface**: User-friendly prompts and clear grid displays enhance the gaming experience.

- **Comprehensive Testing**: Unit tests ensure the reliability and integrity of game mechanics.

## Usage

Run the main program to start the game:

```bash
python main.py
```

Follow the on-screen instructions to select your game mode, place your ships, and begin the battle!

## Directory Structure

```
battleship/
├── .gitignore
├── main.py
├── matrix.py
├── cli.py
├── constants.py
├── game_logic/
│   ├── __init__.py
│   ├── battle.py
│   ├── helper.py
│   ├── place_ship.py
│   └── welcome.py
├── modes/
│   ├── __init__.py
│   ├── attack_mode.py
│   ├── defense_mode.py
│   └── classic_mode.py
└── tests/
    ├── __init__.py
    ├── test_helper.py
    ├── test_battle.py
    ├── test_matrix.py
    ├── test_place_ship.py
    └── test_cli.py
```

### File Descriptions

- **main.py**: The entry point of the application. Handles mode selection and initiates the chosen game mode.
- **matrix.py**: Contains functions for creating and manipulating the game matrix.
- **cli.py**: Manages the command-line interface, including displaying the game grid and clearing the console.
- **constants.py**: Defines constants such as ship types, their sizes, and labels.
  
#### `game_logic/`
- **battle.py**: Handles the core battle mechanics, including attacks, merging grids, and checking win conditions.
- **helper.py**: Provides utility functions for validating inputs, handling positions, and managing rankings.
- **place_ship.py**: Manages ship placement logic, both for user input and random placement.
- **welcome.py**: Displays the welcome animation and game introduction.

#### `modes/`
- **attack_mode.py**: Implements the Attack Mode gameplay logic.
- **defense_mode.py**: Implements the Defense Mode gameplay logic.
- **classic_mode.py**: Implements the Classic Mode gameplay logic.

#### `tests/`
- **test_helper.py**: Tests for helper functions in `game_logic/helper.py`.
- **test_battle.py**: Tests for battle mechanics in `game_logic/battle.py`.
- **test_matrix.py**: Tests for matrix operations in `matrix.py`.
- **test_place_ship.py**: Tests for ship placement in `game_logic/place_ship.py`.
- **test_cli.py**: Tests for CLI functions in `cli.py`.

## Running Tests

All tests are located in the `tests/` directory. To execute the tests, run:

```bash
python -m unittest discover tests
```

Alternatively, to run individual test cases:

```bash
python tests/test_battle.py
```