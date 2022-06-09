"""Implement quick sort.
Input a list.
Output a sorted list."""


class QuickSort(object):
    def __init__(self, array):
        self.array = array

    def quicksort(self):
        return self.sort(0, len(self.array) - 1)

    def sort(self, start, end):
        if start > end:
            return

        p = self.partition(start, end)

        self.sort(start, p - 1)
        self.sort(p + 1, end)

        return self.array

    def partition(self, start, end):
        left = start
        p = end

        while left != p:

            value = self.array[left]

            if value <= self.array[p]:
                left += 1
                continue

            self.array[left] = self.array[p - 1]
            self.array[p - 1] = self.array[p]
            self.array[p] = value
            p -= 1

        return p


