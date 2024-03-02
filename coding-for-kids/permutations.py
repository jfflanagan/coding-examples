def getPermsWithRep(chars, permLength=None, prefix=''):
    if permLength is None:
        permLength = len(chars)
    
    if permLength == 0:
        return [prefix]
    
    results = []
    for char in chars:
        newPrefix = prefix + char

        results.extend(getPermsWithRep(chars, permLength-1, newPrefix))

    return results

def getPermsWithRep2(results, chars, stack, i, n):

    if i == n:
        return results.append(''.join(stack))
    
    for char in chars:
        stack.append(char)
        getPermsWithRep2(results, chars, stack, i + 1, n)
        stack.pop()

    return results

results = []
stack = []
#print(getPermsWithRep2(results, 'ABC', stack, 0, 2))
#print(getPermsWithRep('ABC',2))


def getPerms(results, mySet, i, n):
    if i == n - 1:
        # deep copy
        results.append("".join(mySet))
        return

    for j in range(i, n):
        # swap
        temp = mySet[i]
        mySet[i] = mySet[j]
        mySet[j] = temp

        getPerms(results, mySet, i + 1, n)

        # swap back
        temp = mySet[i]
        mySet[i] = mySet[j]
        mySet[j] = temp

    return results

def getCombs(results, mySet, stack, i, l, k, n):
    if l == k:
        results.append(''.join(stack))
        return

    for j in range(i, n):
        stack.append(mySet[j])
        getCombs(results, mySet, stack, j + 1, l + 1, k, n)
        stack.pop()


    return results

#chars = ['A', 'B', 'C']
#results = []
#stack = []
#print(getPerms(results, chars, 0, len(chars)))
#print(getCombs(results, chars, stack, 0, 0, 2, len(chars)))

def getBalancedParens(results, stack, openLeft, closingLeft):
    if openLeft == 0 and closingLeft == 0:
        results.append("".join(stack))

    if openLeft > 0:
        stack.append('(')
        getBalancedParens(results, stack, openLeft - 1, closingLeft)
        stack.pop()
    if closingLeft - openLeft > 0:
        stack.append(')')
        getBalancedParens(results, stack, openLeft, closingLeft - 1)
        stack.pop()

results = []
stack = []
getBalancedParens(results, stack, 3, 3)
print(results)


