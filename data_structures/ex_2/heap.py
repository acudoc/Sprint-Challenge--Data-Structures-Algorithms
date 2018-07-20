def heapsort(arr):
  length = len(aList) - 1
  leastParent = length / 2
  for i in range (leastParent, -1, -1):
    moveDown(aList, i, length)

  for i in range (length, 0, -1):
    if aList[0] > aList[i]:
      swap(aList, 0, i)
      moveDown(aList, 0, i - 1)

def moveDown(aList, first, last):
  largest = 2 * first + 1
  while largest <= last:

    if (largest < last) and (aList[largest] < aList[largest + 1] ):
      largest += 1

    if aList[largest] > aList[first]:
      swap(aList, largest, first)
      first = largest;
      largest = 2 * first + 1
    else:
      return

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
