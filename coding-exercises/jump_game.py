def jump_game(hops):
    n = len(hops)
    safe_hop = n - 1
    for i in range(n-2,-1,-1):
        if i + hops[i] >= safe_hop:
            safe_hop = i

    return not safe_hop

good = [2,3,1,1,4]
bad = [3,2,1,0,4]

print(jump_game([1,0]))
