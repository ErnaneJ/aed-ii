from Node import Node

class AVLNode(Node):
    """
    Represents a node in an AVL (Adelson-Velsky and Landis) tree,
    which is a self-balancing binary search tree.

    Attributes:
        height (int): The height of the subtree rooted at this node,
                      initializes to 1 when the node is created.
        imbalance (int): The imbalance factor of this node, calculated
                         as the difference between the heights of the left
                         and right subtrees. Initializes to 0.

    Inherits from:
        Node: Inherits attributes and methods from the Node class.
    """

    def __init__(self, value):
        """
        Initializes an AVLNode with a given value.

        Args:
            value: The value to be stored in this node.
        """
        super().__init__(value)
        self.height = 1
        self.imbalance = 0

    def calculate_height_and_imbalance(self):
        """
        Calculates the height and imbalance factor of this node based
        on the heights of its left and right children.

        This method assumes that the heights of the children nodes (if they exist)
        are up-to-date.
        """
        # Calculate the height of the left child subtree
        left_height = 0
        if self.left_child is not None:
            left_height = self.left_child.height

        # Calculate the height of the right child subtree
        right_height = 0
        if self.right_child is not None:
            right_height = self.right_child.height

        # Update the height of this node
        self.height = 1 + max(left_height, right_height)

        # Calculate and update the imbalance factor for this node
        self.imbalance = left_height - right_height