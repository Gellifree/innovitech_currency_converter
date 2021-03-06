# Mérföldkövek és haladás

## Első megvalósított elemek

**2021.08.18**

Jelen állapotában a program rendelkezik egy könnyedén navigálható menüvel (M1-es követelmény), és a nyelvesítés prototípusával (NY1-es követelmény) A továbbiakban könnyedén bövíthető a nyelvi állomány, igény szerint, viszonylag kevés munkával.
A program bővítésre került a Funkció modulból az egyszerű átváltással (F1), és az API (F5) ponttal.
 - [X] M1 - A jelenlegi menürendszer kielégíti a szükségleteimet
 - [X] NY1 - A nyelvesítés könnyedén bővíthető és építhető be az új funkciókba (Az importálás redundáns, megoldás keresése ideális volna)
 - [X] F1 - Egy egyszerű, nem hibatűrő megoldás implementálva lett
 - [X] F5 - Az API kérést optimalizálni kell, később dátum szerint ellenőrizzen, hogy egy nap több kérés ne történjen, és hiba esetén, őrizze meg az előzőt, de jelezze azt hogy nem feltétlenül naprakészek az adatok.


 **2021.08.19**

 Megvalósításra került az átváltások tárolása, és szűrése, bővítve lettek a nyelvi állomámyok, és javítva lett az egyszerű átváltás, hogy kezelje az elgépelési hibát, és erről tájékoztassa a felhasználót. Egy egyszerű valuta kilistázás elkészült, nem feltétlenül ideális a megjelenítés.

 - [X] F2 - Automatikus mentés *.csv* fájlba
 - [X] F3 - Dátum szerinti, és valuta alapú szűrés hozzáadva, teljes listázás mellett
 - [X] K5 - A listázási funkció egy egyszerű megvalósítása kész, későbbi újratervezést igényelhet
 - [X] F1 - Javított, hibatűrése növelve rosz adatbevitellel szemben

 **2021.08.20**

 Javításra került a nyelvesítés importálása, megszüntetve a redundanciát. Az osztályok refaktorálás alá kerültek, és statikussá változtak a függvények, így nem kell felesleges példányokon keresztül elérnünk a függvényeket, amik miatt a nyelvesítés nem működött. Futási időben beállítható a nyelv, ami azonnal megváltozik. Ezenkívül az API hívások optimalizálva lettek, hogy minden nap friss adatokkal dolgozzunk, viszont egy nap, ne intézzünk több API hívást, mert szükségtelen. Amennyiben az API hívás sikertelen, nem veszítjük el a lementett adatokat, viszont a program jelzi, hogy az aktuális adatok, nem naprakészek.

 A mai napon egyenlőre inkább a kódbázis újraírása kapott nagyobb szerepet, nem a követelménylista.

 Elkészült az elemző, ami megkeresi a leggyakrabban használt, és az öt legutoljára használt valutát, és ezek között tudunk állítani a beállításokban, hogy melyiket szeretnénk használni.

 - [X] NY1 - Futási időben cserélhető nyelv, viszont nem menti le az ujraindulás után alaphelyeztbe áll
 - [X] F5 - Optimalizált API hívás megvalósítva
 - [X] F4 - Nem csak az utoljára, hanem a leggyakrabban használt, maximum 5 valutát is választhatjuk a beállításokban

 **2021.08.21**

 Megvalósíŧásra került az automatikus felismerés, a beállítások lementése, és visszatöltése, funkciók ki és bekapcsolásának lehetősége. Ezenkívül újragondolásra kerültek a listázási nézetek, hogy üres táblázat esetén, ne jelenítsük meg a fejlécet. Az átváltásoknál lehetőségünk van bekapcsolni, hogy eredményként megjelenítse a legtöbbet/legutoljára használt cél valutákban, és hogy ezenkívül megadjunk egy valutát.

 - [X] K1 - Az automatikus felismerés működik, végül nem lett kikapcsolható, mert nem vagyunk kénytelenek megadni a valutát használat közben
 - [X] K2 - Megjelenik a lista, amennyiben beállítottuk hogy legyek aktív a funkció. Módosíthatjuk hogy a legutoljára használt 5, vagy a leggyakrabban használt 5 valutába váltson át automatikusan.
 - [X] K4 - A beállítások menüben kikapcsolható két kényelmi funkció
 - [ ] K3 - Nem kerül megvalósításra, a többi funkció mellett felesleges

Ezzel az eredetileg elkészített követelménylista teljesítésre került.

**Pár plusz kényelmi funkció, ami nem volt benne a követelménylistában:**

 - Amennyiben átakarjuk állítani, hogy a legutoljára, vagy legtöbbet használt valutákat használja a program, de a funkció ki van kapcsolva, felhívja rá a figyelmünket.
 - Az adatok naprakészségét jelzi a program
 - A szűréseknél amikor a régi átváltásokban keresünk, megjelenítjük az eredmények darab számát
 - A beállítások gyors áttekintése érdekében azok kilistázhatóak
 - Az előzmények törölhetőek
 - Amennyiben bekapcsoltuk hogy jelenítse meg a legutojára/legtöbbet használt valutákat, de nincs rendelkezésre álló adat, a program jelzi a felhasználónak.
 - Minden kilépésnél elmentjük a program futása közben történt beállítás változásokat, hogy azokat visszatölthessük újraindulás után.

**2021-08-22**

A mai nap folyamán lett pár felületes teszt elvégezve, de nem minden modul lett letesztelve. A legfontosabb, hibakezelő modul le lett fedve, ezenkívül a beállítások modul egy kis része, és a menü is.
Ezenkívül elkészítettem két segéd dokumentumot, ami tartalmazza a program használatához szükséges információkat.
