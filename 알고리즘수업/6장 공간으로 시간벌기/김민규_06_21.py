def hash(k):
    return k%11

def linear_solve(data):
    M = len(data)
    table = [None] * M
    
    def lp_insert(k):
        id = hash(k)
        cnt = M
        while cnt > 0 and table[id] != None:
            print(f"conflict detected at index: {id}, data : {table[id]}")
            id = (id+1) % M
            cnt -= 1
        if cnt > 0:
            table[id] = k
            print(f"inserted at index: {id}")
        return
    for i in range(M):
        print(f"inserting, data : {data[i]}")
        lp_insert(data[i])
        print(*table)
    return table

def double_solve(data):
    M = len(data)
    table = [None] * M
    
    def dp_insert(k):
        id = hash(k)
        i = 0
        idx = id
        while i < M and table[idx] != None:
            print(f"conflict detected at index: {idx}, data : {table[idx]}")
            idx = (id + i*i) % M
            i+=1
        if i < M:
            table[idx] = k
            print(f"inserted at index: {idx}")
    for i in range(M):
        print(f"inserting, data : {data[i]}")
        dp_insert(data[i])
        print(*table)
    return table

def dhash_solve(data):
    M = len(data)
    table = [None] * M
    
    def d_hash(k):
        return 7-(k%7)

    def dh_insert(k):
        for i in range(M):
            id = (hash(k) + i*d_hash(k))%M
            if table[id] == None:
                table[id] = k
                print(f"inserted at index: {id}")
                print()
                return
            else:
                print(f"conflict detected at index: {id}, data : {table[id]}")

    for i in range(M):
        print(f"inserting data: {data[i]}")
        dh_insert(data[i])
        print(*table)
    return table

def chain_solve(data):
    M = len(data)
    table = [[] for _ in range(M)]
    
    def chain_insert(k):
        id = hash(k)
        if table[id]:
            print("conflict detected")
        table[id].append(k)
        print(f"inserted at index: {id}")
        print()
    for i in range(M):
        print(f"inserting data: {data[i]}")
        chain_insert(data[i])
    return table

data = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
# print(f"result : {linear_solve(data)}")
# print(f"result : {double_solve(data)}")
# print(f"result: {dhash_solve(data)}")
print(f"result: {chain_solve(data)}")
