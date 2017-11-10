
class Unique:
    data = []
    used = []
    i = 0
    ignore_case = False

    def __init__(self, data, ignore_case=False):
        self.data = [x for x in data]
        self.ignore_case = ignore_case

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration

        if isinstance(self.data[self.i], str) and self.ignore_case:
            if self.data[self.i].lower() in self.used:
                while (self.data[self.i].lower()) in self.used:
                    self.i += 1
                    if self.i >= len(self.data):
                        raise StopIteration
                self.used.append(self.data[self.i])
                self.i += 1
                return self.data[self.i - 1]
            else:
                self.used.append(self.data[self.i].lower())
                self.i += 1
                return self.data[self.i - 1]
        else:
            if self.data[self.i] in self.used:
                while (self.data[self.i]) in self.used:
                    self.i += 1
                    if self.i >= len(self.data):
                        raise StopIteration
                self.used.append(self.data[self.i])
                self.i += 1
                return self.data[self.i - 1]
            else:
                self.used.append(self.data[self.i])
                self.i += 1
                return self.data[self.i - 1]


    def __iter__(self):
        return self
