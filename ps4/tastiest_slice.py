from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################
def prefix_sum(A):
       if A: return A.prefix_sum
       else: return 0 
class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):

    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################
        A.prefixsum=prefix_sum(A.left)+A.item.val
        if A.right:# aug left->root->right
            A.right.prefixsum=A.prefixsum+A.right.item.val
        #find prev in avl tree ?? how to compare key of coordinate #use conclusion from question 1
class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)
    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        ##################
        cur_node=self.root
        while cur_node:
            Part_B_Node.subtree_update(cur_node)
            if cur_node.prefixsum>s:
                s=cur_node.prefixsum
                k=cur_node.key
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    #define cmp for coordinate 
    for top in toppings:
        item=Key_Val_Item((top[0],top[1]),top[2])
        B.insert(item)
    k,s=B.max_prefix()
    return (k[0], k[1], s)
