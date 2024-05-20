def knapsack (W, wt, val, n):
    
    # Base Case
    if n == 0 or W == 0:
        return 0
    
    # Weight of Item > Knapsack Capacity, W
    if wt[n-1] > W:
        return knapsack (W, wt, val, n-1)
    
    # Return the Maximum
    else: 
        return max(val[n-1] + knapsack (W-wt[n-1], wt, val, n-1), knapsack (W, wt, val, n-1))
    
    


W = 50
val = [120, 60, 100]
wt = [30, 10, 20]
n = len(val)

max_value = knapsack(W, wt, val, n)
print(max_value)
    




