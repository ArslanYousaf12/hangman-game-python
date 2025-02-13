# Hangman Game

## Overview
This is a simple Hangman game implemented in Python. The game randomly selects a word, and the player must guess the word by suggesting letters within a limited number of attempts.

## Features
- Random word selection from a predefined list
- User input for letter guesses
- Tracks incorrect guesses and limits the number of attempts
- Displays the current progress of the word with underscores
- Provides feedback on correct and incorrect guesses
- Ends the game when the word is guessed correctly or attempts run out

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/ArslanYousaf12/hangman-game-python.git
   ```
2. Navigate to the project directory:
   ```sh
   cd hangman-game
   ```
3. Run the game:
   ```sh
   python hangman.py
   ```

## How to Play
1. The game will randomly select a word and display it as underscores.
2. You can enter a single letter as your guess.
3. If the letter is in the word, it will be revealed in the correct position(s).
4. If the letter is not in the word, you will lose an attempt.
5. The game continues until you either guess the word correctly or run out of attempts.

## Example Gameplay
```
Welcome to Hangman!
Word: _ _ _ _ _
Enter a letter: e
Correct! Word: _ e _ _ _
Enter a letter: a
Incorrect! Attempts left: 5
...
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Contact
For any inquiries, reach out to me at [Github (https://github.com/ArslanYousaf12)].

