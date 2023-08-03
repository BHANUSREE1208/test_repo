def find_pairs_with_sum(lst, N):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == N:
                print("(", lst[i], ",", lst[j], ")")
                
l = [4, 3, 6, 8, 2, 9, 7, 5]
N = 10
find_pairs_with_sum(l, N)




def print_number_pattern(n):
    for i in range(n, 5, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()

n = 10

print_number_pattern(n)




def merge_sorted_lists(l1, l2):
    merged = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    while i < len(l1):
        merged.append(l1[i])
        i += 1

    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged

l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = merge_sorted_lists(l1, l2)
print(output)







def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

lst = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
sort_list(lst)
print(lst)

