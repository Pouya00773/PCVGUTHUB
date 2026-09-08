# 06 — CO₂-Bilanzierung: was messbar ist, und was nicht

**Leitsatz:** Bei Kaffee liegen 80–95 % der Emissionen dort, wo ihr **nicht** messen könnt. Ein System, das Scope 1 auf drei Nachkommastellen ausweist und Scope 3 mit einem Literaturwert füllt, erzeugt Scheingenauigkeit. Dieses Dokument beschreibt, wie man das vermeidet, ohne die Bilanzierung aufzugeben.

---

## 1. Die Größenordnungen zuerst

| Position | Wert | Quelle / Status |
|---|---|---|
| Grünkaffee cradle-to-gate (Anbau, Aufbereitung, Transport) | **3,51–15,33 kg CO₂e/kg Grünkaffee** | World Coffee Research, Spannweite **[recherchiert]** ([Übersicht algrano](https://algrano.com/learn/carbon-footprint-coffee)) |
| Alternativer Referenzwert | ~11 kg CO₂e/kg Grünkaffee | ICO-Schätzung **[recherchiert]**, liegt im oberen Drittel obiger Spanne |
| Anteil Anbau an cradle-to-gate | **>84 %** bei gemahlenem Kaffee | LCA-Synthese **[recherchiert]** ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1385894723015243)) |
| Röstprozess | **0,45–0,59 kg CO₂e/kg** Röstkaffee | Fallstudien **[recherchiert]** ([Kaffeemacher CO₂-Bilanz](https://kaffeemacher.de/en/blogs/kaffeewissen/kaffeemacher-roesterei-unser-co2-fussabdruck) · [Röstprozess-LCA](https://ecsdev.org/ojs/index.php/ejsd/article/download/673/668/1336)) |
| Anteil Brennstoff am Röstprozess-Fußabdruck | ~79 % (LPG-Fallstudie) | **[recherchiert]**, gleiche Quelle |
| Scope-3-Anteil an einer Rösterei-Gesamtbilanz | **~96 %** | Fallstudie einer Rösterei **[recherchiert]** |

**Die Botschaft dieser Tabelle:** Die Spannweite des Grünkaffee-Werts (Faktor 4,4 zwischen 3,51 und 15,33) ist **größer als euer gesamter Scope 1 und 2 zusammen**. Präzision bei euch im Haus verändert das Gesamtergebnis kaum; die Wahl des Emissionsfaktors für den Anbau verändert es massiv.

---

## 2. Scope 1 — was ihr tatsächlich messen könnt

| Quelle | Messung | Chargenzuordnung |
|---|---|---|
| **Rösterbrenner (Erdgas/LPG)** | Impulsgaszähler am Röster, idealerweise **separat je Röstmaschine** | **Direkt**: Zählerstand bei Chargenstart und -ende. Das ist der saubere Fall. |
| **Nachverbrenner / Katalysator** | Eigener Gaszähler, sonst rechnerisch | Nachverbrenner läuft auch zwischen Chargen (Warmhaltung). → Anteilige Zuordnung über Chargenlaufzeit, Leerlauf als **Overhead** auf die Tagesproduktion umgelegt. **Nicht** als chargenspezifisch ausweisen. |
| **Firmenfahrzeuge** | Tankbelege | Nicht chargenzuordenbar → Jahresoverhead |
| **Kältemittel** | Wartungsprotokolle | Jahresoverhead |

**Zuordnungsregel, die das Modell tragen muss:**

```
CO2_Scope1(Charge) = Gas_direkt(Charge) × EF_Gas
                   + Gas_Nachverbrenner_Leerlauf(Tag) × EF_Gas × (m_Charge / m_Tagesproduktion)
```

Die zweite Zeile ist eine **Allokation**, keine Messung, und wird im DPP getrennt ausgewiesen. Wer beides zu einer Zahl addiert und „gemessen" nennt, macht denselben Fehler wie bei Scope 3.

**Instrumentierung:** Impulszähler → Modbus/MQTT → Event Store (`EnergyReadingEvent`, `03`). Nachrüstkosten je Röster im niedrigen vierstelligen Bereich **[geschätzt]**. Ohne diese Nachrüstung ist chargengenauer Scope 1 nicht möglich — dann bleibt nur die Monatsrechnung geteilt durch die Monatsproduktion, und **das muss dann auch so dastehen**.

---

## 3. Scope 2 — Strom

| Quelle | Messung |
|---|---|
| Röstermotor, Kühlsieb, Absaugung | Idealerweise Unterzähler je Maschine; sonst Hauptzähler |
| Mühlen, Abpackung | Unterzähler oder Allokation nach Betriebsstunden |
| Gebäude, Büro, Kühlung | Overhead |

**Zwei Werte parallel führen** (marktbasiert und standortbasiert nach GHG Protocol). Bei Ökostrombezug ist der marktbasierte Wert nahe null — das ist bilanziell korrekt und kommunikativ heikel. Im DPP **beide** zeigen oder keinen; nur den günstigen zu zeigen, ist Greenwashing.

---

## 4. Scope 3 — wo die Ehrlichkeit entschieden wird

Scope 3 ist bei euch der Löwenanteil und beruht **unvermeidbar auf Sekundärdaten**. Das ist kein Versagen, sondern der Stand der Technik.

| Kategorie | Datenlage | Vorgehen |
|---|---|---|
| **Anbau + Aufbereitung** (größter Posten) | Primärdaten nur mit Feld-LCA je Kooperative erhebbar — Aufwand fünfstellig je Herkunft **[geschätzt]** | **Emissionsfaktor** nach Land/Anbausystem/Aufbereitung, mit Unsicherheitsband. Bei ≤3 Schlüsselherkünften mit langfristiger Beziehung ist eine echte Primärerhebung überlegenswert — dort verändert sie das Ergebnis wirklich. |
| **Seetransport** | **Primärdaten verfügbar**: Container, Route, Gewicht aus euren eigenen Frachtpapieren | Berechnen, nicht schätzen. Anteil ist klein, aber die Daten sind da und billig. |
| **Landtransport, Lagerung** | teils primär | Berechnen wo möglich |
| **Verpackung** | Herstellerangaben, sonst Materialfaktoren | Lieferantendaten anfordern — hier ist Verbesserung realistisch |
| **Distribution, Nutzung, Entsorgung** | Sekundär | Faktoren; die Nutzungsphase (Zubereitung beim Kunden) ist erheblich und liegt vollständig außerhalb eurer Kontrolle |

**Die entscheidende Frage bei Scope 3 ist nicht die Genauigkeit, sondern die Konsistenz.** Ein über die Jahre konstant angewandter Faktor macht **Veränderung** sichtbar, auch wenn der Absolutwert unsicher ist. Ein jährlich gewechselter Faktor macht jede Aussage über Fortschritt unmöglich. → Faktorquelle und -version werden je Berechnung **mitgespeichert** (`emission_factor_source`, `version`, `retrieved_at`) und bei Wechsel wird die Zeitreihe rückgerechnet **oder** der Bruch offen ausgewiesen.

---

## 5. Regeln gegen Scheingenauigkeit

Diese fünf Regeln sind als Systemverhalten zu implementieren, nicht als Redaktionsrichtlinie:

1. **Keine Nachkommastelle, die die Unsicherheit nicht trägt.** Bei einer Grünkaffee-Spanne von 3,5–15,3 kg CO₂e/kg ist die Ausgabe „7,43 kg CO₂e pro kg" unseriös. Ausgabe als **Bereich** oder als gerundeter Wert mit Bandbreitenangabe.
2. **Primär- und Sekundärdaten werden im Ergebnis getrennt ausgewiesen.** Dies ist das direkte Gegenstück zum Evidence Grading (`09`): jede CO₂-Position trägt `Verified` (gemessen), `Calculated` (aus gemessenen Primärdaten gerechnet) oder `Estimated` (Sekundärfaktor).
3. **Allokationen sind als solche gekennzeichnet.** Der umgelegte Nachverbrenner-Leerlauf ist keine Messung.
4. **Keine Kompensation in derselben Zahl.** Kompensationszertifikate werden getrennt ausgewiesen, nie vom Fußabdruck abgezogen. „Klimaneutral" erscheint nicht im DPP.
5. **Die Nutzungsphase wird genannt oder ganz weggelassen** — nie stillschweigend ausgeklammert, wenn die Zahl als „Fußabdruck einer Tasse" kommuniziert wird.

---

## 6. Was im DPP steht

**Empfohlene Darstellung für den Endkunden (öffentliche Stufe):**

> **CO₂-Fußabdruck dieser Charge: ca. 6–13 kg CO₂e je kg Röstkaffee**
> Davon in unserer Rösterei gemessen: 0,52 kg (Rösten, Strom, Mahlen).
> Der übrige Anteil entfällt überwiegend auf Anbau und Transport und beruht auf Durchschnittswerten der Fachliteratur, nicht auf Messungen bei unseren Erzeugern.
> *Was wir messen: [Verified] · Was wir schätzen: [Estimated]*

Das ist weniger verkaufsstark als „2,1 kg CO₂ — klimaneutral" und um Größenordnungen ehrlicher. Es ist außerdem das Einzige, was einer Prüfung nach der EU-Green-Claims-Logik standhält. **[angenommen — die Green-Claims-Richtlinie war zuletzt im Gesetzgebungsverfahren umstritten; die Anforderung an substantiierte Umweltaussagen folgt aber bereits aus dem UWG und der Richtlinie (EU) 2024/825. Rechtsprüfung vor Veröffentlichung, siehe `10`.]**

**Für den B2B-Kunden (Login-Stufe):** vollständige Aufschlüsselung nach GHG-Protocol-Kategorien, mit Faktorquellen, Allokationsregeln und Unsicherheiten — exportierbar in einem Format, das er in seine eigene Scope-3-Bilanz übernehmen kann. **Das ist der Teil, für den ein Kunde tatsächlich zahlen könnte**, im Gegensatz zum QR-Code auf der Tüte.

---

## 7. Aufwand und Reihenfolge

| Schritt | Aufwand | Nutzen |
|---|---|---|
| Gaszähler je Röster nachrüsten, Anbindung | niedrig-mittel **[geschätzt]** | Chargengenauer Scope 1, der belastbarste Teil der Bilanz |
| Seetransport aus eigenen Frachtdaten rechnen | niedrig | Primärdaten fast umsonst |
| Verpackungsdaten bei Lieferanten anfordern | niedrig | Verbesserungshebel |
| Emissionsfaktor-Bibliothek mit Versionierung | mittel | Voraussetzung für Vergleichbarkeit über Jahre |
| Feld-LCA je Schlüsselherkunft | **hoch** | Nur bei 2–3 Kernherkünften mit langer Bindung sinnvoll |

**Reihenfolge:** erst Scope 1/2 messbar machen (das ist billig und ehrlich), dann Transport rechnen, dann Faktorbibliothek sauber führen. Feld-LCA zuletzt und nur gezielt. Wer umgekehrt anfängt, hat nach einem Jahr eine teure Studie und keine laufenden Daten.
