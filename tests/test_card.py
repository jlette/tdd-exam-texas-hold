from src.card import Card

def test_card_init():
    card = Card('A', 'H')
    assert card.rank == 'A'
    assert card.suit == 'H'
    assert card.value == 14
    
def test_should_consider_king_stronger_than_queen():
    stronger_card = Card("K", "H")
    weaker_card = Card("Q", "S")
    assert stronger_card > weaker_card

def test_should_consider_cards_equal_rank_as_equivalent_strength():
    card_hearts = Card("10", "H")
    card_spades = Card("10", "S")
    assert card_hearts == card_spades

def test_should_identify_ace_as_highest_rank_by_default():
    ace = Card("A", "D")
    king = Card("K", "C")
    assert ace > king