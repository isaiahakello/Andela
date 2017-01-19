class BinarySearch(list):
    def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(b, (b * a) + 1, b))

        self.list_built = range(b, (b * a) + 1, b)
        self.length = len(self.list_built)
        self.count = 0
        self.iter_num = dict()

    def search(self, search_term):
        list_built = [] + self.list_built

        while self.length > 0:
            self.count += 1
            mid = self.length / 2

            if search_term == list_built[mid]:
                self.iter_num['count'] = self.count
                self.iter_num['index'] = self.list_built.index(search_term)
                return self.iter_num
            elif search_term < list_built[mid]:
                list_built[mid:] = []
            elif search_term > list_built[mid]:
                list_built[:mid + 1] = []

self.length = mid
