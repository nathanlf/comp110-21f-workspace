"""Drawing forests in a loop."""

__author__ = "730483098"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
tree_string: str = ""
depth: int = int(input("Depth: "))
i: int = 0

while i < depth:
    tree_string += TREE
    print(tree_string)
    i += 1