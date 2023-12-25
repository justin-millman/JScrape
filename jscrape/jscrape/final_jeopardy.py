from lxml.html import HtmlElement as Element

from .clue import Clue


class FinalJeopardy:
    """
    """

    def __init__(self, table: Element) -> None:
        """
        """
        self.category_name: str = table.cssselect(".category_name")[0].text_content()
        self.clue: Clue = Clue(table.cssselect(".clue")[0])
