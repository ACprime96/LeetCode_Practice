# 1. Balanced Binary Tree
def isBalanced(root):
	def getDepth(root):
		if not root:
			return [True, 0] 
		
		left, right = getDepth(root.left), getDepth(root.right)
		
		balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
		
		return [balanced, 1 + max(left[1],right[1])]
	
	return getDepth(root)[0]

