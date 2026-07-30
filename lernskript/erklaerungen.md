# Einfach erklärt — die wichtigen Themen

Dieses Kapitel erklärt die klausurrelevanten Themen in Alltagssprache, ohne
Formalismus. Die exakten Definitionen stehen im Lernskript; hier geht es darum,
dass die Sache einleuchtet. Wer das Bild im Kopf hat, kann die Definition
rekonstruieren — umgekehrt selten.

---

## Die Automatisierungspyramide — wer entscheidet was

Fünf Ebenen, und die Logik dahinter ist einfach: **Je weiter unten, desto
schneller muss es gehen — und desto dümmer darf es sein.**

Von unten nach oben:

**Feldebene** — Sensoren und Aktoren. Ein Endschalter meldet „Kiste da", ein
Ventil öffnet. Hier gibt es keine Entscheidung, nur Signal.

**Steuerungsebene** — die SPS. Sie entscheidet in Millisekunden: Motor an, Motor
aus. Hier gilt **harte Echtzeit** — eine verpasste Frist ist ein Fehler, nicht
nur ärgerlich.

**Prozessleitebene** — SCADA. Der Leitstand, an dem ein Mensch die Anlage sieht
und eingreift. Reaktionszeit: Sekunden.

**Betriebsleitebene** — MES. Welcher Auftrag läuft auf welcher Maschine, in
welcher Reihenfolge. Reaktionszeit: Minuten bis Stunden.

**Unternehmensebene** — ERP. Einkauf, Lieferkette, Kapazitätsplanung.
Reaktionszeit: Tage.

Zwei Richtungen laufen gleichzeitig durch die Pyramide: **Daten** werden von
unten nach oben verdichtet — aus Millionen Sensorwerten wird eine Kennzahl. Und
**Planung** wirkt von oben nach unten — aus einem Kundenauftrag wird irgendwann
ein Ventil, das öffnet.

Ein Bild dazu: Die Pyramide funktioniert wie ein Unternehmen. Der Werker an der
Maschine reagiert sofort und lokal. Der Schichtleiter plant den Tag. Die
Geschäftsführung plant das Quartal. Niemand erwartet, dass die Geschäftsführung
über einen klemmenden Endschalter entscheidet — dafür ist sie zu langsam, und
das ist auch richtig so.

---

## Steuern und Regeln — der Unterschied in einem Bild

Stell dir vor, du duschst.

**Steuern** heißt: Du drehst den Hahn auf eine Position, von der du aus Erfahrung
weißt, dass sie ungefähr 38 Grad ergibt. Dann stellst du dich drunter. Dreht der
Nachbar seine Waschmaschine auf, wird dein Wasser kalt — und du merkst es erst am
eigenen Rücken. Die Steuerung hat keine Rückmeldung. Sie rechnet vorwärts und
hofft.

**Regeln** heißt: Ein Thermostat misst ständig die tatsächliche Wassertemperatur,
vergleicht sie mit deinen eingestellten 38 Grad und dreht nach. Der Nachbar kann
machen was er will — die Regelung merkt die Abweichung und korrigiert.

Daraus folgt alles Weitere:

- Die Steuerung ist eine **offene Kette**, die Regelung ein **geschlossener Kreis**.
- Nur die Regelung kann auf **Störungen** reagieren, weil nur sie misst.
- Und der stärkste Punkt: Eine Regelung kann sogar **instabile Systeme
  stabilisieren**. Ein Besen auf der Handfläche fällt um (instabil), aber mit
  ständigem Nachschauen und Nachfahren balancierst du ihn. Genau das ist eine
  Regelung. Ohne Hinsehen — also gesteuert — geht das prinzipiell nicht.

---

## Statisch oder dynamisch — hat das Ding ein Gedächtnis?

Die Frage ist immer dieselbe: **Kann das System Energie speichern?**

Ein **Widerstand** ist statisch. Legst du Spannung an, fließt sofort Strom. Nimmst
du die Spannung weg, ist der Strom sofort weg. Der Widerstand erinnert sich an
nichts. Beschreibung: eine simple Gleichung, U = R·I.

Ein **Kondensator** ist dynamisch. Er lädt sich auf, und wie hoch die Spannung
jetzt ist, hängt davon ab, wie lange und wie stark er vorher geladen wurde. Er
hat ein Gedächtnis. Deshalb braucht man eine Differentialgleichung — die
beschreibt nämlich, wie sich etwas **über die Zeit** ändert.

Merksatz fürs Erkennen: Kondensator, Spule, Tank, Schwungmasse, Wärmespeicher →
dynamisch. Widerstand, Hebel, Getriebe, Logikgatter → statisch.

Das ist übrigens dieselbe Unterscheidung wie später bei Schaltnetz und
Schaltwerk. Nur heißt der Speicher dort nicht Kondensator, sondern Flipflop.

---

## Stabilität — die Kugel auf der Fläche

Das beste Bild der ganzen Vorlesung. Eine Kugel liegt irgendwo und wird
angestoßen.

**In der Mulde**: Die Kugel rollt hin und her, Reibung frisst die Energie, sie
kommt in der Mitte zur Ruhe. → **asymptotisch stabil**. Das ist der Normalfall,
den man haben will.

**Auf der Ebene**: Du stößt an, die Kugel rollt ein Stück und bleibt liegen. Sie
kommt nicht zurück, haut aber auch nicht ab. → **grenzstabil**.

**Auf der Kuppe**: Ein Stubser genügt, und sie rollt immer schneller davon. →
**instabil**.

Wenn du in der Klausur nach der Definition gefragt wirst, zeichne die drei
Flächen. Die Formulierung ergibt sich dann von selbst: „ein System ist
asymptotisch stabil, wenn es nach einer Anregung mit endlicher Energie wieder
seine Ruheposition erreicht."

---

## Abtastung und Aliasing — warum Wagenräder rückwärts laufen

Im Western drehen sich die Speichenräder der Kutsche manchmal rückwärts. Das ist
Aliasing, und es erklärt das ganze Thema.

Die Kamera macht 24 Bilder pro Sekunde — sie **tastet ab**. Dreht sich das Rad
fast genau so schnell, dass eine Speiche pro Bild eine Speichenposition weiter
ist, sieht es aus, als stünde das Rad still. Ist es etwas langsamer, sieht es aus,
als liefe es rückwärts.

Die Information zwischen zwei Bildern ist verloren, und zwar **unwiederbringlich**.
Man kann aus den Bildern nicht rekonstruieren, was wirklich passiert ist. Genau
das ist Aliasing: Es entsteht eine Frequenz im abgetasteten Signal, die im
Original gar nicht vorkam.

Die Abhilfe: schnell genug abtasten. Und dafür muss das Signal **bandbegrenzt**
sein — es darf keine beliebig hohen Frequenzen enthalten, sonst reicht keine
Abtastrate der Welt.

**Wie schnell ist schnell genug?** Darauf antwortet das
**Shannon-Nyquist-Abtasttheorem**: Man braucht mehr als **zwei** Abtastwerte pro
Periode der höchsten vorkommenden Frequenz.

```
f_A > 2 · f_max        beziehungsweise        T_A < 1 / (2 · f_max)
```

Anschaulich: Um eine Schwingung überhaupt als Schwingung zu erkennen, musst du
mindestens einmal den Berg und einmal das Tal erwischen. Mit nur einem Wert pro
Periode könnte die Kurve zwischen deinen Messpunkten alles Mögliche tun — und
genau das ist das Wagenrad im Western.

Praxisbeispiel: Musik auf CD wird mit 44,1 kHz abgetastet, weil das menschliche
Ohr bis etwa 20 kHz hört. 2 × 20 = 40, plus Sicherheitsabstand für den
Anti-Aliasing-Filter.

Der zweite Begriff, **Quantisierung**, ist etwas anderes und wird gern
verwechselt:

- **Abtastung** betrifft die **Zeitachse**: Wann schaue ich hin?
- **Quantisierung** betrifft die **Werteachse**: Wie fein kann ich den Wert
  angeben?

Ein Digitalfoto: Abtastung ist die Auflösung in Pixeln, Quantisierung die
Farbtiefe in Bit.

---

## DNF und KNF — Einsen sammeln oder Nullen sammeln

Du hast eine Wahrheitstabelle und willst daraus eine Formel. Es gibt zwei Wege,
und beide führen zum selben Ergebnis.

**Der DNF-Weg — die Einsen sammeln.** Du schaust dir jede Zeile an, in der der
Ausgang 1 ist, und schreibst auf, welche Bedingung dort herrscht. „Y ist 1, wenn
a=0 und b=1 und c=1." Das schreibt man `¬a ∧ b ∧ c`. Das machst du für jede
Einser-Zeile und verbindest alles mit ODER: „Y ist 1 in diesem Fall **oder** in
jenem Fall **oder** …"

Die Negation dreht sich dabei um, und das ist die häufigste Fehlerquelle: Steht in
der Zeile eine **0**, kommt die Variable **negiert** in den Term. Denn du willst
ja ausdrücken „a ist nicht gesetzt".

**Der KNF-Weg — die Nullen sammeln.** Umgekehrt: Du schaust die Zeilen an, in
denen der Ausgang 0 ist, und formulierst für jede eine Bedingung, die diesen Fall
**verbietet**. Alle Verbote werden mit UND verknüpft: „es darf nicht dieser Fall
sein **und** nicht jener Fall …"

**Wann nimmt man was?** Hat die Funktion wenige Einsen, wird die DNF kurz. Hat sie
wenige Nullen, wird die KNF kurz. In der Klausur ist meistens vorgegeben, welche
Form gefragt ist — lies das genau, denn KNF wird gerne verlangt und dann rechnen
alle reflexhaft die DNF.

---

## Das KV-Diagramm — Nachbarn zusammenfassen

Die Idee dahinter ist erstaunlich einfach.

Wenn eine Funktion sowohl bei `a=0, b=1` als auch bei `a=1, b=1` eine 1 liefert,
dann ist a offensichtlich **egal** — es kommt nur darauf an, dass b=1 ist. Aus
zwei Termen wird einer, und eine Variable verschwindet.

Das KV-Diagramm ist nichts anderes als eine Anordnung der Wahrheitstabelle, bei
der solche Paare **nebeneinander liegen**. Deshalb der Gray-Code: Von Feld zu
Feld darf sich immer nur **eine** Variable ändern. Nur dann bedeutet „zwei Felder
nebeneinander" auch „eine Variable ist egal".

Daraus ergeben sich alle Regeln von selbst:

- **Warum Zweier-, Vierer-, Achterblöcke?** Weil bei jeder Verdopplung genau eine
  weitere Variable herausfällt. Ein Zweierblock eliminiert 1 Variable, ein
  Viererblock 2, ein Achterblock 3.
- **Warum möglichst groß einkreisen?** Weil jede Vergrößerung eine weitere
  Variable spart.
- **Warum dürfen sich Blöcke überlappen?** Weil ein Feld mehrfach durch
  verschiedene Regeln erklärt werden darf. Das schadet nicht.
- **Warum gelten Randfelder als benachbart?** Weil sich auch dort nur eine
  Variable ändert. Das Diagramm ist gedanklich zu einem Ring gebogen — links und
  rechts hängen zusammen, oben und unten auch.

**Und was liest man aus einem Block ab?** Genau die Variablen, die im ganzen Block
**gleich bleiben**. Alles, was innerhalb des Blocks wechselt, ist egal und fällt
weg.

### Don't-Care — der Joker

Manche Eingangskombinationen können physikalisch gar nicht vorkommen. Beispiel:
Ein oberer Füllstandssensor meldet „Wasser da", der untere meldet „kein Wasser" —
unmöglich, das Wasser müsste in der Luft schweben.

Für solche Fälle ist es **egal**, was die Schaltung tut. Man trägt ein **X** ein
und darf es beim Blockbilden als 0 oder als 1 lesen — je nachdem, was besser
passt.

Der Joker hat eine Regel: Du **musst** ihn nicht überdecken. Nur echte Einsen
müssen in einem Block liegen. Ein X, das keinen Block größer macht, lässt du
einfach links liegen. Das ist der häufigste Fehler beim Thema.

---

## Selbsthaltung — warum die Klingel weiterklingelt

Du drückst einen Klingelknopf und lässt los. Die Klingel hört auf. Das ist ein
**Schaltnetz** — kein Gedächtnis.

Jetzt willst du eine Maschine mit einem kurzen Tastendruck starten, und sie soll
weiterlaufen. Der Trick: Du legst **einen Kontakt des Schützes parallel zum
Taster**, und dieser Kontakt wird von genau dem Schütz geschaltet, das der Taster
einschaltet.

Der Ablauf:

1. Du drückst den Taster. Strom fließt, das Schütz zieht an.
2. Das Schütz schließt seinen eigenen Hilfskontakt — der liegt parallel zum
   Taster und überbrückt ihn.
3. Du lässt los. Der Taster öffnet, aber der Strom fließt weiter über den
   Hilfskontakt.
4. Das Schütz hält sich selbst. Daher der Name.

Ausschalten geht nur, wenn man diesen Kreis auftrennt — deshalb liegt der
AUS-Taster **in Reihe** und ist ein **Öffner**.

Genau hier steht die handschriftliche Notiz auf der Folie, und sie bringt es auf
den Punkt: **Schaltnetz = ohne Selbsthaltung, Schaltwerk = mit Selbsthaltung.**
Der gespeicherte Zustand ist der ganze Unterschied.

---

## Öffner und Schließer — warum der AUS-Taster verkehrt herum ist

Ein **Schließer** schließt den Kontakt, wenn man drückt. Logisch: betätigt = 1.
Ein **Öffner** öffnet ihn beim Drücken. Also: betätigt = 0.

Warum baut man AUS-Taster und Not-Aus als Öffner, wo das doch verwirrend ist?

**Wegen Drahtbruch.** Stell dir vor, das Kabel zum Not-Aus reißt.

- Wäre der Not-Aus ein Schließer, käme nie ein Signal an. Die Maschine liefe
  weiter, und niemand würde es merken — bis jemand den Not-Aus drückt und nichts
  passiert.
- Als Öffner liegt im Normalbetrieb dauerhaft Spannung an. Reißt das Kabel, ist
  das Signal weg — genau wie beim Drücken. Die Maschine geht aus.

Das Prinzip heißt **Ruhestromprinzip**: Der sichere Zustand wird durch das
Vorhandensein von Strom aufrechterhalten. Fällt irgendetwas aus, fällt die Anlage
in den sicheren Zustand.

Fürs Programmieren folgt daraus etwas Wichtiges: Ein unbetätigter Öffner liefert
bereits eine **1**. Du fragst ihn also **nicht negiert** ab, obwohl er „AUS"
heißt.

---

## SR und RS — wer gewinnt, wenn beide drücken?

Ein Speicher hat zwei Eingänge: Setzen und Rücksetzen. Was passiert, wenn beide
gleichzeitig 1 sind? Irgendwer muss gewinnen, sonst wäre das Verhalten
undefiniert.

- **SR-Baustein**: **S**etzen gewinnt (setzdominant).
- **RS-Baustein**: **R**ücksetzen gewinnt (rücksetzdominant).

Merkhilfe: Der **erste** Buchstabe im Namen ist der Gewinner.

In der Vorlesung wird es über die Abarbeitungsreihenfolge erklärt, und das ist
sogar anschaulicher. Die SPS arbeitet Zeile für Zeile ab:

```
IF E1 THEN A := TRUE;  END_IF;     (* setzen *)
IF E0 THEN A := FALSE; END_IF;     (* ruecksetzen *)
```

Sind beide 1, wird erst gesetzt, dann rückgesetzt — und **die letzte Anweisung
gewinnt**. Hier also das Rücksetzen. Im Funktionsplan erkennt man das daran,
welcher Eingang **unten am Q** steht.

**Welchen nimmt man?** In der Sicherheitstechnik immer **rücksetzdominant**. Wenn
jemand gleichzeitig Start und Not-Aus drückt, muss Not-Aus gewinnen. Immer.

---

## Der SPS-Zyklus — warum die Steuerung blinzelt

Eine SPS macht nicht alles gleichzeitig, sondern immer wieder dasselbe im Kreis:

1. **Alle Eingänge einlesen** und einfrieren. Das eingefrorene Abbild heißt PAE.
2. **Das Programm durchrechnen**, von der ersten bis zur letzten Zeile.
3. **Alle Ausgänge auf einmal setzen**, aus dem Abbild PAA.

Dann wieder von vorn. Ein Durchlauf ist die **Zykluszeit**.

**Warum das Einfrieren?** Angenommen, ein Sensor flackert. Wenn das Programm ihn
in Zeile 5 abfragt und nochmal in Zeile 200, könnte er zwischendurch gekippt
sein — dieselbe Variable hätte im selben Durchlauf zwei verschiedene Werte. Das
Programm würde sich widersprechen. Das Prozessabbild verhindert das: Innerhalb
eines Zyklus ist ein Eingang **garantiert konstant**.

**Warum ist die Reaktionszeit länger als die Zykluszeit?** Weil die SPS
zwischendurch blinzelt. Ändert sich ein Eingang **direkt nachdem** eingelesen
wurde, verpasst sie ihn für diesen Durchlauf komplett. Er wird erst im nächsten
Zyklus gesehen und wirkt sich erst an dessen Ende aus. Im ungünstigsten Fall also
fast zwei Zyklen.

**Und die berüchtigte Mehrfachzuweisung?** Wenn du denselben Ausgang an zwei
Stellen im Programm beschreibst, gewinnt immer die spätere Stelle — die frühere
wird im PAA einfach überschrieben, bevor überhaupt etwas nach außen geht. Der
erste Befehl war wirkungslos, ohne jede Fehlermeldung. Deshalb steht auf der
Folie so deutlich: Mehrfachzuweisungen führen **immer** zu Programmfehlern.

---

## Hazards — wenn die Physik der Logik widerspricht

Auf dem Papier gilt: `a ∧ ¬a = 0`. Immer. Eine Variable und ihr Gegenteil können
nicht gleichzeitig wahr sein.

In echter Hardware stimmt das nicht ganz. Denn `¬a` entsteht durch einen Inverter,
und der braucht Zeit — sagen wir 5 Nanosekunden. Kippt `a` nun von 0 auf 1, dann
ist `a` sofort 1, aber `¬a` ist noch 5 Nanosekunden lang **auch** 1, weil der
Inverter noch nicht umgeschaltet hat.

In diesem Zeitfenster sind beide Eingänge des UND-Gatters 1, und am Ausgang
erscheint ein kurzer Puls, den es laut Formel gar nicht geben dürfte.

Zwei Begriffe, die gern verwechselt werden:

- Ein **Glitch** ist der Puls selbst — die unerwünschte Signaländerung.
- Ein **Hazard** ist die Konstellation, in der so ein Puls entstehen **kann**.
  Muss er aber nicht — bei anderen Temperaturen oder Bauteilen passiert vielleicht
  nichts.

**Warum ist das gefährlich?** Weil ein nachgeschalteter Speicher den Puls
mitbekommen und kippen kann. Dann bleibt der Fehler dauerhaft.

**Wie repariert man es?** Im KV-Diagramm sieht man Hazards daran, dass zwei Blöcke
**bündig aneinandergrenzen**, ohne sich zu überlappen. Beim Wechsel von einem
Block in den anderen gibt es einen kurzen Moment, in dem keiner der beiden Terme
greift. Die Lösung: einen **zusätzlichen Block** einzeichnen, der die Lücke
überbrückt.

Dieser Zusatzterm ist logisch **überflüssig** — er ändert die Funktion nicht.
Genau deshalb der wichtigste Merksatz zum Thema: **Die minimale Schaltung ist
nicht immer die richtige.** Hazardfreiheit kostet einen redundanten Term.

---

## Mealy, Moore, Medwedjew — drei Automaten

Alle drei tun im Kern dasselbe: Sie merken sich einen Zustand und wechseln ihn
abhängig von der Eingabe. Der Unterschied liegt nur darin, **woher die Ausgabe
kommt**.

**Moore** — die Ausgabe hängt **nur vom Zustand** ab. Eine Ampel ist ein
Moore-Automat: Wenn sie im Zustand „Rot" ist, leuchtet Rot. Punkt. Es spielt keine
Rolle, ob gerade jemand auf den Knopf drückt.

**Mealy** — die Ausgabe hängt vom **Zustand und der Eingabe** ab. Ein
Getränkeautomat ist ein Mealy-Automat: Im Zustand „2 Euro eingeworfen" passiert
gar nichts — erst wenn du eine weitere Münze einwirfst, kommt in genau diesem
Moment die Flasche heraus. Die Ausgabe hängt am Übergang, nicht am Zustand.

**Medwedjew** — es gibt **gar keine** Ausgabefunktion, die Ausgabe **ist** der
Zustand. Man liest die Speicherbits direkt ab. Das ist der einfachste Fall.

**Woran erkennt man es im Zustandsgraphen?**

- Ausgabe steht **im Kreis** → Moore
- Ausgabe steht **an der Kante**, geschrieben als `Eingang / Ausgabe` → Mealy

**Warum braucht Mealy weniger Zustände?** Weil er mehr Information zur Verfügung
hat. Beim Moore-Automaten musst du für jede unterschiedliche Ausgabe einen eigenen
Zustand anlegen. Beim Mealy kann derselbe Zustand je nach Eingabe verschieden
reagieren — das spart Zustände.

**Und der Preis?** Der Moore-Automat reagiert um einen Takt verzögert, dafür ist
sein Ausgang **stabil**, solange der Zustand steht. Der Mealy reagiert sofort,
aber sein Ausgang zappelt mit der Eingabe mit. Für eine Ampel will man Moore, für
schnelle Reaktion Mealy.

---

## Die Ablaufkette — ein Kochrezept als Steuerung

Eine Ablaufsteuerung ist nichts anderes als ein Rezept: Schritt 1, dann Schritt 2,
dann Schritt 3. Und zwischen den Schritten steht eine Bedingung, die erfüllt sein
muss, bevor es weitergeht.

- Ein **Schritt** ist ein Zustand der Anlage, in dem bestimmte Dinge aktiv sind
  („Ventil offen, Rührwerk läuft").
- Eine **Transition** ist die Bedingung dazwischen („bis Füllstand erreicht" oder
  „bis 30 Sekunden um sind").

Zwei Regeln, und beide sind streng:

1. **Immer nur ein Schritt ist aktiv.** Ein Rezept ist nicht gleichzeitig bei
   Schritt 2 und Schritt 5.
2. **Ist die Bedingung erfüllt, muss weitergeschaltet werden.** Kein Zögern.

**Die zwei Verzweigungen** kann man sich ebenfalls am Rezept klarmachen:

**ODER-Verzweigung (Alternative)** — „wenn Teig zu fest, dann Wasser zugeben,
sonst weiter." Es wird **genau ein Weg** genommen. Deshalb darf nur eine Bedingung
gleichzeitig wahr sein, sonst weiß die Steuerung nicht, wohin. Wenn doch mehrere
wahr sein können, legt man eine Priorität fest — der linke Strang gewinnt, wenn
ein Stern das anzeigt.

**UND-Verzweigung (parallel)** — „während der Teig geht, heize den Ofen vor."
**Beide Wege** laufen gleichzeitig. Und zusammengeführt wird erst, wenn **beide**
fertig sind. Der Ofen wartet auf den Teig und der Teig auf den Ofen.

**Der klassische Programmierfehler** taucht in Übung 6 auf: Drei Pumpen sollen mit
demselben Taster nacheinander eingeschaltet werden. Wenn du einfach auf „Taster
ist gedrückt" prüfst, laufen alle drei Schritte in einem einzigen SPS-Zyklus durch
— denn der Taster ist ja immer noch gedrückt, wenn Schritt 2 geprüft wird, und
auch noch bei Schritt 3. Du brauchst die **Flanke**, also den Moment des
Drückens, nicht den Zustand „ist gedrückt". Dafür gibt es R_TRIG.

---

## Vom Stromlaufplan zur Formel — die Übersetzung

Das ist die häufigste Klausuraufgabe, und sie besteht aus zwei Vokabeln:

- **Reihenschaltung = UND.** Der Strom muss durch beide Kontakte. Beide müssen
  geschlossen sein.
- **Parallelschaltung = ODER.** Der Strom sucht sich einen Weg. Einer reicht.
- **Öffner = negierte Variable.**

Mehr ist es nicht. Bei verschachtelten Schaltungen arbeitest du dich von innen
nach außen vor, wie beim Ausrechnen einer Klammer.

Beispiel aus Übung 2: a und b liegen parallel → `(a ∨ b)`. Das Ganze in Reihe mit
c → `(a ∨ b) ∧ c`. Und d liegt parallel zum Ganzen → `((a ∨ b) ∧ c) ∨ d`.

Die Gegenrichtung — von der Formel zum Plan — geht genauso, nur rückwärts. Und
für FUP gilt dasselbe nochmal mit anderen Symbolen: `&` ist UND, `≥1` ist ODER,
ein Kreis am Eingang ist die Negation.
