class SparseArray:
    def __init__(self):
        self.sparse_array = {}

    def __setitem__(self, index, value):
        self.sparse_array[index] = value

    def __getitem__(self, index):
        return self.sparse_array.get(index, 0)


arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))