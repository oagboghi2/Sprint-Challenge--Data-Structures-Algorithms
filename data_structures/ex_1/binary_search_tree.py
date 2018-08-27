class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def breadth_first_for_each(self, cb):
    queue = []
    queue.append(self)
    while len(queue):
      current_node = queue.pop(0)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)
      cb(current_node.value)

  def depth_first_for_each(self, cb):
    arr = []
    arr.append(self)
    while len(arr):
      current_node = arr.pop()
      if current_node.right:
        arr.append(current_node.right)
      if current_node.left:
        arr.append(current_node.left)
      cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
