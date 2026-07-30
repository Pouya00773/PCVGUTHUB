# Übungsaufgaben mit Lösungsweg

Alle Minimalformen in diesem Dokument sind rechnerisch geprüft: Die
Wahrheitstabellen wurden vollständig aufgestellt und die angegebenen
Minimalformen gegen die Originalfunktion für jede Eingangskombination
verglichen.

---

## Übung 1 — Wahrheitstabellen und Gatter

Für sieben Gattersymbole ist jeweils die Wahrheitstabelle auszufüllen und der
Ausgangsverlauf Z zu zeichnen.

> **Achtung, Reihenfolge der Spalten.** Auf dem Blatt sind die Spalten **B, A**
> überschrieben, nicht A, B. Wer schematisch die gewohnte Reihenfolge einträgt,
> vertauscht bei den unsymmetrischen Funktionen die mittleren beiden Zeilen.

| Symbol | Funktion | B A → Z |
|---|---|---|
| `&` | UND: Z = A ∧ B | 00→0, 01→0, 10→0, 11→1 |
| `≥1` | ODER: Z = A ∨ B | 00→0, 01→1, 10→1, 11→1 |
| `&` mit Kreis am Ausgang | NAND: Z = ¬(A ∧ B) | 00→1, 01→1, 10→1, 11→0 |
| `≥1` mit Kreis am Ausgang | NOR: Z = ¬(A ∨ B) | 00→1, 01→0, 10→0, 11→0 |
| `=` | Äquivalenz: Z = A ≡ B | 00→1, 01→0, 10→0, 11→1 |
| `=1` | XOR: Z = A ≢ B | 00→0, 01→1, 10→1, 11→0 |
| `&` mit Kreis am Eingang B | Z = A ∧ ¬B | 00→0, 01→1, 10→0, 11→0 |

Beim Zeichnen des Zeitverlaufs gilt: Z ändert sich genau dort, wo sich A oder B
ändern. Ein Kreis am Eingang negiert **vor** der Verknüpfung, ein Kreis am
Ausgang **danach**.

---

## Übung 1 (Minimierung) — KNF-Minimalformen und FUP

Aus einer gegebenen Wahrheitstabelle sind mit dem KV-Diagramm die
**nichtnegierten KNF-Minimalformen** für Y1, Y2 und Y3 zu bestimmen und in FUP
umzusetzen.

### Der entscheidende Punkt

Gefragt ist die **konjunktive** Minimalform. Der Weg dorthin:

1. Werte in die KV-Tafel eintragen.
2. Nicht die Einsen, sondern die **Nullen** zu Blöcken zusammenfassen.
3. Aus den Nullblöcken die disjunktive Minimalform von **¬Y** ablesen.
4. Auf ¬Y De Morgan anwenden. Ergebnis ist die konjunktive Minimalform von Y.

Beispiel für den letzten Schritt: Ergibt sich aus den Nullen
`¬Y = (¬A ∧ C) ∨ (B ∧ ¬C)`, dann folgt

```
Y = ¬((¬A ∧ C) ∨ (B ∧ ¬C))
  = ¬(¬A ∧ C) ∧ ¬(B ∧ ¬C)
  = (A ∨ ¬C) ∧ (¬B ∨ C)
```

In FUP wird daraus eine ODER-vor-UND-Struktur: je Klammer ein `≥1`-Block, deren
Ausgänge auf einen gemeinsamen `&`-Block laufen.

---

## Übung 2 — Gatterlogik und Kontaktlogik ★ klausurrelevant

Dies ist die vom Dozenten ausdrücklich als klausurrelevant markierte Aufgabe.
Sie entspricht exakt dem Format, das auf Übungsblatt 1 notiert ist: Schaltplan
gegeben, Wahrheitstabelle und KV-Diagramm gesucht.

### Aufgabenstellung

Gegeben ist eine Kontaktschaltung mit der Lampe y und den Schaltern a, b, c, d.
Verlangt sind: Wertetabelle, DNF, Vereinfachung per KV-Diagramm und die Umsetzung
der Kontaktlogik mit digitalen Gattern.

### Schritt 1 — Schaltfunktion aus dem Kontaktplan ablesen

Im Stromlaufplan liegen **a und b parallel**, diese Parallelschaltung liegt in
**Reihe mit c**, und **d liegt parallel** zu dieser ganzen Reihenschaltung.

Übersetzungsregel: Reihenschaltung = UND, Parallelschaltung = ODER.

```
y = ((a ∨ b) ∧ c) ∨ d
```

### Schritt 2 — Wertetabelle

| Nr. | a | b | c | d | y |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 2 | 0 | 0 | 1 | 0 | 0 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 1 | 0 | 0 | 0 |
| 5 | 0 | 1 | 0 | 1 | 1 |
| 6 | 0 | 1 | 1 | 0 | 1 |
| 7 | 0 | 1 | 1 | 1 | 1 |
| 8 | 1 | 0 | 0 | 0 | 0 |
| 9 | 1 | 0 | 0 | 1 | 1 |
| 10 | 1 | 0 | 1 | 0 | 1 |
| 11 | 1 | 0 | 1 | 1 | 1 |
| 12 | 1 | 1 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 | 1 | 1 |
| 14 | 1 | 1 | 1 | 0 | 1 |
| 15 | 1 | 1 | 1 | 1 | 1 |

Elf Einsen, fünf Nullen.

### Schritt 3 — DNF

Die DNF sammelt die elf Einsen als Minterme:

```
y = ¬a¬b¬c d ∨ ¬a¬b c d ∨ ¬a b¬c d ∨ ¬a b c¬d ∨ ¬a b c d
  ∨ a¬b¬c d ∨ a¬b c¬d ∨ a¬b c d ∨ a b¬c d ∨ a b c¬d ∨ a b c d
```

Elf Terme mit je vier Variablen — genau deshalb wird minimiert.

### Schritt 4 — KV-Diagramm und Minimierung

Die fünf Nullen liegen alle dort, wo d = 0 **und** nicht gleichzeitig c mit a
oder b zusammentrifft. Daraus ergeben sich drei Blöcke:

- **d** — ein Achterblock: alle acht Felder mit d = 1 sind 1. Drei Variablen
  entfallen, übrig bleibt `d`.
- **a ∧ c** — ein Viererblock: alle vier Felder mit a = 1 und c = 1. Zwei
  Variablen entfallen.
- **b ∧ c** — ein Viererblock: alle vier Felder mit b = 1 und c = 1.

```
y = d ∨ (a ∧ c) ∨ (b ∧ c)
```

oder zusammengefasst `y = d ∨ c ∧ (a ∨ b)` — was genau die Ausgangsfunktion aus
Schritt 1 ist. Das ist die Kontrolle: Eine korrekt abgelesene Kontaktschaltung
liefert nach der Minimierung wieder die Struktur der Schaltung.

> **Probe:** Zeile 2 (a=0, b=0, c=1, d=0): d = 0, a∧c = 0, b∧c = 0 → y = 0 ✓.
> Zeile 6 (a=0, b=1, c=1, d=0): b∧c = 1 → y = 1 ✓.

### Schritt 5 — Konjunktive Minimalform

Fasst man stattdessen die fünf Nullen zusammen, ergibt sich

```
y = (a ∨ b ∨ d) ∧ (c ∨ d)
```

Auch diese Form ist geprüft und liefert für alle 16 Kombinationen dasselbe
Ergebnis. Sie braucht nur zwei Blöcke und ist damit sogar kompakter als die DNF.

### Schritt 6 — Umsetzung mit digitalen Gattern

Für `y = d ∨ (a ∧ c) ∨ (b ∧ c)`:

- zwei UND-Gatter: `a & c` und `b & c`
- ein ODER-Gatter mit drei Eingängen: die beiden UND-Ausgänge und `d`

Für die konjunktive Form `y = (a ∨ b ∨ d) ∧ (c ∨ d)`:

- ein ODER-Gatter mit drei Eingängen: `a`, `b`, `d`
- ein ODER-Gatter mit zwei Eingängen: `c`, `d`
- ein UND-Gatter über beide ODER-Ausgänge

Die zweite Variante kommt mit drei Gattern statt vier aus.

---

## Übungsblatt 2 — Schaltnetz zur Wasserstandsregelung

### Aufgabenstellung

Ein Wasserbehälter hat zwei Abflüsse AB1 und AB2 und wird über zwei Pumpen P1
und P2 gespeist. Vier Schwimmer X1 bis X4 überwachen den Wasserstand Xw, wobei
X1 der oberste und X4 der unterste ist. Gesucht sind die Wahrheitstabelle
einschließlich einer Fehlervariablen F sowie die minimalen Gleichungen in DNF.

### Schritt 1 — Konvention festlegen

Ein Schwimmer meldet 1, wenn der Wasserstand ihn erreicht hat. Da X4 unten und X1
oben liegt, wird von unten nach oben zugeschaltet: Steigt das Wasser, geht erst
X4 auf 1, dann X3, dann X2, dann X1.

### Schritt 2 — Erlaubte Zustände aus der Aufgabenbeschreibung

| Füllstand | X1 | X2 | X3 | X4 | P1 | P2 | AB1 | AB2 |
|---|---|---|---|---|---|---|---|---|
| unterhalb X4 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| zwischen X4 und X3 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 |
| zwischen X3 und X2 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| zwischen X2 und X1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
| oberhalb X1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 |

Nur **fünf** der 16 Kombinationen sind physikalisch möglich. Die übrigen **elf**
sind unerlaubt.

### Schritt 3 — Fehlervariable F

Eine Kombination ist genau dann unmöglich, wenn ein oberer Schwimmer anspricht,
während ein direkt darunterliegender es nicht tut. Daraus:

```
F = (X1 ∧ ¬X2) ∨ (X2 ∧ ¬X3) ∨ (X3 ∧ ¬X4)
```

Diese Form ist geprüft: Sie liefert für genau die elf unerlaubten Kombinationen
eine 1 und für die fünf erlaubten eine 0. Drei Zweierterme genügen — man muss
nicht elf Minterme aufschreiben.

### Schritt 4 — Minimale Gleichungen der Ausgänge

Für P1, P2, AB1 und AB2 werden die elf unerlaubten Kombinationen als
**Don't-Care** behandelt, weil sie im Betrieb nicht auftreten. Das erlaubt
deutlich größere Blöcke:

```
P1  = ¬X1 ∧ ¬X2
P2  = (¬X1 ∧ X2 ∧ X3 ∧ X4) ∨ (¬X1 ∧ ¬X2 ∧ ¬X3)
AB1 = (X2 ∧ X3 ∧ X4) ∨ (¬X1 ∧ ¬X2 ∧ ¬X3 ∧ X4)
AB2 = X3 ∧ X4
```

Alle vier sind gegen die fünf erlaubten Zustände geprüft.

> **Das ist der Wert der Don't-Cares.** P1 schrumpft auf zwei Literale, obwohl
> die Funktion über drei erlaubte Zustände 1 ist. Ohne Don't-Cares wären die
> Ausdrücke deutlich länger.

---

## Übung Haltegliedsteuerung

### Aufgabenstellung

Zwei AUS-Taster S1 und S2, zwei EIN-Taster S3 und S4, zwei Leuchtmelder H1 und
H2. H2 zeigt den betriebsbereiten Zustand. Wird S3 oder S4 betätigt, zieht Schütz
K1 an, hält sich selbst, schaltet H1 ein und H2 aus. Bei Betätigung von S1 oder
S2 fällt K1 ab, H1 erlischt und H2 wird eingeschaltet.

### Schritt 1 — Kontaktarten festlegen

EIN-Taster S3, S4 sind **Schließer**. AUS-Taster S1, S2 sind **Öffner** — das ist
die sicherheitstechnische Konvention: Bei Drahtbruch fällt die Anlage ab.

### Schritt 2 — Stromlaufplan

Steuerstromkreis von oben (L, 24 V) nach unten (N):

1. In Reihe die beiden Öffner **S1** und **S2**.
2. Danach der Parallelzweig: **S3 ∥ S4 ∥ Selbsthaltekontakt K1** (Schließer).
3. Danach die Spule **K1**.

Die Leuchtmelder liegen in eigenen Strompfaden:

- **H1** über einen Schließer von K1
- **H2** über einen Öffner von K1

### Schritt 3 — Schaltfunktion

Mit S1, S2 als Öffner (unbetätigt = 1):

```
K1 = (S3 ∨ S4 ∨ K1) ∧ S1 ∧ S2
H1 = K1
H2 = ¬K1
```

Der Term `∨ K1` in der eigenen Gleichung ist die Selbsthaltung. Dass K1 auf
beiden Seiten steht, ist kein Fehler, sondern genau das Merkmal eines
Schaltwerks.

### Schritt 4 — Umsetzung in FUP

Sauberer als die Rückkopplung von Hand ist der Speicherbaustein:

```
Setzbedingung    S := S3 ∨ S4
Rücksetzbedingung R := ¬S1 ∨ ¬S2      (Taster betätigt)
```

Als **RS-Baustein**, also rücksetzdominant — ein gleichzeitiges AUS muss
gewinnen. H1 wird direkt vom Ausgang gespeist, H2 über eine Negation.

---

## Übung 3 — Verbindungsprogrammierte Steuerung / SPS

### Aufgabe 1 — dieselbe Logik in vier Sprachen

Gegeben ist ein Funktionsplan für das Schalten eines Schützes Q1. Gesucht sind
Stromlaufplan, Kontaktplan, Strukturierter Text und Anweisungsliste.

Übersetzungstabelle:

| Logik | FUP | KOP | ST | Stromlaufplan | AWL |
|---|---|---|---|---|---|
| UND | `&`-Block | Kontakte in Reihe | `A AND B` | Reihenschaltung | `U A` / `U B` |
| ODER | `≥1`-Block | Kontakte parallel | `A OR B` | Parallelschaltung | `O A` / `O B` |
| NICHT | Kreis am Eingang | Öffnerkontakt | `NOT A` | Öffner | `UN A` |
| Zuweisung | Ausgangspfeil | Spule | `Q := …;` | Spule | `= Q` |
| Setzen | S-Eingang | S-Spule | `IF … THEN Q := TRUE;` | Selbsthaltung | `S Q` |

> Auf dem Übungsblatt ist handschriftlich vermerkt, dass **Aufgabe 2**
> (Belüftungsanlage mit K11, K12, K13) nicht behandelt wird.

### Aufgabe 3 — Förderband

Das Band startet mit dem Taster Start und läuft, bis der Endlagenschalter rechts
eine Kiste erkennt. Dann stoppt es und läuft erst wieder an, wenn der
Endlagenschalter links eine Kiste feststellt. Die Endlagenschalter sind als
**Öffner** (Lichtschranken) ausgeführt.

Speicherlogik:

```
Setzbedingung    Start ∨ Endlage_links
Rücksetzbedingung Endlage_rechts
```

Da die Lichtschranken Öffner sind, liefert eine **freie** Lichtschranke das
Signal 1 und eine **unterbrochene** eine 0. Das Erkennen einer Kiste entspricht
also der 0 — im Programm ist entsprechend auf den negierten Zustand abzufragen.
Genau hier entstehen die meisten Fehler.

---

## Übung 4 — Kombinatorische Schaltnetze

Ein Stellglied K1 wird durch vier Sensoren nach einem gegebenen Stromlaufplan
angesteuert. Die Ansteuerung soll künftig über eine SPS erfolgen.

Der Aufgabenkatalog ist das Standardschema für Typ A und lohnt sich als
Ablaufmuster:

1. Zuordnungstabelle mit SPS-Eingangs- und Ausgangsvariablen
2. Funktionsplan, der der logischen Struktur des Stromlaufplans entspricht
3. Ansteuerfunktion für K1 aus dem Stromlaufplan
4. Funktionstabelle für den Ausgang K1
5. Minimierung mit dem KV-Diagramm
6. Funktionsplan der minimierten Funktion
7. Deklarationsteil und Programm in FUP, KOP oder ST

Punkt 2 und Punkt 6 sind bewusst getrennt: Erst die Struktur eins zu eins
übersetzen, dann minimieren. Wer sofort minimiert, kann den Zwischenschritt nicht
mehr zeigen — und der wird bepunktet.

---

## Übung 5 — Einfache Schaltwerke

### Aufgabe 1 — drei Förderbänder

Nach Betätigung von S1 werden die Motoren im Abstand von 5 Sekunden in der
Reihenfolge M3, M2, M1 eingeschaltet. Bei S2 werden sie in umgekehrter
Reihenfolge mit 10 Sekunden Abstand ausgeschaltet. STOPP-Taster S0 oder Auslösen
eines der Überstromrelais F1, F2, F3 schaltet sofort alles ab.

**Warum diese Reihenfolge?** Eingeschaltet wird **gegen** die Förderrichtung —
das letzte Band im Materialfluss zuerst. Sonst liefe Material auf ein noch
stehendes Band und würde sich stauen.

Lösungsweg mit erweiterter RS-Tabelle:

| Speicher | Setzbedingung | Rücksetzbedingung |
|---|---|---|
| M3 | S1 | S0 ∨ F1 ∨ F2 ∨ F3 ∨ T_aus3 |
| M2 | T_ein1 (5 s nach M3) | S0 ∨ F1 ∨ F2 ∨ F3 ∨ T_aus2 |
| M1 | T_ein2 (5 s nach M2) | S0 ∨ F1 ∨ F2 ∨ F3 ∨ T_aus1 |

Entscheidend: Die Sofortabschaltung `S0 ∨ F1 ∨ F2 ∨ F3` gehört an **jeden**
Speicher, nicht nur an den ersten der Kette.

### Aufgabe 2 — Funktion FC_Max3

Aus drei Realzahlen IN1 bis IN3 ist die größte auszuwählen. Als **Funktion FC**,
also ohne Speicher.

In Strukturiertem Text kompakt:

```
OUT := IN1;
IF IN2 > OUT THEN OUT := IN2; END_IF;
IF IN3 > OUT THEN OUT := IN3; END_IF;
```

In FUP über zweiwertige Vergleichsblöcke, deren Ausgänge zwischengespeichert
werden — deutlich umständlicher. Das ist der Punkt der Aufgabe: Für
Datenverarbeitung ist ST die passende Sprache, für Verknüpfungslogik FUP.

### Aufgabe 3 — Bäckerei, Durchlaufgeschwindigkeit

Ein Taktgenerator mit 10 s Puls und 1 s Pause gibt die Zeitbasis. Während der
Pulszeit werden die Drehimpulse von Sensor B1 gezählt. Pro Impuls legt das
Backgut 0,1 cm zurück.

```
v = (Impulse · 0,1 cm) / 10 s
```

Bei 150 Impulsen also v = 1,5 cm/s. Der Baustein soll den Wert als
**Integerwert** ausgeben — die Division ist also mit Bedacht zu skalieren, damit
keine Nachkommastellen verloren gehen.

---

## Übung 6 — Ablaufsteuerungen

### Aufgabe 1 — drei Pumpen ★ klausurrelevant

Drei Pumpen werden über Q1, Q2, Q3 nacheinander durch **jeweils eine erneute
Betätigung** von S1 eingeschaltet. Mit S0 werden alle laufenden Pumpen
gleichzeitig abgeschaltet.

Ablaufkette:

| Schritt | Aktion | Transition zum nächsten |
|---|---|---|
| 0 (Init) | alle Pumpen aus | S1 |
| 1 | Q1 | S1 |
| 2 | Q1, Q2 | S1 |
| 3 | Q1, Q2, Q3 | — |

Aus jedem Schritt führt S0 zurück zu Schritt 0.

> **Der Fallstrick:** Derselbe Taster S1 wird dreimal verwendet. Ohne
> **Flankenauswertung** (R_TRIG) würde ein einziger langer Tastendruck die
> gesamte Kette in einem einzigen SPS-Zyklus durchlaufen, weil S1 in jedem Zyklus
> weiterhin 1 ist. Die Transitionen müssen auf die **steigende Flanke** von S1
> reagieren, nicht auf den Pegel.

### Aufgabe 2 — Ampel

Grundzustand Grün. S1 leitet die Gelbphase ein: Gelb 3 s, dann Rot, nach 10 s
Rot-Gelb für 2 s, zurück zu Grün.

| Schritt | Aktion | Transition |
|---|---|---|
| 0 | Grün | S1 |
| 1 | Gelb | 3 s abgelaufen |
| 2 | Rot | 10 s abgelaufen |
| 3 | Rot + Gelb | 2 s abgelaufen → zurück zu 0 |

Vier Schritte, drei zeitgesteuerte Transitionen und eine tastergesteuerte.

### Aufgabe 3 — Anlassersteuerung

Beim Drehstrom-Schleifringläufermotor werden Widerstandsgruppen in den
Läuferkreis geschaltet, um den Einschaltstrom zu begrenzen. S1 lässt Q1 anziehen,
dann ziehen Q2, Q3, Q4 nach jeweils 5 s Verzögerung an und schließen R1 bis R3
nacheinander kurz. Nach dem letzten Schütz sind die Schleifringe kurzgeschlossen
und der Motor läuft im Nennbetrieb. S0 schaltet ab.

Lineare Kette aus fünf Schritten mit drei zeitgesteuerten Transitionen à 5 s.

---

## Übung 7 — Automaten ★ mit Punkteschlüssel

Diese Übung trägt als einzige Punkteangaben und ist damit die beste verfügbare
Referenz für das Klausurformat.

### Aufgabe 1 — Automat analysieren, 13 Punkte

| Teilaufgabe | Punkte |
|---|---|
| Automatentyp bestimmen und begründen | 1 |
| Folgezustandstabelle ergänzen | 2 |
| KV-Diagramme für z1(n+1), z0(n+1), y und minimale DNF | 6 |
| Schaltplan mit D-Flipflops sowie NOT-, AND-, OR-Gattern | 3 |
| unzulässige Eingangskombination benennen | 1 |

Der Automat hat die Eingänge {e1, e0}, den Ausgang {y} und die Zustände
{z1, z0}.

**Teil 1 — Typ.** Die Musterantwort steht handschriftlich auf dem Blatt:
„Moore-Automat, weil die Ausgabefunktion y nur vom aktuellen Zustand abhängig
ist." Bei einem Mealy-Automaten stünde die Ausgabe an den Kanten.

**Teil 2 — Folgezustandstabelle.** Zwei Zustandsbits und zwei Eingangsbits
ergeben 2⁴ = **16 Zeilen**. Spalten: z1(n), z0(n), e1, e0, z1(n+1), z0(n+1), y.

**Teil 3 — KV-Diagramme.** Drei Tafeln mit je vier Eingangsvariablen — den beiden
Zustandsbits und den beiden Eingangsbits. Die unzulässige Eingangskombination
wird als **X** eingetragen und darf frei als 0 oder 1 gelesen werden, was die
Blöcke vergrößert.

Sechs von dreizehn Punkten liegen auf diesem Teil. Wer die KV-Minimierung sicher
beherrscht, holt hier fast die Hälfte der Aufgabe.

**Teil 4 — Schaltplan.** Je Zustandsbit ein D-Flipflop. Vor jedes Flipflop das
Gatternetz nach der minimierten Gleichung für z(n+1). Der Ausgang y wird
ebenfalls aus dem Netz gebildet — beim Moore-Automaten **nur** aus den
Zustandsbits, nicht aus den Eingängen.

**Teil 5 — Unzulässige Kombination.** Das ist die Kombination, für die im
Zustandsdiagramm kein Übergang eingezeichnet ist.

**Zusatz.** Soll der Automat bei unzulässiger Eingabe im aktuellen Zustand
bleiben, muss z(n+1) = z(n) für diese Kombination gelten. Praktisch: den
unzulässigen Fall aus den bisherigen Termen ausblenden und den Selbsthalte-Term
`z(n) ∧ unzulässig` ergänzen.

### Aufgabe 2 — Fahrkartenautomat

Fahrkarten für 3 EUR und 5 EUR, bezahlbar mit 1- und 2-EUR-Münzen. Tasten A
(Abbruch), K3 und K5.

Als **Mealy-Automat** modellieren: Zustände sind die eingeworfenen Beträge
0, 1, 2, 3, 4, 5 EUR. Kanten sind Münzeinwürfe und Tastendrücke, die Ausgabe
(Fahrkarte, Rückgeld) steht an der Kante.

Zur Teilaufgabe „Warum wäre es schlecht, den Abbruchknopf wegzulassen?" — ohne
Abbruch bliebe Geld im Automaten gefangen, wenn der Kunde einen Betrag einwirft,
der für keine Fahrkarte reicht und den er nicht aufstocken will. Der Automat
hätte dann Zustände ohne Ausweg.

### Aufgabe 3 — Baustellenampel

Als **Moore-Automat** zu entwerfen. Anforderungen: Rotphasen mindestens 10 s;
Grünphasen werden auf Anforderung durch Induktionsschleife S1 oder S2 geschaltet;
Grünphasen enden, wenn 20 s abgelaufen sind **und** eine Anforderung der
Gegenseite besteht; Abschalten ist nur im Anschluss an eine Grünphase möglich.

Zwei Bedingungen sind hier verknüpft — die 20 Sekunden allein beenden Grün
**nicht**, es muss zusätzlich eine Gegenanforderung vorliegen. Wer das übersieht,
baut eine Ampel, die ohne Verkehr sinnlos umschaltet.
