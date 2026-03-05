from src.card import Card

def test_card_attributes():
    card = Card('A', 'H')
    assert card.rank == 'A'
    assert card.suit == 'H'
    assert card.value == 14