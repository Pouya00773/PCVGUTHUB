# Belegte Klausurmarkierungen

Diese Datei ist die **einzige Wahrheitsquelle** dafür, was im Lernmaterial als
belegt klausurrelevant gilt. Das Build-Skript liest sie und vergibt das ★ auf
den Karteikarten allein anhand dieser Fundstellen. Von Hand gesetzte Sterne gibt
es nicht mehr.

## Woher die Markierungen stammen

Es sind **handschriftliche Notizen in den Vorlesungsfolien** — mit blauem Stift
geschrieben, meist mit türkisem Textmarker umkringelt. Sie stammen aus der
eigenen Mitschrift, vermutlich notiert, als der Dozent den Hinweis in der
Vorlesung gegeben hat.

> **Das ist ein guter Hinweis, aber keine offizielle Festlegung des Dozenten.**
> Es gibt kein Dokument, in dem die Hochschule oder Prof. Fabian den
> Klausurstoff verbindlich abgrenzt. Wer sich allein hierauf verlässt, verlässt
> sich auf eine Mitschrift.

## Wie die Liste zustande kam

Erzeugt mit `scripts/finde_klausurmarker.py`, aber **nicht** von ihm bestimmt:
Jede Zeile unten wurde an der gerenderten Folie mit dem Auge geprüft. Das war
nötig, weil beide maschinellen Verfahren unzuverlässig sind.

Der Textpass durchsucht die Textebene nach „klausurrelevant". Die
Handschrifterkennung zerlegt das Wort aber oft — in den Rohdaten steht etwa
`K2lansar relevant`, `1)lansurrelevant` oder `Kausurrelevant`. Und auf
Kap. 4.2/18 fehlt der Marker in der Textebene vollständig, obwohl er groß und
umkringelt auf der Folie steht.

Der Markerpass sucht türkise Flächen. Er hat Kap. 4.2/18 gefunden, meldet aber
auch Folien mit **gedruckten** hellblauen Tabellenköpfen ohne jede Handschrift,
etwa Kap. 4.2/14. Türkis heißt außerdem nur „hier ist etwas betont" — die
meisten so markierten Folien tragen kein Wort „Klausur".

Die Sichtprüfung hat sich auch inhaltlich gelohnt: Auf Kap. 4.2/7 steht
„**Vielleicht** Klausurrelevant!". Die Texterkennung hatte das „Viel"
verschluckt, sodass es zunächst als „leicht klausurrelevant" gelesen wurde — aus
einem Vorbehalt wäre so eine abgeschwächte Zusage geworden.

## Positive Markierungen

Sechzehn Folien. Jede einzeln am Bild bestätigt.

| Fundstelle | Thema | Wortlaut auf der Folie |
|---|---|---|
| Kap. 2/13 | Blockschaltbild zu einer Gleichung aufstellen | „Klausurrelevant!" mit Pfeil auf das Blockschaltbild |
| Kap. 2.1/30 | Signale in geschlossener Darstellung angeben | „Klausur relevant!!" |
| Kap. 3/12 | Verknüpfungen mit Konstanten | „Klausur relevant" |
| Kap. 3/13 | Verknüpfungen mit Konstante und Variable | „Klausur relevant" |
| Kap. 3/29 | Anzahl Verknüpfungen, K = 2ⁿ und V = 2^K | „Klausur relevant", dazu „wahrscheinlich bis max. 3 Variablen" |
| Kap. 3/45 | Aufzug-Beispiel, BCD-Code | „Klausurrelevant", dazu „mit Videos im Internet lernen" |
| Kap. 3/70 | Don't-Care-Terme im KV-Diagramm | „Klausurrelevant" |
| Kap. 3/73 | Generatorüberwachung | „Klausurrelevant" |
| Kap. 4/31 | Kennzeichnung von Relais- und Schützkontakten | „Klausurrelevant ↓", dazu „beschriften in Klausur" |
| Kap. 4/42 | Selbsthaltung | „Klausurrelevant!", dazu „Schaltnetz → ohne Selbsthaltung / Schaltwerk → mit Selbsthaltung" |
| Kap. 4/53 | Übung Förderband | „Klausurrelevant 24 V" |
| Kap. 4.2/7 | Beispiel Werktor | „**Vielleicht** Klausurrelevant!" — also ausdrücklich unsicher |
| Kap. 4.2/18 | Beispiel mit Speichern, drei Pumpen | „Klausurrelevant!" — nur im Bild, nicht in der Textebene |
| Kap. 6/36 | Übungsaufgabe 3 Pumpen | „Klausurrelevant" |
| Kap. 7/4 | Unterschied Schaltnetz und Schaltwerk | „→ Klausurrelevant", dazu „Speicher vor Schaltwerk ordentlich erklären können" |
| Kap. 7/8 | Automatentypen ineinander umwandeln | „Automatentypen in andere umwandeln — klausurrelevant" |

## Negative Markierungen

Zwei Themen sind ausdrücklich als **nicht** klausurrelevant gekennzeichnet.

| Fundstelle | Thema | Wortlaut |
|---|---|---|
| Kap. 3/17 | De Morgansche Gesetze, Herleitung | „Nicht Klausurrelevant!!" |
| Kap. 2.1/15 | Übersicht wichtiger Signale | „nicht Klausurrelevant" |

De Morgan bleibt als **Werkzeug** trotzdem nötig — beim Umformen von NAND und
NOR und auf dem Weg zur konjunktiven Minimalform. Nicht klausurrelevant ist die
Herleitung der Gesetze.

## Hinweise auf den Übungsblättern

Kein Folienmarker, aber gleichwertig belastbar:

| Quelle | Inhalt |
|---|---|
| Übung 1, Minimierung logischer Gleichungen | handschriftlich: „Klausuraufgabe: Ein Schaltplan wird vorgegeben und soll analysiert werden. Daraus sollen wir eine Wahrheitstabelle und ein KV-Diagramm darstellen." |
| Übung 2, Gatterlogik und Kontaktlogik | trägt „Klausurrelevant" bereits im Dateinamen |
| Übung 7, Automaten | einziges Blatt mit Punkteschlüssel — 6 von 13 Punkten auf der KV-Minimierung |

Diese drei sind die Grundlage für die Reihenfolge im Lernplan.

## Was daraus folgt — und was nicht

Belegt ist: Diese sechzehn Folien und drei Übungsblätter tragen einen Hinweis.

**Nicht** belegt ist, dass alles Übrige nicht drankommt. Die Markierungen sind
Stichproben aus der Vorlesung, keine Stoffabgrenzung. Karten ohne ★ können
genauso in der Klausur auftauchen.

Karten mit ◆ sind meine eigene Einschätzung: Sie behandeln dasselbe Thema wie
eine markierte Folie. Beispiel: Kap. 3/70 zu Don't-Care ist markiert, also sind
die übrigen KV-Karten vermutlich ebenfalls wichtig — aufgeschrieben hat das aber
niemand.
