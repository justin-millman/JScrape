from lxml.html import HtmlElement as Element
from typing import Optional


class Clue:
	"""
	Represents a single clue in a round of Jeopardy!.
	
	A Clue consists of the "answer" (which is presented to the players) and the "question" (which the players are
	attempting to provide). The question is not actually framed in the form of a question. A Clue is not intrinsically
	associated with a dollar amount.
	"""

	def __init__(self, cell: Element) -> None:
		"""
		Initializes a Clue.

		Note that this function should **not** be called directly. To create a new instance of the Clue class, use the
		``Clue.create`` function, which is capable of handling Clues that were not actually revealed during the game.
		
		:param cell: The ``<td>`` element from the J!Archive HTML document in which the Clue is displayed.
		"""
		self.answer: str = cell.cssselect(".clue_text")[0].text_content()
		self.question: str = cell.cssselect(".correct_response")[0].text_content()
		self.is_daily_double: bool = bool(cell.cssselect(".clue_value_daily_double"))

	@classmethod
	def create(cls, cell: Element) -> Optional["Clue"]:
		"""
		Creates a Clue from a ``<td>`` element that may or may not contain an exposed Clue.

		Clues are only exposed if one of the players selects the category/amount during gameplay. Depending on the speed
		of the game, some Clues may stay unrevealed, in which case neither the players nor the audience get to see them.
		Within J!Archive, such Clues are displayed as blank squares in the table grid.

		:param cell: The ``<td>`` element from the J!Archive HTML document in which the Clue would be displayed if it
		  was revealed.
		"""
		if not list(cell):
			return None
		else:
			return cls(cell)
