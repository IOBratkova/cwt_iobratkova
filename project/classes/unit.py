class Unit():
    def __init__(self, id, t, d):
        self.id = id
        self.title = t
        self.descr = d

    def __eq__(self, other):
        return other.title == self.title and other.descr == self.descr

