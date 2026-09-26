#Provide pseudocode for a function that traverses all nodes in a binary tree. Hint:
#The two recursive algorithms from the lecture both use recursion to visit all the
#nodes in a binary tree.

#pre-order
# traverse(u)
#   if u is None then
#     return
#   print(u.key)
#   traverse(u.left)
#   traverse(u.right)


#in-order
# traverse(u)
#   if u is None then
#     return
#   traverse(u.left)
#   print(u.key)
#   traverse(u.right)


#post-order
# traverse(u)
#   if u is None then
#     return
#   traverse(u.left)
#   traverse(u.right)
#   print(u.key)
