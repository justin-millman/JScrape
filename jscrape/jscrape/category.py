from lxml.html import HtmlElement as Element
from typing import List, Optional

from .clue import Clue


def _get_category_note(note: str) -> Optional[str]:
	"""
	Retrieve the "note" for a particular Category.
	
	Some Jeopardy! Categories are introduced with a note or additional directive from the host explaining the conceit of
	the Category or otherwise providing additional information to the players. On J!Archive, this is represented by a
	parenthetical displayed below the Category name. Not all Categories have a note; in fact, most Categories do not.
	
	:param note: The note text, as extracted from the relevant ``<td>`` element on the J!Archive HTML document. This
	  cell always exists in the DOM, so an empty string should indicate "no note."
	:returns: The note from ``note``, with any parentheses (or brackets, or curly braces) removed from the beginning and
	  the end. If the host's name is attached to the front of the text (e.g. "Alex: ") this is stripped as well.
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
	Represents a single category of five clues in a round of Jeopardy!.
	
	A Category consists of a name, possibly a note, and five clues ordered from lowest-valued (and easiest) to
	highest-valued (and hardest). A Category can be played in either the Jeopardy! round or the Double Jeopardy! round,
	and as such is not associated with any dollar amounts.
	"""

	def __init__(self, header: Element, q1: Element, q2: Element, q3: Element, q4: Element, q5: Element) -> None:
		"""
		Initializes a Category.
		
		:param header: The ``<td>`` element from the J!Archive HTML document that serves as the header cell for the
		  Category.
		:param q1: The ``<td>`` element from the J!Archive HTML document in which the lowest-valued clue for the
		  Category is displayed.
		:param q2: The ``<td>`` element from the J!Archive HTML document in which the second-lowest-valued clue for the
		  Category is displayed.
		:param q3: The ``<td>`` element from the J!Archive HTML document in which the middle-valued clue for the
		  Category is displayed.
		:param q4: The ``<td>`` element from the J!Archive HTML document in which the second-highest-valued clue for the
		  Category is displayed
		:param q5: The ``<td>`` element from the J!Archive HTML document in which the highest-valued clue for the
		  Category is displayed.
		"""
		header_rows: List[Element] = header.cssselect("tr")
		self.name: str = header_rows[0].text_content()
		self.note: Optional[str] = _get_category_note(header_rows[1].text_content())
		self.clues: List[Clue] = [Clue(q1), Clue(q2), Clue(q3), Clue(q4), Clue(q5)]
