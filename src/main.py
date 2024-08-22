import random

class RockPaperScissors:
    """Main class for the game Rock, Paper, Scissors
    """
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']

    def get_players_choice(self):
        """Gets the user's choice

        :return: User's choice
        :rtype: str
        """
        players_choice = input("Enter your choice (rock/paper/scissors):").lower()
        if players_choice in self.options:
            return players_choice
        else:
            print("Please enter a valid option (rock/paper/scissors):")
            return self.get_players_choice()
    
    def get_computers_choice(self):
        """Gets the computer's random choice

        :return: Computer's choice
        :rtype: str
        """
        comp_choice = random.choice(self.options)
        return comp_choice
    
    def determine_winner(self,player_choice, comp_choice):
        """Decides which player wins the game (between user and computer)

        :param player_choice: User's choice
        :type player_choice: str
        :param comp_choice: Computer's choice
        :type comp_choice: str
        """
        if (player_choice == comp_choice):
            print("It's a tie!")
        elif (player_choice == 'rock' and comp_choice == 'scissors') or (player_choice == 'scissors' and comp_choice == 'paper') or (player_choice == 'paper' and comp_choice == 'rock'):
            print(f"computer choosed: {comp_choice}.You won!")
        else:
            print(f"computer choosed: {comp_choice}. Computer Won!")
            



if __name__ == '__main__':

    game = RockPaperScissors()

    while True:
        player_choice = game.get_players_choice()
        comp_choice = game.get_computers_choice()
        game.determine_winner(player_choice, comp_choice)
        again = input('Do you want to play again? (y/n):')
        if again == 'y':
            continue
        elif again == 'n':
            break