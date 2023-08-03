def find_pairs_with_sum(lst, N):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == N:
                print("(", lst[i], ",", lst[j], ")")
                
l = [4, 3, 6, 8, 2, 9, 7, 5]
N = 10
find_pairs_with_sum(l, N)
