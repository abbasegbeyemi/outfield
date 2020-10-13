from random import shuffle


class Card:

    def __init__(self, value: str, suit: str):
        self._card_value = value
        self._card_suit = suit

    @property
    def card_value(self):
        return self._card_value

    @property
    def card_suit(self):
        return self._card_suit

    def __repr__(self):
        return f"Card {self.card_value} of {self.card_suit}"

    def __str__(self):
        if self.card_value == "1":
            return f"Card: A{self.card_suit}"
        elif self.card_suit == "Joker":
            return f"Card: Joker!"
        else:
            return f"Card: {self.card_value}{self.card_suit}"

    def __eq__(self, other):
        return self.card_suit == other.card_suit and self.card_value == other.card_value


class CardDeck:
    suits = (u"\u2660", u"\u2666", u"\u2666", u"\u2663")
    values = [str(n) for n in range(1, 11)]
    values.extend(["J", "Q", "K"])
    joker = ("Joker", "Joker")

    def __init__(self, jokers: int = 0, deck_num: int = 1):
        """
        Deck of playing cards. Takes an int for the amout of joker cards required.
        :param jokers: {int} number of joker cards. Default is 0
        """
        self.deck_num = deck_num
        self.jokers = jokers
        self.deck = []
        self.init_deck()

    # The deck manages itself
    def init_deck(self):
        """
        This is where we initialise the deck
        :return:
        """
        self.deck = [Card(v, s) for v in self.values for s in self.suits for _ in range(self.deck_num)]
        if self.jokers:
            j = [Card(*self.joker) for _ in range(self.jokers)]
            # Extend the deck by the number of joker cards required
            self.deck.extend(j)
        # We shuffle the deck after initialisng
        shuffle(self.deck)

    def get_card(self):
        """
        Get a card from the shuffled deck
        :return: Returns a card, or None if deck is empty
        """
        try:
            card = self.deck.pop()
        except IndexError:
            card = None
        return card


class Player:
    """"""

    def __init__(self):
        """Constructor for Blackjack player"""
        self.player_cards = []


class BlackJack:
    """Black Jack Game """

    def __init__(self):
        """
        The black jack game board.
        The goal is to get a total of 21 or as close to 21 as you can.
        Face cards i.e J, Q, and K are valued at 10
        Ace can be 1 or 11
        The remaining cards are worth their values.
        """
        self.player_num = 0
        self.players = {}
        self.card_deck = CardDeck()
        self.start_game(self.player_num)

    def start_game(self, players):
        print("Hello, welcome to Mimi's Blackjack table... I'm Mimi, your dealer")
        while not players:
            players = check_num(input("How many people will be joining us? "))
            if not players:
                print("Apologies, that number does not look right")
        self.player_num = players

        if self.player_num == 1:
            n = input("Fantastic! We've got a loner. What's your name buddy? ")
            name = n if n.strip() else "Player"
            print(f"You're welcome to the table {name}")
            self.players = {n: Player() for n in [name, "***Dealer***"]}
        else:
            print("Fantastic!, We've got a party!")
            for p in range(1, self.player_num + 1):
                n = input(f"What is Player {p}'s name? ")
                name = n if n.strip() else f"Player {p}"
                print(f"You're welcome to the table {name}")
                self.players[name] = Player()

        print("***The rules of the Game***\nYou want to get a total card value of 21 on the table or close to 21.")
        print("-Suits do not matter\n-Cards have their base values apart from *J, Q, K, A*")
        print("-J, Q, K are worth 10 points")
        print("-A is worth 1 or 11, You decide!")
        print("**Let's GO!**")
        self.play_game()

    def play_game(self):
        game_complete = False
        game_round = 0
        while not game_complete:
            print(f"Round {game_round}!")

            choices = ["", "d"] if game_round == 0 else ["", "d", "c"]
            for name, player in self.players.items():
                print(f"{name}'s turn to draw a card...")
                if name != "***Dealer***":
                    choice = player_choice(choices)
                    # Deal with the players choice
                    self.player_play(choice, name)
                else:
                    self.dealer_play(name)

                score = self.evaluate_cards(name)
                print(
                    f"{name} has cards: {[c for c, _ in self.players[name].player_cards]} on the table | Total score of {score}")

            leader_name, leader_score, game_complete = self.check_winner()

            if game_complete:
                print(f"Game over! The winner is {leader_name} with a score of {leader_score}")

                print("**Game Summary**")
                for name, player in self.players.items():
                    score = self.evaluate_cards(name)
                    print(f"{name} with cards: {[c for c, _ in player.player_cards]} | total score of | {score}")

            else:
                game_round += 1

    def dealer_play(self, name):
        dealer_score = self.evaluate_cards(name)
        if dealer_score < 12:
            self.player_play("d", name)
        else:
            self.player_play("c", name)

    def player_play(self, choice, name):
        if choice in ["d", ""]:
            draw = self.card_deck.get_card()
            print(f"{name} drew {draw}")
            if draw.card_value == "1":
                mod = ""
                while mod not in ["j", "k"]:
                    mod = input("You drew an Ace! Should it be (j) 1 or (k) 11\nEnter (j) or (k): ")
                    if mod not in ["j", "k"]:
                        print("Apologies, I did not get that.")

                val = 1 if mod == "j" else 11

            elif draw.card_value in ["J", "Q", "K"]:
                val = 10

            else:
                val = int(draw.card_value)

            self.players[name].player_cards.append((draw, val))

        elif choice == "c":
            print(f"{name} has chosen to skip this round")

    def check_winner(self):
        """Game is complete if someone goes above 21"""
        leader_name = ""
        leader_score = 0
        complete = False
        for name, _ in self.players.items():
            score = self.evaluate_cards(name)

            if (score < 21) and (score > leader_score):
                leader_name = name
                leader_score = score
            elif score > 21:
                complete = True

        return leader_name, leader_score, complete

    def evaluate_cards(self, name: str):
        value = 0
        cards = self.players[name].player_cards

        for _, val in cards:
            value += val

        return value


def player_choice(choices):
    choice = "**ny**"
    while choice.strip().lower() not in choices:
        choice = input("Type 'd' or press *enter* to draw a card, 'c' to check...")
        if choice not in choices:
            print("Apologies, that choice is not available in this round")
    return choice


def check_num(n):
    n = n.strip()
    try:
        n = int(n)
    except ValueError:
        return 0
    return n if n else 0


if __name__ == '__main__':
    board = BlackJack()
