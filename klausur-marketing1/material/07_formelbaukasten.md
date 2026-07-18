# Material 7 — Formelbaukasten Marktvolumen

> Skriptbasis `S. 42–44`: Quellen (Statistiken, Verbände, kumulierte Wettbewerberumsätze, Ableitung aus anderen Märkten, S. 42) · Stabilität der Rahmenbedingungen bestimmt Prognosesicherheit (S. 43) · Verfahren: Trendextrapolation, demographisch gestützte Schätzung, **„abgeleiteter Bedarf: bei Gebrauchsgütern Neu- und Ersatzbedarf"** (S. 44 — Skriptterminus für Formel 2+3!).
> Jede Schätzung in 5 Elementen notieren: **Annahmen → Formel → Rechnung → Bandbreite → Plausibilitätscheck.**

## Universalformeln
| # | Formel | Typischer Einsatz |
|---|---|---|
| 1 | Kunden × Ø Bestand je Kunde | Pistenraupen (Skigebiete × Raupen), Mähdrescher |
| 2 | **Bestand ÷ Nutzungsdauer = Ersatzbedarf p. a.** | fast alle langlebigen Güter — wichtigste Formel! |
| 3 | Neubedarf + Ersatzbedarf = Jahresabsatz | wachsende Märkte (Aufzüge international) |
| 4 | Einwohner × Bedarf pro Kopf | Wasser, Strom, Blut (Transfusionen je 1 000 EW) |
| 5 | Standorte × Einheiten je Standort | Handtrockner (WC-Anlagen), Ticketautomaten (Parkhäuser) |
| 6 | Nutzer × Nutzungshäufigkeit × Preis | Dienstleistungsmärkte, Betreibermärkte |
| 7 | Streckenkilometer × Ausstattung je km | Bahnstrom, Verkehrsleittechnik, Ampeln je Kreuzung |
| 8 | Flugzeuge × Sitze je Flugzeug (÷ Erneuerungszyklus) | Flugzeugsitze |
| 9 | Betriebe × Maschinen je Betrieb | Landwirtschaft, Industrieausrüstung |
| 10 | Stückvolumen × Ø Preis = Umsatzvolumen | immer als zweiter Schritt |

## Rechen-Notation für die Klausur (4–6 Zeilen)
```
Annahme: D hat ~80 Mio. EW; ~1 Stadtbus je 2.000–2.500 EW → Bestand ~35.000
Formel:  Jahresabsatz = Bestand ÷ Nutzungsdauer
Rechnung: 35.000 ÷ 12 J. ≈ 3.000 Busse p.a.; × ~300 T€ ≈ 0,9 Mrd. € p.a.
Bandbreite: 2.500–3.500 Stück, 0,7–1,2 Mrd. €
Plausibel, weil: großes Verkehrsunternehmen (BVG ~1.500 Busse) ersetzt ~120 p.a. → passt.
```

## Regeln
1. Runde Zahlen verwenden (80 Mio., nicht 83,2 Mio.) — Herleitung zählt, nicht Präzision.
2. Immer Bezugsgröße klären: Stück p. a.? Bestand? Umsatz? Muss zur Marktdefinition (Schritt 1) passen!
3. Bandbreite angeben; einen Anker aus Material 8 als Startpunkt nennen.
4. Plausibilitätscheck gegen eine unabhängige zweite Größe (Top-down vs. Bottom-up).
5. Bei Betreiber-/Dienstleistungsmärkten: Umsatz = Menge × Preis der **Dienstleistung**, nicht der Hardware.
