T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    input_string = input()

    window = N // 4
    nums= set([])

    for _ in range(N - 1):
        for idx in range(4):
            nums.add(int(input_string[idx * window : (idx + 1) * window], base = 16))
        input_string = input_string[-1] + input_string[:-1]
    
    print(f"#{test_case} {sorted(nums, reverse = True)[K - 1]}")