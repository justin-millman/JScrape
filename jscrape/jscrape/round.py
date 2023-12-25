from lxml.html import HtmlElement as Element
from typing import List

from .category import Category


class Round:
	"""
	"""

	def __init__(self, table: Element) -> None:
		"""
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
