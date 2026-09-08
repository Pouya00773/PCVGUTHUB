# 09 — Evidence Grading, Risiken und Schwachstellen

---

## Teil A — Evidence Grading

Das Evidence Grading ist der wertvollste Baustein des Referenzfalls und wird vollständig übernommen. Die Grundidee: **schwächere Daten werden nicht abgelehnt, sondern gekennzeichnet.** Das verhindert die zwei typischen Fehler — entweder gar keine Kette zu haben, weil man Perfektion verlangt, oder eine perfekt aussehende Kette zu haben, deren Schwachstellen unsichtbar sind.

### A.1 Die Stufen

| Stufe | Definition | Beispiel |
|---|---|---|
| **Verified** | Zeitgleich am Ort des Geschehens erfasst, kryptografisch signiert von einem identifizierten Erfasser oder Gerät, Zeitstempel aus vertrauenswürdiger Quelle, seither unverändert | Röstchargen-Auswaage direkt von der angebundenen Waage; Gaszählerstand; Wareneingangsbuchung durch angemeldete Person |
| **Declared** | Von einer benannten Partei erklärt, aber nicht zeitgleich erfasst oder nicht durch den Handelnden selbst signiert | Parzellendaten, von der Kooperative stellvertretend für den Erzeuger erfasst; Erntedatum aus dem Lieferschein |
| **Imported** | Aus einem Altsystem oder einer Datei übernommen, ohne Erfassungskontext | Historische ERP-Chargendaten; Excel-Liste des Exporteurs |
| **Estimated** | Berechnet oder aus Sekundärquellen abgeleitet | CO₂-Anteil Anbau aus Emissionsfaktor; umgelegter Nachverbrenner-Leerlauf |

### A.2 Die Regeln, maschinell prüfbar

Ein Datenpunkt ist **Verified** nur, wenn **alle** folgenden Bedingungen erfüllt sind:

1. **Zeitgleichheit** — Differenz zwischen Ereigniszeit und Erfassungszeit ≤ 15 Minuten (Produktion) bzw. ≤ 24 Stunden (Wareneingang). **[angenommen, Schwellen sind zu kalibrieren]**
2. **Identifizierter Erfasser** — gültiger Organisations- oder Geräteschlüssel, gültig **zum Ereigniszeitpunkt** (`03`, Abschn. 5)
3. **Signatur** über den kanonisierten Datensatz, verifizierbar
4. **Herkunft der Messgröße** — Wert stammt aus einem angebundenen Gerät, nicht aus einem Freitextfeld
5. **Unverändertheit** — keine nachträgliche Korrektur; eine Korrektur erzeugt ein neues Ereignis und stuft die Kette auf **Declared** herab, unter Beibehaltung beider Versionen

Fällt eine Bedingung, fällt die Stufe. **Eine Aufwertung von Declared zu Verified ist nachträglich nicht möglich.** Das ist der Punkt, an dem die Klassifikation ihre Aussagekraft gewinnt oder verliert.

### A.3 Aggregationsregel — die entscheidende Detailfrage

Eine Charge besteht aus vielen Datenpunkten unterschiedlicher Stufen. Für die Anzeige gilt:

> **Die Kette ist so stark wie ihr schwächstes Glied — und das schwächste Glied wird benannt.**

Keine Durchschnittsbildung, keine Punktzahl, kein „87 % verifiziert". Stattdessen: *„Herkunftsangabe: Declared (erfasst durch Kooperative X am 12.03.2026). Röstdaten: Verified."*

Der Grund: Eine Prozentzahl lädt dazu ein, die schwache Stelle wegzumitteln — und die schwache Stelle ist bei Kaffee **immer** die Herkunftsangabe, also genau das, worum es geht.

### A.4 Kommunikation gegenüber Kunden — ohne „Declared" zum Gütesiegel zu machen

Die Gefahr ist real: Ein hübsches Icon neben „Declared" liest sich wie eine Auszeichnung. Gegenmaßnahmen:

1. **Keine Symbole, keine Farben, keine Häkchen** für Declared. Nur Text.
2. **Aktiv formuliert, mit Akteur:** nicht „Declared", sondern *„Vom Erzeuger angegeben, von uns nicht überprüft."* Das ist verständlich und nicht schmeichelhaft.
3. **Verified wird nicht als Qualitätsaussage formuliert.** *„Von unserer Waage automatisch erfasst"* — nicht *„geprüft"* oder *„zertifiziert"*. Verified bedeutet **wie** ein Wert entstand, nicht **ob** er stimmt.
4. **Keine Gesamtnote.** Kein „Trust Score", kein Sternesystem. Ein aggregierter Vertrauenswert ist ein Marketinginstrument, das eine methodische Aussage vortäuscht.
5. **Im B2B-Interface**: vollständige Tabelle mit Stufe je Feld, Erfasser und Zeitpunkt — dort ist Detailtiefe erwünscht und wird gelesen.

> **Die unbequeme Konsequenz:** Bei einer typischen Kaffeekette wird die Herkunftsangabe — der werblich wichtigste Datenpunkt — dauerhaft **Declared** bleiben. Wer das nicht aushält, sollte das Evidence Grading nicht einführen, denn seine einzige Funktion ist, genau das sichtbar zu machen.

---

## Teil B — Risikoanalyse

Bewertet wird je Risiko nicht nur die Maßnahme, sondern die entscheidende Frage: **Adressiert das Design das Risiko wirklich, oder verlagert es das Problem nur?**

### B.1 Garbage in — eine falsch erfasste Koordinate wird unveränderlich falsch

| | |
|---|---|
| **Eintritt** | Hoch. Bei manueller Feldkartierung sind Fehler die Regel, nicht die Ausnahme. |
| **Wirkung** | Hoch. Eine falsche Parzelle kann eine Charge fälschlich als entwaldungsfrei ausweisen — oder fälschlich als riskant. |
| **Maßnahmen** | Plausibilitätsprüfungen (Polygonüberlappung, Fläche vs. Ertrag, Höhenlage vs. Kaffeeanbau, Erntefenster vs. Klimazone); Polygonqualität als Annahmekriterium **[recherchiert]** ([Koltiva](https://www.koltiva.com/post/polygon-quality-matters-why-geolocation-accuracy-will-define-eudr-ready-coffee-procurement)); Stichproben-Nachkartierung; Korrekturereignis statt Überschreiben |
| **Ehrliche Bewertung** | **Nur verlagert.** Das System verhindert grobe Fehler und dokumentiert Korrekturen. Es kann eine plausible falsche Koordinate nicht erkennen. In einem verankerten System wird der Fehler zusätzlich *unveränderlich*, was die Lage **verschlechtert** statt verbessert. Deshalb: Verankerung erst, wenn die Erfassungsqualität stabil ist — nie am Anfang. |

### B.2 Kollusion mehrerer Akteure

| | |
|---|---|
| **Eintritt** | Mittel. Kooperative und Exporteur haben ein gemeinsames Interesse an Verkäuflichkeit. |
| **Wirkung** | Sehr hoch. Abgestimmte Falschangaben sind aus den Daten nicht erkennbar. |
| **Maßnahmen** | Unabhängige Quellen gegenrechnen: Satelliten-Waldverlustdaten gegen Polygone; Ertrag/ha gegen regionale Statistik; Exportmengen gegen Behördendaten; Stabilisotopen-Stichprobe (`04`, Abschn. 4) |
| **Ehrliche Bewertung** | **Verlagert.** Kein Traceability-System löst Kollusion — es erhöht nur den Koordinationsaufwand und die Zahl der zu fälschenden Belege. Die einzigen wirksamen Instrumente sind **unabhängige physische Messung** (Isotopenanalyse) und **Vor-Ort-Audit**. Beide sind stichprobenhaft und teuer. Wer Blockchain gegen Kollusion anführt, hat das Problem nicht verstanden: Ein Ledger sichert die Integrität der Aufzeichnung, nicht die der Aussage. |

### B.3 Verlustfaktor-Manipulation

| | |
|---|---|
| **Eintritt** | Niedrig-mittel (setzt inneren Vorsatz voraus) |
| **Wirkung** | Hoch: 2 Prozentpunkte ≈ 20 t Grünkaffee/Jahr können eingeschleust werden (`05`, Abschn. 4) |
| **Maßnahmen** | Fünfstufiges Verfahren in `05`, Abschn. 4: gemessen statt deklariert, profilspezifischer Korridor, begründungspflichtige Ausreißer, Trendkontrolle, Abgleich gegen Einkaufs- und Zollbelege |
| **Ehrliche Bewertung** | **Weitgehend adressiert — mit einer verbleibenden Lücke.** Ebene 5 (Belegabgleich) ist die stärkste, weil sie Daten außerhalb der Produktion heranzieht. Übrig bleibt: Manipulation der Waage selbst plus Fälschung der Einkaufsbuchhaltung. Das ist dann Wirtschaftskriminalität, kein Datenqualitätsthema, und gehört in die Zuständigkeit der internen Revision, nicht des Traceability-Systems. |

### B.4 Adoptionsverweigerung upstream

| | |
|---|---|
| **Eintritt** | **Hoch — das wahrscheinlichste Scheiterszenario.** |
| **Wirkung** | Sehr hoch: Ohne Geodaten kein DDS, ohne DDS keine Einfuhr. |
| **Maßnahmen** | Kostenlose Wege zuerst nutzen (Fairtrace) **[recherchiert]**; Datenaufwand vergüten statt einfordern; Formatanforderungen minimal halten (Kooperativen ächzen unter fünf verschiedenen Käuferformaten, `02`); Frühwarnschwelle KW 43 (`07`); Rückfallposition Umstellung auf Importeursbezug |
| **Ehrliche Bewertung** | **Nicht durch Technik adressierbar.** Dies ist ein Beschaffungs- und Beziehungsthema. Die einzige technische Maßnahme mit echtem Effekt ist: **so wenig Format- und Toolzwang wie möglich.** Jede Anforderung, die Kooperative X zwingt, ein sechstes System zu bedienen, erhöht das Risiko. Das ist ein starkes Argument gegen Option C, deren DID/VC-Onboarding genau diesen Zwang erzeugt. |

### B.5 Anbieter-Lock-in

| | |
|---|---|
| **Eintritt** | Mittel-hoch. EUDR-SaaS ist ein junger, konsolidierender Markt. |
| **Wirkung** | Mittel — bis hin zu Preissetzungsmacht am Tag vor einer Compliance-Frist |
| **Maßnahmen** | EPCIS 2.0 als kanonisches Format statt Anbieterformat (`03`); vertraglich zugesicherter vollständiger Datenexport in offenem Format, mit Frist; eigener Event Store als Kopie der Wahrheit (Option B); Verankerungssenke austauschbar (`04`, Abschn. 2) |
| **Ehrliche Bewertung** | **Bei Option B gut adressiert**, weil ihr eine eigene Kopie und ein Standardformat haltet. **Bei Option A teilweise**, weil die Compliance-Logik beim Anbieter bleibt — das ist aber die bewusst gewählte Arbeitsteilung. **Bei Option C schlecht:** Plattform, Ledger, Token-Modell und Identitätssystem stecken beim selben Anbieter, und ein Wechsel entwertet die verankerte Historie. Lock-in ist das stärkste Sachargument gegen Option C — stärker als die Kosten. |

### B.6 Regulatorische Änderung

| | |
|---|---|
| **Eintritt** | **Hoch.** Die EUDR wurde zweimal verschoben und mehrfach geändert; im Mai und Juli 2026 kamen Vereinfachungspaket und delegierte Maßnahmen **[recherchiert]**. |
| **Wirkung** | Mittel — bei Verschärfung Nacherfassungsaufwand, bei Erleichterung Fehlinvestition |
| **Maßnahmen** | Regulatorik-Interpretation **kaufen, nicht bauen** (`04`, Abschn. 3) — Anbieter pflegen Formate und Fristen nach; Datenmodell fachlich statt regulatorisch schneiden (`03`); beide Auslegungen der Rösten-Frage abdecken (`01`, 2.4) |
| **Ehrliche Bewertung** | **Gut adressiert, weil das Design bewusst mehr erfasst, als die Pflicht verlangt** — und weil der teuerste Teil (die Regelinterpretation) beim Anbieter liegt. Restrisiko: eine Erleichterung, die Phase 1 nachträglich als überflüssig erscheinen lässt. Damit muss man leben; die Datenqualität nutzt auch ohne Regulatorik. |

### B.7 Weitere Risiken, kurz

| Risiko | Bewertung |
|---|---|
| **Interne Erfassungsdisziplin bricht ein** | **Adressiert nur, wenn Erfassung aus ohnehin stattfindenden Handlungen fällt.** Sonst nicht adressierbar. H2 in `07` misst genau das — und ist die Hypothese, die am ehesten scheitert. |
| **Schlüsselverlust / Schlüsselkompromittierung** (nur Phase 2) | Sperrliste mit Gültigkeit zum Ereigniszeitpunkt (`03`, 5). Ein verlorener Organisationsschlüssel entwertet sonst rückwirkend die gesamte Historie. |
| **DSGVO-Verstoß durch personenbezogene Daten im Ledger** | **Adressiert durch die Drei-Zonen-Regel** (`03`, 4.2) — aber nur, wenn sie technisch erzwungen wird (Schema-Validierung vor der Verankerung), nicht als Richtlinie. Ein Verstoß hier ist irreversibel. |
| **Green-Claims-/Irreführungsvorwurf** wegen CO₂- oder Herkunftsaussagen | Adressiert durch die Regeln in `06`, Abschn. 5 und die Blend-Darstellungsregeln in `03`, Abschn. 6. Restrisiko bleibt bei jeder werblichen Zuspitzung. |
| **Rückruf funktioniert im Ernstfall nicht** | Nur adressiert, wenn die Trace-Abfrage **geprobt** wird. Ein jährlicher Rückruftest (Mock Recall) mit Zeitmessung gehört in den Betrieb — er ist der einzige echte Test des Datenmodells. |

---

## Teil C — Die drei Risiken, die das Projekt tatsächlich beenden

Von allen oben genannten sind drei tödlich, und keines davon ist technisch:

1. **Upstream liefert nicht** (B.4) → Frist verfehlt, Ware nicht verkäuflich.
2. **Die Röstmannschaft erfasst nicht** (B.7, H2 in `07`) → Datenbestand wertlos, egal wie gut die Architektur ist.
3. **Niemand fragt nach dem Ergebnis** (H4 in `07`) → Phase 1 und 2 sind eine Investition ohne Gegenwert; Phase 0 bleibt trotzdem Pflicht.

Jede Steuerung dieses Projekts sollte diese drei zuerst messen und alles andere danach.
