def solve(W, wt, val):
    '''
    W = 배낭의 무게
    wt = 물건의 무게(리스트)
    val = 물건의 가치(리스트)
    n = 물건의 개수
    '''
    n = len(wt)
    A = [[0 for x in range(W+1)] for x in range(n+1)]
    # K[i][w] = i개의 물건을 고려하고, 배낭의 무게가 w일 때의 최대 가치
    # 0으로 초기화된 2차원 리스트를 생성한다.
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > W: # 용량을 초과하는 경우
                A[i][w] = A[i-1][w]
            else: # 배낭에 넣을 수 있을 때=
                valWith = val[i-1] + A[i-1][w-wt[i-1]] # 넣는 경우
                if w-wt[i-1] < 0: # 넣으려고 시도할 때, 무게 초과
                    valWith = 0
                valWithout = A[i-1][w] # 안 넣는 경우
                A[i][w] = max(valWith, valWithout) # 더 큰 값 선택
    return A

import time
import random
import numpy as np
import matplotlib.pyplot as plt

# 테스트 케이스 생성 함수
def make_testcase(testcase=100, testset=100, randrange=(1, 1000)):
    cases = []
    for i in range(testcase):
        weight = []
        value = []
        for j in range(testset):
            weight.append(random.randint(*randrange))
            value.append(random.randint(*randrange))
        capacity = random.randint(*randrange)
        cases.append([weight, value, capacity])
    return cases


# 평균 실행 시간 측정 함수
def measure_time(size=100):
    times = []
    cases = make_testcase(size)
    for weights, values, capacity in cases:
        start_time = time.time()
        solve(capacity, weights, values)  # 블랙박스 알고리즘 실행
        end_time = time.time()
        times.append(end_time - start_time)  # 실행 시간 계산
    max_time = np.max(times)  # 최대 시간 계산
    average_time = np.mean(times)  # 평균 시간 계산
    min_time = np.min(times)  # 최소 시간 계산
    return average_time, min_time, max_time

# 평균 시간 리스트 생성 및 가시화
def visualize_execution_times(sizes = [10, 50, 100, 500, 1000] ): # 테스트 케이스 크기 목록
    
    average_times, min_times, max_times = [], [], []

    # 각 크기별로 평균 시간 측정
    for size in sizes:
        avg_time, min_time, max_time = measure_time(size)
        average_times.append(avg_time)
        min_times.append(min_time)
        max_times.append(max_time)
        print(f"테스트 케이스 크기 {size}일 때 평균 실행 시간: {avg_time:.6f}초")

    # Matplotlib을 사용하여 가시화
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, min_times, marker='o', linestyle='-', color='g', label='minimum execution time')
    plt.plot(sizes, average_times, marker='o', linestyle='-', color='b', label='average execution time')
    plt.plot(sizes, max_times, marker='o', linestyle='-', color='r', label='maximum execution time')
    plt.title(f"each testcase size's excution time", fontsize=14)
    plt.xlabel('test case size', fontsize=12)
    plt.ylabel(f'excution time (sec)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

# 실행
if __name__ == "__main__":
    visualize_execution_times()
