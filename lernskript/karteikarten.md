# Karteikarten — Grundlagen der Automation

Die Karten decken alle grün hinterlegten Kästchen der Foliensätze ab. Die
Kästchen wurden maschinell aus den PDFs ausgelesen (Füllfarbe der Zeichenobjekte),
sodass keines übersehen wurde: 100 grüne Flächen in den Kapiteln 2, 3, 4, 4.2
und 5. Reine Beschriftungskästen ohne Lerninhalt sind zu inhaltlichen Karten
zusammengefasst.

Format: **V** ist die Vorderseite (Frage), **R** die Rückseite (Antwort). Die
Fundstelle steht als „Kap./Folie" dabei.

Karten mit **★** gehören zu den in den Folien handschriftlich als klausurrelevant
markierten Themen. Die zuerst lernen.

---

## Kapitel 2 — Systeme

**V:** Wie definiert DIN 19226 Teil 1 das Steuern? — *Kap. 2/67* ★
**R:** Das Steuern ist ein Vorgang in einem System, bei dem die Eingangsgrößen die
Ausgangsgrößen aufgrund der dem System eigentümlichen Gesetzmäßigkeiten
beeinflussen. Kennzeichen: offene Wirkungskette, keine Rückführung.

**V:** Was leistet die Systemtheorie in der Automatisierung? — *Kap. 2/64*
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

**V:** Welche drei Verkettungsarten gibt es im Blockschaltbild? — *Kap. 2/13–15* ★
**R:** Reihenschaltung (Ausgang des einen ist Eingang des nächsten),
Parallelschaltung (gleicher Eingang auf mehrere Blöcke, Ausgänge summiert) und
Rückführung (Ausgang wird auf den Eingang zurückgeführt — die Struktur des
Regelkreises).

**V:** Welche Voraussetzung muss jeder Block im Blockschaltbild erfüllen?
**R:** Rückwirkungsfreiheit. Signale fließen nur vom Eingang eines Blocks zu
dessen Ausgang, es gibt keine nicht dargestellten Nebeneffekte zwischen Blöcken.

---

## Kapitel 2.1 — Signale

**V:** Was ist ein Signal, was ein System?
**R:** Ein Signal ist eine Funktion einer oder mehrerer unabhängiger Variablen —
meist der Zeit — und trägt Information. Ein System verarbeitet Eingangssignale und
erzeugt daraus Ausgangssignale.

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

**V:** Was ist Aliasing und wie vermeidet man es? — *Kap. 2.1/40*
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
