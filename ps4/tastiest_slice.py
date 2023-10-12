from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################
def sum(A):
       if A: return A.sum
       else: return 0 
def max_prefix(A):
       if A:return A.max_prefix
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
        A.sum=sum(A.left)+A.item.val+sum(A.right)
        A.max_prefix=max(sum(A.left),sum(A.left)+A.item.val,sum(A.left)+A.item.val+max_prefix(A.right))
        if A.max_prefix==sum(A.left):
            max_prefix_key=A.left.item.key
        elif A.max_prefix==sum(A.left)+A.item.val:
            max_prefix_key=A.item.key
        else: max_prefix_key=A.right.item.key
        if max_prefix_key: A.max_prefix_key=max_prefix_key
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
        return (self.root.max_prefix_key, self.root.max_prefix)
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
    sorted_topping=sorted(toppings,key=lambda topping:topping[0]) #sort by x
    for topping in sorted_topping:
        B.insert(Key_Val_Item(topping[0],topping[1]))
    return B.max_prefix()
