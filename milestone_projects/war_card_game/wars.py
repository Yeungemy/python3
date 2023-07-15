class Wars():

    def __init__(self, wars_count, war_collateral = 0, wars_collateral_count = 0) -> None:
        self.wars_count = wars_count
        self.war_collateral = war_collateral
        self.wars_collateral_count = wars_collateral_count

    def war_alert(self): 
        self.wars_count += 1
        self.wars_collateral_count += (self.war_collateral + 1)
        print('\n\n')
        print('*' * 64)
        print(f'WAR ALERT!!! WAR ALERT!!! WAR ALERT!!! \nThat is the war {self.wars_count}! \nTo declare a war, each player must collaterlize extra {self.war_collateral} cards!')
        print('*' * 64)
        
    def declare_tie_game(self):
        print(f"\nTIE GAME since both players cannot declare a war!")

    def display_war_collateral(self):
         print(f"\nTo declare a war, each player must collateralize extra {self.war_collateral} cards")
      
    def wars_collateral_update(self):
        if self.wars_count > 0:
            msg = '{} wars'.format(self.wars_count)
            if self.wars_count == 1:
                msg = '1 war'

            print(f"\nEach player has collateralized total of {self.wars_collateral_count} cards for {msg}!")
            print(f"\nEach player has collateralized {self.war_collateral + 1} cards at war {self.wars_count}!")
        else:
            print(f"The game proceeds very peacefully without any wars!")