from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for itemm in range(size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code
  
  def compress(self, hash_code):
    array_index = hash_code % self.array_size
    return array_index

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    # self.array[array_index] = [key, value]
    payload = Node([key, value])
    list_at_array = self.array[array_index]

    for item in list_at_array:
      if item[0] == payload.get_value()[0]:
        item[1] = value
        return
    list_at_array.insert(payload)
      

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None

  

blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assign(element[0], element[1])

# blossom.assign('snapdragon', 'flavor')
# for List in blossom.array:
#   for ele in List:
#     print(blossom.array.index(List), ele)
#   print()

print(blossom.retrieve('daisy'))
