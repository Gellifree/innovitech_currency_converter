import settings as s

# Megfelelő nyelvi fájl betöltése
if(s.settings["language"] == "hungarian"):
	import languages.hungarian as l
elif(s.settings["language"] == "english"):
	import languages.english as l
else:
	# nem értelmezhető nyelvi beállítás
	import languages.hungarian as l


# Menü kirajzolását megvalósító osztály
class MenuDrawer:
    def draw(self, elements):
        index = 0
        for element in elements:
            if(element == l.lang["menu_item_quit"]):
                print("    [Q] {}".format(element))
            else:
                print("    [{}] {}".format(index, element))
            index += 1
        print()
        answer = input(" >> ")

        try:
            answer = int(answer)
            if(answer >= 0 and answer < len(elements)):
                if(elements[answer] == l.lang["menu_item_quit"]):
                    return -1
                return answer
                # normal answer between array indexes including quitting
            else:
                print(l.lang["bad_index"])
                return -2
                # over, or underindexing
        except:
            if(answer == "Q" or answer == "q"):
                return -1
                # exitcode again
            else:
                print(l.lang["unknown_answer"])
                return -3
                # unidentified command
