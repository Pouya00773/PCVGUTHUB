# Grundlagen der Automation — Lernskript

Quelle: Vorlesung Prof. Patrick Fabian, HTW Berlin, Studiengang WIW, SS 2026.
Grundlage sind acht Kapitelfoliensätze (375 Seiten), zehn Handouts und die
Übungsblätter 1–7.

Der Text ist eigenständig formuliert. Fundstellen sind als „Kap. 3/58" notiert
und meinen Foliensatz/Foliennummer — dort stehen die Abbildungen, die hier aus
urheberrechtlichen Gründen nicht abgedruckt sind.

> **Hinweis zur Vollständigkeit:** Kapitel 1 der Vorlesung liegt nicht vor. Die
> Foliensätze beginnen bei Kapitel 2. Falls Kapitel 1 prüfungsrelevant ist, muss
> es ergänzt werden.

## Was laut Foliensatz klausurrelevant ist

Die folgenden Punkte sind in den Folien handschriftlich als klausurrelevant
markiert. Sie bilden die Prioritätenliste beim Lernen.

| Thema | Fundstelle | Markierung |
|---|---|---|
| Blockschaltbild eines Systems aufstellen | Kap. 2/12 | klausurrelevant |
| Signale in geschlossener Darstellung angeben | Kap. 2.1/30 | klausurrelevant (doppelt betont) |
| Verknüpfungen mit Konstanten (Regeln 1–18) | Kap. 3/12–13 | klausurrelevant |
| Anzahl möglicher Verknüpfungen, K = 2^n und V = 2^K | Kap. 3/29 | klausurrelevant, „max. 3 Variablen wahrscheinlich" |
| Aufzug-Beispiel: Wahrheitstabelle → DNF → Minimierung | Kap. 3/45 | klausurrelevant |
| KV-Diagramm mit Don't-Care-Termen | Kap. 3/70 | klausurrelevant |
| Generatorüberwachung (systematischer Programmentwurf) | Kap. 3/73 | klausurrelevant |
| Kennzeichnung von Relais- und Schützkontakten beschriften | Kap. 4/31 | klausurrelevant, „beschriften in Klausur" |
| Selbsthaltung — Schaltnetz ohne, Schaltwerk mit | Kap. 4/42 | klausurrelevant |
| Übung Förderband, 24-V-Steuerkreis | Kap. 4/53 | klausurrelevant |
| Beispiel Werktor (SR-Speicher) | Kap. 4.2/7 | leicht klausurrelevant |
| Beispiel mit Speichern | Kap. 4.2/18 | klausurrelevant |
| Übungsaufgabe 3 Pumpen (Ablaufkette) | Kap. 6/36 | klausurrelevant |
| Unterschied Schaltnetz ↔ Schaltwerk „ordentlich erklären können" | Kap. 7/4 | klausurrelevant |
| Automatentyp erkennen und umwandeln | Kap. 7/8 | klausurrelevant |

Ausdrücklich **nicht** klausurrelevant sind laut Markierung die De Morganschen
Gesetze als Herleitung (Kap. 3/17) und die Signalübersicht auf Kap. 2.1/15.
De Morgan wird als Werkzeug trotzdem gebraucht — beim Umformen von NAND/NOR und
beim Weg von der disjunktiven zur konjunktiven Minimalform.

Auf Übungsblatt 1 ist zusätzlich das Klausurformat notiert: *„Ein Schaltplan wird
vorgegeben und soll analysiert werden. Daraus sollen wir eine Wahrheitstabelle und
ein KV-Diagramm darstellen."* Das ist der wahrscheinlichste Aufgabentyp überhaupt.

---

## Teil 1 — Signale und Systeme

### Kernbegriffe

Ein **Signal** ist eine Funktion einer oder mehrerer unabhängiger Variablen —
meist der Zeit, manchmal des Ortes — und trägt Information über das Verhalten
einer Erscheinung. Geschrieben wird die Zeitabhängigkeit ausdrücklich als `y(t)`.

Ein **System** verarbeitet Eingangssignale und erzeugt daraus Ausgangssignale.
Entscheidend ist die Rückwirkungsfreiheit: Eingangssignale existieren unabhängig
vom System, das System wirkt nicht auf sie zurück. Die Ausgangssignale heißen
auch Systemantwort oder Reaktion.

**SISO** bezeichnet ein Eingrößensystem mit einer Eingangsgröße `u(t)` und einer
Ausgangsgröße `y(t)`. **MIMO** bezeichnet ein Mehrgrößensystem. Die Vorlesung
behandelt bevorzugt SISO.

Der **Zustand** eines Systems ist die in ihm gespeicherte Energie. Ändert sich
die Anregung, ändert sich der Zustand. Beim RC-Tiefpass ist das die Ladung des
Kondensators.

### Statisch oder dynamisch

Das ist die wichtigste Unterscheidung, weil sie festlegt, mit welcher Mathematik
gearbeitet wird.

**Statische Systeme** haben keinen Energiespeicher. Der Ausgang zum Zeitpunkt `t`
hängt allein vom Eingang zum selben Zeitpunkt ab. Beschreibung: algebraische
Gleichung.

| Beispiel | Eingang | Ausgang |
|---|---|---|
| Ohmscher Widerstand | Spannung u(t) | i(t) = u(t)/R |
| UND-Gatter | A(t), B(t) ∈ {0,1} | Y(t) = A(t) ∧ B(t) |
| Gewicht | Volumen V(t) | m(t) = ρ·V(t) |

**Dynamische Systeme** haben mindestens einen Energiespeicher. Der Ausgang hängt
von der Vorgeschichte ab. Beschreibung: Differentialgleichung (zeitkontinuierlich)
beziehungsweise Differenzengleichung (zeitdiskret).

| Beispiel | Eingang | Ausgang |
|---|---|---|
| Kondensator | u_C(t) | i_C(t) = C · du_C/dt |
| Spule | i_L(t) | u_L(t) = L · di_L/dt |
| Tankfüllstand | Zufluss F_in(t) | dl/dt = a · F_in(t) |

> **Merksatz:** Energiespeicher vorhanden → dynamisch → Differentialgleichung.
> Kein Speicher → statisch → algebraische Gleichung.

### Systemeigenschaften

| Eigenschaft | Definition |
|---|---|
| Linearität | Superposition und Homogenität: Reagiert das System auf u = α₁u₁ + α₂u₂ mit y = α₁y₁ + α₂y₂, ist es linear. |
| Zeitinvarianz | Ein um T verzögertes Eingangssignal u(t−T) erzeugt ein um T verzögertes Ausgangssignal y(t−T). |
| Kausalität | Das System reagiert erst nach Beginn der Anregung, nie vorher. |
| Determiniertheit | Reproduzierbarkeit: gleicher Anfangszustand erzeugt gleiche Zwischen- und Endzustände. |
| Asymptotische Stabilität | Nach Anregung endlicher Energie kehrt das System in die Ruhelage zurück. |
| Grenzstabilität | Nach Anregung endlicher Energie konvergiert der Ausgang gegen einen konstanten Wert. |
| Instabilität | Nach Anregung endlicher Energie divergiert die Systemantwort. |

Die Kombination **linear + zeitinvariant** (LTI) ist der Normalfall der weiteren
Vorlesung, weil sie eine geschlossene Berechnung der Systemantwort erlaubt.

### Gleichgewicht und Stabilität

Ein System ist im **Gleichgewicht** (steady state), wenn sich seine Zustandsgrößen
zeitlich nicht mehr ändern.

- kontinuierlich: `dx/dt = 0` für alle t
- diskret: `x[k+1] − x[k] = 0` für alle k

Ein Gleichgewicht muss nicht existieren; es kann eines, mehrere oder unendlich
viele geben.

Die Stabilität wird über das Kugel-Gedankenexperiment veranschaulicht (Kap. 2/56 ff.,
H2 Abb. 4): Eine Kugel liegt in einer Ruhelage x = 0 und wird um x₀ ausgelenkt.

- **Mulde** — eine tangentiale Kraft treibt die Kugel zurück, Reibung entzieht
  Energie, die Kugel kommt in x = 0 zur Ruhe → asymptotisch stabil.
- **Ebene** — keine tangentiale Kraft, die Kugel bleibt liegen, wandert aber auch
  nicht weiter → grenzstabil.
- **Kuppe** — die tangentiale Kraft wächst mit der Auslenkung, die Kugel rollt
  davon → instabil.

Anschauliches Gegenbeispiel für den steady state: Ein Behälter mit Zufluss > Abfluss
ist im transienten Zustand, der Wasserstand ändert sich. Bei Zufluss = Abfluss
bleibt der Wasserstand konstant — Gleichgewicht.

### Blockschaltbild

**Klausurrelevant (Kap. 2/12).** Ein Blockschaltbild stellt Signalflüsse und
Wirkungszusammenhänge grafisch dar: Rechtecke sind Verarbeitungsschritte, Linien
sind Signalflüsse. Voraussetzung ist Rückwirkungsfreiheit jedes Blocks — Signale
laufen nur vom Eingang eines Blocks zu dessen Ausgang, unsichtbare Nebeneffekte
gibt es nicht.

Blockschaltbilder sind **nicht eindeutig**: dasselbe System lässt sich verschieden
zerlegen. Drei Verkettungsarten sind zu unterscheiden (Kap. 2/13–15):

1. **Reihenschaltung** — Ausgang des ersten Blocks ist Eingang des zweiten.
2. **Parallelschaltung** — dasselbe Eingangssignal auf mehrere Blöcke, Ausgänge
   werden summiert.
3. **Rückführung** — der Ausgang wird auf den Eingang zurückgeführt und dort
   verglichen. Das ist die Struktur des Regelkreises.

### Steuern und Regeln

Die Abgrenzung ist ein klassischer Prüfungsklassiker und trägt durch die gesamte
Vorlesung.

| | Steuerung | Regelung |
|---|---|---|
| Signalfluss | offene Kette, rein vorwärts | geschlossener Kreis |
| Messung des Ausgangs | nein | ja, Rückführung |
| Reaktion auf Störungen | keine | ja, über Soll-Ist-Vergleich |
| Instabile Strecke | nicht beherrschbar | kann stabilisiert werden |

Der entscheidende Vorteil der Regelung: Die tatsächliche Ausgangsgröße wird
gemessen. Dadurch kann eine Regelung auch von Haus aus instabile Systeme
stabilisieren und technisch nutzbar machen. Eine Steuerung kann das nicht, weil
sie Störungen — nicht kontrollierbare Eingänge — gar nicht bemerkt.

### Signale, Abtastung, Aliasing

**Klausurrelevant (Kap. 2.1/30):** Signale in geschlossener Darstellung angeben.
Gemeint ist, einen skizzierten Signalverlauf durch Überlagerung von
Standardfunktionen als eine Formel zu schreiben.

Die dafür gebrauchten Bausteine:

- **Sprungfunktion** σ(t): 0 für t < 0, 1 für t ≥ 0. Ein um T verschobener Sprung
  ist σ(t−T).
- **Rechteckfunktion**: Differenz zweier Sprünge, σ(t) − σ(t−T).
- **Rampenfunktion**: linear ansteigend, r(t) = t · σ(t). Eine Steigung a
  entspricht a · t · σ(t).
- **Signumfunktion** sgn(t): −1 für t < 0, +1 für t > 0.
- **Impuls** δ(t): Dirac-Stoß, in der Zeichnung ein Pfeil der Höhe des Gewichts.
- **Exponentialfunktion** und periodische Signale.

Vorgehen: Das Signal in Abschnitte zerlegen, für jede Kante einen verschobenen
Sprung ansetzen, für jede Rampe eine verschobene Rampe, und alles addieren. Ein
Sprung nach oben bekommt positives Vorzeichen, ein Sprung nach unten negatives.

**Abtastung** wandelt ein zeitkontinuierliches in ein zeitdiskretes Signal, indem
zu festen Zeitpunkten Werte entnommen werden. **Quantisierung** wandelt
wertkontinuierlich in wertdiskret, indem Werte auf Stufen gerundet werden. Beides
zusammen ergibt die Digitalisierung.

Wesentlich ist die Wahl der Abtastfrequenz. Wird zu langsam abgetastet, entstehen
irreführende diskrete Signale: Das rekonstruierte Signal zeigt eine Frequenz, die
im Original gar nicht vorkommt. Dieser Effekt heißt **Aliasing** und bedeutet
einen nicht reparierbaren Informationsverlust. Voraussetzung für korrekte
Abtastung ist deshalb ein bandbegrenztes Signal — die auftretenden Frequenzen
müssen nach oben beschränkt sein.

**Fundstellen:** Kap. 2 (74 S.), Kap. 2.1 (44 S.), Handout H2.

---

## Teil 2 — Digitaltechnik: Schaltalgebra

### Von analog zu binär

| Begriff | Definition |
|---|---|
| Analoges Signal | Der Signalparameter bildet Nachrichten kontinuierlich ab, kann beliebig viele Werte annehmen. |
| Digitales Signal | Der Signalparameter stellt Daten dar, die nur aus Zeichen bestehen; endliche Anzahl von Werten. |
| Signalparameter | Diejenige Größe des Signals, deren Wert die Nachricht darstellt (z. B. Amplitude). |
| Zeichen | Element aus einer vereinbarten Menge; die Menge heißt Zeichenvorrat. |
| Nachricht | Zeichen oder kontinuierliche Funktion zum Zweck der Weitergabe. |
| Daten | Zeichen oder kontinuierliche Funktionen zum Zweck der Verarbeitung. |
| Signal | Die physikalische Darstellung von Nachrichten oder Daten. |
| Binärzeichen | Zeichen aus einem Zeichenvorrat mit genau zwei Elementen. |
| Bit / bit / Byte | Binärziffer / Maßeinheit der Information / Gruppe von 8 Binärzeichen. |

Binäre Signale dominieren die Automatisierungstechnik aus drei Gründen: weniger
Übertragungsfehler bei nur zwei unterscheidbaren Interpretationen, einfache
Speicherung (Systeme mit mehr als zwei stabilen Zuständen sind aufwendig und
unsicher) und die Vielfalt technischer Realisierungen — Ein/Aus, Potential
vorhanden/nicht vorhanden, Rechtecksignal, Potentialdifferenz.

### Schaltalgebra

Die Schaltalgebra geht auf George Boole zurück und wurde von Claude Shannon auf
technische Schaltungen angewendet. Sie kennt die Konstanten 0 und 1,
Schaltvariablen mit genau zwei Zuständen und Schaltfunktionen, die die
Gesetzmäßigkeit einer Steuerung beschreiben.

> **Voraussetzung für uneingeschränkte Gültigkeit:** alle Schaltzeiten müssen
> null sein. Genau hier setzt später das Hazard-Thema an — reale Gatter verletzen
> diese Annahme.

Zuordnung ist Definitionssache und muss in der Aufgabe festgelegt werden:
„Tür offen" entspricht 1, „Tür geschlossen" entspricht 0.

### Rechenregeln mit Konstanten — klausurrelevant

**Kap. 3/12–13, ausdrücklich markiert.** Diese Regeln muss man auswendig
beherrschen; sie sind das Handwerkszeug jeder Minimierung.

Funktionen mit Konstanten:

| UND | ODER |
|---|---|
| 0 ∧ 0 = 0 | 0 ∨ 0 = 0 |
| 0 ∧ 1 = 0 | 0 ∨ 1 = 1 |
| 1 ∧ 0 = 0 | 1 ∨ 0 = 1 |
| 1 ∧ 1 = 1 | 1 ∨ 1 = 1 |

Funktionen mit einer Konstanten und einer Variablen:

| Regel | Ergebnis | Regel | Ergebnis |
|---|---|---|---|
| 0 ∧ A | 0 | 0 ∨ A | A |
| 1 ∧ A | A | 1 ∨ A | 1 |
| A ∧ A | A | A ∨ A | A |
| A ∧ ¬A | 0 | A ∨ ¬A | 1 |

Weitere Grundregeln:

- **Doppelte Negation:** ¬¬A = A, ¬0 = 1, ¬1 = 0
- **Kommutativgesetz:** A ∧ B = B ∧ A, A ∨ B = B ∨ A
- **Assoziativgesetz:** (A ∧ B) ∧ C = A ∧ (B ∧ C) = A ∧ B ∧ C, analog für ∨
- **Distributivgesetz:** A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C) und
  A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)

### De Morgan

Als Herleitung laut Folie **nicht klausurrelevant** (Kap. 3/17), als Werkzeug
aber unverzichtbar:

- ¬(A ∧ B) = ¬A ∨ ¬B
- ¬(A ∨ B) = ¬A ∧ ¬B

In Worten: Bei der Negation einer Klammer wird jedes Element negiert und das
Verknüpfungszeichen gekippt — aus UND wird ODER und umgekehrt.

Alltagsbeispiel aus der Vorlesung: „Wenn Milch oder Zucker enthalten ist, trinke
ich den Kaffee nicht" ist wertgleich mit „Wenn ich den Kaffee trinke, ist keine
Milch und kein Zucker enthalten."

Praktische Bedeutung: Eine Konjunktion lässt sich durch drei Negationen und eine
Disjunktion darstellen und umgekehrt. Dadurch können Gattertypen gegeneinander
ausgetauscht und Bauteile eingespart werden — man kommt mit reinen NAND- oder
reinen NOR-Gattern aus.

### Verknüpfungen mit zwei Eingangsvariablen

| Verknüpfung | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| UND (Konjunktion) | 0 | 0 | 0 | 1 |
| ODER (Disjunktion) | 0 | 1 | 1 | 1 |
| NAND | 1 | 1 | 1 | 0 |
| NOR | 1 | 0 | 0 | 0 |
| XOR (Antivalenz) | 0 | 1 | 1 | 0 |
| Äquivalenz | 1 | 0 | 0 | 1 |
| 1. Implikation | 1 | 1 | 0 | 1 |
| 2. Implikation | 1 | 0 | 1 | 1 |

### Anzahl möglicher Verknüpfungen — klausurrelevant

**Kap. 3/29.** Bei `n` Eingangsvariablen gibt es

- `K = 2^n` Kombinationsmöglichkeiten der Eingangswerte (Zeilen der Wahrheitstabelle)
- `V = 2^K = 2^(2^n)` mögliche Verknüpfungen

Für n = 2 also K = 4 Zeilen und V = 16 Verknüpfungen — genau die 16 Spalten, aus
denen die Tabelle oben acht benannte herausgreift. Die handschriftliche Notiz auf
der Folie hält fest, dass in der Klausur maximal drei Variablen zu erwarten sind;
das ergäbe K = 8 und V = 256.

### Vorrangregeln

Ein Detail, das in der Klausur Punkte kostet, weil deutsche und amerikanische
Norm sich unterscheiden:

| | Deutsche Norm | US-Norm |
|---|---|---|
| Negation | bindet stärker als ∧ und ∨ | bindet stärker als ∧ und ∨ |
| ∧ gegen ∨ | **binden gleich stark** | ∧ bindet stärker als ∨ (Punkt vor Strich) |
| ∧, ∨, NAND, NOR gegen ≡, ≢ | binden stärker | binden stärker |
| Klammern | nur Außenklammern weglassbar | alle Klammern weglassbar |

> **Empfehlung aus der Vorlesung:** Bei ODER immer klammern, ebenso beim Anwenden
> der De Morganschen Gesetze auf NAND und NOR. Da nach deutscher Norm UND und ODER
> gleich stark binden, ist ein unklammerter Ausdruck dort mehrdeutig.

**Fundstellen:** Kap. 3/3–43, Handout H6.

---

## Teil 3 — Normalformen und Minimierung

Das rechenintensivste Kapitel und nach den Markierungen der Klausurschwerpunkt.

### DNF und KNF

Eine **Normalform** gibt den logischen Zusammenhang disjunktiv oder konjunktiv
wieder, ohne dass gekürzt wurde.

**Disjunktive Normalform (DNF).** Man betrachtet alle Zeilen der Wahrheitstabelle,
in denen die Ausgangsvariable 1 ist. Für jede dieser Zeilen bildet man einen
**Minterm**: alle Eingangsvariablen UND-verknüpft, dabei wird eine Variable negiert
notiert, wenn sie in der Zeile 0 ist, und nicht negiert, wenn sie 1 ist. Alle
Minterme werden ODER-verknüpft. Kurz: UND vor ODER.

**Konjunktive Normalform (KNF).** Man betrachtet alle Zeilen, in denen die
Ausgangsvariable 0 ist. Für jede bildet man einen **Maxterm**: alle Variablen
ODER-verknüpft, dabei negiert, wenn sie in der Zeile 1 ist, nicht negiert, wenn
sie 0 ist. Alle Maxterme werden UND-verknüpft.

Beispiel für drei Variablen a, b, c:

| Nr. | a | b | c | Y | Minterm | Maxterm |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | m₀ = ¬a·¬b·¬c | M₀ = a+b+c |
| 1 | 0 | 0 | 1 | 0 | m₁ = ¬a·¬b·c | M₁ = a+b+¬c |
| 2 | 0 | 1 | 0 | 0 | m₂ = ¬a·b·¬c | M₂ = a+¬b+c |
| 3 | 0 | 1 | 1 | 1 | m₃ = ¬a·b·c | M₃ = a+¬b+¬c |
| 4 | 1 | 0 | 0 | 1 | m₄ = a·¬b·¬c | M₄ = ¬a+b+c |
| 5 | 1 | 0 | 1 | 0 | m₅ = a·¬b·c | M₅ = ¬a+b+¬c |
| 6 | 1 | 1 | 0 | 0 | m₆ = a·b·¬c | M₆ = ¬a+¬b+c |
| 7 | 1 | 1 | 1 | 1 | m₇ = a·b·c | M₇ = ¬a+¬b+¬c |

Daraus: `Y = m₃ ∨ m₄ ∨ m₇` als DNF und `Y = M₀ ∧ M₁ ∧ M₂ ∧ M₅ ∧ M₆` als KNF.

> **Merksatz:** DNF sammelt die Einsen, KNF sammelt die Nullen. Die Negation dreht
> sich jeweils um: In der DNF wird negiert, was 0 ist; in der KNF wird negiert,
> was 1 ist.

Maxterme gewinnt man aus Mintermen durch Anwendung von De Morgan. Und man kann
jede Normalform in die andere überführen: Ist eine Funktion als DNF gegeben,
erhält man die KNF, indem man die DNF der Umkehrfunktion bildet und diese
invertiert.

### Das Aufzug-Beispiel — klausurrelevant

**Kap. 3/45–49.** In einem Gebäude mit acht Stockwerken verbindet ein Aufzug die
Stockwerke 4, 5, 6, 7 und die Eingangshalle. Die Geschossnummer liegt dreistellig
binär codiert vor (c, b, a). Gesucht ist das Haltesignal Y mit Y = 1 für „darf
halten".

| c | b | a | Y |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Die DNF hat fünf Minterme:

```
Y = ¬a¬b¬c  ∨  ¬a¬b c  ∨  a¬b c  ∨  ¬a b c  ∨  a b c
```

Ausklammern von c über die vier Minterme mit c = 1 und anschließendes Anwenden
von A ∨ ¬A = 1 sowie 1 ∧ X = X liefert

```
Y = ¬a¬b¬c ∨ c
```

Ein letzter Schritt fehlt hier noch: Nach der Absorptionsregel `X¬c ∨ c = X ∨ c`
fällt das ¬c weg. Die Minimalform lautet

```
Y = (¬a ∧ ¬b) ∨ c
```

Also: halten, wenn c = 1 ist, oder wenn a und b beide 0 sind — letzteres trifft
nur auf die Eingangshalle zu. Das ist der ganze Witz der Minimierung: aus fünf
Termen mit je drei Variablen werden zwei Terme mit zusammen drei Variablen.

> **Kontrolle:** Minimalformen immer gegen die Wahrheitstabelle prüfen. Alle acht
> Zeilen einsetzen kostet eine Minute und fängt genau die Flüchtigkeitsfehler ab,
> die beim Ausklammern entstehen.

### KV-Diagramm

Die grafische Minimierung nach Karnaugh und Veitch (1952/53) ist bis etwa sechs
Variablen praktikabel.

Aufbauregeln:

- Nachbarfelder unterscheiden sich in **genau einer** Variablen (Gray-Code).
- **Randfelder gelten als benachbart** — die Tafel ist gedanklich ein Torus.
- Bei n Eingangsvariablen gibt es 2^n Felder.
- Jedes Feld erhält den Funktionswert 0 oder 1 aus der Wahrheitstabelle.

Zwei Variablen:

| | ¬A | A |
|---|---|---|
| **¬B** | ¬A·¬B | A·¬B |
| **B** | ¬A·B | A·B |

Drei Variablen — die Feldnummern in der Anordnung der Vorlesung (Kap. 3/62), mit
der Feldnummer als c·4 + b·2 + a:

| | ¬A ¬C | ¬A C | A C | A ¬C |
|---|---|---|---|---|
| **¬B** | 0 | 4 | 5 | 1 |
| **B** | 2 | 6 | 7 | 3 |

Man prüft die Gray-Bedingung, indem man von Spalte zu Spalte geht: Es ändert sich
jeweils genau eine Variable, und das gilt auch beim Übergang von der letzten
Spalte zurück zur ersten.

Vier Variablen ergeben 16 Felder in einer 4×4-Tafel, ebenfalls Gray-codiert in
beiden Richtungen.

### Minimierungsverfahren — die vier Regeln

Aus Handout 4, wörtlich das Prüfungsschema:

1. In die nummerierten Felder des KV-Diagramms die Signalwerte eintragen.
2. Symmetrisch liegende 1-Felder zu Zweier-, Vierer-, Achterblöcken einkreisen.
3. Jedes 1-Feld muss mindestens einmal eingekreist sein. Möglichst große
   Einkreisungen finden.
4. Bei Zweier-, Vierer-, Achtereinkreisungen entfallen genau 1, 2, 3 Variablen.

> **Merksatz zu Regel 4:** Die Blockgröße bestimmt, wie viele Variablen wegfallen.
> Ein Block der Größe 2^k eliminiert k Variablen. Deshalb: immer so groß wie
> möglich einkreisen, Überlappungen sind erlaubt und oft nötig.

Aus jedem Block liest man den Term ab, der aus genau den Variablen besteht, die
innerhalb des Blocks konstant bleiben — negiert, wenn sie konstant 0 sind, nicht
negiert, wenn konstant 1.

### Konjunktive Minimalform

Fasst man statt der Einsen die **Nullen** zusammen, erhält man die disjunktive
Minimalform der negierten Funktion ¬Y. Wendet man darauf De Morgan an, ergibt
sich die konjunktive Minimalform von Y.

Das ist genau der Weg, den Übungsblatt 1 verlangt („nichtnegierte KNF-Minimalform").

### Don't-Care-Terme — klausurrelevant

**Kap. 3/70.** Manche Eingangskombinationen können technisch nicht auftreten oder
ihr Ergebnis ist gleichgültig. Diese Redundanzen trägt man als **X** in die
KV-Tafel ein.

Ein X darf nach Belieben als 0 oder als 1 gelesen werden — je nachdem, was größere
Blöcke ermöglicht. Ein X, das keinen Block vergrößert, lässt man einfach
außerhalb; es muss **nicht** überdeckt werden. Nur echte Einsen müssen überdeckt
sein.

> **Häufiger Fehler:** X-Felder zwingend mit einkreisen. Richtig ist: X nur dann
> einbeziehen, wenn es einen Block vergrößert.

### Analyse eines gegebenen Schaltnetzes

Der laut Übungsblatt 1 wahrscheinlichste Klausuraufgabentyp: *Schaltplan wird
vorgegeben, Wahrheitstabelle und KV-Diagramm sind daraus zu entwickeln.*

Vorgehen (Kap. 3/56–57):

1. Schaltung von den Eingängen zum Ausgang durchlaufen, an jedem Gatterausgang
   einen Hilfsnamen h₁, h₂, … vergeben und dessen Funktion notieren.
2. Die Hilfsfunktionen ineinander einsetzen, bis der Ausgang als Funktion der
   Eingangsvariablen dasteht.
3. Für alle 2^n Eingangskombinationen den Ausgangswert ausrechnen →
   Wahrheitstabelle.
4. Werte in die KV-Tafel eintragen, Blöcke bilden, Minimalform ablesen.
5. Minimierte Funktion als Funktionsplan (FUP) zeichnen.

**Fundstellen:** Kap. 3/44–75, Handout H6, Handout 4 (kombinatorische SN),
Übungsblätter 1 und 2, KV-Vorlage H12.

---

## Teil 4 — Schaltnetze: Laufzeiten und Hazards

### Gatterverzögerung

Eine Änderung am Gattereingang wirkt sich erst nach einer Verzögerung am Ausgang
aus — der **Gatterverzögerung** oder propagation delay time. Typische
Größenordnung: 100 Pikosekunden bis 100 Nanosekunden, je nach Logikfamilie. Die
Verzögerung bei fallender Flanke kann sich von der bei steigender unterscheiden.

Damit ist die Grundannahme der Schaltalgebra — alle Schaltzeiten null — in der
Realität verletzt.

### Glitch und Hazard

| Begriff | Definition |
|---|---|
| Glitch | eine nicht beabsichtigte Signaländerung am Ausgang eines Logikgatters |
| Hazard | eine Konfiguration, bei der ein Glitch auftreten **kann**, aber nicht muss |

Ein Glitch entsteht, wenn verschiedene Pfade durch ein Schaltnetz unterschiedliche
Laufzeiten haben. Beispiel: Nach boolescher Algebra ist A ∧ ¬A immer 0. Führt man
¬A aber über einen Inverter mit Laufzeit, entsteht beim Umschalten ein kurzer
Zeitraum, in dem beide Eingänge 1 sind — am Ausgang erscheint ein kurzer Puls.

Man unterscheidet **statische Hazards** (der Ausgang sollte konstant bleiben,
zeigt aber einen kurzen Ausreißer) und **dynamische Hazards** (der Ausgang soll
einmal wechseln, wechselt aber mehrfach).

### Hazardfreie Konstruktion

Beobachtung aus der Vorlesung (Kap. 3/85): *Hazards entstehen, wenn zwei
Primterm-Blöcke im KV-Diagramm überlappungsfrei aneinandergrenzen.*

Lösung (Kap. 3/86): Mit zusätzlichen Gattern erzeugt man einen weiteren
Primterm-Block, der die Überlappung der 1-Menge garantiert. Man fügt also
bewusst einen redundanten Term hinzu — die Schaltung wird größer, aber sicher.

> **Merksatz:** Minimale Schaltung und hazardfreie Schaltung sind nicht dasselbe.
> Hazardfreiheit kostet einen zusätzlichen, logisch redundanten Term.

**Fundstellen:** Kap. 3/76–88.

---

## Teil 5 — VPS und Kontaktsteuerung

### Steuerungsarten

Drei Arten werden unterschieden (Kap. 4/5–8):

- **binäre Steuerung** — Signalverarbeitung mit binären Signalen, z. B. Vorschubtisch
  einer Schleifmaschine, der ständig hin und her fährt
- **kombinatorische Steuerung** — mehrere Bedingungen werden logisch verknüpft,
  z. B. Zünden eines Schweißbrenners nur wenn Zelle geschlossen, Tür zu,
  Kühlwasserpumpe läuft, Roboter läuft und keine Störung
- **digitale Steuerung** — Signalverarbeitung codiert in Zahlen, z. B. CNC

Bei sequentiellen Steuerungen (Ablaufsteuerungen) löst der vorherige Schritt nach
Erfüllung einer Weiterschaltbedingung den Folgeschritt aus. Zwei Typen:
**zeitgeführt** (Weiterschaltung nach Ablauf einer Zeit; wird immer seltener
eingesetzt, weil zu unflexibel) und **prozessgeführt** (Weiterschaltung durch
Ereignisse aus dem Prozess).

### VPS gegen SPS

| Merkmal | VPS | SPS |
|---|---|---|
| Hardware | aufgabenspezifisch (elektronische Baugruppe) | weitgehend aufgabenneutral (Mikrorechner) |
| Funktionsrealisierung | elektrische Verbindungen zwischen Komponenten (Signalfluss) | als Programm abgespeicherte Anweisungssequenz |
| Interne Verarbeitung | zeitlich parallel | zeitzyklisch, im Zyklus seriell |
| Arbeitsgeschwindigkeit | sehr hoch (Gatterlaufzeiten) | weniger hoch |
| Aufgabenänderung | Neuentwurf oder Neuverdrahtung | Neuprogrammierung |

Der Punkt „parallel gegen seriell" ist die Wurzel vieler SPS-Eigenheiten: Weil die
SPS seriell abarbeitet, braucht sie ein Prozessabbild und kennt eine Zykluszeit.

### Relais und Schütze

Beide übertragen Schaltsignale von einem Stromkreis in einen anderen, verstärken
und vervielfachen sie, ohne dass die Kreise galvanisch verbunden sind. Es erfolgt
die **Trennung zwischen Steuer- und Laststromkreis**.

| | Relais | Schütz |
|---|---|---|
| Schaltleistung | bis etwa 1 kW | bis etwa 500 kW |
| Kontakte | einfach unterbrechend | doppelt unterbrechend |
| Löschkammern | meist keine | Lichtbogen-Löscheinrichtungen |
| Bezeichnung | K | Q |

Zusätzlich unterscheidet man **Leistungsschütze** (Schalten großer Lasten, mit
Lichtbogenlöschung) und **Hilfsschütze** (kleinere Steuerspannungen).

### Kennzeichnung von Kontakten — klausurrelevant

**Kap. 4/31, handschriftlich „beschriften in Klausur".** Die Nummerierung ist
genormt und muss sicher sitzen:

| Element | Kennzeichnung |
|---|---|
| Spulenanschlüsse | A1 (+) und A2 (−) |
| Hauptstromkontakte | einstellig: 4 (−) und 3 (+), bei Wechselstrom 1 (~) und 2 (~) |
| Steuerkontakte | zweistellig: erste Ziffer = fortlaufende Ordnungsziffer, zweite Ziffer = Funktionsziffer |
| Funktionsziffer 1/2 | Öffner |
| Funktionsziffer 3/4 | Schließer |

Also: Kontakt „13/14" ist der erste Schließer, „21/22" der zweite Öffner.

Zur Kennzeichnung im Schaltplan kommen drei Aspekte mit eigenen Vorzeichen
(Kap. 4/24): **Produktaspekt** mit Minuszeichen (woraus besteht das Objekt),
**Funktionsaspekt** mit Gleichheitszeichen (was soll es tun), **Ortsaspekt** mit
Pluszeichen (wo steht es).

### Lichtbogen und Funkenlöschung

Beim Öffnen unter Last entsteht durch die Leitungsinduktivität ein Lichtbogen: Die
Induktivität will den Stromfluss aufrechterhalten, die Berührungsfläche wird
kleiner, Stromdichte und Temperatur steigen, die Luft ionisiert und wird leitend.
Folge ist Abbrand — Kontaktmaterial schmilzt und verdampft.

Bei Wechsel- und Drehstrom ist der Abbrand schwächer als bei Gleichstrom, weil im
Nulldurchgang die Ionisierung unterbrochen wird. Konstruktiv versucht man, die
Kontakte möglichst schnell und sprunghaft zu öffnen.

Löschmethoden bei kleinen Leistungen: RC-Kombination, Varistor
(spannungsabhängiger Widerstand), Freilaufdiode. Bei großen Leistungen:
Löschkammern.

### Stromlaufplan

> **Grundregel:** Elektrische Kontaktsteuerungen werden im Schaltplan stets im
> **nicht geschalteten Zustand** dargestellt — also stromlos, Taster unbetätigt.

Zwei Darstellungsformen:

- **ausführlich** — alle Einzelheiten, wird wegen des Umfangs nur noch selten
  verwendet
- **kompakt / aufgelöst** — jedes Betriebsmittel bekommt einen senkrecht
  gezeichneten Stromweg, von oben nach unten und von links nach rechts

Der kompakte Plan wird in **Leistungsteil** und **Steuerteil** getrennt. Im
Steuerteil dient eine Sicherung F1 dem Leitungsschutz. Die Übung Förderband ist
mit „24 V" als klausurrelevant markiert — die Steuerspannung ist typischerweise
24 V, der Leistungsteil liegt am Drehstromnetz L1/L2/L3.

### Grundfunktionen mit Relais

Mit einem Relais oder Schütz kann man übertragen (Hilfsstromkreis auf
Hauptstromkreis), verstärken (kleine Steuerleistung schaltet große Last),
umkehren, verriegeln, allgemein logisch verknüpfen — und speichern.

### Selbsthaltung — klausurrelevant

**Kap. 4/42.** Im Stromkreis des Relais K1 liegt ein Schließer desselben Relais
K1, parallel zum EIN-Taster S1. Wird S1 kurz betätigt, zieht K1 an, der Schließer
K1 schließt den zu S1 parallelen Zweig, und K1 bleibt erregt, auch wenn S1
losgelassen wird. Der Einschaltimpuls ist damit gespeichert.

Die handschriftliche Notiz auf dieser Folie bringt die Verbindung zum
Digitaltechnik-Teil auf den Punkt:

> **Schaltnetz = ohne Selbsthaltung. Schaltwerk = mit Selbsthaltung.**

Speichernde Schaltungen gibt es in zwei Varianten, die sich darin unterscheiden,
wie sie auf gleichzeitiges EIN und AUS reagieren:

- **dominierend setzend** — die Erregung hat Vorrang vor dem AUS-Taster
- **dominierend rücksetzend** — der AUS-Taster hat Vorrang

### Typische Schaltungen

| Schaltung | Zweck |
|---|---|
| Kontaktvervielfachung durch Hilfsschütz | mehr Kontakte, als das Hauptschütz bietet |
| Kontaktverriegelung | verhindert, dass zwei Schütze gleichzeitig anziehen |
| Wendeschützschaltung | Drehrichtungsumkehr durch Vertauschen zweier Außenleiter, zwei Schütze Q1 und Q2, zwingend verriegelt |
| Stern-Dreieck-Schaltung | reduzierter Anlaufstrom bei großen Drehstrommotoren mit Kurzschlussläufer; vermeidet Auslösen des Überstromschutzes |

**Fundstellen:** Kap. 4 (54 S.), Handout Schaltzeichen, Handout H3.

---

## Teil 6 — Schaltwerke: Speicher, Zähler, Zeiten

### Vom Schaltnetz zum Schaltwerk

Bisher wurden rein kombinatorische **Schaltnetze** betrachtet: Der Ausgang hängt
nur von der aktuellen Eingangsbelegung ab. Viele Schaltungen brauchen zusätzlich
Speicher oder Zeitglieder — damit werden sie zu **Schaltwerken**. Der Ausgang
hängt dann von Eingang **und** innerem Zustand ab.

**Klausurrelevant (Kap. 7/4):** Diesen Unterschied „ordentlich erklären können",
mit dem Stichwort Speicher.

### SR- und RS-Speicher

Der Unterschied liegt allein im Vorrang bei gleichzeitigem Setzen und Rücksetzen:

| Baustein | Verhalten bei S = 1 und R = 1 |
|---|---|
| **SR** | Setzen dominiert, Ausgang wird 1 |
| **RS** | Rücksetzen dominiert, Ausgang wird 0 |

> **Merkhilfe:** Der **erste** Buchstabe im Bausteinnamen dominiert. SR → S
> gewinnt, RS → R gewinnt.

Nachvollziehen lässt sich das an der Bausteingleichung nach IEC 61131-3:

```
SR:  Q := S OR (NOT R AND Q)      (* S steht aussen, gewinnt *)
RS:  Q := NOT R AND (S OR Q)      (* R steht aussen, gewinnt *)
```

In der Sicherheitstechnik ist fast immer **rücksetzdominant** gefordert: Ein
gleichzeitiges AUS muss gewinnen.

Für den systematischen Programmentwurf mit mehreren Speichern empfiehlt Handout 4
die **RS-Tabelle**: Man betrachtet Ausgangsvariablen (Schütze, Hilfsschütze) als
Speicher und trägt je Speicher Setz- und Rücksetzbedingung ein.

| Speicherglied | Setzbedingung | Rücksetzbedingung |
|---|---|---|
| Q1 | K1 ∧ Q2 … | B1 ∨ B2 … |
| K1 | K2 ∧ Q1 … | B1 ∨ B2 … |

### Zähler

Der Standardbaustein nach IEC 61131 ist **CTUD** — count up/down. Er zählt bei
steigender Flanke an CU aufwärts, an CD abwärts, wird über LOAD auf einen Wert PV
gesetzt und über RESET genullt. Ausgänge signalisieren das Erreichen der Grenzen.
Anwendungsbeispiel aus der Vorlesung: Parkhausanzeige.

### Zeitglieder

**TON** ist die Einschaltverzögerung: Liegt IN für die Zeit PT durchgehend an,
wird Q wahr. Fällt IN vorher ab, beginnt die Zeit von vorn. **TOF** ist die
Ausschaltverzögerung, **TP** der Impuls fester Länge.

### Flankenauswertung

Zur Flankenauswertung gehören zwei Operanden: ein **Flankenoperand F0**, der den
veränderten Signalwert speichert, und ein **Impulsoperand I0**, der beim Auftreten
der Flanke für die Dauer **eines Programmzyklus** den Wert 1 führt.

In Codesys stehen dafür die Bausteine **R_TRIG** (steigende Flanke, 0 → 1) und
**F_TRIG** (fallende Flanke) zur Verfügung.

Auf den Impulsoperanden kann verzichtet werden, wenn die Flankenauswertung nur an
einer Stelle des Programms gebraucht wird — dann wird der Ausgang direkt
verwendet, etwa zum Setzen eines SR-Speichers.

**Fundstellen:** Kap. 4.2 (22 S.), Handout 4, Handout Funktionsbausteine FUP.

---

## Teil 7 — Speicherprogrammierbare Steuerungen

### Aufgaben und Aufbau

Eine SPS (englisch PLC) ist ein digital programmiertes Gerät zur Steuerung oder
Regelung einer Maschine oder Anlage. Typische Aufgaben:

- binäre Informationsverarbeitung: logische Funktionen, Speicherfunktionen,
  Zeitfunktionen, Zählfunktionen, Flankenerkennung
- analoge Informationsverarbeitung: Konditionierung (Verstärkung, Skalierung,
  Filterung), Selektion (Grenzwerte, Begrenzung, Maximumauswahl), Kombination,
  Transformation
- Steuern im engeren Sinne, Messen, Stellen, Regeln

Die CPU besteht aus **Steuerwerk** (Befehlszähler, Befehlsregister, Befehlsdecoder,
Operationssteuerung — arbeitet das Programm sequentiell ab) und **Rechenwerk**
(ALU, führt Bit-, Byte- und Wortoperationen aus). Dazu kommen **Arbeitsspeicher**
(Abarbeitung des Anwenderprogramms), **Ladespeicher** (Code- und Datenbausteine,
Hardwarekonfiguration) und **Systemspeicher** (Operandenbereiche Merker, Zeiten,
Zähler sowie die Prozessabbilder und Lokaldaten).

### EVA-Prinzip und Zyklus

Eine SPS arbeitet nach dem **EVA-Prinzip**: Eingabe — Verarbeitung — Ausgabe.

Der Zyklus läuft in drei Phasen:

1. **Prozessabbild der Eingänge (PAE) erstellen** — alle Eingänge werden einmalig
   eingelesen und eingefroren
2. **Anwenderprogramm abarbeiten** — Anweisung für Anweisung, seriell
3. **Prozessabbild der Ausgänge (PAA) ausgeben** — alle Ausgänge werden gesetzt

Die **Zykluszeit T_Z** ist die Zeit für einen kompletten Durchlauf einschließlich
aller Kommunikationsaufgaben. Sie hängt von der Anzahl der Anweisungen ab.
Höherpriorisierte Tasks unterbrechen den Zyklus und verlängern ihn.

Die **Reaktionszeit** ist die Zeitdauer zwischen der Änderung eines
Eingangssignals und der Reaktion am Ausgang. Sie ist im ungünstigsten Fall
deutlich länger als die Zykluszeit: Ändert sich ein Eingang kurz nach dem
Einlesen, wird er erst im nächsten Zyklus erfasst und wirkt sich erst am Ende
dieses Zyklus aus.

Echtzeitfähigkeit erreicht die SPS über eine geringe Zykluszeit.

### Konsequenzen der zyklischen Bearbeitung

Vorteil: Die Rechenleistung wird immer genutzt, Zykluszeiten müssen nicht
berechnet werden.

Nachteile, die in der Klausur gern abgefragt werden:

- Weil die Rechenzeit schwanken kann, ist das System streng genommen **nicht
  deterministisch**.
- Zeitkritische Programmteile werden durch Änderungen an ganz anderer Stelle
  beeinflusst.
- Das Programm rechnet grundsätzlich mit Werten aus dem Prozessabbild — andernfalls
  könnten Eingangssignale innerhalb eines Zyklus mit unterschiedlichen Werten
  eingehen.
- **Mehrfachzuweisungen führen immer zu Programmfehlern:** Wird ein Ausgang
  mehrfach geschrieben, überschreibt der spätere Wert den früheren im PAA.

### Programmorganisationseinheiten

Nach DIN EN 61131-3:

| POU | Eigenschaft |
|---|---|
| Programm (PLC_PRG) | Zyklusbaustein, Hauptprogramm |
| Funktionsbaustein FB | parametrierbar, **mit** Speicher |
| Funktion FC | parametrierbar, **ohne** Speicher |

### Die fünf Programmiersprachen

| Kürzel | Name | Bezug | Zielstellung |
|---|---|---|---|
| IL / AWL | Anweisungsliste | Assemblersprache | laufzeit- und speicheroptimierte Programme |
| LD / KOP | Kontaktplan | Stromlaufplan für Relaissteuerungen | Verknüpfungssteuerungen |
| FBD / FUP | Funktionsbausteinsprache | Logikplan | komplexe Verarbeitungsstrukturen |
| ST / SCL | Strukturierter Text | Hochsprache (Pascal-artig) | Datenverarbeitungsaufgaben |
| SFC / AS | Ablaufsprache | Funktionsplan nach DIN EN 60848 | sequentielle Vorgänge, Schrittketten |

Alle fünf sind in DIN EN 61131-3 genormt. Herstellerspezifisch kommen S7-HiGraph
(Zustandsgraph) und CFC (Continuous Function Chart) hinzu.

**Kontaktplan** wird wie ein Stromlaufplan von links nach rechts gelesen: UND ist
Reihenschaltung, ODER ist Parallelschaltung. Jeder Kontaktplan muss mit einer
Zuweisung, einem Funktions- oder Bausteinaufruf abgeschlossen werden.

**Strukturierter Text** ist zeilenweise aufgebaut, Kommentare beginnen mit `//`.

```
(* Wertzuweisung *)
A1.0 := E1.0 AND E1.1;   // Ergebnis der UND-Verknuepfung

(* Kontrollanweisung *)
IF Wert1 <= Wert2 THEN
    A1.0 := TRUE;
END_IF;
```

### Variablen mit festen Speicherbereichen

Der Systemspeicher ist in Operandenbereiche aufgeteilt: Eingänge E (I), Ausgänge
A (Q), Merker M. Bei Siemens zusätzlich Datenbaustein DB sowie bei S7-300/400
Zeiten T und Zähler Z.

Die Adressierung nach IEC 61131-3 setzt sich zusammen aus Prozentzeichen, Präfix
für den Speicherort, Präfix für die Größe und einer oder mehreren durch Punkte
getrennten Zahlen.

| Präfix Speicherort | | Präfix Größe | |
|---|---|---|---|
| I (E) | Eingang | X | Bit |
| Q (A) | Ausgang | B | Byte |
| M | Merker | W | Wort |
| DB | Datenbaustein | D | Doppelwort |
| T / Z | Zeiten / Zähler | L | Langwort |

Beispiele: `%IX136.1` ist das Eingangsbit 136.1, `%QW800` das Ausgangswort 800,
`%MD10` das Merker-Doppelwort 10.

### IEC-Datentypen

| Schlüsselwort | Typ | Größe | Wertebereich |
|---|---|---|---|
| BOOL | Einzelbit | 1 Bit | FALSE, TRUE |
| BYTE | Bitfolge | 8 Bit | 16#00 … FF |
| WORD | Bitfolge | 16 Bit | 16#0000 … FFFF |
| DWORD | Bitfolge | 32 Bit | 16#0000_0000 … FFFF_FFFF |
| INT | Festpunktzahl | 16 Bit | −32768 … +32767 |
| DINT | Festpunktzahl | 32 Bit | −2147483648 … +2147483647 |
| REAL | Gleitpunktzahl | 32 Bit | 341.7 oder 3.417E+02 |
| TIME | Zeitdauer | 32 Bit | t#12h20m30s |
| TIME_OF_DAY | Uhrzeit | 32 Bit | tod#08:36:12 |
| DATE | Datum | 16 Bit | d#1990-01-01 |
| STRING | ASCII-Zeichen | variabel | Zeichenfolge |

Zu beachten: BYTE, WORD und DWORD sind nicht zwingend vorzeichenlose Dualzahlen,
sondern auch reine Bitfolgen, deren Bits keine Stellenwertigkeit haben.

### Namenskonvention für Variablen

Ein Variablenname setzt sich aus drei Bestandteilen zusammen, in der Reihenfolge
Anwendungsbereich, Kontrolle, Datentyp:

| Datentyp | | Anwendungsbereich | | Kontrolle | |
|---|---|---|---|---|---|
| Bool | x | Global | g | Input | i |
| Integer | i | Local | l | Output | o |
| Real | r | POU-Parameter | p | | |
| Time | tim | Temporäre Variable | tmp | | |
| Date | dt | | | | |
| Char | c | | | | |
| Word | w | | | | |
| String | str | | | | |

Beispiel: `gixS1` ist eine globale Eingangsvariable vom Datentyp BOOL.

### Zuordnungstabelle

Die Zuordnungstabelle verbindet die technologische Beschreibung mit den
SPS-Adressen und ist in fast jeder Übungsaufgabe der erste Teilschritt. Sie
enthält je Signal: Betriebsmittelkennzeichen, Bedeutung im Klartext, Signalart
(Öffner/Schließer), logische Zuordnung und SPS-Adresse.

| BMK | Bedeutung | Art | Logik | Adresse |
|---|---|---|---|---|
| S1 | EIN-Taster | Schließer | betätigt = 1 | %IX0.0 |
| S0 | AUS-Taster | Öffner | betätigt = 0 | %IX0.1 |
| Q1 | Leistungsschütz Motor | — | angezogen = 1 | %QX0.0 |

> **Fallstrick:** Öffner. Ein AUS-Taster wird als Öffner ausgeführt (Drahtbruch­sicherheit).
> Im Programm muss er deshalb **nicht** negiert abgefragt werden — der unbetätigte
> Öffner liefert bereits 1.

**Fundstellen:** Kap. 5 (28 S.), Handout H3, Handout 4, Handout FUP-Bausteine.

---

## Teil 8 — Ablaufsteuerung und SFC

### Definition

Die DIN IEC 60050-351 bezeichnet eine Ablaufsteuerung als „eine Steuerung mit
schrittweisem Ablauf, bei der der Übergang von einem Schritt auf den folgenden
programmgemäß entsprechend den vorgegebenen Übergangsbedingungen
(Weiterschaltbedingungen, Transitionen) erfolgt".

Merkmale:

- Es ist **immer nur ein Schritt aktiv** (bei linearer Kette).
- Der Übergang erfolgt, wenn die Weiterschaltbedingung erfüllt ist. Ist sie
  erfüllt, **muss** weitergeschaltet werden.

### Gesamtstruktur

Eine Ablaufsteuerung gliedert sich in vier Teile: **Ablaufkette**, **Betriebsarten**,
**Meldungen** und **Befehlsausgabe**.

Kernstück ist die **Ablaufkette**. Sie hat eine eindeutige zeitliche und funktionale
Zuordnung zu den technologischen Abläufen. Daraus folgen hohe Übersichtlichkeit,
gute Wartungsfreundlichkeit und schnelle Fehlersuche — man muss nur zwischen
Weiterschaltbedingung und Befehlsausgabe unterscheiden.

Ein konkreter Schaltzustand der Anlage wird durch einen **Schritt** dargestellt.
Ist ein Schritt aktiv, sind alle ihm zugeordneten qualifizierten Befehle aktiv.
Die Kette beginnt mit einem **Anfangsschritt** (initial step), der die Anlage in
Grundstellung bringt. Nach Beendigung geht die Kette in die Grundstellung zurück.

### Betriebsarten

| Betriebsart | Bedeutung |
|---|---|
| Automatik (AUT) | Ablauf programmgemäß ohne Bedienereingriff |
| Hand | Bediener greift direkt auf den Ausgang durch |
| Einrichten | Stellgeräte einzeln, unter Umgehung vorhandener Verriegelungen |
| Tippbetrieb / Einzelschritt | Weiterschaltung auf den nächsten Schritt durch Bedieneingriff |

Um eine Ablaufsteuerung im industriellen Umfeld scharf zu schalten, muss das
hochgeladene Programm zunächst in den Automatikmodus versetzt werden.

### Zeitgeführt und prozessgeführt

**Zeitgeführt** — die Weiterschaltung erfolgt nach Ablauf einer Zeit. Unflexibel,
weil die Anlage nicht auf tatsächliche Ereignisse reagiert; wird zunehmend
seltener eingesetzt.

**Prozessgeführt** — die Weiterschaltung erfolgt durch Ereignisse aus dem Prozess,
gemeldet über Sensoren.

### Strukturelemente

Wesentliche Elemente sind **Schritte/Zustände mit zugehörigen Aktionen** und
**Transitionen**.

Aktionsarten: kontinuierlich wirkend; kontinuierlich wirkend, aber von einer
Bedingung abhängig; zeitgesteuert.

Transitionsarten: einfache Transition; zeitgesteuerte Transition;
Abfallverzögerung.

### Verzweigungen

**ODER-Verzweigung (Alternativverzweigung).** Von mehreren Kettensträngen wird
nur einer bearbeitet. Am Anfang der Verzweigung darf nur **eine**
Weiterschaltbedingung wahr sein, sonst muss eine Priorität vorgegeben werden. Ein
Stern zeigt an, dass die Bedingungen von links nach rechts abgearbeitet werden —
der linke Strang hat dann die höhere Priorität.

> **Entwurfsfalle:** Es darf nicht eine Bedingung immer sofort erfüllt sein, sonst
> besteht keine Chance, je eine Alternative zu wählen.

Beispiel: Ergebnis einer Qualitätskontrolle. Ist das Teil nicht in Ordnung, wird
es ausgeschleust; nach Nachbearbeitung kann es wieder integriert werden, was in
der Kette einen Sprung oder eine Schleife erzeugt.

**UND-Verzweigung (Simultanverzweigung).** Mehrere Stränge laufen parallel. Nach
DIN IEC 60050-351 werden durch **eine** Weiterschaltbedingung alle parallelen
Zweige aktiviert und nur durch Erfüllung einer **gemeinsamen**
Weiterschaltbedingung wieder zusammengeführt.

Beispiel: Zwei Bauteile müssen alle vorgelagerten Arbeitsgänge durchlaufen haben,
bevor die Montage starten kann.

Wird die Kette nicht in einer Ablaufsprache, sondern etwa in FUP implementiert,
muss man selbst sicherstellen, dass bei der ODER-Verzweigung nur ein Strang
durchlaufen wird und bei der UND-Verzweigung die Weiterführung erst nach
Beendigung **jedes** parallelen Strangs erfolgt.

### Normen und Werkzeuge

Die Darstellung ist in IEC 61131-3 und DIN EN 60848 (GRAFCET) geregelt.
Herstellerwerkzeuge setzen darauf auf: S7-GRAPH bei Siemens, SFC (Sequential
Function Chart) in Codesys.

**Fundstellen:** Kap. 6 (37 S.), Handout Ablaufsprache, Übungsblatt 6.

---

## Teil 9 — Endliche Automaten

### Schaltwerk und Automat

Ein Schaltwerk mit Speichern ist dasselbe wie ein **endlicher Zustandsautomat**:
Der Ausgang hängt vom Eingang und vom gespeicherten Zustand ab, und der Zustand
ändert sich getaktet.

Formal wird ein endlicher Automat beschrieben durch Zustandsmenge, Eingabemenge,
Ausgabemenge, Übergangsfunktion und Ausgabefunktion sowie einen Anfangszustand.

### Mealy und Moore — klausurrelevant

**Kap. 7/8, handschriftlich: Automatentyp erkennen und umwandeln.**

| | Moore | Mealy |
|---|---|---|
| Ausgabefunktion hängt ab von | **nur** vom aktuellen Zustand | Zustand **und** Eingang |
| Notation im Graphen | Ausgabe steht **im Zustandskreis** | Ausgabe steht **an der Kante**, als `Eingang / Ausgabe` |
| Reaktion | verzögert, erst im Folgezustand | sofort im selben Takt |
| Zustandsanzahl | tendenziell mehr | tendenziell weniger |

Die Musterbegründung steht handschriftlich auf Übung 7: *„Moore-Automat, weil die
Ausgabefunktion y nur vom aktuellen Zustand abhängig ist."* Genau diese
Formulierung ist in der Klausur gefragt.

**Umwandlung Mealy → Moore:** Für jede Kombination aus Zustand und dort
auftretender Ausgabe einen eigenen Zustand anlegen und die Ausgabe in den Zustand
verschieben.
**Umwandlung Moore → Mealy:** Die Ausgabe aus dem Zustand an alle eingehenden
Kanten schreiben.

### Akzeptor und Transduktor

Zwei Anwendungsbereiche endlicher Automaten:

- **Akzeptor** — prüft, ob eine Eingabefolge zu einer Sprache gehört. Kennt
  akzeptierende Endzustände. Ausgabe ist im Kern ja/nein.
- **Transduktor** — erzeugt zu jeder Eingabe eine Ausgabe, wandelt also
  Eingabefolgen in Ausgabefolgen um. Beispiel aus der Vorlesung: Game-Design.

### Zustandsübergangsgraph und Folgezustandstabelle

Der **Zustandsübergangsgraph** zeigt Zustände als Kreise und Übergänge als
beschriftete Pfeile. Die **Folgezustandstabelle** listet zu jeder Kombination aus
aktuellem Zustand und Eingang den Folgezustand und die Ausgabe.

Aufbau der Tabelle bei zwei Zustandsbits z1, z0 und zwei Eingängen e1, e0:

| z1(n) | z0(n) | e1 | e0 | z1(n+1) | z0(n+1) | y |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | … | … | … |
| … | | | | | | |

Die Zahl der Zeilen ist 2^(Zustandsbits + Eingangsbits) — bei zwei plus zwei also
16. Die handschriftliche Notiz zum Warenautomaten hält genau das fest: „alle
Kombinationsmöglichkeiten, 2⁴ gibt es".

### Vom Graphen zur Schaltung

Der Standardweg, den Übung 7 abfragt:

1. **Automatentyp bestimmen** und begründen.
2. **Folgezustandstabelle** aufstellen: alle Kombinationen aus Zustand und Eingang.
3. **KV-Diagramme** aufstellen — je eines für jedes Zustandsbit z1(n+1), z0(n+1)
   und eines für die Ausgangsvariable y. Minimale DNF ablesen.
4. **Schaltplan zeichnen**: Die Zustandsbits werden in D-Flipflops gespeichert,
   die minimierten Gleichungen als Netz aus NOT-, AND- und OR-Gattern davor.

Unzulässige Eingangskombinationen behandelt man als Don't-Care — oder, wenn
gefordert wird, dass der Automat im aktuellen Zustand bleibt, ergänzt man die
Gleichungen so, dass z(n+1) = z(n) für diese Kombination gilt.

### Beispiele aus der Vorlesung

- **Warenautomat** — Zustands-Übergangs-Tabelle mit Zustand, Eingabe,
  Folgezustand, Ausgabe; anschließend Umsetzung als Schaltwerk (Kap. 7/12–15)
- **Ampelschaltung** — Zustandsübergangsgraph über sechs Folien entwickelt
  (Kap. 7/22–27)

**Fundstellen:** Kap. 7 (28 S.), Handout Automaten, Übungsblatt 7.

---

## Formelsammlung

### Boolesche Grundregeln

| | UND | ODER |
|---|---|---|
| Neutralelement | 1 ∧ A = A | 0 ∨ A = A |
| Dominanz | 0 ∧ A = 0 | 1 ∨ A = 1 |
| Idempotenz | A ∧ A = A | A ∨ A = A |
| Komplement | A ∧ ¬A = 0 | A ∨ ¬A = 1 |
| Doppelnegation | ¬¬A = A | |
| De Morgan | ¬(A ∧ B) = ¬A ∨ ¬B | ¬(A ∨ B) = ¬A ∧ ¬B |
| Distributiv | A ∧ (B ∨ C) = (A∧B) ∨ (A∧C) | A ∨ (B ∧ C) = (A∨B) ∧ (A∨C) |

### Abzählformeln

- Zeilen der Wahrheitstabelle bei n Variablen: `K = 2^n`
- Mögliche Verknüpfungen bei n Variablen: `V = 2^K = 2^(2^n)`
- Felder im KV-Diagramm bei n Variablen: `2^n`
- Bei Block der Größe `2^k` entfallen `k` Variablen

### Normalformen

- **DNF**: Zeilen mit Y = 1, Minterme (UND), verknüpft mit ODER. Variable negiert,
  wenn sie 0 ist.
- **KNF**: Zeilen mit Y = 0, Maxterme (ODER), verknüpft mit UND. Variable negiert,
  wenn sie 1 ist.
- Konjunktive Minimalform: Nullen im KV zusammenfassen → disjunktive Minimalform
  von ¬Y → De Morgan anwenden.

### Systeme

- Gleichgewicht kontinuierlich: `dx/dt = 0`
- Gleichgewicht diskret: `x[k+1] − x[k] = 0`
- Linearität: `u = α₁u₁ + α₂u₂` → `y = α₁y₁ + α₂y₂`
- Zeitinvarianz: `u(t−T)` → `y(t−T)`

### Kontaktkennzeichnung

- Spule: A1, A2
- Hauptkontakte: einstellig (1/2 bei Wechselstrom, 3/4 bei Gleichstrom)
- Steuerkontakte: zweistellig — Ordnungsziffer, dann Funktionsziffer
- Funktionsziffer 1/2 = Öffner, 3/4 = Schließer
- K = Relais, Q = Schütz

### Speichervorrang

- SR: setzdominant
- RS: rücksetzdominant
- Sicherheitstechnik: rücksetzdominant wählen

### Automaten

- Moore: Ausgabe nur aus Zustand → Ausgabe im Kreis
- Mealy: Ausgabe aus Zustand und Eingang → Ausgabe an der Kante
- Zeilen der Folgezustandstabelle: `2^(Zustandsbits + Eingangsbits)`
