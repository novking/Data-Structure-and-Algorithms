# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    for i in reversed(range(len(self._data))):
        while self._data[int((i-1)/2)] > self._data[i]:
            parent = self._data[int((i-1)/2)]
            p = int((i-1)/2)
            child = self._data[i]
            c = i
       
            self._swaps.append([p,c])
            self._data[int((i-1)/2)] = child
            self._data[i] = parent
            i = int((i-1)/2)
               
        

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()
    
if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
