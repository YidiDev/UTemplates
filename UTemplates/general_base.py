from abc import (ABC, abstractmethod)


class GeneralBaseElement(ABC):
    def __str__(self) -> str:
        """
        Return the HTML element as a string.

        General Use Case:
            This method is called when the object is passed to the str() function
            or needs to be converted to a string. It essentially calls the to_string
            method to get the HTML element in string form.

        Example:
            print(str(my_element))  # Outputs the HTML string representation of my_element

        :return: String representation of the HTML element.
        """
        return self.to_string()

    @abstractmethod
    def to_string(self) -> str:
        """
        Abstract method to generate the HTML element as a string.

        General Use Case:
            This method should be implemented in subclasses to generate
            the HTML representation of the element. The __str__ method
            calls this method to get the string form of the element.

        Example:
            Should be overridden in subclass. E.g.
            def to_string(self):
                return "<tag>content</tag>"

        :return: Should return the HTML string representation when implemented.
        """
        pass


class GroupedBaseElement(GeneralBaseElement):
    def __init__(self, elements: iter | GeneralBaseElement) -> None:
        """
        Initialize with an iterable of elements.

        :param elements: An iterable containing the elements to concatenate.
        """
        self.elements: iter | GeneralBaseElement = elements

    def to_string(self) -> str:
        if isinstance(self.elements, GeneralBaseElement):
            return str(self.elements)
        else:
            return "".join(map(str, self.elements))
