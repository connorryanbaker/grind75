from typing import List

def coin_change(self, coins: List[int], amount: int) -> int:
    coins.sort()
    table = [ [float('inf')] * (amount + 1) for i in range(len(coins)) ]

    for i in range(len(table)):
        table[i][0] = 0

    for i in range(1, len(table[0])):
        if i % coins[0] == 0: 
            table[0][i] = i // coins[0]

    for i in range(1, len(coins)):
        coin = coins[i]
        for subamt in range(len(table[i])):
            if coin <= subamt:
                possible_values = [table[i][subamt - coin] + 1]
                for c in range(0, i):
                    v = table[c][subamt - coin]
                    if v < float('inf'):
                        possible_values.append(table[c][subamt - coin] + 1)
                table[i][subamt] = min(possible_values)
    num_coins = min([ row[-1] for row in table ])
    if num_coins < float('inf'):
        return num_coins
    return -1