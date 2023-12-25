import urllib.request as web
from http.client import HTTPResponse
from lxml import html
from lxml.html import HtmlElement as Element
from typing import Final

from .final_jeopardy import FinalJeopardy as FinalJ
from .round import Round

BASE_URL: Final[str] = "https://j-archive.com/showgame.php"


class Game:
	"""
	"""

	def __init__(self, game_id: int) -> None:
		"""
		"""
		game_url: str = f"{BASE_URL}?game_id={game_id}"
		webpage: HTTPResponse = web.urlopen(game_url)
		document: Element = html.document_fromstring(webpage.read())

		title: str = document.get_element_by_id("game_title").text_content()

		self.game_id: int = game_id
		self.show_number: int = title.split(" ")[1][1:]
		self.game_date: str = " ".join(title.split(" ")[-3:])
		self.jeopardy: Round = Round(document.get_element_by_id("jeopardy_round").cssselect("table")[0])
		self.double_jeopardy: Round = Round(document.get_element_by_id("double_jeopardy_round").cssselect("table")[0])
		self.final_jeopardy: FinalJ = FinalJ(document.get_element_by_id("final_jeopardy_round").cssselect("table")[0])
