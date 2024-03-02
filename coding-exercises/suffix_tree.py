# python3
import sys

class Node(object):
  def __init__(self):
    self.children = {}
    self.begin = -1
    self.length = 0

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  text_len = len(text)
  tree = Node()
  for i in range(text_len):
    current_node = tree
    for j in range(i, text_len):

      if text[j] in current_node.children:
        parent = current_node #cba parent
        current_node = current_node.children[text[j]] # cba
        if current_node.begin >= 0:
          # now ba
          current_node.begin += 1
          current_node.length -= 1

          branch_node = Node() #c
          branch_node.children[text[current_node.begin]] = current_node #ba
          parent.children[text[j]] = branch_node # c points to C internal node

          current_node = branch_node

      else:
        node = Node()
        node.begin = j
        node.length = text_len - j
        current_node.children[text[j]] = node
        break

  result = []
  traversal_stack = [(None, tree)]
  while traversal_stack:
    hash_key, current_node = traversal_stack.pop()
    if current_node.begin >= 0:
      result.append(text[current_node.begin:current_node.begin+current_node.length])
    else:
      if hash_key is not None:
        node_str = hash_key
        while len(current_node.children) == 1:
          for key, node in current_node.children.items():
            node_str += key
            current_node = node

        result.append(node_str)
        
    for key, node in current_node.children.items():
      traversal_stack.append((key, node))


  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))