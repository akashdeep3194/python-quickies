# python-quickies
* ## Basic Python Functions

  * ### *tree_quick_functions.py*
    ```
    class BinaryTreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    ```
    *Common Binary Tree Functions:*
    
    * **Ways to print Trees:**
      * Print Pre Order Traversal of a Binary tree
      * Print In Order Traversal of a Binary tree
      * Print Post Order Traversal of a Binary tree
      * Print Level Wise Tree Traversal of a Binary tree
 
    * **Take Level Wise Input in a Binary Tree (-1 denotes no child)**  
    * **Find the Lowest Common Ancestor between two nodes of a Binary Tree Node**


  * ### *subsequences.py*
    This function takes an array as an argument and returns another array that has all the subsequences possible
  
    ###Example:
      * ####Input string = "asd"
      * ####Output array = ['', 'd', 's', 'sd', 'a', 'ad', 'as', 'asd']
    
* ## Basic Algorithms

  * ### *01 Knapsack:*

  * **Given the following problem:**
    * A Knapsack of given capacity (W)
    * An array of value of items
    * An array of weight of items
    * Return the maximum sum of values of the items that can be held in the Knapsack at a time
