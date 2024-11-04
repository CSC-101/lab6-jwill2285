import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        input1 = [data.Book(["Dorthy"],"Good Book"),data.Book(["Bob"],"Better Book")]
        result = lab6.selection_sort_books(input1)
        expected = [data.Book(["Bob"],"Better Book"), data.Book(["Dorthy"],"Good Book"),]
        self.assertEqual(expected,result)
    def test_selection_sort_books_2(self):
        input1 = []
        result = lab6.selection_sort_books(input1)
        expected = None
        self.assertEqual(expected,result)
    # Part 2
    def test_swap_case(self):
        input1 = "aRE THESE CORRECT? idk!"
        result = lab6.swap_case(input1)
        expected = "Are these correct? IDK!"
        self.assertEqual(expected,result)
    def test_swap_case_2(self):
        input1 = "δ tEST IF NON ENGL"
        result = lab6.swap_case(input1)
        expected = "Δ Test if non engl"
        self.assertEqual(expected,result)
    # Part 3
    def test_str_translate(self):
        input1 = "Change Characters"
        input2 = "C"
        input3 = "Z"
        result = lab6.str_translate(input1,input2,input3)
        expected = "Zhange Zharazters"
        self.assertEqual(expected,result)
    def test_str_translate_2(self):
        input1 = "Testing for lots of T's"
        input2 = "t"
        input3 = "B"
        result = lab6.str_translate(input1,input2,input3)
        expected = "Besbing for lobs of B's"
        self.assertEqual(expected,result)
    # Part 4
    def test_histogram(self):
        input1 = "many of same words that are many of words many"
        result = lab6.histogram(input1)
        expected = {"many":3,"of":2,"same":1,"words":2,"that":1,"are":1}
        self.assertEqual(expected,result)
    def test_histogram_2(self):
        input1 = "lots of same words but not lots of lots"
        result = lab6.histogram(input1)
        expected = {"lots":3,"of":2,"same":1,"words":1,"but":1,"not":1}
        self.assertEqual(expected,result)






if __name__ == '__main__':
    unittest.main()
