   from email import generator


def __iter__(self):
        return self.data

    def __next__(self):
        count = 0
        if count <= len(self.data):
            for key in self.data:
                count += 1
                yield self.data[key]

        raise StopIteration

    def iterator(self):

        if ((len(self.data) - self.page*self.N) // self.N) != 0:
            self.page += 1
            for _ in range(self.N):
                print(self.__next__())

            return f'Page {self.page}'

        elif ((len(self.data) - self.page*self.N) // self.N) == 0:
            print(len(self.data) - self.page*self.N)
            for _ in range(len(self.data) - self.page*self.N):
                print(next(self))
            self.page = 0
            return f'It was last page'

    def iterator(self):
        for _, value in self.data.items():
            yield value


    def __iter__(self):
        return self.data

    def __next__(self):
        count = 0
        if count <= len(self.data):
            for value in self.data.values:
                count += 1
                return value

        raise StopIteration


def show_pages(*args):

    if ((len(CONTACTS) - CONTACTS.page*CONTACTS.N) // CONTACTS.N) != 0:
        CONTACTS.page += 1

        for _ in range(CONTACTS.N):
            print(next(generator))

        return f'Page {CONTACTS.page}'

    elif ((len(CONTACTS) - CONTACTS.page*CONTACTS.N) // CONTACTS.N) == 0:
        for _ in range(len(CONTACTS) - CONTACTS.page*CONTACTS.N):
            print(next(generator))

        CONTACTS.page = 0

        return f'It was last page'


    def iterator(self):
        records = []

        for record in self.data.values():

            if len(records) >= self.N:
                yield records
                records = []

            records.append(record)

        if records:
            yield records
