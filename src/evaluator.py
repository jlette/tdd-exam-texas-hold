from collections import Counter

class Evaluator:
    @staticmethod
    def evaluate_best_hand(available_cards):

        ranks_counts = Counter(card.rank for card in available_cards)
        
        for rank, count in ranks_counts.items():
            if count == 4:
                four_cards = [c for c in available_cards if c.rank == rank]
                kicker = sorted([c for c in available_cards if c.rank != rank], reverse=True)[0]
                return {"category": "Four of a Kind", "chosen_five_cards": four_cards + [kicker]}
            
            if count == 3:
                three_cards = [c for c in available_cards if c.rank == rank]
                kickers = sorted([c for c in available_cards if c.rank != rank], reverse=True)[:2]
                return {"category": "Three of a Kind", "chosen_five_cards": three_cards + kickers}
        
        pair_ranks = sorted(
            [rank for rank, count in ranks_counts.items() if count >= 2],
            key=lambda r: available_cards[0].RANK_VALUES[r],
            reverse=True
        )

        if len(pair_ranks) >= 2:
            best_two_ranks = pair_ranks[:2]
            
            pair_cards = []
            for rank in best_two_ranks:
                cards_of_this_rank = [c for c in available_cards if c.rank == rank]
                pair_cards.extend(cards_of_this_rank[:2])
            
            remaining_cards = [c for c in available_cards if c not in pair_cards]
            sorted_kickers = sorted(remaining_cards, reverse=True)
            
            return {
                "category": "Two Pair",
                "chosen_five_cards": pair_cards + sorted_kickers[:1]
            }

        if len(pair_ranks) == 1:
            best_rank = pair_ranks[0]
            pair_cards = [c for c in available_cards if c.rank == best_rank]
            
            remaining_cards = [c for c in available_cards if c.rank != best_rank]
            sorted_kickers = sorted(remaining_cards, reverse=True)
            
            return {
                "category": "One Pair",
                "chosen_five_cards": pair_cards + sorted_kickers[:3]
            }

        sorted_all = sorted(available_cards, reverse=True)
        return {
            "category": "High Card",
            "chosen_five_cards": sorted_all[:5]
        }