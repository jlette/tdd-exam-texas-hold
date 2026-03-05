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
    
def test_should_identify_one_pair_category_and_prioritize_pair_in_chosen_cards():
   
    all_available_cards = [
        Card(rank='8', suit='Hearts'),   
        Card(rank='8', suit='Spades'),   
        Card(rank='A', suit='Diamonds'), 
        Card(rank='K', suit='Clubs'),    
        Card(rank='Q', suit='Hearts'),   
        Card(rank='5', suit='Spades'),   
        Card(rank='2', suit='Diamonds')
    ]
    
    result = Evaluator.evaluate_best_hand(all_available_cards)
    
    assert result["category"] == "One Pair"
    
    assert len(result["chosen_five_cards"]) == 5
    assert result["chosen_five_cards"][0].rank == '8'
    assert result["chosen_five_cards"][1].rank == '8'
    
    assert result["chosen_five_cards"][2].rank == 'A'
    assert result["chosen_five_cards"][3].rank == 'K'
    assert result["chosen_five_cards"][4].rank == 'Q'
    
def test_should_identify_two_pair_category_and_order_them_by_rank():

    all_available_cards = [
        Card(rank='10', suit='Hearts'),   
        Card(rank='10', suit='Spades'),   
        Card(rank='8', suit='Diamonds'), 
        Card(rank='8', suit='Clubs'),   
        Card(rank='2', suit='Hearts'),   
        Card(rank='2', suit='Spades'),   
        Card(rank='A', suit='Clubs')
    ]
    
    result = Evaluator.evaluate_best_hand(all_available_cards)
    
    assert result["category"] == "Two Pair"
    
    chosen_ranks = [card.rank for card in result["chosen_five_cards"]]
    assert chosen_ranks == ['10', '10', '8', '8', 'A']

def test_should_identify_three_of_a_kind():
    all_available_cards = [
        Card('J', 'H'), Card('J', 'S'), Card('J', 'D'), # Brelan
        Card('A', 'C'), Card('2', 'H'), Card('3', 'S'), Card('4', 'D')
    ]
    result = Evaluator.evaluate_best_hand(all_available_cards)
    assert result["category"] == "Three of a Kind"
    assert result["chosen_five_cards"][0].rank == 'J'
    assert result["chosen_five_cards"][2].rank == 'J'