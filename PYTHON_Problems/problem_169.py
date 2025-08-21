# Problem 169
# Given a dictionary mapping person->friends(list), find the person with the most mutual friends.
def most_mutual_friends(network: dict):
    max_person, max_count = None, -1
    for person, friends in network.items():
        mutuals = sum(1 for f in friends if person in network.get(f, []))
        if mutuals > max_count:
            max_person, max_count = person, mutuals
    return max_person

# Example
network = {
    "Ali": ["Sara", "John"],
    "Sara": ["Ali"],
    "John": ["Ali", "Sara"]
}
print(most_mutual_friends(network))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
