from share_module import Shared
shared = Shared()

class War:
    def __init__(self) -> None:
        self.greeting = f'welcome Blackjack game!'

    def displayGreetingMsg(self): 
        print('\n' * 100)
        print(self.greeting)

    def requestStartGameNow(self, msg):
        return shared.request_confirmation(msg)