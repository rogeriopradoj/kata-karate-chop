class Chop(object):
    @staticmethod
    def chop(search, array):
        for (index, item) in enumerate(array):
            if item == search:
                return index

        return -1
