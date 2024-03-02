code_line = "{myfunction{arg1}}"

bracket_counter = 0
for c in code_line:
    if c == "{":
        bracket_counter += 1
    if c == "}":
        bracket_counter -= 1

print(bracket_counter)
