from player import Player

"""
Bot Class
Subclass of Player. Contains the bot brain.
"""

class Bot(Player):

    def choose_action(self, game) -> str:
        # far, can't attack, approaches
        if game.dtp > game.MAX_ATK_DIST:
            return '1' 
        
        # close (less than 3 steps) and low HP, runs away
        elif game.dtp <= game.MAX_ATK_DIST - 1 and self.hp < self.opponent.hp:
            return '2' 
        
        # close, can attack, attacks
        else:
            return '3' 
        
