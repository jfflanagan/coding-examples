
def days_to_target(apps, target):
    days = 1
    users = [apps]
    while sum(users[-1]) < target:
        users.append([i**2 for i in users[-1]])
        days *= 2

    if len(users) == 1:
        return 1

    x = users[-2]
    days /= 2
    for i in range(len(users) - 3, -1, -1):
        test = [x[j]*users[i][j] for j in range(len(x))]
        if sum(test) < target:
            x = test
            days += 2**i

    return days + 1

users = [1.1,1.2,1.3]
users = [1.01,1.02]
print(days_to_target(users, 1e9))