
def is_round_robin(t1, t2):
    for i in range(len(t1)):
        if not t1[i] == t2[(i + 1) % len(t1)]:
            return False
    return True

print(is_round_robin('cdab', 'bcda'))
    