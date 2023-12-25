from lxml.html import HtmlElement as Element


class Clue:
	"""
	"""

	def __init__(self, cell: Element) -> None:
		"""
		"""
		self.answer: str = cell.cssselect(".clue_text")[0].text_content()
		self.question: str = cell.cssselect(".correct_response")[0].text_content()
		self.is_daily_double: bool = bool(cell.cssselect(".clue_value_daily_double"))
