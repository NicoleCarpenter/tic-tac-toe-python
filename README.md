# Tic Tac Toe

[![Build Status](https://travis-ci.org/NicoleCarpenter/tic-tac-toe-python.svg?branch=master)](https://travis-ci.org/NicoleCarpenter/tic-tac-toe-python)

Tic tac toe is a console application built with Python. The classic game of tic tac toe is a two player game where players trade turns placing a mark on a square board until either one player has won, or the game results in a draw. A player can win by placing three consecutive marks, either horizontally, vertically, or diagonally

``` python
   X | X | X       X |   |         X |   |
  ===+===+===     ===+===+===     ===+===+===
     |   |         X |   |           | X |
  ===+===+===     ===+===+===     ===+===+===
     |   |         X |   |           |   | X
```

## Requirements

* [Python](https://www.python.org/)

## Running the Application

In your desired location in terminal, clone the repo

```
git clone git@github.com:NicoleCarpenter/tic-tac-toe-python.git
```

Then `cd` into the application's root directory

```
cd tic-tac-toe
```

From there, to run the application, type

``` python
python ttt.py
```

## Running the Tests

From the root directory, type

``` python
python -m unittest discover -v
```
