from lxml.html import HtmlElement as Element
from typing import List

from .category import Category


class Round:
	"""
	Represents a single non-final round of Jeopardy!.
	
	A Jeopardy! game is broken into three rounds: Jeopardy! (sometimes called "Single Jeopardy!"), Double Jeopardy! and
	Final Jeopardy! The first two rounds each consist of 30 clues broken into six categories; clues are valued starting
	at $200 for the Jeopardy! round and $400 for the Double Jeopardy! round, with each subsequent clue incrementing in
	value by that same amount. Not all of the 30 clues in the round are guaranteed to be revealed over the course of the
	game.
	"""

	def __init__(self, table: Element) -> None:
		"""
		Initializes a Round.
		
		:param table: The ``<table>`` element from the J!Archive HTML document in which the 6x6 grid for the Round is
		  displayed (with each column dedicated to a single category of five clues plus a header cell).
		"""
		category_cells: List[Element] = table.cssselect(".category")
		clue_cells: List[Element] = table.cssselect(".clue")
		
		self.categories: List[Category] = []
		for idx, category_cell in enumerate(category_cells):
			q1: Element = clue_cells[idx]
			q2: Element = clue_cells[idx + 6]
			q3: Element = clue_cells[idx + 12]
			q4: Element = clue_cells[idx + 18]
			q5: Element = clue_cells[idx + 24]
			self.categories.append(Category(category_cell, q1, q2, q3, q4, q5))
