from lxml.html import HtmlElement as Element


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
		
		:param cell: The ``<td>`` element from the J!Archive HTML document in which the Clue is displayed.
		"""
		self.answer: str = cell.cssselect(".clue_text")[0].text_content()
		self.question: str = cell.cssselect(".correct_response")[0].text_content()
		self.is_daily_double: bool = bool(cell.cssselect(".clue_value_daily_double"))
