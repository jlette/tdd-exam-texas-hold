from src.card import Card
from src.evaluator import Evaluator

def test_should_identify_high_card_category_and_choose_five_best_cards():
  
    all_available_cards = [
        Card(rank='A', suit='Hearts'),  
        Card(rank='K', suit='Spades'),  
        Card(rank='Q', suit='Diamonds'), 
        Card(rank='J', suit='Clubs'),    
        Card(rank='9', suit='Hearts'),   
        Card(rank='5', suit='Spades'),   
        Card(rank='2', suit='Diamonds')
    ]
    
    result = Evaluator.evaluate_best_hand(all_available_cards)
    
    assert result["category"] == "High Card"
    
    assert len(result["chosen_five_cards"]) == 5
    assert result["chosen_five_cards"][0].rank == 'A'
    assert result["chosen_five_cards"][4].rank == '9'