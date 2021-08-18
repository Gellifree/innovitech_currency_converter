# Dokumentáció

## Környezet paraméterei

 - OS: elementary OS 5.1.7
 - Kernel: 5.4.0-80-generic
 - Shell: fish 2.7.1
 - Python: 3.6.9

## Feladat áttekintése

Az alkalmazás célja hogy lehetővé tegye a valutaátváltást a felhasználó számára az aktuális árfolyamokat figyelembe véve. A feladatot konzolos alkalmazásként fogom elkészíteni.

## Követelménylista

| Modul | ID | Név | Kifejtés |
|-------|:----:|-----|----------|
| Funkció | F1 | Egyszerű átváltás | A felhasználó képes legyen, megadva egy számot, majd kijelölni annak a valutáját, és a cél valutát, átváltani az összeget. |
| Funkció | F2 | Logolás | A program mentse el, a régebbi átváltásokat, és azok legyenek megtekinthetőek a felhasználó számára. |
| Funkció | F3 | Keresés | A mentett váltásokban lehessen dátum, illetve valuta szerint szűrni/keresni. |
| Funkció | F4 | Gyors elérés és rendezés | Az utoljára használt 5 valutatípus legyen felül/könnyedén elérhető, a maradék pedig abc szerint rendezve. |
| Funkció | F5 | API | Az aktuális árfolyamot valamilyen API használatával kell megszerezni. |
| Megjelenés | M1 | Menürendszer | A program rendelkezzen könnyedén használható, és navigálható menüvel, egyértelmű jelzésekkel. |
| Kényelem | K1 | Automatikus felismerés | A program automatikusan ismerje fel a beírt valutákat. ($, Ft ...) |
| Kényelem | K2 | Listázás | A legtöbbet/utoljára használt valutákban alapesetben jelenítse meg az átváltott értéket a gyorsaság érdekében. |
| Kényelem | K3 | Beállítás | Beállításokban előre állíthassunk be preferált cél, és kiinduló valutákat, amik így a K2 követelményben megjelennek. |
| Kényelem | K4 | Kikapcsolás | A beállításokban legyen lehetőségünk kényelmi funkciókat ki/be kapcsolni. |
| Kényelem | K5 | Megnevezés | A pénznemekhez legyenek megjelenítve a megnevezéseik |
| Nyelvesítés | NY1 | Kétnyelvűség | A programban állítható legyen a nyelv angol, illetve magyar nyelv között. |

## Használati esetek

A programban nem lesz felhasználókezelés, mivel nem kezelünk érzékeny adatokat.

## Képernyő tervek
A képernyőtervek a valódi megvalósítástól eltérhetnek. Nem beszélhetünk valódi képernyőtervről, de a menü megjelenése a következő mintát kell kövesse:

```
2021                                                 Innovitech - Valutaátváltó

      [0] Valutaátváltás
      [1] Tárolt átváltások megtekintése
      [2] Beállítások
      [3] Segítség
      [Q] Kilépés

    >> Q

  Biztos vagy benne hogy kiszeretnél lépni? [I/n]
  >> _
```
