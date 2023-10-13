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
def max_prefix_key(A):
       if A: return A.max_prefix_key
       else: return None
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
        A.max_prefix=max(max_prefix(A.left),sum(A.left)+A.item.val,sum(A.left)+A.item.val+max_prefix(A.right))
        if A.max_prefix==max_prefix(A.left):
            A.max_prefix_key=max_prefix_key(A.left)
        elif A.max_prefix==sum(A.left)+A.item.val:
            A.max_prefix_key=A.item.key
        else: A.max_prefix_key=max_prefix_key(A.right)
        if not A.max_prefix_key:
             A.max_prefix_key=A.item.key
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
        B.insert(Key_Val_Item(topping[1],topping[2]))
        if B.max_prefix()[1]>T:
             Y,T=B.max_prefix()
    for top in toppings:
         if top[1]==Y:
              return (top[0],top[1],T)
        
