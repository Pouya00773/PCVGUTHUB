# Karteikarten — Grundlagen der Automation

Die Karten decken alle grün hinterlegten Kästchen der Foliensätze ab, Kapitel 1
bis 7. Gefunden wurden sie mit `scripts/finde_gruene_kaesten.py` über zwei
Verfahren, weil eines allein nicht reicht:

- **Vektorpass** — liest die Füllfarbe der Zeichenobjekte im PDF. Findet 109
  Kästen.
- **Pixelpass** — rendert jede Folie und sucht grüne Flächen im Bild. Nötig,
  weil ein erheblicher Teil der Kästen als **Rastergrafik** eingebettet ist und
  damit für den Vektorpass unsichtbar bleibt. Meldet 51 zusätzliche Seiten, die
  einzeln gesichtet wurden.

Ohne den zweiten Pass fehlten unter anderem das Shannon-Nyquist-Abtasttheorem,
die Definitionen von Kausalität, Zeitinvarianz und Linearität sowie **sämtliche**
Kästen der Kapitel 1, 2.1 und 7.

Reine Beschriftungskästen ohne Lerninhalt sind zu inhaltlichen Karten
zusammengefasst.

Format: **V** ist die Vorderseite (Frage), **R** die Rückseite (Antwort). Die
Fundstelle steht als „Kap./Folie" dabei.

Karten mit **★** gehören zu den in den Folien handschriftlich als klausurrelevant
markierten Themen. Die zuerst lernen.

---

## Kapitel 1 — Grundlagen

**V:** Wie ist Automatisierung definiert? — *Kap. 1/8*
**R:** Durch Automatisierung werden dynamische Prozesse in ihrem Verlauf erfasst
und derart gezielt beeinflusst, dass sie vorgegebene Aufgaben und Funktionen
selbsttätig erfüllen.

**V:** Wie ist ein System definiert? — *Kap. 1/9*
**R:** Ein System ist ein aus mehreren Einzelteilen zusammengesetztes Ganzes: die
Gesamtheit von Elementen, die miteinander verbunden sind und dadurch als eine
aufgaben-, sinn- oder zweckgebundene Einheit angesehen werden können — als
strukturierte systematische Ganzheit.

**V:** Unterscheide offenes, geschlossenes und abgeschlossenes System. —
*Kap. 1/9*
**R:** Beim **offenen** System fließen Energie und Stoff über die Grenze. Beim
**geschlossenen** nur Energie, kein Stoff. Beim **abgeschlossenen** weder noch.

**V:** Wie ist ein Prozess definiert? — *Kap. 1/11*
**R:** Die Gesamtheit von aufeinander einwirkenden Vorgängen und Veränderungen in
einem System, durch die Materie, Energie oder Information umgeformt,
transportiert oder gespeichert wird. Ein technischer Prozess ist die Gesamtheit
der Vorgänge in einer technischen Anlage.

**V:** Was wird in einem Fertigungsprozess umgewandelt? — *Kap. 1/11*
**R:** Drei Flüsse laufen parallel: Stoffumwandlung (Eingangsstoff →
Ausgangsstoff), Energieumwandlung und Informationsumwandlung.

**V:** Wie ist ein Automat definiert? — *Kap. 1/12*
**R:** Eine Maschine, die vorbestimmte Abläufe selbsttätig ausführt. Der Begriff
Automatik steht für eine Vorrichtung, die einen Vorgang steuert und regelt.
Beispiel: Fahrkartenautomat.

**V:** Was ist ein Agent? — *Kap. 1/12*
**R:** Automaten, die rein auf Informationsebene arbeiten. Sie bestehen aus
Software in Form eines Programmcodes. Beispiel: Twitter-Bot.

**V:** Nenne die sieben allgemeinen Ziele der Automation mit Beispiel. —
*Kap. 1/19*
**R:** Ökonomisch (Rationalisierung, Optimierung), gleichmäßig (Stromproduktion),
zuverlässig und präzise (Weltraumsonde), sicher (Kraftwerk), ökologisch
(ressourcenschonend), komfortabel (Spülmaschine), flexibel (3D-Drucker).
Oberziel: Kosteneffizienz und Qualität.

**V:** Nenne die fünf Basisaufgaben der Automation. — *Kap. 1/20*
**R:** Messen und Wandeln von Prozessgrößen. Steuern und Sichern durch Abarbeitung
von Logikprogrammen. Regeln zur Stabilisierung von Prozessgrößen. Überwachen und
Erkennen von gefährlichen Prozesszuständen. Anzeigen und Bedienen — Darstellen
von und Eingriff auf Prozess- und Führungsgrößen.

**V:** Nenne die drei Basisaufgaben der Information. — *Kap. 1/20*
**R:** Archivieren (Bereitstellen über lange Zeiträume), Vermitteln (zwischen den
Leitebenen) und Absichern (gegen unerlaubte Zugriffe von innen oder außen).
Realisiert werden sie durch moderne Prozessleitsysteme.

**V:** Wie ist ein Prozessleitsystem definiert? — *Kap. 1/21*
**R:** Ein Prozessleitsystem (PLS, englisch Distributed Control System DCS) ist
ein hierarchisches und integriertes System zur technischen Realisierung der
Aufgaben der Prozessleittechnik.

**V:** Nenne die fünf Ebenen der Automatisierungspyramide von oben nach unten. —
*Kap. 1/21* ★
**R:** ERP (Enterprise Resource Planning) auf der Unternehmensebene. MES
(Manufacturing Execution System) auf der Betriebsleitebene. SCADA (Supervisory
Control and Data Acquisition) auf der Prozessleitebene. PLC beziehungsweise SPS
auf der Steuerungsebene. Ein- und Ausgangssignale auf der Feldebene.

**V:** In welche Richtung laufen Daten und Planung in der
Automatisierungspyramide? — *Kap. 1/21*
**R:** Daten werden von unten nach oben erfasst, Planung wirkt von oben nach
unten.

**V:** Was kennzeichnet Industrie 1.0? — *Kap. 1/24*
**R:** Mechanisierung. 1784 der erste mechanische Webstuhl; die mechanische
Massenproduktion führte zu hoher Arbeitslosigkeit und den Weberaufständen. Später
Dampfmaschinen, Eisenbahnen, Kohleabbau, Schwerindustrie.

**V:** Was kennzeichnet Industrie 2.0? — *Kap. 1/24*
**R:** Elektrifizierung. 1870 das erste Fließband, Ende des 19. Jahrhunderts die
Einführung der Elektrizität als Antriebskraft. Fließband, Motoren, Telefon,
Telegramm, Schreibmaschine.

**V:** Was kennzeichnet Industrie 3.0? — *Kap. 1/25* ★
**R:** Automatisierung. 1941 entwickelte Konrad Zuse den Z3-Computer, 1969 kam
die erste speicherprogrammierbare Steuerung. Personal Computer begründen einen
neuen Industriezweig; Vernetzung von Elektronik und IT steht im Fokus.

**V:** Was kennzeichnet Industrie 4.0? — *Kap. 1/25*
**R:** Vernetzung. Weltweite Vernetzung und Interaktion, Integration
cyber-physischer Systeme, Informatisierung der Lebens- und Arbeitswelt,
künstliche Intelligenz in allen Arbeitsbereichen, neue Geschäftsmodelle wie
Predictive Maintenance.

**V:** Welche war die erste SPS der Welt? — *Kap. 1/28* ★
**R:** Die „Modicon 084" von Richard E. Morley, 1968. Ihr Prinzip: programmierte
Verknüpfungen von Ein- und Ausgängen statt fester Verdrahtung.

**V:** Nenne die drei Ebenen einer intelligenten Produktionsanlage. — *Kap. 1/35*
**R:** **Kognitive Ebene** — Auswertung von Langzeitdaten ermöglicht
Optimierungen, die die Szenarien der assoziativen Ebene modifizieren.
**Assoziative Ebene** — Überwachung und Erkennung etwa von Notfallszenarien,
Umschaltung der Konfiguration, weiche Echtzeit. **Klassische Steuerungsebene** —
elementare Funktionen durch die SPS, harte Echtzeit.

**V:** Wodurch unterscheiden sich intelligente von klassischen
Automatisierungssystemen? — *Kap. 1/36*
**R:** Durch die Erweiterung um Wahrnehmungs- und Lernfähigkeiten. Das ist der
signifikante Evolutionsschritt gegenüber der klassischen Automation.

**V:** Welche Anforderungen stellt modellbasierte Automation in Produktion und
Fertigung? — *Kap. 1/23*
**R:** Harte Echtzeit, Verfügbarkeit und Sicherheit.

**V:** Was ist der Vorteil der Modulbauweise bei Flachbaugruppen? — *Kap. 1/29*
**R:** Sie ist für einfache und komplexe Systeme gleichermaßen geeignet.

---

## Kapitel 2 — Systeme

**V:** Wie definiert DIN 19226 Teil 1 das Steuern? — *Kap. 2/70* ★
**R:** Das Steuern ist ein Vorgang in einem System, bei dem die Eingangsgrößen die
Ausgangsgrößen aufgrund der dem System eigentümlichen Gesetzmäßigkeiten
beeinflussen. Kennzeichen: offene Wirkungskette, keine Rückführung.

**V:** Wie lautet die exakte Definition der Kausalität? — *Kap. 2/37*
**R:** Ein System ist kausal, wenn der Output zu jedem Zeitpunkt nur von den
Werten des Inputs zu der betreffenden Zeit und davor abhängt.

**V:** Wie lautet die exakte Definition der Zeitinvarianz? — *Kap. 2/44*
**R:** Ein System ist zeitinvariant, wenn eine Zeitverschiebung des Inputs zu
einer Zeitverschiebung des Outputs führt. Ist y(t) der Output zum Input u(t), so
ist y(t−T) der Output, wenn u(t−T) angelegt wird. Zeitdiskret entsprechend:
y[k−K] zum Input u[k−K].

**V:** Woran erkennt man ein zeitvariantes System? — *Kap. 2/44*
**R:** Taucht die Zeit **explizit** im Modell auf, ist das System zeitvariant.
Beispiel Rakete: Die Masse ist wegen des Treibstoffverbrauchs zeitabhängig, das
Modell lautet ÿ(t) = u(t) / M(t).

**V:** Welche zwei Eigenschaften machen ein System linear? — *Kap. 2/48* ★
**R:** **Superposition** — der Output für u₁(t) + u₂(t) ist gleich y₁(t) + y₂(t).
**Homogenität** — der Output von α·u₁(t) ist gleich α·y₁(t). Zusammengefasst:
α·u₁(t) + β·u₂(t) → α·y₁(t) + β·y₂(t).

**V:** Welche Folgerung ergibt sich direkt aus der Homogenität? — *Kap. 2/48* ★
**R:** Input Null ergibt Output Null. Liefert ein System bei Eingang null einen
Ausgang ungleich null, kann es nicht linear sein — ein schneller Test.

**V:** Wie ist das Gleichgewicht definiert und wie heißt es noch? — *Kap. 2/55*
**R:** Ein System befindet sich im Gleichgewicht, wenn sich die Kenn- und
Zustandsgrößen nicht mehr mit der Zeit ändern. Weitere Namen: Stationärzustand,
Steady State, Fließgleichgewicht. Bedingung kontinuierlich dx/dt = 0 für alle t,
diskret x[k+1] − x[k] = 0 für alle k.

**V:** Welche Frage beantwortet die Stabilität? — *Kap. 2/63*
**R:** Welche Auswirkung eine kleine Störung auf ein System im Steady State hat.
Asymptotisch stabil: erreicht nach Anregung mit endlicher Energie wieder seine
Ruheposition. Grenzstabil: konvergiert zu einem konstanten Ausgangswert.
Instabil: kehrt nicht ins Gleichgewicht zurück und divergiert.

**V:** Was leistet die Systemtheorie in der Automatisierung? — *Kap. 2/67*
**R:** Drei Dinge: Simulation „in silico", also computerbasierte und mathematische
Modelle, mit denen physikalische und physiologische Vorgänge virtuell nachgestellt
werden. Mächtige systemtheoretische Werkzeuge zur Analyse und Optimierung. Und
eine Vielzahl an Steuerungs- und Regelmethoden für ein gewünschtes
Systemverhalten.

**V:** Was ist der Unterschied zwischen Steuerung und Regelung?
**R:** Die Steuerung ist eine offene Kette ohne Messung des Ausgangs und kann
deshalb nicht auf Störungen reagieren. Die Regelung misst die Ausgangsgröße und
führt sie zurück, vergleicht mit dem Sollwert und korrigiert. Nur die Regelung
kann von Haus aus instabile Systeme stabilisieren.

**V:** Wann ist ein System statisch, wann dynamisch?
**R:** Statisch, wenn es keinen Energiespeicher hat — der Ausgang hängt allein vom
Eingang zum selben Zeitpunkt ab, Beschreibung durch eine algebraische Gleichung.
Dynamisch, wenn es mindestens einen Energiespeicher hat — Beschreibung durch eine
Differentialgleichung, bei zeitdiskreten Systemen durch eine Differenzengleichung.

**V:** Was bedeuten SISO und MIMO?
**R:** SISO ist ein Eingrößensystem mit einer Eingangs- und einer Ausgangsgröße.
MIMO ist ein Mehrgrößensystem mit mehreren. Die Vorlesung behandelt bevorzugt
SISO.

**V:** Nenne die sieben Systemeigenschaften aus Handout H2.
**R:** Linearität, Zeitinvarianz, Kausalität, Determiniertheit, asymptotische
Stabilität, Grenzstabilität, Instabilität.

**V:** Was besagt Linearität?
**R:** Superposition und Homogenität: Reagiert das System auf eine
Linearkombination von Eingangssignalen u = α₁u₁ + α₂u₂ mit derselben
Linearkombination der Ausgangssignale y = α₁y₁ + α₂y₂, ist es linear.

**V:** Was besagt Zeitinvarianz?
**R:** Ein um T verzögertes Eingangssignal u(t−T) erzeugt ein um T verzögertes
Ausgangssignal y(t−T). Das System verhält sich heute wie morgen.

**V:** Was besagt Kausalität?
**R:** Das System reagiert auf ein Eingangssignal erst nach Beginn der Anregung,
niemals vorher.

**V:** Wie lautet die Gleichgewichtsbedingung?
**R:** Kontinuierlich dx/dt = 0 für alle t, diskret x[k+1] − x[k] = 0 für alle k.
Ein Gleichgewicht muss nicht existieren; es kann eines, mehrere oder unendlich
viele geben.

**V:** Erkläre asymptotisch stabil, grenzstabil und instabil am Kugelbild.
**R:** Kugel in der Mulde: Kraft treibt zurück, Reibung entzieht Energie, die
Kugel kommt in der Ruhelage an — asymptotisch stabil. Kugel auf der Ebene: keine
tangentiale Kraft, sie bleibt liegen, wandert aber nicht weiter — grenzstabil.
Kugel auf der Kuppe: die Kraft wächst mit der Auslenkung, sie rollt davon —
instabil.

**V:** Welche drei Verkettungsarten gibt es im Blockschaltbild? — *Kap. 2/14–16* ★
**R:** Reihenschaltung (Ausgang des einen ist Eingang des nächsten),
Parallelschaltung (gleicher Eingang auf mehrere Blöcke, Ausgänge summiert) und
Rückführung (Ausgang wird auf den Eingang zurückgeführt — die Struktur des
Regelkreises).

**V:** Welche Voraussetzung muss jeder Block im Blockschaltbild erfüllen?
**R:** Rückwirkungsfreiheit. Signale fließen nur vom Eingang eines Blocks zu
dessen Ausgang, es gibt keine nicht dargestellten Nebeneffekte zwischen Blöcken.

---

## Kapitel 2.1 — Signale

**V:** Was ist ein Signal, was ein System? — *Kap. 2.1/5*
**R:** Signale sind Funktionen einer oder mehrerer unabhängiger Variablen — zum
Beispiel Zeit oder Ort — und enthalten Information über das Verhalten bestimmter
Erscheinungen. Systeme verarbeiten spezielle Signale und erzeugen wiederum neue:
Aus Eingangssignalen werden Ausgangssignale erzeugt.

**V:** Wie wirkt die Umgebung auf ein System ein? — *Kap. 2.1/4*
**R:** Alle nicht abgeschlossenen Systeme — offene wie geschlossene — stehen im
Kontakt mit ihrer Umwelt und tauschen mit ihr Materie, Energie oder Information
aus. Die Umwelt wirkt typischerweise durch **Störungen** auf das System ein.

**V:** Wie notiert man zeitkontinuierliche und zeitdiskrete Signale? —
*Kap. 2.1/47* ★
**R:** Kontinuierliche Signale bekommen **runde** Klammern, die unabhängige
Variable ist reell und heißt meist t: u(t). Diskrete Signale bekommen **eckige**
Klammern, die unabhängige Variable ist ganzzahlig und heißt meist k oder n: u[k].

**V:** Wie ist die Abtastung formal definiert? — *Kap. 2.1/37* ★
**R:** Ein kontinuierliches Signal wird mit dem Abtastintervall T_A beziehungsweise
der Abtastfrequenz f_A := 1/T_A zu äquidistanten Zeitpunkten k·T_A gemessen, mit
k = {0, 1, 2, …}. Dabei entsteht das zeitdiskrete Signal `x[k] := x(k · T_A)`.

**V:** Wie lautet das Shannon-Nyquist-Abtasttheorem? — *Kap. 2.1/41* ★
**R:** Eine Funktion, die keine Frequenzen höher als f_max enthält, ist durch eine
beliebige Reihe von Funktionswerten im Abstand `T_A < 1/(2·f_max)` eindeutig
bestimmt. Das entspricht einer Abtastrate `f_A > 2 · f_max`.

**V:** Warum muss die Bandbreite begrenzt sein? — *Kap. 2.1/41* ★
**R:** Bei der Abtastung ist zu beachten, dass die Bandbreite — also die im Signal
auftretenden Frequenzen — begrenzt ist. Ansonsten tritt ein gravierender
Informationsverlust auf, genannt **Aliasing**.

**V:** Nenne die wichtigen Standardsignale. — *Kap. 2.1/11–19*
**R:** Sprungfunktion, Rechteckfunktion, Signumfunktion, Rampenfunktion,
Exponentialfunktion, periodische Signale und der Dirac-Impuls.

**V:** Wie schreibt man eine Rechteckfunktion mit Sprungfunktionen? — *Kap. 2.1/12* ★
**R:** Als Differenz zweier verschobener Sprünge: σ(t) − σ(t−T).

**V:** Was ist der Unterschied zwischen Abtastung und Quantisierung?
**R:** Abtastung macht aus zeitkontinuierlich zeitdiskret — es werden zu festen
Zeitpunkten Werte entnommen. Quantisierung macht aus wertkontinuierlich
wertdiskret — die Werte werden auf Stufen gerundet. Zusammen ergibt das die
Digitalisierung.

**V:** Was ist Aliasing und wie vermeidet man es? — *Kap. 2.1/43*
**R:** Wird zu langsam abgetastet, erscheint im rekonstruierten Signal eine
Frequenz, die im Original gar nicht vorkommt. Der Informationsverlust ist nicht
reparierbar. Vermeidung: Das Signal muss bandbegrenzt sein und hinreichend schnell
abgetastet werden.

---

## Kapitel 3 — Digitaltechnik

**V:** Was sagen die De Morganschen Gesetze? — *Kap. 3/17*
**R:** ¬(A ∧ B) = ¬A ∨ ¬B und ¬(A ∨ B) = ¬A ∧ ¬B. In Worten: Bei der Negation
einer Klammer wird jedes Element negiert und das Verknüpfungszeichen gekippt.
Benannt nach Augustus De Morgan, bekannt waren sie schon dem mittelalterlichen
Logiker Wilhelm von Ockham.

> Auf der Folie steht „Nicht klausurrelevant" — gemeint ist die Herleitung. Als
> Werkzeug beim Umformen von NAND/NOR und beim Weg zur konjunktiven Minimalform
> wird De Morgan trotzdem gebraucht.

**V:** Wozu dienen die De Morganschen Gesetze in der Praxis? — *Kap. 3/18*
**R:** Eine Konjunktion lässt sich durch drei Negationen und eine Disjunktion
darstellen und umgekehrt. Dadurch kann man Gattertypen gegeneinander austauschen
und Bauteile einsparen — eine Schaltung lässt sich mit reinen NAND- oder reinen
NOR-Gattern aufbauen.

**V:** Was ist der BCD-Code? — *Kap. 3/45* ★
**R:** Binary-coded decimal, dualkodierte Dezimalziffer. Jede Dezimalziffer 0 bis
9 wird durch vier Bit dargestellt, also in einem Halbbyte.

**V:** Unterscheide analoges und digitales Signal.
**R:** Beim analogen Signal bildet der Signalparameter Nachrichten kontinuierlich
ab und kann beliebig viele Werte annehmen. Beim digitalen Signal besteht die
Nachricht nur aus Zeichen, der Signalparameter kann nur endlich viele Werte
annehmen.

**V:** Was ist ein Signalparameter?
**R:** Diejenige Größe des Signals, deren Wert oder Werteverlauf die Nachricht
darstellt — zum Beispiel die Amplitude bei einer amplitudenmodulierten
Wechselspannung.

**V:** Warum dominieren binäre Signale in der Automatisierungstechnik?
**R:** Drei Gründe: weniger Übertragungsfehler, weil nur zwei Interpretationen
möglich sind; einfache Speicherung, da Systeme mit mehr als zwei stabilen
Zuständen aufwendig und unsicher sind; und viele technische Realisierungen —
Ein/Aus, Potential vorhanden oder nicht, Rechtecksignal, Potentialdifferenz.

**V:** Unterscheide Bit, bit und Byte.
**R:** Bit ist die Kurzform für Binärzeichen, also Binärziffer oder -stelle. bit
ist die Maßeinheit der Information. Byte ist eine Gruppe von 8 Binärzeichen.

**V:** Welche Voraussetzung braucht die Schaltalgebra für uneingeschränkte
Gültigkeit? — *Kap. 3/10*
**R:** Alle Schaltzeiten müssen null sein. Genau hier setzt das Hazard-Thema an:
Reale Gatter haben Laufzeiten und verletzen diese Annahme.

**V:** Nenne die vier UND-Regeln mit Konstanten. — *Kap. 3/13* ★
**R:** 0 ∧ A = 0, 1 ∧ A = A, A ∧ A = A, A ∧ ¬A = 0.

**V:** Nenne die vier ODER-Regeln mit Konstanten. — *Kap. 3/13* ★
**R:** 0 ∨ A = A, 1 ∨ A = 1, A ∨ A = A, A ∨ ¬A = 1.

**V:** Wie viele Zeilen und wie viele Verknüpfungen gibt es bei n
Eingangsvariablen? — *Kap. 3/29* ★
**R:** K = 2ⁿ Kombinationsmöglichkeiten, also Zeilen der Wahrheitstabelle, und
V = 2^K = 2^(2ⁿ) mögliche Verknüpfungen. Bei n = 2 also 4 Zeilen und 16
Verknüpfungen.

**V:** Wie unterscheiden sich deutsche und amerikanische Norm bei den
Vorrangregeln? — *Kap. 3/43*
**R:** In der deutschen Norm binden UND und ODER **gleich stark**, in der
amerikanischen bindet UND stärker als ODER (Punkt vor Strich). In beiden bindet
die Negation am stärksten. Empfehlung der Vorlesung: Bei ODER immer klammern.

**V:** Wie bildet man die DNF? — *Kap. 3/50* ★
**R:** Alle Zeilen mit Ausgang 1 betrachten. Je Zeile einen Minterm bilden: alle
Variablen UND-verknüpft, negiert wenn die Variable in der Zeile 0 ist. Alle
Minterme ODER-verknüpfen. Kurz: UND vor ODER.

**V:** Wie bildet man die KNF? — *Kap. 3/52* ★
**R:** Alle Zeilen mit Ausgang 0 betrachten. Je Zeile einen Maxterm bilden: alle
Variablen ODER-verknüpft, negiert wenn die Variable in der Zeile 1 ist. Alle
Maxterme UND-verknüpfen.

**V:** Wie kommt man von der DNF zur KNF?
**R:** Man bildet die DNF der Umkehrfunktion und invertiert sie. Alternativ im
KV-Diagramm die Nullen zusammenfassen, das ergibt die disjunktive Minimalform von
¬Y, und darauf De Morgan anwenden.

**V:** Wie sind KV-Tafeln aufgebaut? — *Kap. 3/59* ★
**R:** Nachbarfelder unterscheiden sich in genau einer Variablen (Gray-Code).
Randfelder gelten als benachbart, die Tafel ist gedanklich ein Torus. Bei n
Eingangsvariablen gibt es 2ⁿ Felder. Jedes Feld erhält den Funktionswert aus der
Wahrheitstabelle.

**V:** Nenne die vier Regeln des KV-Minimierungsverfahrens. — *Handout 4* ★
**R:** 1. Signalwerte in die nummerierten Felder eintragen. 2. Symmetrisch
liegende 1-Felder zu Zweier-, Vierer- oder Achterblöcken einkreisen. 3. Jedes
1-Feld mindestens einmal einkreisen, möglichst große Einkreisungen finden.
4. Bei Zweier-, Vierer-, Achterblöcken entfallen genau 1, 2, 3 Variablen.

**V:** Wie viele Variablen entfallen bei einem Block der Größe 2^k?
**R:** Genau k Variablen. Deshalb immer so groß wie möglich einkreisen,
Überlappungen sind erlaubt und oft nötig.

**V:** Was sind Don't-Care-Terme und wie behandelt man sie? — *Kap. 3/70* ★
**R:** Eingangskombinationen, die technisch nicht auftreten können oder deren
Ergebnis gleichgültig ist. Sie werden als X in die KV-Tafel eingetragen und dürfen
nach Belieben als 0 oder 1 gelesen werden. Ein X wird nur einbezogen, wenn es
einen Block vergrößert — es **muss** nicht überdeckt werden.

**V:** Bis wie viele Variablen ist das KV-Diagramm praktikabel? — *Kap. 3/58*
**R:** Etwa sechs. Vorgeschlagen 1952 von Veitch, 1953 von Karnaugh modifiziert.

**V:** Was ist der Unterschied zwischen Glitch und Hazard? — *Kap. 3/80*
**R:** Ein Glitch ist eine nicht beabsichtigte Signaländerung am Gatterausgang.
Ein Hazard ist die Konfiguration, bei der ein Glitch auftreten **kann**, aber
nicht muss.

**V:** Wodurch entstehen Glitches?
**R:** Dadurch, dass verschiedene Pfade durch ein Schaltnetz unterschiedliche
Laufzeiten haben. Beispiel: A ∧ ¬A müsste immer 0 sein, durch die
Inverter-Laufzeit entsteht aber ein kurzer Puls.

**V:** Wie groß ist eine typische Gatterverzögerung? — *Kap. 3/78*
**R:** Etwa 100 Pikosekunden bis 100 Nanosekunden, je nach Logikfamilie. Die
Verzögerung bei fallender Flanke kann sich von der bei steigender unterscheiden.

**V:** Wann entstehen Hazards im KV-Diagramm und wie beseitigt man sie? —
*Kap. 3/85–86*
**R:** Hazards entstehen, wenn zwei Primterm-Blöcke überlappungsfrei
aneinandergrenzen. Lösung: einen zusätzlichen Primterm-Block einfügen, der die
Überlappung der 1-Menge garantiert — also einen logisch redundanten Term ergänzen.

---

## Kapitel 4 — VPS und Kontaktsteuerung

**V:** Welche drei Arten der Steuerung werden unterschieden? — *Kap. 4/5–8*
**R:** Binäre Steuerung (Beispiel: Vorschubtisch einer Schleifmaschine),
kombinatorische Steuerung (Beispiel: Zünden eines Schweißbrenners) und digitale
Steuerung, bei der die Signalverarbeitung codiert in Zahlen erfolgt (Beispiel:
CNC-Vorschubantrieb).

**V:** Was unterscheidet zeitgeführte von prozessgeführter Steuerung? —
*Kap. 4/10–11*
**R:** Bei der zeitgeführten Steuerung erfolgt die Weiterschaltung nach Ablauf
einer Zeit — sie wird immer weniger eingesetzt, weil sie nicht flexibel genug ist.
Bei der prozessgeführten Steuerung sind die Ereignisse prozessabhängig, die
Weiterschaltung erfolgt durch Sensorsignale.

**V:** Nenne die beiden Ausführungen elektrischer Steuerungen. — *Kap. 4/13*
**R:** Verbindungsprogrammiert (VPS) und speicherprogrammiert (SPS).

**V:** Vergleiche VPS und SPS in vier Merkmalen. — *Kap. 5/3* ★
**R:** Hardware: VPS aufgabenspezifisch, SPS aufgabenneutral. Funktionsrealisierung:
VPS über elektrische Verbindungen, SPS als abgespeichertes Programm. Interne
Verarbeitung: VPS zeitlich parallel, SPS zeitzyklisch und im Zyklus seriell.
Aufgabenänderung: VPS Neuverdrahtung, SPS Neuprogrammierung.

**V:** Wozu dienen Relais und Schütze? — *Kap. 4/26*
**R:** Sie übertragen Schaltsignale von einem Stromkreis in einen anderen,
verstärken und vervielfachen sie, ohne dass die Kreise verbunden sind. Es erfolgt
die Trennung zwischen Steuer- und Laststromkreis.

**V:** Wie unterscheiden sich Relais und Schütz? — *Kap. 4/27–29*
**R:** Relais schalten bis etwa 1 kW, haben meist keine Funkenlöschkammern und
einfach unterbrechende Kontakte. Schütze schalten bis etwa 500 kW, arbeiten
elektromagnetisch mit Anker und haben immer doppelt unterbrechende Kontakte.

**V:** Was unterscheidet Leistungsschütz und Hilfsschütz? — *Kap. 4/30*
**R:** Leistungsschütze schalten große Lasten und haben
Lichtbogen-Löscheinrichtungen. Hilfsschütze schalten kleinere Steuerspannungen.

**V:** Wie werden Relais und Schütze gekennzeichnet? — *Kap. 4/31* ★
**R:** K für Relais, Q für Schütz. Spulenanschlüsse A1 (+) und A2 (−).
Hauptstromkontakte einstellig: 3/4 bei Gleichstrom, 1/2 bei Wechselstrom.
Steuerkontakte zweistellig: erste Ziffer ist die fortlaufende Ordnungsziffer,
zweite Ziffer die Funktionsziffer — 1/2 bedeutet Öffner, 3/4 bedeutet Schließer.

**V:** Was bedeutet die Kontaktbezeichnung 13/14, was 21/22? ★
**R:** 13/14 ist der erste Schließer (Funktionsziffer 3/4), 21/22 der zweite
Öffner (Funktionsziffer 1/2).

**V:** Welche drei Aspekte kennt die Kennzeichnung im Schaltplan? — *Kap. 4/24*
**R:** Produktaspekt mit Vorzeichen Minus (woraus besteht das Objekt),
Funktionsaspekt mit Vorzeichen Gleich (was soll es tun) und Ortsaspekt mit
Vorzeichen Plus (wo steht es).

**V:** Wie entsteht ein Lichtbogen beim Schalten? — *Kap. 4/35*
**R:** Beim Öffnen unter Last will die Leitungsinduktivität den Stromfluss
aufrechterhalten. Die Berührungsfläche wird kleiner, Stromdichte und Temperatur
steigen, die Luft ionisiert und wird leitend. Folge ist Abbrand: Kontaktmaterial
schmilzt und verdampft.

**V:** Warum ist der Abbrand bei Wechselstrom schwächer als bei Gleichstrom?
**R:** Weil im Nulldurchgang des Wechselstroms die Ionisierung unterbrochen wird.

**V:** Nenne drei Funkenlöschmethoden bei kleinen Leistungen. — *Kap. 4/36*
**R:** RC-Kombination, Varistor (spannungsabhängiger Widerstand) und
Freilaufdiode.

**V:** In welchem Zustand werden Kontaktsteuerungen im Schaltplan dargestellt? —
*Kap. 4/39* ★
**R:** Immer im nicht geschalteten Zustand — stromlos, Taster unbetätigt.

**V:** Was unterscheidet den ausführlichen vom kompakten Stromlaufplan? —
*Kap. 4/39–40*
**R:** Der ausführliche zeigt alle Einzelheiten und wird wegen des Umfangs nur
noch selten verwendet. Im kompakten, aufgelösten Plan bekommt jedes
Betriebsmittel einen senkrecht gezeichneten Stromweg, von oben nach unten und von
links nach rechts.

**V:** Was kann man mit einem Relais oder Schütz tun? — *Kap. 4/41–42*
**R:** Übertragen (Hilfsstromkreis auf Hauptstromkreis), verstärken (kleine
Steuerleistung schaltet große Last), umkehren, verriegeln, allgemein logisch
verknüpfen und speichern.

**V:** Wie funktioniert die Selbsthaltung? — *Kap. 4/42* ★
**R:** Im Stromkreis des Relais K1 liegt ein Schließer desselben Relais K1
parallel zum EIN-Taster S1. Wird S1 kurz betätigt, zieht K1 an, der Schließer K1
überbrückt S1, und K1 bleibt erregt. Der Einschaltimpuls ist gespeichert.

**V:** Was ist der Zusammenhang zwischen Selbsthaltung und Schaltnetz/Schaltwerk? —
*Kap. 4/42* ★
**R:** Schaltnetz = ohne Selbsthaltung, der Ausgang hängt nur vom aktuellen
Eingang ab. Schaltwerk = mit Selbsthaltung, es gibt einen gespeicherten Zustand.

**V:** Was bedeutet dominierend setzend und dominierend rücksetzend? — *Kap. 4/46*
**R:** Das dominierende Verhalten gibt an, wie die Schaltung auf gleichzeitiges
EIN und AUS reagiert. Bei dominierend setzend hat die Erregung Vorrang vor dem
AUS-Taster, bei dominierend rücksetzend ist es umgekehrt.

**V:** Wozu dient die Wendeschützschaltung? — *Kap. 4/49*
**R:** Zur Umkehr der Drehrichtung von Drehstrommotoren. Zwei Schütze Q1 und Q2
vertauschen im Laststromkreis zwei Außenleiter. Sie müssen zwingend gegeneinander
verriegelt sein.

**V:** Wozu dient die Stern-Dreieck-Schaltung? — *Kap. 4/51*
**R:** Größere Drehstrommotoren mit Kurzschlussläufer mit reduzierter
Leistungsaufnahme anlaufen zu lassen. Das vermeidet das Auslösen von
Überstromschutzeinrichtungen wegen des sonst hohen Anlaufstroms bei direktem
Anlauf in Dreieckschaltung.

**V:** Wozu dient die Kontaktvervielfachung durch Hilfsschütz? — *Kap. 4/47*
**R:** Um mehr Kontakte zur Verfügung zu haben, als das Hauptschütz selbst bietet.

---

## Kapitel 4.2 — Schaltwerke

**V:** Was unterscheidet Schaltnetz und Schaltwerk? — *Kap. 4.2/3, Kap. 7/4* ★
**R:** Beim Schaltnetz hängt der Ausgang nur von der aktuellen Eingangsbelegung
ab, es ist rein kombinatorisch. Das Schaltwerk hat zusätzlich Speicher oder
Zeitglieder — der Ausgang hängt von Eingang **und** innerem Zustand ab.

**V:** Was ist der Unterschied zwischen SR- und RS-Speicher? — *Kap. 4.2/5* ★
**R:** Nur der Vorrang bei gleichzeitigem Setzen und Rücksetzen. SR ist
setzdominant, RS ist rücksetzdominant. In der Foliennotation gilt: Der Eingang,
der im Funktionsplan **unten am Q** steht, wird in der Anweisungsliste zuletzt
ausgeführt und gewinnt deshalb.

**V:** Wie sieht „Speichern mit vorrangigem Rücksetzen" in der Anweisungsliste
aus? — *Kap. 4.2/5*
**R:** Erst setzen, dann rücksetzen — die letzte Operation gewinnt:
`U E1 / S A / U E0 / R A`. In ST: `IF E1 THEN A := TRUE; END_IF; IF E0 THEN
A := FALSE; END_IF;`

**V:** Welchen Speichervorrang wählt man in der Sicherheitstechnik?
**R:** Rücksetzdominant. Ein gleichzeitig anliegendes AUS muss in jedem Fall
gewinnen.

**V:** Welcher Zählerbaustein ist der Standard nach IEC 61131? — *Kap. 4.2/10*
**R:** CTUD, count up/down. Er zählt bei steigender Flanke an CU aufwärts und an
CD abwärts, wird über LOAD auf den Vorgabewert PV gesetzt und über RESET genullt.

**V:** Was tun TON, TOF und TP?
**R:** TON ist die Einschaltverzögerung: liegt IN durchgehend für die Zeit PT an,
wird Q wahr. TOF ist die Ausschaltverzögerung. TP ist der Impuls fester Länge.

**V:** Welche zwei Operanden gehören zur Flankenauswertung? — *Handout 4*
**R:** Ein Flankenoperand F0, der den veränderten Signalwert speichert, und ein
Impulsoperand I0, der beim Auftreten der Flanke für die Dauer **eines
Programmzyklus** den Wert 1 führt.

**V:** Welche Codesys-Bausteine gibt es für die Flankenauswertung?
**R:** R_TRIG für die steigende Flanke 0 → 1 und F_TRIG für die fallende Flanke.

**V:** Wann kann man auf den Impulsoperanden verzichten?
**R:** Wenn die Flankenauswertung nur an einer Stelle des Programms gebraucht
wird. Dann verwendet man den Ausgang direkt, etwa zum Setzen eines SR-Speichers.

**V:** Was ist die RS-Tabelle und wozu dient sie? — *Handout 4*
**R:** Ein Hilfsmittel für den systematischen Programmentwurf mit mehreren
Speichern. Man betrachtet Ausgangsvariablen — insbesondere Schütze und
Hilfsschütze — als Speicher und trägt je Speicher die Setz- und die
Rücksetzbedingung ein.

**V:** Wie lautet die Aufgabe „Parkhausanzeige"? — *Kap. 4.2/11*
**R:** Anzeige der freien Plätze. S1 sensiert ein einfahrendes, S2 ein
ausfahrendes Auto. Mit dem Taster „Setzen" wird der Anfangswert 10 eingestellt.
Sind keine freien Plätze da, leuchtet eine rote Lampe. Umsetzung mit dem
vorgefertigten Zähler **CTUD**.

**V:** Wie sieht die erweiterte RS-Tabelle der Drei-Pumpen-Aufgabe aus? —
*Kap. 4.2/21* ★
**R:** Schritt 1: Bedingung S1 (0→1), setzt IO1. Schritt 2: IO1 ∧ ¬Q1 ∧ ¬Q2,
setzt Q1, setzt IO1 zurück. Schritt 3: IO1 ∧ Q1 ∧ ¬Q2, setzt Q2, setzt IO1
zurück. Schritt 4: IO1 ∧ Q1 ∧ Q2, setzt Q3, setzt IO1 zurück. Zusätzlich: ¬S0
setzt Q1, Q2 und Q3 gemeinsam zurück.

**V:** Warum braucht die Drei-Pumpen-Aufgabe eine Flankenauswertung? —
*Kap. 4.2/21* ★
**R:** Weil derselbe EIN-Taster S1 dreimal verwendet wird. Ohne Flanke wäre S1 im
nächsten Zyklus immer noch 1 und die Kette liefe in einem einzigen Durchlauf
durch. Im FUP steht deshalb ein P-Baustein hinter S1, der den Merker IO1 für
genau einen Zyklus setzt.

---

## Kapitel 5 — SPS

**V:** Welche binären Aufgaben erfüllt eine SPS typischerweise? — *Kap. 5/4*
**R:** Logische Funktionen (UND, ODER), Speicherfunktionen (JK-Flipflop,
D-Speicher), Zeitfunktionen (Einschaltverzögerung, Puls), Zählfunktionen
(Vorwärts-, Rückwärtszähler) und Flankenerkennung.

**V:** Welche analogen Aufgaben erfüllt eine SPS? — *Kap. 5/4*
**R:** Konditionierung (Verstärkung, Skalierung, Filterung), Selektion
(Grenzwertüberschreitung, Begrenzung, Maximum-Auswahl), Kombination
(arithmetische Verknüpfung) und Transformation (Radizieren, Differenzieren,
Betrag, Exponieren).

**V:** Was bedeutet das EVA-Prinzip? — *Kap. 5/11* ★
**R:** Eingabe — Verarbeitung — Ausgabe. Eine SPS besteht in minimaler Ausführung
immer aus Eingabeeinheit, Verarbeitungseinheit und Ausgabeeinheit. Die zyklische
Abarbeitung ist grundlegendes Merkmal und nutzt ein Prozessabbild.

**V:** Beschreibe den SPS-Zyklus in drei Schritten. — *Kap. 5/12* ★
**R:** Erstens Prozessabbild der Eingänge (PAE) erstellen — alle Eingänge werden
einmalig eingelesen und eingefroren. Zweitens Anwenderprogramm abarbeiten,
Anweisung für Anweisung seriell. Drittens Prozessabbild der Ausgänge (PAA)
ausgeben.

**V:** Was ist die Zykluszeit? — *Kap. 5/14* ★
**R:** Die Zeit für die Abarbeitung eines Zyklus einschließlich aller
Kommunikationsaufgaben. Sie hängt von der Rechenzeit ab, also von der Zahl der
Anweisungen. Höherpriorisierte Tasks unterbrechen den Zyklus und verlängern ihn.

**V:** Was ist die Reaktionszeit und warum ist sie länger als die Zykluszeit? —
*Kap. 5/14* ★
**R:** Die Reaktionszeit ist die Dauer zwischen der Änderung eines Eingangssignals
und der Reaktion am Ausgang. Ändert sich ein Eingang kurz nach dem Einlesen, wird
er erst im nächsten Zyklus erfasst und wirkt erst an dessen Ende — im ungünstigsten
Fall also fast zwei Zyklen.

**V:** Nenne einen Vorteil und drei Nachteile der zyklischen Programmbearbeitung. —
*Kap. 5/15*
**R:** Vorteil: Die Rechenleistung wird immer genutzt, Zykluszeiten müssen nicht
berechnet werden. Nachteile: Weil die Rechenzeit schwanken kann, ist das System
streng genommen nicht deterministisch. Zeitkritische Programmteile werden durch
Änderungen an anderer Stelle beeinflusst. Und Mehrfachzuweisungen auf einen Ausgang
führen immer zu Programmfehlern, weil der spätere Wert den früheren im PAA
überschreibt.

**V:** Warum rechnet das Programm mit dem Prozessabbild statt direkt mit den
Eingängen?
**R:** Weil Eingangssignale sonst innerhalb eines Zyklus mit unterschiedlichen
Werten in die Programmbearbeitung eingehen könnten. Das Prozessabbild friert sie
für die Dauer eines Zyklus ein.

**V:** Woraus besteht die CPU einer SPS? — *Kap. 5/10*
**R:** Steuerwerk (Befehlszähler, Befehlsregister, Befehlsdecoder,
Operationssteuerung — arbeitet das Programm sequentiell ab) und Rechenwerk (ALU
für Bit-, Byte- und Wortoperationen).

**V:** Unterscheide Arbeitsspeicher, Ladespeicher und Systemspeicher. — *Kap. 5/10*
**R:** Der Arbeitsspeicher dient der Abarbeitung des Anwenderprogramms. Der
Ladespeicher nimmt Code- und Datenbausteine sowie Systemdaten wie die
Hardwarekonfiguration auf. Der Systemspeicher enthält die Operandenbereiche
Merker, Zeiten und Zähler sowie die Prozessabbilder und Lokaldaten.

**V:** Nenne die drei Programmorganisationseinheiten nach DIN EN 61131-3. —
*Handout H3* ★
**R:** Programm (Zyklusbaustein, PLC_PRG), Funktionsbaustein FB — parametrierbar
**mit** Speicher — und Funktion FC — parametrierbar **ohne** Speicher.

**V:** Nenne die fünf SPS-Programmiersprachen nach IEC 61131-3. — *Kap. 5/23* ★
**R:** Textsprachen: Anweisungsliste AWL (IL) und Strukturierter Text ST (SCL).
Grafische Sprachen: Funktionsbausteinsprache FUP (FBD), Kontaktplan KOP (LD) und
Ablaufsprache AS (SFC).

**V:** Welches Beschreibungsmittel liegt FBD zugrunde und wofür ist es gedacht? —
*Kap. 5/25*
**R:** Der Logikplan. Zielstellung: Programmierung komplexer
Verarbeitungsstrukturen. Standard DIN EN 61131-3, Funktionsbausteinsprache.

**V:** Welches Beschreibungsmittel liegt SFC zugrunde? — *Kap. 5/25*
**R:** Der Funktionsplan nach DIN 40719 Teil 6, ab 1.4.2005 DIN EN 60848.
Zielstellung: komfortable Beschreibung sequentieller Vorgänge, also Schrittketten.

**V:** Welches Beschreibungsmittel liegt IL/AWL zugrunde? — *Kap. 5/25*
**R:** Algebraische Gleichung und Assemblersprache. Zielstellung: laufzeit- und
speicherplatzoptimierte Programme.

**V:** Was ist CFC und ist es genormt? — *Kap. 5/25*
**R:** Continuous Function Chart, Beschreibungsmittel Signalflussplan und
Logikplan, zur Beschreibung kontinuierlicher Vorgänge. Es ist **proprietär**
(Siemens), nicht Teil von IEC 61131-3. Ebenso S7-HiGraph mit dem Zustandsgraphen.

**V:** Wie liest man einen Kontaktplan? — *Handout H3*
**R:** Wie einen Stromlaufplan von links nach rechts. UND ist eine
Reihenschaltung, ODER eine Parallelschaltung. Jeder Kontaktplan muss mit einer
Zuweisung, einem Funktions- oder Bausteinaufruf abgeschlossen werden.

**V:** Nenne die Bit-Datentypen mit ihrer Größe. — *Kap. 5/26* ★
**R:** BOOL 1 Bit (FALSE, TRUE), BYTE 8 Bit, WORD 16 Bit, DWORD 32 Bit, STRING
variabel.

**V:** Nenne die Arithmetiktypen mit Wertebereich. — *Kap. 5/26* ★
**R:** INT 16 Bit von −32768 bis +32767. DINT 32 Bit von −2147483648 bis
+2147483647. REAL 32 Bit als Dezimalzahl mit Punkt, etwa 341.7, oder in
Exponentialdarstellung 3.417E+02.

**V:** Nenne die drei Zeittypen mit Größe und Schreibweise. — *Kap. 5/26* ★
**R:** TIME 32 Bit, geschrieben `t#12h20m30s`. TIME_OF_DAY 32 Bit, geschrieben
`tod#08:36:12`. DATE 16 Bit, geschrieben `d#1990-01-01`.

**V:** Warum sind BYTE, WORD und DWORD nicht einfach vorzeichenlose Zahlen? —
*Kap. 5/26*
**R:** Weil sie auch reine Bitfolgen darstellen können, deren einzelne Bits keine
Stellenwertigkeit haben — etwa EB 0 als E 0.0 bis E 0.7.

**V:** Wie ist die Namenskonvention für Variablen aufgebaut? — *Kap. 5/27* ★
**R:** Aus drei Bestandteilen: Anwendungsbereich, Kontrolle, Datentyp.
Anwendungsbereich: Global g, Local l, POU-Parameter p, Temporary tmp. Kontrolle:
Input i, Output o. Datentyp: Bool x, Integer i, Real r, Time tim, Date dt, Char c,
Word w, String str.

**V:** Was bedeutet der Variablenname `gixS1`? — *Kap. 5/27* ★
**R:** g = global, i = Input, x = BOOL. Also eine globale Eingangsvariable vom
Datentyp BOOL mit dem Bezeichner S1.

**V:** Wie ist die Adressierung nach IEC 61131-3 aufgebaut? — *Handout 4* ★
**R:** Prozentzeichen, Präfix für den Speicherort, Präfix für die Größe, dann eine
oder mehrere durch Punkte getrennte Zahlen. Speicherort: I (E) Eingang, Q (A)
Ausgang, M Merker, DB Datenbaustein, T Zeiten, Z Zähler. Größe: X Bit, B Byte,
W Wort, D Doppelwort, L Langwort.

**V:** Was bedeuten `%IX136.1`, `%QW800` und `%MD10`? — *Handout 4* ★
**R:** Eingangsbit 136.1, Ausgangswort 800 und Merker-Doppelwort 10.

**V:** Was enthält eine Zuordnungstabelle in Kurzform? ★
**R:** Drei Spalten: Symbol, Adresse, Kommentar. Beispiel: S1 | E0.1 | Start-Taster,
Schließer.

**V:** Was enthält eine Zuordnungstabelle in Langform? ★
**R:** Fünf Spalten, getrennt nach Ein- und Ausgängen: Bezeichnung, Datentyp,
Symbol, Adresse, Zuordnung. Beispiel: Start-Taster | Bool | S1 | E0.1 |
Betätigt = 1. Bei einem Öffner steht dort Betätigt = 0.

**V:** Wozu dient die Zuordnungstabelle?
**R:** Sie ordnet alle für die Steuerung relevanten Betriebsmittel den Ein- und
Ausgängen zu und legt fest, welche Adresse welches Betriebsmittel bekommt. Sie ist
Grundlage für die Planung und für die Deklaration der Variablen in Funktionen und
Funktionsbausteinen.

---

## Kapitel 6 — Ablaufsteuerung / SFC

**V:** Wie definiert DIN IEC 60050-351 die Ablaufsteuerung? ★
**R:** Als eine Steuerung mit schrittweisem Ablauf, bei der der Übergang von einem
Schritt auf den folgenden programmgemäß entsprechend den vorgegebenen
Übergangsbedingungen — Weiterschaltbedingungen, Transitionen — erfolgt.

**V:** Nenne die zwei Merkmale einer Ablaufsteuerung. — *Kap. 6/10* ★
**R:** Es ist immer nur ein Schritt aktiv. Und die Transition erfolgt, wenn die
Weiterschaltbedingung erfüllt ist — dann **muss** weitergeschaltet werden.

**V:** In welche vier Teile gliedert sich eine Ablaufsteuerung? — *Kap. 6/5*
**R:** Ablaufkette, Betriebsarten, Meldungen und Befehlsausgabe.

**V:** Nenne die Betriebsarten und was sie bedeuten. — *Kap. 6/6*
**R:** Automatik — Ablauf programmgemäß ohne Bedienereingriff. Hand — der Bediener
greift direkt auf den Ausgang durch. Einrichten — Stellgeräte einzeln, unter
Umgehung vorhandener Verriegelungen. Tippbetrieb/Einzelschritt — Weiterschaltung
durch Bedieneingriff.

**V:** Welche zwei Strukturelemente hat ein Ablaufplan? — *Kap. 6/13* ★
**R:** Zustände beziehungsweise Schritte mit den dazugehörigen Aktionen, und
Transitionen.

**V:** Welche drei Aktionsarten gibt es? — *Kap. 6/14*
**R:** Kontinuierlich wirkend; kontinuierlich wirkend, aber von einer Bedingung
abhängig; und zeitgesteuert.

**V:** Was ist eine Transition, formal betrachtet? — *Kap. 6/13*
**R:** Ein boolescher Ausdruck mit dem Ergebnis 0 oder 1 beziehungsweise FALSE
oder TRUE. UND wird als `a UND b` oder `a * b` geschrieben, ODER als `a ODER b`
oder `a + b`.

**V:** Was ist eine Wirkverbindung? — *Kap. 6/13*
**R:** Die Linie, die Schritte miteinander verbindet und den Ablauf der Kette
darstellt.

**V:** Was unterscheidet Zuweisung und Zuordnung im Wirkungsteil? — *Kap. 6/13*
**R:** Die Zuweisung schaltet einen Ausgang, etwa „Motor EIN". Die Zuordnung setzt
einen Wert, etwa „Zähler := 7".

**V:** Womit beginnt und endet eine Ablaufkette?
**R:** Sie beginnt mit einem Anfangsschritt (initial step), der die Anlage in
Grundstellung bringt. Nach Beendigung geht die Kette in die Grundstellung zurück.

**V:** Welche Regel gilt am Anfang einer ODER-Verzweigung? ★
**R:** Es darf nur **eine** Weiterschaltbedingung wahr sein, sonst muss eine
Priorität vorgegeben werden. Ein Stern zeigt an, dass von links nach rechts
abgearbeitet wird — der linke Strang hat dann höhere Priorität.

**V:** Welche Entwurfsfalle lauert bei der ODER-Verzweigung?
**R:** Es darf nicht eine Bedingung immer sofort erfüllt sein, sonst besteht keine
Chance, je eine Alternative zu wählen.

**V:** Welche Regel gilt für die UND-Verzweigung? ★
**R:** Nach DIN IEC 60050-351 werden durch **eine** Weiterschaltbedingung alle
parallelen Zweige aktiviert und nur durch Erfüllung einer **gemeinsamen**
Weiterschaltbedingung wieder zusammengeführt.

**V:** Welche Normen regeln die Darstellung von Ablaufketten?
**R:** IEC 61131-3 und DIN EN 60848 (GRAFCET). Herstellerwerkzeuge: S7-GRAPH bei
Siemens, SFC in Codesys.

---

## Kapitel 7 — Automaten

**V:** Wie sind Schaltwerke definiert? — *Kap. 7/6* ★
**R:** Schaltwerke sind universelle Beschreibungen für zeit- und wertdiskrete
Systeme. Diese werden **endliche Automaten** genannt, englisch finite state
machine.

**V:** In welche Bestandteile lässt sich jedes Schaltwerk zerlegen? —
*Kap. 7/6* ★
**R:** In zwei Schaltnetze plus Zustandsregister (Speicherwerk aus Flipflops).
Schaltnetz 1 ist die **Übergangsfunktion** und berechnet den Folgezustand,
Schaltnetz 2 ist die **Ausgangsfunktion** und berechnet den Ausgang.

**V:** Wodurch ist ein endlicher Automat definiert? — *Kap. 7/7* ★
**R:** Durch eine endliche Menge von Eingabesymbolen x_i ∈ X (Alphabet), eine
endliche Menge von Zuständen z_i ∈ Z, einen Anfangszustand z₀ ∈ Z und eine
Zustandsübergangsfunktion δ: Z × X → Z. Zusätzlich kann er eine endliche Menge
von Ausgabesymbolen y_i ∈ Y und eine Ausgabefunktion λ: Z × X → Y umfassen.

**V:** Wie lautet das 6-Tupel eines Automaten? — *Kap. 7/7* ★
**R:** `A = (X, Z, z₀, Y, δ, λ)` — Eingabealphabet, Zustandsmenge,
Anfangszustand, Ausgabealphabet, Übergangsfunktion, Ausgabefunktion.

**V:** Beschreibe das Trivialbeispiel Türsystem. — *Kap. 7/11*
**R:** Die Tür soll aufgehen, wenn Taster S1 gedrückt wird (x₁ = 1), und zugehen,
wenn Taster S2 gedrückt wird (x₂ = 1). Ansonsten verbleibt die Tür in ihrem
Zustand. Zwei Zustände: z₁ „Tür zu" (Anfangszustand) und z₂ „Tür auf". Ausgänge:
y₁ = 1 „öffnet", y₂ = 1 „schliesst".

**V:** Beschreibe den Warenautomaten als Automat. — *Kap. 7/12* ★
**R:** Er liefert gegen ein 2-€-Stück oder zwei 1-€-Stücke eine Ware. Der
Rückgabeknopf gibt eingeworfenes Geld zurück, sofern 2 € noch nicht erreicht
sind. Eingabealphabet X = {1, 2, r} mit r für Rückgabe. Ausgabealphabet
Y = {w, n, 1, 2} mit w für Ware und n für Nichts. Zustandsmenge Z = {z₁, z₂},
wobei z₀ der neutrale Anfangs- und zugleich Endzustand ist.

**V:** Aus welchen drei Blöcken besteht das Schaltwerk der Ampelschaltung? —
*Kap. 7/27* ★
**R:** Ausgabefunktion (liefert y₀, y₁, y₂ an die drei Lampen),
Übergangsfunktion (verarbeitet die Eingabe x₀ vom Ampelknopf und die Zustände
q₀, q₁) und Zustandsspeicher aus zwei D-Flipflops, die q₀ und q₁ halten.

**V:** Nenne die drei Automatentypen und ihre Ausgabefunktion. — *Kap. 7/8* ★
**R:** Mealy-Automat: die Ausgabefunktion λ hängt vom aktuellen Zustand **und der
Eingabe** ab. Moore-Automat: die Ausgabefunktion μ hängt **nur vom aktuellen
Zustand** ab. Medwedjew-Automat: **keine** Ausgabefunktion, die Ausgabe **ist**
der aktuelle Zustand.

**V:** Wie ist ein Mealy-Automat formal definiert? — *Kap. 7/8* ★
**R:** A = (X, Z, z₀, Y, δ, λ) mit Eingabemenge X, Zustandsmenge Z,
Anfangszustand z₀, Ausgabemenge Y, Übergangsfunktion δ und Ausgabefunktion λ.

**V:** Welcher Automatentyp kommt mit den wenigsten Zuständen aus? — *Kap. 7/8* ★
**R:** Der Mealy-Automat. Alle drei Typen sind ineinander transferierbar, aber
Mealy braucht die wenigsten Zustände — weil die Ausgabe zusätzlich von der Eingabe
abhängen darf und deshalb weniger Zustände zur Unterscheidung nötig sind.

**V:** Woran erkennt man im Zustandsgraphen, ob Moore oder Mealy vorliegt? ★
**R:** Steht die Ausgabe **im Zustandskreis**, ist es ein Moore-Automat. Steht sie
**an der Kante** in der Form `Eingang / Ausgabe`, ist es ein Mealy-Automat.

**V:** Formuliere die Musterbegründung für einen Moore-Automaten. — *Übung 7* ★
**R:** „Es handelt sich um einen Moore-Automaten, weil die Ausgabefunktion y nur
vom aktuellen Zustand abhängig ist."

**V:** Wie wandelt man Mealy in Moore um? — *Kap. 7/8* ★
**R:** Jeden Zustand für jede dort auftretende Ausgabe aufspalten und die Ausgabe
in den Zustand schreiben. Die Zustandszahl steigt.

**V:** Wie wandelt man Moore in Mealy um? — *Kap. 7/8* ★
**R:** Die Ausgabe eines Zustands an alle **eingehenden** Kanten schreiben. Die
Zustandszahl bleibt gleich oder sinkt.

**V:** Was ist der Unterschied zwischen Akzeptor und Transduktor? — *Kap. 7/18*
**R:** Der Akzeptor prüft, ob eine Eingabefolge zu einer Sprache gehört, und kennt
akzeptierende Endzustände — die Ausgabe ist im Kern ja/nein. Der Transduktor
erzeugt zu jeder Eingabe eine Ausgabe, wandelt also Eingabefolgen in
Ausgabefolgen um.

**V:** Wie viele Zeilen hat die Folgezustandstabelle? ★
**R:** 2 hoch (Anzahl Zustandsbits + Anzahl Eingangsbits). Bei zwei Zustandsbits
und zwei Eingängen also 2⁴ = 16 Zeilen.

**V:** Welche Spalten hat die Folgezustandstabelle? ★
**R:** Aktueller Zustand, Eingang, Folgezustand und Ausgabe.

**V:** Wie kommt man vom Zustandsgraphen zur Schaltung? — *Übung 7* ★
**R:** Erstens Automatentyp bestimmen. Zweitens Folgezustandstabelle aufstellen.
Drittens je ein KV-Diagramm für jedes Zustandsbit z(n+1) und eines für die
Ausgangsvariable, daraus die minimale DNF. Viertens Schaltplan zeichnen: je
Zustandsbit ein D-Flipflop, davor das Gatternetz aus NOT, AND und OR.

**V:** Wie behandelt man eine unzulässige Eingangskombination? — *Übung 7* ★
**R:** Als Don't-Care in den KV-Diagrammen. Soll der Automat bei unzulässiger
Eingabe im aktuellen Zustand bleiben, ergänzt man die Gleichungen so, dass
z(n+1) = z(n) für diese Kombination gilt.
