def can_achieve_score(hp, m, pumpkins, required_score):
    mhp = [[0] * (hp + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        p_hp, p_poins = pumpkins[i - 1]
        for j in range(hp + 1):
            if j >= p_hp:
                mhp[i][j] = max(mhp[i - 1][j], mhp[i - 1][j - p_hp] + p_poins)
            else:
                mhp[i][j] = mhp[i - 1][j]

    return mhp[m][hp] >= required_score


def min_hp_to_score(n, m, pumpkins):
    for i in range(m):
        p_hp = pumpkins[i]
        if p_hp >= 200:
            pumpkins[i] = (p_hp, 3)
        elif p_hp >= 100:
            pumpkins[i] = (p_hp, 2) 
        else:
            pumpkins[i] = (p_hp, 1) 

    left, right = 0, sum(i for i, j in pumpkins)
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if can_achieve_score(mid, m, pumpkins, n):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


n, m = [int(x) for x in input().split()]
pumpkins = [int(x) for x in input().split()]
print(min_hp_to_score(n, m, pumpkins))
