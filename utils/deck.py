import random


def create_card(rank:str,suite:str) -> dict:
    rank = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
    suite = "H", "C", "D", "C"
    value = rank
    return {rank: rank, suite: suite, value: rank}
# create_card()


def compare_cards(p1_card:dict, p2_card:dict) -> str:


    p1_card1 = "human players (p1) card"
    p2_card2 = "AI (p2) players card"
    for k,v in enumerate(compare_cards()):

        if p1_card[v] > p2_card[v]:
            return f"The winner of the card is:{p1_card1}"
        if p2_card[v] > p1_card[v]:
            return f"The winner of the card is:{p2_card2}"
        elif p1_card[v] == p2_card[v]:
            return "war"
    # return
# compare_cards()




def create_deck() -> list[dict]:

    # card = create_card()
    # return card[0:4]

    return [
        {"rank": "2", "suite": "H", "value": 2},
        {"rank": "3", "suite": "H", "value": 3},
        {"rank": "4", "suite": "H", "value": 4},
        {"rank": "5", "suite": "H", "value": 5},
        {"rank": "6", "suite": "H", "value": 6},
        {"rank": "7", "suite": "H", "value": 7},
        {"rank": "8", "suite": "H", "value": 8},
        {"rank": "9", "suite": "H", "value": 9},
        {"rank":"10", "suite": "H", "value": 10},
        {"rank": "J", "suite": "H", "value": 11},
        {"rank": "Q", "suite": "H", "value": 12},
        {"rank": "K", "suite": "H", "value": 13},
        {"rank": "A", "suite": "H", "value": 14},

        {"rank": "2", "suite": "C", "value": 2},
        {"rank": "3", "suite": "C", "value": 3},
        {"rank": "4", "suite": "C", "value": 4},
        {"rank": "5", "suite": "C", "value": 5},
        {"rank": "6", "suite": "C", "value": 6},
        {"rank": "7", "suite": "C", "value": 7},
        {"rank": "8", "suite": "C", "value": 8},
        {"rank": "9", "suite": "C", "value": 9},
        {"rank":"10", "suite": "C", "value": 10},
        {"rank": "J", "suite": "C", "value": 11},
        {"rank": "Q", "suite": "C", "value": 12},
        {"rank": "K", "suite": "C", "value": 13},
        {"rank": "A", "suite": "C", "value": 14},

        {"rank": "2", "suite": "D", "value": 2},
        {"rank": "3", "suite": "D", "value": 3},
        {"rank": "4", "suite": "D", "value": 4},
        {"rank": "5", "suite": "D", "value": 5},
        {"rank": "6", "suite": "D", "value": 6},
        {"rank": "7", "suite": "D", "value": 7},
        {"rank": "8", "suite": "D", "value": 8},
        {"rank": "9", "suite": "D", "value": 9},
        {"rank":"10", "suite": "D", "value": 10},
        {"rank": "J", "suite": "D", "value": 11},
        {"rank": "Q", "suite": "D", "value": 12},
        {"rank": "K", "suite": "D", "value": 13},
        {"rank": "A", "suite": "D", "value": 14},

        {"rank": "2", "suite": "S", "value": 2},
        {"rank": "3", "suite": "S", "value": 3},
        {"rank": "4", "suite": "S", "value": 4},
        {"rank": "5", "suite": "S", "value": 5},
        {"rank": "6", "suite": "S", "value": 6},
        {"rank": "7", "suite": "S", "value": 7},
        {"rank": "8", "suite": "S", "value": 8},
        {"rank": "9", "suite": "S", "value": 9},
        {"rank":"10", "suite": "S", "value": 10},
        {"rank": "J", "suite": "S", "value": 11},
        {"rank": "Q", "suite": "S", "value": 12},
        {"rank": "K", "suite": "S", "value": 13},
        {"rank": "A", "suite": "S", "value": 14},
    ]

# print(len(create_deck()))



cd = create_deck()

from random import randint
def shuffle(deck:list[dict]) -> list[dict]:
    deck = cd


    c = 1
    while c <= 1000:
        index_1, index_2 = 0,0
        while index_1 == index_2:
            index_1 = randint(1,52)
            index_2 = randint(1,52)
        print(index_1,index_2)
        # two_random = randint(1,52)
        c += 1

    return deck

shuffle()



# if __name__ == "__main__":