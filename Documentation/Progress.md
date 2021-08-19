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
 - [ ] F4 - Az átváltás nem listából történik, hanem begépelés szerint, keresni kell egy alkalmas módszert a megvalósításra
 - [ ] K1 - A jelenlegi rendszer hibatűrésének javítása után lesz prioritás
 - [ ] K2 - A jelenlegi rendszer hibatűrésének javítása után lesz prioritás
 - [ ] K3 - A jelenlegi rendszer hibatűrésének javítása után lesz prioritás
 - [ ] K4 - Kényelmi funkciók megvalósítását követi
