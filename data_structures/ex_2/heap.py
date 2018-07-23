def heapsort(arr):
  counter = 0
  empArr = []
  heapObj = Heap()

  # arr should be in self.storage
  # heapObj.size is increased by 1 per element of arr
  # divide by 2, round down to floor
  for item in arr:
    heapObj.insert(item)
  #print(heapObj.storage)
  
  for j in range(len(arr)):
  # heapObj.delete return a arr[i] with the highest value. This is retval
  #print(res)
    res = heapObj.delete()
    empArr.append(res)
    counter += 1
    #print(empArr)
  print(list(reversed(empArr)))
  answer = list(reversed(empArr))
  return answer
  

class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1