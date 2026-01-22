import random
from enum import Enum
from typing import Optional


class Difficulty(Enum):
    """Difficulty levels with corresponding number of attempts."""
    NORMAL = 10
    HARD = 5


class GameState(Enum):
    """Possible states of the game."""
    PLAYING = 0
    WON = 1
    LOST = 2


def get_valid_input(prompt: str, valid_options: list[str]) -> str:
    """
    Get validated user input that matches one of the valid options.
    
    Args:
        prompt: The message to display to the user
        valid_options: List of acceptable input values
        
    Returns:
        Validated user input string
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


def validate_guess_range(guess: int, min_val: int = 0, max_val: int = 100) -> bool:
    """
    Check if guess is within valid range.
    
    Args:
        guess: The number guessed by the user
        min_val: Minimum allowed value (default: 0)
        max_val: Maximum allowed value (default: 100)
        
    Returns:
        True if guess is within range, False otherwise
    """
    return min_val <= guess <= max_val


def select_difficulty(difficulty_input: str) -> Difficulty:
    """
    Select game difficulty based on user input.
    
    Args:
        difficulty_input: User's difficulty choice ('0' for normal, '1' for hard)
        
    Returns:
        Selected Difficulty enum value
    """
    if difficulty_input == '0':
        print('Normal Difficulty Selected')
        return Difficulty.NORMAL
    else:
        print('Hard Difficulty Selected')
        return Difficulty.HARD


def check_guess(target_number: int, user_guess: int) -> str:
    """
    Check if the user's guess is correct, too high, or too low.
    
    Args:
        target_number: The random number to guess
        user_guess: The number guessed by the user
        
    Returns:
        String indicating result: 'correct', 'too_high', or 'too_low'
    """
    if user_guess > target_number:
        return 'too_high'
    elif user_guess < target_number:
        return 'too_low'
    else:
        return 'correct'


def show_life_hearts(remaining_attempts: int) -> None:
    """
    Display remaining attempts as heart symbols.
    
    Args:
        remaining_attempts: Number of attempts left
    """
    for _ in range(remaining_attempts):
        print('❤ ', end='')
    print()


def show_game_result(target_number: int, game_state: GameState) -> None:
    """
    Display the final game result.
    
    Args:
        target_number: The correct number that was to be guessed
        game_state: The final state of the game (WON or LOST)
    """
    if game_state == GameState.WON:
        print('Congratulations! You Win! 🎉')
    elif game_state == GameState.LOST:
        print(f'The correct number was: {target_number}')
        print('You Lose! Better luck next time! 💔')


def get_user_guess() -> Optional[int]:
    """
    Get and validate user's guess input.
    
    Returns:
        Valid integer guess or None if input is invalid
    """
    try:
        guess = int(input('Enter your guess (0-100): '))
        if not validate_guess_range(guess):
            print('Please enter a number between 0 and 100.')
            return None
        return guess
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
        return None


def run_game() -> None:
    """
    Main game loop. Manages the game flow from start to finish.
    """
    print('=' * 40)
    print('Welcome to the Number Guessing Game!')
    print('=' * 40)
    
    play_again = 'y'
    
    while play_again == 'y':
        print('\n' + '=' * 40)
        print('New Game Started!')
        print('=' * 40)
        
        # Generate random number
        target_number = random.randint(0, 100)
        
        # Select difficulty
        print('\nSelect Difficulty:')
        difficulty_input = get_valid_input(
            'Normal (0) or Hard (1): ',
            ['0', '1']
        )
        difficulty = select_difficulty(difficulty_input)
        remaining_attempts = difficulty.value
        
        # Initialize game state
        game_state = GameState.PLAYING
        
        print(f'\nGuess the number between 0 and 100!')
        print(f'You have {remaining_attempts} attempts.')
        
        # Main game loop
        while game_state == GameState.PLAYING:
            print(f'\nAttempts remaining: ', end='')
            show_life_hearts(remaining_attempts)
            
            # Get valid guess from user
            user_guess = None
            while user_guess is None:
                user_guess = get_user_guess()
            
            # Check the guess
            result = check_guess(target_number, user_guess)
            
            if result == 'correct':
                game_state = GameState.WON
            else:
                remaining_attempts -= 1
                if remaining_attempts == 0:
                    game_state = GameState.LOST
                else:
                    if result == 'too_high':
                        print(f'{user_guess} is too high! ↓')
                    else:
                        print(f'{user_guess} is too low! ↑')
        
        # Show final result
        print('\n' + '=' * 40)
        show_game_result(target_number, game_state)
        print('=' * 40)
        
        # Ask if user wants to play again
        play_again = get_valid_input(
            '\nWould you like to play again? (y/n): ',
            ['y', 'n']
        )
    
    print('\n' + '=' * 40)
    print('Thanks for playing! Goodbye! 👋')
    print('=' * 40)


if __name__ == "__main__":
    run_game()