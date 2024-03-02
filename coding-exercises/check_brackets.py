# python3

#Bracket = namedtuple("Bracket", ["char", "position"])
class Bracket(object):
    def __init__(self, char, position):
        self.char = char
        self.position = position

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if opening_brackets_stack:
                openening_char = opening_brackets_stack.pop()
                if not are_matching(openening_char.char, next):
                    return i + 1
            else:
                return i + 1

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[-1].position


def main():
    text = input()
    mismatch = find_mismatch(text)

    print(mismatch)

def unit_tests():
    print(find_mismatch(""))
    print(find_mismatch("]"))
    print(find_mismatch("]]"))
    print(find_mismatch("[]]"))
    print(find_mismatch("[]"))
    print(find_mismatch("{}[]"))
    print(find_mismatch("[()]"))
    print(find_mismatch("(())"))
    print(find_mismatch("{[]}()"))
    print(find_mismatch("{"))
    print(find_mismatch("{[}"))
    print(find_mismatch("foo(bar);"))
    print(find_mismatch("foo(bar[i);"))


if __name__ == "__main__":
    main()
    #unit_tests()
