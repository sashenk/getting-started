'''Getting Started (Assignment #0)

Please add your code where indicated. You may conduct a superficial test of
your code by executing this file in a python interpreter.

'''

def square(n):
    """Calculate the square of a number.

    Args:
        n: An integer or a real number to be squared.

    Returns:
        The square of the number `n`

    """
    return n*n


def cube(n):
    """Calculate the cube of a number.

    Args:
        n: An integer or a real number to be cubed.

    Returns:
        The cube of the number `n`

    """
    # YOUR CODE HERE



# DO NOT EDIT CODE BELOW THIS LINE

import unittest


class TestGettingStarted(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)


if __name__ == '__main__':
    unittest.main()
