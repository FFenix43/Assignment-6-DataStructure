class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    # Delete this line and implement the class below
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("The team tree is empty.")
            return False

        if current_node is None:
            current_node = self.root

        # Base case: Found the target manager node
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"{employee_name} added as LEFT subordinate of {manager_name}.")
                    return True
                else:
                    print(f"{manager_name} already has a LEFT subordinate.")
                    return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added as RIGHT subordinate of {manager_name}.")
                    return True
                else:
                    print(f"{manager_name} already has a RIGHT subordinate.")
                    return False

        # Recursive case: Traverses subtrees to find the manager
        added = False
        if current_node.left:
            added = self.insert(manager_name, employee_name, side, current_node.left)

        if not added and current_node.right:
            added = self.insert(manager_name, employee_name, side, current_node.right)

        if not added and current_node == self.root:
            print(f"Manager '{manager_name}' not found in the team tree.")

        return added
        


    
    def print_tree(self, node=None, level=0):     
        if node is None:
            if level == 0:
                if self.root is None:
                    print("The team tree is empty.")
                    return
                node = self.root

        if node is not None:
            indent = "  " * level
            print(f"{indent}- {node.name}")
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)
    
                
            
        


# Test your code here
'''employee1 = EmployeeNode("Alice")
print(employee1.name)  # Should print "Alice"
print(employee1.left)  # Should print None
print(employee1.right)  # Should print None


company_directory = TeamTree()
print(company_directory.root)  # Should print None since the tree is empty

company_directory = TeamTree()
company_directory.root = EmployeeNode("Jordan")
company_directory.insert("Jordan", "Taylor", "right")
company_directory.insert("Jordan", "Riley", "left")
company_directory.insert("Riley", "Dana", "right")
company_directory.insert("Riley", "Morgan", "left")


company_directory.print_tree()


'''






# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


company_directory()


'''

Recursive insertion works by breaking down the search for the user into smaller pieces of information. Starting at the root node, the insert function first checks whether the current node matches the target value of the manager's name. If there is a match, the new employee is assigned to either the left or the right of the manager’s name. But if another employee is already occupying the spot, the system flags the user, indicating that the manager already has a subordinate on that side of the network.

The main challenge faced for this project was finding the right sport for a new employee, since it was managing the traversal state across recursive steps. Since the manager could’ve been located anywhere on the tree, ensuring that the code checks both left and right efficiently.

The structure of trees might be preferable when a hierarchical structure is needed for the data or when the algorithm requires efficient search or organization. For example, organizational charts, file directories, and decision trees. 



'''