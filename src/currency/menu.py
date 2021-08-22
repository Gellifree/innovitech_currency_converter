from . import settings as s
from currency.language_handler import LanguageHandler

class MenuDrawer:
	l = LanguageHandler.reimport_language()

	@staticmethod
	def update_language():
		MenuDrawer.l = LanguageHandler.reimport_language()

	@staticmethod
	def draw(elements):
		index = 0
		for element in elements:
			if(element == MenuDrawer.l.lang["menu_item_quit"]):
				print("    [Q] {}".format(element))
			else:
				print("    [{}] {}".format(index, element))
			index += 1
		print()
		answer = input(" >> ")

		try:
			answer = int(answer)
			if(answer >= 0 and answer < len(elements)):
				if(elements[answer] == MenuDrawer.l.lang["menu_item_quit"]):
					return -1
				return answer
			# normal answer between array indexes including quitting
			else:
				print(MenuDrawer.l.lang["bad_index"])
				return -2
				# over, or underindexing
		except:
			if(answer == "Q" or answer == "q"):
				return -1
				# exitcode again
			else:
				print(MenuDrawer.l.lang["unknown_answer"])
				return -3
				# unidentified command
