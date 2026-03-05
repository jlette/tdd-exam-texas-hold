from collections import Counter
class Evaluator:
    @staticmethod
    def evaluate_best_hand(available_cards):

        ranks_counts = Counter(card.rank for card in available_cards)
        
        pair_ranks = [rank for rank, count in ranks_counts.items() if count == 2]
        
        if pair_ranks:

            best_pair_rank = max(pair_ranks, key=lambda r: Card.RANK_VALUES[r])
            
            pair_cards = [card for card in available_cards if card.rank == best_pair_rank]
            remaining_cards = [card for card in available_cards if card.rank != best_pair_rank]
            
            sorted_kickers = sorted(remaining_cards, reverse=True)
            
            chosen_five = pair_cards + sorted_kickers[:3]
            
            return {
                "category": "One Pair",
                "chosen_five_cards": chosen_five
            }
            
        sorted_cards = sorted(available_cards, reverse=True)
        return {
            "category": "High Card",
            "chosen_five_cards": sorted_cards[:5]
        }