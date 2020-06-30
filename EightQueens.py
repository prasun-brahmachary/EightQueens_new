
__author__ = '432849'

#Single Solution for Eight Queens Puzzle
class EightQueens:

    def __init__(self, size):
        # Initialize
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):

        positions = [-1] * self.size
        self.put_queen(positions, 0)


    def put_queen(self, positions, target_row):

        # Stop when u get the first Solution
        if(self.solutions == 1):
            return
        if target_row == self.size:
            self.show_matrix(positions)
            self.solutions += 1
        else:
            # Check Feasiblity
            for column in range(self.size):
                # Reject
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, ocuppied_rows, column):
        """
        Is the given position under attack
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_matrix(self, positions):
        #Print Queen Matrix
        QueenMatrix=[]
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    QueenMatrix.append(column+1)

        print(QueenMatrix)


def main(nmbr):
        # initiate
        EightQueens(8)

if __name__ == "__main__":

         main(8)
