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

tests.append({
    "input": {
        "cards": [11, 9, 8, 6, 6, 6, 4, 3, 1, 1],
        "query": 6
    },
    "output": 3
})

def locate_card_brute_force(cards, query):
    position = 0

    while position<len(cards):
        if cards[position] == query:
            return position
        position+=1
    return -1


# evaluate_test_cases(locate_card_brute_force, tests)

def locate_card_binary_search(cards, query):
    lo = 0
    hi = len(cards) - 1

    while (lo<=hi):
        mid = (hi + lo) // 2
        mid_number = cards[mid]

        if(query == mid_number):
            return mid
        elif(query>mid_number):
            hi = mid - 1
        elif(query<mid_number):
            lo = mid + 1
    return -1


evaluate_test_cases(locate_card_binary_search, tests)
