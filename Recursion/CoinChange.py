# PROBLEM : Given a target amount n and a list (array) of distinct coin values, 
# what's the fewest coins needed to make the change amount.

def coinChangeRecursively(target,coins):
    # Defining min_coins for our answer and return and assigning target value to min_coins
    min_coins=target
    if target in coins:
        return 1
    # Looping over every coins value less than target.
    for i in [c for c in coins if c<=target ]:
        # And counting the how many coins need for change
        num_coins = 1 + coinChangeRecursively(target-i,coins)
        # And if num_coins less than min_coins, assigning to min_coins
        if num_coins< min_coins:
            min_coins=num_coins
    return min_coins

print(coinChangeRecursively(50,[1,5,10,25]))




# Dynamicly Solution
def coinChangeDynamicly(target,coins,known_results):
    min_coins=target

    if target in coins:
        return 1
    # With this line if value cached (saved in memory)returning directly
    elif known_results[target]>0:
        return known_results[target]

    else:    
        for i in [c for c in coins if c<=target ]:
               # Recursive call for number of coins for change.
               num_coins = 1 + coinChangeDynamicly(target-i,coins,known_results)
      
               if num_coins< min_coins:
                    min_coins=num_coins

                    # Saving the known_result for other values.(No need to search and find value for same values.)
                    known_results[target]=min_coins
    return min_coins

target=74
coins=[1,5,10,25]
known_results = [0] * (target+1)
print(known_results)

print(coinChangeDynamicly(target,coins,known_results))