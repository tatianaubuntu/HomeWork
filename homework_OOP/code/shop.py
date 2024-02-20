class Shop:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        if self.current + 1 < len(self.category.products):
            result = self.category.products[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration
