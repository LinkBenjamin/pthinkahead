# pThinkAhead
A reimplementation of [Think Ahead+](https://www.macintoshrepository.org/4279-think-ahead-) by Keith Lambert.

# How to play
The game is a one- or two- player board game (play against the CPU or a friend). The goal is to have more points than your opponent by the time all the moves are made. Each player takes a turn moving the cursor - one player is only allowed to move vertically, the other horizontally. The space they move to provides them with the number of points displayed. Some spaces have negative numbers, some have positive numbers, and some have special abilities, like a mystery box whose score can't be seen until it's played. Once a square has been played, it's no longer a valid move. The game continues until a player can no longer make a move.    

# How to interact with the code

`main.py` is the main module, you should be able to execute `#> python main.py` and the game should start.

This is implemented with the [pygame](https://www.pygame.org/docs/) library.