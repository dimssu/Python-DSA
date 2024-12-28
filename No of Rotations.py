from jovian.pythondsa import evaluate_test_cases

tests = []

tests.append({
    "input": {
        "array": [7, 8, 1, 2, 3, 4, 5, 6]
    },
    "output": 2
})

tests.append({
    "input": {
        "array": [3, 4, 5, 1, 2]
    },
    "output": 3
})

tests.append({
    "input": {
        "array": [1]
    },
    "output": 0
})

tests.append({
    "input": {
        "array": [2, 1]
    },
    "output": 1
})

tests.append({
    "input": {
        "array": [1, 2, 3, 4, 5]
    },
    "output": 0
})

def get_number_of_rotations(array):
    if(len(array)<=1):
        return 0
    return array.index(min(array))

evaluate_test_cases(get_number_of_rotations, tests)