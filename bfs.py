def bfs(root):
	queue = [root]
	result = []
	while queue:
        #run while the queue is not empty
        node = queue.pop(0)
        result.append(node.val)
        #add the children to queue in the order they come
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
		
def bfs_with_levels(root):
    result = []
    queue =[root]
    #iterate while queue is not empty
    while queue:
        #get the number of elements at a particular level
        level_size = len(queue)
        current_level = []
        #now we'll go through all the nodes at this level and dequeue them on my one
        #While dequeeing them will save their value in our result and add their child nodes
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left is not None:
                queue.add(node.left)
            if node.right is not None:
                queue.add(node.right)
        result.append(result_level)
    return result


def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    queue =[root]
    result = []
    l=True # when l is true all the elements at level will be displayed in the order in which they were added, if it is false tey will be dispalyed in the reverse order
    while queue:
        #we iterate till the time queue is not empty
        #nuber of nodes at this each_level
        n = len(queue)
        current_level = []
        for _ in range(n)
            #visit all the nodesin the current level and add their children to the queue
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        #now lets get the direction concept
        
        
        if l==False:
                current_level=current_level[::-1]
          #ad the traversal of the current level to the result
          result.append(current_level)
            