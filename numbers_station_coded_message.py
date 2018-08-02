def answer(broadcast_nums, broadcast_key):
    if broadcast_key:
        for i in range(len(broadcast_nums)):
            for j in range(i, len(broadcast_nums)):
                s = sum(broadcast_nums[i:j+1])
                if s == broadcast_key:
                    return [i, j]
                elif s < broadcast_key:
                    continue
                elif s > broadcast_key:
                    break
    return [-1, -1]


assert answer([4, 3, 10, 2, 8], 12) == [2, 3]
assert answer([1, 2, 3, 4], 15) == [-1, -1]
assert answer([5, 1, 1, 1, 5], 5) == [-1, -1]
