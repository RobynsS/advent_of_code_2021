import numpy as np


class Grid:
    def __init__(self, data):
        self.numbers = np.array(data)
        self.marks = np.zeros(self.numbers.shape)
        self.complete = False

    def update(self, number):
        # Only update if the grid was not complete yet
        if not self.complete:
            # Find number on grid
            pos = np.where(self.numbers == number)

            # If number found, update marks
            for index in range(len(pos[0])):
                self.marks[pos[0][index], pos[1][index]] = 1

            # Check if grid is complete
            if self.is_complete():
                self.complete = True
                return True

        return False

    def is_complete(self):
        for row in self.marks:
            if sum(row) == 5:
                return True
        for col in self.marks.T:
            if sum(col) == 5:
                return True

        return False

    def get_unmarked_sum(self):
        # Keep only the unmarked elements
        unmarked_els = np.multiply(1 - self.marks, self.numbers)

        # Sum all elements
        return np.sum(unmarked_els)
