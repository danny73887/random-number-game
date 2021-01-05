
def start_game():
        answer=random.randint(1,10)
        attempts = 0
        
        print('Hello player! This is the number guessing game! Can you guess the number between 1-10 inclusive?')
        
        if not score:
                print('No Highscore!')
        else:
                print('Your highscore is',min(score),'!')

        while True:
                try:
                        player_guess = int(input('Please guess a number now!    '))
                                
                except ValueError:
                        print('Please enter a whole number! Your breaking my program!')
                        continue
                
                attempts += 1
                
                if player_guess > 10:
                        print('Please enter a value from 1 to 10.')
                        continue
                elif player_guess < 1:
                        print('Please enter a value from 1 to 10.')
                        continue

                elif player_guess > answer:
                        print('Too High!')
                        continue
                elif player_guess < answer:
                        print('Too low!')
                        continue
                elif player_guess == answer:
                        break
                        
        score.append(attempts)   
        
        print('Congratulations you win!')       
        print('You finished the game in only', attempts, 'tries!')
        
        want = input('Would you like to play again?   Y/N     ').lower()
        if want == 'y':
                start_game()
        else:
                print('goodbye!')



import random
score = []                
start_game()
