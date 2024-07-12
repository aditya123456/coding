

def money_change(money, coins):
    if money == 0 :
        return 0
    minnunmber = 9999999
    for i in range(len(coins)):
        if money > coins[i]:
            coins_required = money_change(money-coins[i], coins)
            if minnunmber > coins_required + 1:
                minnunmber = coins_required
    return minnunmber


def min_coins(coins, target):
    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (target + 1)

    # Base case: 0 coins needed for 0 amount
    dp[0] = 0

    # Iterate over all amounts from 1 to the target
    for amount in range(1, target + 1):
        # Iterate over all coin denominations
        for coin in coins:
            # If the current coin is less than or equal to the current amount
            if coin <= amount:
                print(coin, amount)
                # Update the minimum number of coins needed for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                print(dp)
            # print(dp)

    # If dp[target] is still infinity, no combination of coins was found
    if dp[target] == float('inf'):
        return -1
    else:
        return dp[target]


# Example usage:
coins = [1, 2, 5]
target = 11
result = min_coins(coins, target)

if result != -1:
    print(f"Minimum number of coins needed to make {target} is: {result}")
else:
    print("No combination of coins can make the target amount.")
