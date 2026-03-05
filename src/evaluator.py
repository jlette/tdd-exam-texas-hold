class Evaluator:
    
    @staticmethod
    def evaluate_best_hand(available_cards):
        
        sorted_cards = sorted(available_cards, reverse=True)
        
        chosen_five = sorted_cards[:5]
        
        return {
            "category": "High Card",
            "chosen_five_cards": chosen_five
        }