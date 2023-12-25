from lxml.html import HtmlElement as Element
from typing import List, Optional

from .clue import Clue


def _get_category_note(note: str) -> Optional[str]:
	"""
	"""
	if not note:
		return None

	if note[0] in ("(", "[", "{"):
		note = note[1:-1]

	first_token_position: int = note.find(" ")
	if ":" in note[0:first_token_position]:
		return note[first_token_position + 1:]
	else:
		return note

class Category:
	"""
	"""

	def __init__(self, header: Element, q1: Element, q2: Element, q3: Element, q4: Element, q5: Element) -> None:
		"""
		"""
		header_rows: List[Element] = header.cssselect("tr")
		self.name: str = header_rows[0].text_content()
		self.note: Optional[str] = _get_category_note(header_rows[1].text_content())
		self.clues: List[Clue] = [Clue(q1), Clue(q2), Clue(q3), Clue(q4), Clue(q5)]
