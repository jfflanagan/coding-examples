# python3
import sys

class Node(object):
	def __init__(self):
		self.children = {}

def solve(text, n, patterns):
	result = []
	trie = Node()

    # Make Trie
	for pattern in patterns:
		current_node = trie
		for c in pattern:
			if c in current_node.children:
				current_node = current_node.children[c]
			else:
				current_node.children[c] = Node() # make a new node
				current_node = current_node.children[c] # update the current node

    # FInd patterns
	for i in range(len(text)):
		current_node = trie
		for j in range(len(text) - i):
			if text[i+j] in current_node.children:
				current_node = current_node.children[text[i+j]]
			else:
				break
			if not current_node.children:
				result.append(i)
				break
				
	return result

text = sys.stdin.readline().strip()
n = int (sys.stdin.readline().strip())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline().strip()]

ans = solve (text, n, patterns)

sys.stdout.write(' '.join (map (str, ans)) + '\n')
