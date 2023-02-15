class Card:
    SUIT_HEARTS = 'Hearts'
    SUIT_DIAMONDS = 'Diamonds'
    SUIT_CLUBS = 'Clubs'
    SUIT_SPADES = 'Spades'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
