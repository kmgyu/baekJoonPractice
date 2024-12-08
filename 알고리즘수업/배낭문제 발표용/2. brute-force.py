# implementation of kanpsack problem's brute force algorithm

def solve(weight, value, capacity):
    n = len(weight)
    best_value = 0
    
    for i in range(1, 2**n):
        # There are 2^n cases to put in or not, so it can be expressed in bits.
        # 0 is useless
        current_weight = 0
        current_value = 0
        for j in range(n):
            if (i >> j) & 1: # bit shift technic
                # index j is bit I want to check(also current index of weight and value)
                # if shift move to right, & operate with 1 means that the bit is 1 (there is a bit!)
                current_weight += weight[j]
                current_value += value[j]
        
        if current_weight > capacity: continue
        if best_value < current_value: best_value = current_value
    return best_value

# input values
weight = [10, 20, 30]
value = [60, 100, 120]
capacity = 50
# all... you can use like this
# inputs = [(1, 1), (3, 4), (4, 5), (5, 7)]

result = solve(weight, value, capacity)
print(result)