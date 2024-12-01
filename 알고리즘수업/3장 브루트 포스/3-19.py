# implementation of job assign ment problem's brute force algorithm

def permutation(arr, n): # arr is used to store unadded elements or input values...
    # recursive implementation of permutation
    result = []
    if n > len(arr):
        return 
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        # hard to understand it...
        for i in range(len(arr)):
            temp = [i for i in arr] # copy the list..
            temp.remove(arr[i]) # remove the element sequentially and recursively call the function
            for p in permutation(temp, n-1):
                result.append([arr[i]] + p) # add the removed element to the result...
    return result

def solve(tasks):
    length = len(tasks)
    taskorders = permutation([i for i in range(length)], length)
    best_cost = float('inf')
    for taskorder in taskorders:
        cost = 0
        for i in range(length):
            cost += tasks[i][taskorder[i]]
        best_cost = min(best_cost, cost)
    return best_cost
            

# input values
inputs = [[9, 2, 6, 8],
          [6, 4, 3, 7],
          [5, 7, 1, 9],
          [7, 6, 8, 4]]

print(solve(inputs))