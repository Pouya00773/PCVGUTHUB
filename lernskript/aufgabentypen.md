# Klausur-Aufgabentypen mit Lösungsschema

Grundlage sind die Übungsblätter 1–7 sowie die als klausurrelevant markierten
Folien. Übung 7 trägt Punkteangaben und ist damit die beste verfügbare Referenz
für das tatsächliche Klausurformat.

## Was über das Klausurformat bekannt ist

Auf Übungsblatt 1 steht handschriftlich vermerkt: *„Klausuraufgabe: Ein Schaltplan
wird vorgegeben und soll analysiert werden. Daraus sollen wir eine Wahrheitstabelle
und ein KV-Diagramm darstellen."*

Übung 7 zeigt den Punkteschlüssel einer Automatenaufgabe:

| Teilaufgabe | Punkte |
|---|---|
| Automatentyp bestimmen und begründen | 1 |
| Folgezustandstabelle ergänzen | 2 |
| KV-Diagramme und minimale DNF | 6 |
| Schaltplan mit D-Flipflops und Gattern zeichnen | 3 |
| Unzulässige Eingangskombination benennen | 1 |

Die Gewichtung ist aufschlussreich: Über die Hälfte der Punkte liegt auf
KV-Minimierung. Das deckt sich mit den Klausurmarkierungen in Kapitel 3.

Auf Übung 3, Aufgabe 2 (Belüftungsanlage mit K11/K12/K13) ist handschriftlich
vermerkt, dass dieses Thema nicht behandelt wird.

---

## Typ A — Schaltnetz analysieren

**Vorkommen:** Übung 1, Übung 4 Aufgabe 1, Übungsblatt 2, laut Notiz der
wahrscheinlichste Klausurtyp.

**Gegeben:** ein Stromlaufplan oder Funktionsplan.
**Gesucht:** Wahrheitstabelle, minimierte Gleichung, FUP.

### Lösungsschema

1. **Zuordnungstabelle** aufstellen: Betriebsmittelkennzeichen, Bedeutung,
   Öffner/Schließer, SPS-Adresse. Öffner sauber kennzeichnen — sie liefern im
   Ruhezustand 1.
2. **Ansteuerfunktion ablesen.** Im Stromlaufplan gilt: Reihenschaltung = UND,
   Parallelschaltung = ODER, Öffner = negierte Variable. Bei mehrstufigen Netzen
   an jedem Gatterausgang einen Hilfsnamen h₁, h₂, … vergeben und rückwärts
   einsetzen.
3. **Funktionstabelle** für alle 2ⁿ Kombinationen ausfüllen.
4. **KV-Diagramm** anlegen, Werte eintragen, Blöcke bilden. Größtmögliche Blöcke,
   Randfelder sind benachbart, Überlappungen erlaubt.
5. **Minimalform ablesen** — je Block die Variablen, die im Block konstant bleiben.
6. **Funktionsplan** der minimierten Funktion zeichnen.
7. Falls gefordert: **Deklarationsteil** und Programm in FUP, KOP oder ST.

### Stolperstellen

- Verlangt die Aufgabe die **KNF**-Minimalform (Übung 1 tut das), müssen die
  **Nullen** zusammengefasst werden. Ergebnis ist die DNF von ¬Y; anschließend
  De Morgan anwenden.
- Ist eine Fehlervariable für unerlaubte Eingangskombinationen gefragt
  (Übungsblatt 2, Wasserstandsregelung), zuerst festlegen, welche Kombinationen
  physikalisch unmöglich sind — bei Füllstandssensoren etwa „oberer Sensor
  bedeckt, unterer frei".
- Don't-Care-Felder nur einbeziehen, wenn sie einen Block vergrößern.

---

## Typ B — Kontaktsteuerung entwerfen

**Vorkommen:** Übung Haltegliedsteuerung, Übung 3 Aufgaben 1 und 3, Übung
Förderband (Kap. 4/53, klausurrelevant mit 24 V).

**Gegeben:** eine verbale Funktionsbeschreibung.
**Gesucht:** Stromlaufplan und Programm in FUP/KOP.

### Lösungsschema

1. Betriebsmittel auflisten und mit Kennbuchstaben versehen: S für Taster/Schalter,
   K für Relais, Q für Schütz, H für Leuchtmelder, M für Motor, F für Sicherung
   und Überstromrelais, B für Sensoren.
2. Festlegen, welche Taster **Öffner** sind. Konvention: AUS- und STOPP-Taster
   sowie Überstromrelais werden als Öffner ausgeführt, damit Drahtbruch zum
   sicheren Zustand führt.
3. **Stromlaufplan** zeichnen, stets im nicht geschalteten Zustand, getrennt in
   Leistungsteil (L1/L2/L3) und Steuerteil (24 V, abgesichert über F1).
4. **Selbsthaltung** einbauen, wo ein Tastendruck gespeichert werden soll:
   Schließer des eigenen Schützes parallel zum EIN-Taster.
5. AUS-Taster **in Reihe** vor den Selbsthaltezweig legen, damit er die Haltung
   auftrennt.
6. **Verriegelung** ergänzen, wenn zwei Schütze sich gegenseitig ausschließen
   (Wendeschütz): Öffner des jeweils anderen Schützes in Reihe.
7. Übersetzung nach FUP: Selbsthaltung wird zum SR- oder RS-Baustein.
   Setzbedingung = EIN-Taster, Rücksetzbedingung = AUS-Taster ODER Störung.

### Musterlösung Haltegliedsteuerung

Zwei AUS-Taster S1, S2, zwei EIN-Taster S3, S4, zwei Leuchtmelder H1, H2.

- Setzbedingung K1: `S3 ∨ S4`
- Rücksetzbedingung K1: `¬S1 ∨ ¬S2` — abhängig davon, ob S1 und S2 als Öffner
  ausgeführt sind; bei Öffnern in Reihe: Rücksetzen, sobald einer betätigt wird
- `H1 = K1` (Anlage läuft)
- `H2 = ¬K1` (betriebsbereit)

Als RS-Baustein: rücksetzdominant, damit AUS in jedem Fall gewinnt.

---

## Typ C — Schaltwerk mit Speichern und Zeiten

**Vorkommen:** Übung 5 Aufgabe 1 (drei Förderbänder), Kap. 4.2/18
(klausurrelevant), Kap. 4.2/7 Werktor (leicht klausurrelevant).

**Gegeben:** ein zeitlicher Ablauf mit Verzögerungen.
**Gesucht:** Zuordnungstabelle, erweiterte RS-Tabelle, Funktionsplan.

### Lösungsschema

1. **Zuordnungstabelle** der Ein- und Ausgänge.
2. **RS-Tabelle** aufstellen — für jedes Speicherglied eine Zeile mit Setz- und
   Rücksetzbedingung. Bei Zeitabläufen die Tabelle um die Zeitglieder erweitern.
3. Reihenfolge und Verzögerungen als Kette von TON-Bausteinen abbilden: Der
   Ausgang eines Speichers startet den nächsten Timer, dessen Ablauf setzt den
   nächsten Speicher.
4. Sofortabschaltungen (STOPP, Überstromrelais) als **gemeinsame
   Rücksetzbedingung** auf alle Speicher legen.
5. **Funktionsplan** zeichnen.

### Beispiel Übung 5, drei Förderbänder

Einschalten mit S1: M3, dann nach 5 s M2, dann nach 5 s M1 — gegen die
Förderrichtung, damit kein Material auf ein stehendes Band läuft.
Ausschalten mit S2: umgekehrte Reihenfolge, Abstand 10 s.
STOPP S0 oder Auslösen von F1, F2, F3: alle Motoren sofort aus.

Die sofortige Abschaltung gehört als Rücksetzbedingung an **jeden** Speicher, nicht
nur an den ersten der Kette.

---

## Typ D — Ablaufsteuerung entwerfen

**Vorkommen:** Übung 6 (drei Pumpen, Ampel, Anlassersteuerung), Kap. 6/36
(klausurrelevant).

**Gegeben:** ein schrittweiser Prozess.
**Gesucht:** Ablaufkette mit Schritten, Aktionen und Transitionen.

### Lösungsschema

1. **Anfangsschritt** definieren: Grundstellung der Anlage.
2. Jeden stabilen Anlagenzustand als **Schritt** zeichnen, fortlaufend nummeriert.
3. Zu jedem Schritt die **Aktionen** notieren — welche Ausgänge sind aktiv,
   mit welchem Qualifier.
4. Zwischen die Schritte die **Transitionen** setzen und jede mit ihrer
   Weiterschaltbedingung beschriften: Sensorsignal, Taster oder abgelaufene Zeit.
5. Rückführung zum Anfangsschritt nicht vergessen.
6. Prüfen: Ist zu jedem Zeitpunkt genau ein Schritt aktiv? Führt jede Transition
   aus dem Schritt heraus, in dem sie steht?

### Beispiel Übung 6, drei Pumpen

Drei Pumpen über Q1, Q2, Q3, eingeschaltet durch **jeweils eine erneute
Betätigung** von S1. AUS-Taster S0 schaltet alle laufenden Pumpen gleichzeitig ab.

Kette: Schritt 0 Grundstellung → S1 → Schritt 1 (Q1) → S1 → Schritt 2 (Q1, Q2)
→ S1 → Schritt 3 (Q1, Q2, Q3). Aus jedem Schritt führt S0 zurück zu Schritt 0.

Achtung bei der Transition: Weil derselbe Taster S1 dreimal verwendet wird, braucht
es eine **Flankenauswertung** (R_TRIG). Ohne sie würde ein einziger langer
Tastendruck die Kette in einem Zyklus durchlaufen.

### Beispiel Übung 6, Ampel

Grundzustand Grün. S1 leitet die Gelbphase ein, Gelb 3 s, dann Rot, nach 10 s
Rot-Gelb für 2 s, zurück zu Grün. Vier Schritte, drei zeitgesteuerte Transitionen
und eine tastergesteuerte.

---

## Typ E — Automat analysieren

**Vorkommen:** Übung 7 Aufgabe 1 (mit Punkteschlüssel), Kap. 7/8 klausurrelevant.

**Gegeben:** ein Zustandsdiagramm.
**Gesucht:** Typ, Folgezustandstabelle, KV-Diagramme, Schaltplan.

### Lösungsschema

1. **Automatentyp bestimmen.** Steht die Ausgabe im Zustandskreis, ist es ein
   Moore-Automat; steht sie an der Kante als `Eingang / Ausgabe`, ein
   Mealy-Automat. Begründung im Antwortsatz mitliefern: „Moore-Automat, weil die
   Ausgabefunktion y nur vom aktuellen Zustand abhängt."
2. **Folgezustandstabelle** aufstellen. Spalten: aktueller Zustand (z1, z0),
   Eingang (e1, e0), Folgezustand (z1(n+1), z0(n+1)), Ausgang y. Zeilenzahl ist
   2^(Zustandsbits + Eingangsbits).
3. **KV-Diagramme**: je eines für z1(n+1), z0(n+1) und y. Eingangsvariablen des
   KV sind sowohl die Zustandsbits als auch die Eingangsbits. Minimale DNF ablesen.
4. **Schaltplan zeichnen**: je Zustandsbit ein D-Flipflop; davor das Schaltnetz
   aus NOT, AND und OR gemäß der minimierten Gleichungen. Der Ausgang y wird
   ebenfalls aus dem Netz gebildet.
5. **Unzulässige Eingangskombination** benennen — meist die, für die im Graphen
   kein Übergang eingezeichnet ist.
6. Soll der Automat bei unzulässiger Eingabe im Zustand bleiben, sind die
   Gleichungen so zu ergänzen, dass `z(n+1) = z(n)` für diese Kombination gilt.
   Praktisch: den unzulässigen Fall aus den bisherigen Termen ausblenden und
   stattdessen den Selbsthalte-Term `z(n) ∧ unzulässig` hinzufügen.

### Typ-Umwandlung

Wird die Umwandlung verlangt (Kap. 7/8 markiert):

- **Mealy → Moore:** Jeden Zustand für jede dort auftretende Ausgabe aufspalten,
  Ausgabe in den Zustand schreiben. Die Zustandszahl steigt.
- **Moore → Mealy:** Die Ausgabe eines Zustands an alle **eingehenden** Kanten
  schreiben. Die Zustandszahl bleibt oder sinkt.

---

## Typ F — Sprachumsetzung zwischen den Fachsprachen

**Vorkommen:** Übung 3 Aufgabe 1.

**Gegeben:** ein Funktionsplan.
**Gesucht:** Stromlaufplan, Kontaktplan, Strukturierter Text, Anweisungsliste —
dieselbe Logik in vier Darstellungen.

### Übersetzungstabelle

| Logik | FUP | KOP | ST | Stromlaufplan |
|---|---|---|---|---|
| UND | `&`-Block | Kontakte in Reihe | `A AND B` | Reihenschaltung |
| ODER | `>=1`-Block | Kontakte parallel | `A OR B` | Parallelschaltung |
| NICHT | Kreis am Eingang | Öffnerkontakt | `NOT A` | Öffner |
| Zuweisung | Ausgangspfeil | Spule am Zeilenende | `Q := …;` | Relaisspule |
| Speicher | SR/RS-Block | Set-/Reset-Spule | `IF … THEN Q := TRUE;` | Selbsthaltung |

Der Kontaktplan wird von links nach rechts gelesen und muss stets mit einer
Zuweisung, einem Funktions- oder Bausteinaufruf abgeschlossen werden.

---

## Typ G — Signale in geschlossener Darstellung

**Vorkommen:** Kap. 2.1/30, doppelt als klausurrelevant markiert.

**Gegeben:** ein skizzierter Signalverlauf.
**Gesucht:** eine Formel aus Standardfunktionen.

### Lösungsschema

1. Signal in Abschnitte zerlegen, alle Knickpunkte und Sprungstellen mit ihren
   Zeitpunkten notieren.
2. Für jede **Sprungstelle** einen verschobenen Sprung ansetzen: Höhe des Sprungs
   mal σ(t − t₀). Sprung nach oben positiv, nach unten negativ.
3. Für jeden **Knick im Anstieg** eine verschobene Rampe ansetzen: Änderung der
   Steigung mal (t − t₀) · σ(t − t₀).
4. Für jede **Nadel** einen gewichteten Dirac-Impuls: Gewicht mal δ(t − t₀).
5. Alle Terme addieren und zur Probe an zwei, drei Zeitpunkten einsetzen.

> **Kontrolle:** Die Summe aller Sprunghöhen bis zum Zeitpunkt t muss den
> Funktionswert an dieser Stelle ergeben. Stimmt das nicht, fehlt ein Term oder
> ein Vorzeichen ist falsch.

---

## Lernreihenfolge nach Punkteerwartung

1. **KV-Minimierung** — trägt in Übung 7 allein 6 von 13 Punkten und ist der laut
   Notiz erwartete Klausurtyp. Bis zur Sicherheit üben: Wahrheitstabelle → KV →
   Minimalform, mit drei und vier Variablen, mit und ohne Don't-Care.
2. **Automaten** — vollständiges Schema von Typ E, weil es KV-Minimierung
   einschließt und damit doppelt zahlt.
3. **Stromlaufplan mit Selbsthaltung** — Typ B, klausurrelevant markiert,
   überschaubarer Umfang.
4. **Kontaktkennzeichnung** — Kap. 4/31, „beschriften in Klausur", reines
   Auswendiglernen mit hoher Punktdichte.
5. **Ablaufkette** — Typ D, klausurrelevant markiert.
6. **Systemeigenschaften und Steuern/Regeln** — Definitionsfragen, schnell zu
   sichern.
7. **Signale in geschlossener Darstellung** — Typ G, klausurrelevant, aber nur bei
   Zeit sinnvoll zu vertiefen.
