

class Number:
    """
    Number class represents a numeric value and provides methods for basic arithmetic operations.

    Attributes:
        value (int or float): The numeric value stored in the object.

    Methods:
        __init__(self, n): Initializes a Number object with the given numeric value.
        val(self): Returns the numeric value stored in the object.
        add(self, n2): Adds the value of another Number object to the current object.
        __add__(self, n2): Overloads the addition operator to add two Number objects.
        __str__(self): Returns a string representation of the Number object.
        addall(cls, number_obj_iter): Class method that adds the values of all Number objects in an iterable.
    """

    def __init__(self, n):
        """
        Initializes a Number object with the given numeric value.

        Args:
            n (int or float): The numeric value to initialize the object with.
        """
        self.value = n

    def val(self):
        """
        Returns the numeric value stored in the object.

        Returns:
            int or float: The numeric value stored in the object.
        """
        return self.value

    def add(self, n2):
        """
        Adds the value of another Number object to the current object.

        Args:
            n2 (Number): The Number object whose value is to be added to the current object.
        """
        self.value += n2.val()

    def __add__(self, n2):
        """
        Overloads the addition operator to add two Number objects.

        Args:
            n2 (Number): The Number object to be added to the current object.

        Returns:
            Number: A new Number object with the sum of the values of the two Number objects.
        """
        return self.__class__(self.value + n2.val())

    def __str__(self):
        """
        Returns a string representation of the Number object.

        Returns:
            str: A string representation of the numeric value stored in the object.
        """
        return str(self.val())

    @classmethod
    def addall(cls, number_obj_iter):
        """
        Class method that adds the values of all Number objects in an iterable.

        Args:
            number_obj_iter (iterable): An iterable containing Number objects.

        Returns:
            Number: A new Number object with the sum of the values of all Number objects in the iterable.
        """
        return cls(sum(n.val() for n in number_obj_iter))


def f1(a: str, b: str) -> None:
    """print value of a and b"""
    print(a, b)
