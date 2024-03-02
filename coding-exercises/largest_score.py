def does_match(item, stack_top):
  if item == ")":
    return stack_top == "("
  if item == "]":
    return stack_top == "["
  if item == "}":
    return stack_top == "{"
  return False

def isBalanced(s):

  if not s:
    return True
  
  stack = []
  for item in s:
    if item in ["(", "[", "{"]:
      stack.append(item)
      continue
      
    if does_match(item, stack[-1]):
      stack.pop()
    else:
      return False
    
  return (not bool(stack))

print(isBalanced("{{[[(())]]}}"))