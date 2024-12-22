from jovian.pythondsa import evaluate_test_cases

tests = []

tests.append({
    "input": {
        "cards": [13, 11, 10, 7, 6, 3,2,1],
        "query": 1
    },
    "output": 7
})

tests.append({
    "input": {
        "cards": [13, 11, 10, 7, 6, 3,2,1],
        "query": 13
    },
    "output": 0
})

tests.append({
    "input": {
        "cards": [13, 11, 10, 7, 6, 3,2,1],
        "query": 12
    },
    "output": -1
})

tests.append({
    "input": {
        "cards": [],
        "query": 12
    },
    "output": -1
})

def locate_card(cards, query):
    position = 0

    while position<len(cards):
        if cards[position] == query:
            return position
        position+=1
    return -1


evaluate_test_cases(locate_card, tests)

