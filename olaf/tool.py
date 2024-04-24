"""a set on usefull classes and functions"""


class MyClass:
    """A simple classe to get start to my documentation course.

    Attributes
    ----------
    label : str
        The object label
    """

    def __init__(self, label: str) -> None:
        """Initialise concept instance.

        Parameters
        ----------
        label : str
            The object label."""
        self.label = label

    def set_label(self, new_label: str) -> None:
        """Set a new lbel value

        Parameters
        ----------
        new_label : str
            new value of label attribute.
        """
        self.label = new_label


def f1(a: str, b: str) -> None:
    """print value of a and b"""
    print(a, b)
