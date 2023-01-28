import itertools
from collections import defaultdict

def make_the_winner(community_cards, hands, selected_winner):
    next_cards = []
    # Create a list of all possible 5-card hands for each player
    player_hands = [[*hand, *community_cards] for hand in hands]
    # Find the best 5-card hand for each player
    best_hands = [max(itertools.combinations(hand, 5), key=hand_rank) for hand in player_hands]
    # Find the player with the highest-ranked hand
    winner = max(zip(best_hands, hands), key=lambda x: hand_rank(x[0]))[1]
    if winner == selected_winner:
        return next_cards

def hand_rank(hand):
    # Assign a numeric rank to each hand, with the highest rank being the best hand
    ranks = ['High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
    hand_rank = ranks.index(classify_hand(hand))
    return hand_rank

def classify_hand(hand):
    # Classify the hand based on the combination of cards
    hand = sorted(hand, key=lambda x: x[0])
    if is_royal_flush(hand):
        return 'Royal Flush'
    elif is_straight_flush(hand):
        return 'Straight Flush'
    elif is_four_of_a_kind(hand):
        return 'Four of a Kind'
    elif is_full_house(hand):
        return 'Full House'
    elif is_flush(hand):
        return 'Flush'
    elif is_straight(hand):
        return 'Straight'
    elif is_three_of_a_kind(hand):
        return 'Three of a Kind'
    elif is_two_pairs(hand):
        return 'Two Pairs'
    elif is_pair(hand):
        return 'Pair'
    else:
        return 'High Card'


def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False

def is_four_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdit(lambda:0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.value() == [1,4]):
        return True
    else:
        return False

def is_full_house(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdit(lambda:0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.value() == [2,3]):
        return True
    else:
        return False

def is_flush(hand):
    suits = [i[0] for i in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False

def is_straight(hand):
    # Check for a straight
    pass

def is_three_of_a_kind(hand):
    # Check for three of a kind
    pass

def is_two_pairs(hand):
    # Check for two pairs
    pass

def is_pair(hand):
    # Check for a pair
    pass

hand = ["S3", "S3", "S4", "S4", "S4"]import itertools
from collections import defaultdict

# Don't forget to convert 10 to T
card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "t":10,"j":11, "q":12, "k":13, "a":14}
hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}

def make_the_winner(community_cards, hands, selected_winner):
    next_cards = []
    # Create a list of all possible 5-card hands for each player
    player_hands = [[*hand, *community_cards] for hand in hands]
    # Find the best 5-card hand for each player
    best_hands = [max(itertools.combinations(hand, 5), key=hand_rank) for hand in player_hands]
    # Find the player with the highest-ranked hand
    winner = max(zip(best_hands, hands), key=lambda x: hand_rank(x[0]))[1]
    if winner == selected_winner:
        return next_cards

def hand_rank(hand):
    # Assign a numeric rank to each hand, with the highest rank being the best hand
    ranks = ['High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
    hand_rank = ranks.index(classify_hand(hand))
    return hand_rank

def classify_hand(hand):
    # Classify the hand based on the combination of cards
    hand = sorted(hand, key=lambda x: x[0])
    if is_straight_flush(hand):
        return 9
    elif is_four_of_a_kind(hand):
        return 8
    elif is_full_house(hand):
        return 7
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif is_three_of_a_kind(hand):
        return 4
    elif is_two_pairs(hand):
        return 3
    elif is_pair(hand):
        return 2
    else:
        return 1


def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False

def is_four_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1,4]:
        return True
    else:
        return False

def is_full_house(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2,3]:
        return True
    else:
        return False

def is_flush(hand):
    suits = [i[0] for i in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False

def is_straight(hand):
    values = [i[1] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if value_range == 4 and len(set(values)) == 5:
        return True
    elif set(values) == set(["A", "2", "3", "4", "5"]):
        return True
    else:
        return False

def is_three_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False    

def is_two_pairs(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    else:
        return False

def is_pair(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    else:
        return False


hand = ["St", "Sj", "S9", "S8", "S5"]
print(is_straight_flush(hand))
suits = [i[0] for i in hand]
if len(set(suits))==1:
    print("True")
else:
    print("False")
print(suits)
print(set(suits))
