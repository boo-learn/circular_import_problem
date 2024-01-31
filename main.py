from module import Apple, AppleTree


tree = AppleTree(10)
print(tree.get_apple(3))

new_apple = Apple("green")
print(new_apple)
tree.add_apple(new_apple)
print(new_apple)