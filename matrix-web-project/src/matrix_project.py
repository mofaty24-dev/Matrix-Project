class MatrixProject:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def set_dimensions(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_matrix_elements(self, elements):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = elements[i][j]

    def display_matrix(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def verify_matrix(self, user_input):
        return user_input.lower() == "yes"

    def edit_element(self, i, j, new_value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = new_value
            return True
        return False

    def first_element_check(self):
        if self.matrix and self.matrix[0]:
            if self.matrix[0][0] == 0:
                return self.swap_rows()
        return "The first element isn't equal to zero, so we will skip to step 4."

    def swap_rows(self):
        for r in range(1, self.rows):
            if self.matrix[r][0] != 0:
                self.matrix[0], self.matrix[r] = self.matrix[r], self.matrix[0]
                return f"First row swapped successfully with row number {r + 1}."
        return "No suitable row found to swap with the first row."