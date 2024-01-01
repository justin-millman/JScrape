from lxml.html import HtmlElement as Element

from .clue import Clue


class FinalJeopardy:
    """
    Represents the Final Jeopardy! clue of a Jeopardy! game.
    
    In Final Jeopardy!, all players are given the category prior to issuing a wager; the answer is then revealed, and
    each player has a limited amount of time to write the corresponding question. Unlike in the Jeopardy! or Double
    Jeopardy! rounds, there is only a single clue, and there is no intrinsic dollar amount associated therewith. Players
    who identify the correct question are rewarded with their wager; those who fail are deducted that amount.
    """

    def __init__(self, table: Element) -> None:
        """
        Initializes a FinalJeopardy.
        
        :param table: The ``<table>`` element from the J!Archive HTML document in which the Final Jeopardy! information
          (category, answer, and question) is displayed.
        """
        self.category_name: str = table.cssselect(".category_name")[0].text_content()
        self.clue: Clue = Clue(table.cssselect(".clue")[0])
