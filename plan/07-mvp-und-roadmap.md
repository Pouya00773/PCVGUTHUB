# 07 — MVP-Zuschnitt und Roadmap

---

## 1. Phase 0 zuerst: das ist kein MVP, das ist eine Frist

Bevor über einen Piloten geredet wird: **Bis zum 30.12.2026 sind es ab heute (08.09.2026) rund 16 Wochen.** Phase 0 ist kein Experiment, sondern Pflichterfüllung. Sie hat keinen „Abbruchpunkt" — nur einen Endtermin.

### Phase 0 — EUDR-Fähigkeit (jetzt → 30.12.2026)

| # | Meilenstein | Frist | Abhängigkeit |
|---|---|---|---|
| 0.1 | **Rollenklärung je Lieferbeziehung** (Zollanmelderstatus). Ergebnis: Liste aller Bezugsquellen mit Zuordnung Primärbetreiber / Downstream | **KW 39 (Ende Sep.)** | Rechtsabteilung, Zolldienstleister |
| 0.2 | Rechtsgutachten „Rösten = erneutes Inverkehrbringen?" beauftragt | KW 39 | — |
| 0.3 | **Bestandsaufnahme Geodaten**: welche Herkunft ist bereits kartiert (Fairtrace, Exporteur, Zertifizierer), welche nicht | **KW 41** | Einkauf, Lieferanten |
| 0.4 | Anbieterauswahl EUDR-Compliance-SaaS, Vertrag | KW 42 | 0.1, 0.3 |
| 0.5 | Vertragliche Zusicherung der DDS-Referenznummern von allen Importeuren | KW 44 | Einkauf, Recht |
| 0.6 | Geodatenbeschaffung für alle Direct-Trade-Herkünfte abgeschlossen | **KW 46** | **kritischer Pfad** |
| 0.7 | Risikoscreening (Polygone gegen Waldverlustdaten) für alle Lots | KW 48 | 0.6 |
| 0.8 | Testeinreichung DDS in TRACES | KW 49 | 0.4, 0.7 |
| 0.9 | Referenznummern-Register produktiv, Prozesse geschult | KW 51 | 0.4, 0.5 |
| 0.10 | **Go-live EUDR** | **30.12.2026** | alle |

**Kritischer Pfad ist 0.6, nicht die Software.** Wenn eine Kooperative im Oktober nicht kartiert ist, hilft kein Systemvorsprung. → Frühwarnung: Wenn zum **KW 43** nicht mindestens 80 % der Direct-Trade-Menge mit belastbaren Geodaten unterlegt ist, muss über Umstellung der betroffenen Herkünfte auf Importeursbezug (Pfad B) entschieden werden. Das ist die **einzige realistische Notbremse** — sie kostet Marge und Beziehung, aber sie erhält die Verkaufsfähigkeit.

---

## 2. Der eigentliche MVP (Phase 1, Pilot)

### Zuschnitt

| | |
|---|---|
| **Eine Herkunft** | Ein Direct-Trade-Lot, bei dem ihr Primärbetreiber seid und die Kooperative kooperationsbereit und bereits kartiert ist |
| **Eine SKU** | Single Origin, 250 g, kein Blend |
| **Ein Röstprofil** | damit der Verlustkorridor (`05`) mit wenigen Chargen kalibrierbar ist |
| **Ein Röster** | eine Maschine, mit Gaszähler nachgerüstet |
| **Ende-zu-Ende** | Parzelle → Kooperative → Exporteur → Wareneingang → Röstung → Abpackung → QR-Code → Endkunde |
| **Ausdrücklich nicht im MVP** | Blends, mehrere Herkünfte, Ledger-Verankerung, physische Marker, Consumer-App, Token |

Der Blend fehlt bewusst: Er ist fachlich der interessantere Fall, aber er verdeckt im Piloten die Frage, ob die Kette überhaupt hält. Blend kommt in Phase 1b.

### Die Hypothesen, die der Pilot falsifizieren soll

Ein Pilot, der nichts widerlegen kann, ist eine Demo. Diese vier Hypothesen sind so formuliert, dass sie scheitern können:

**H1 — Datenkette (technisch).**
*„Für ≥95 % der Masse einer verkauften Röstcharge lässt sich eine lückenlose Kette bis zur Parzellenebene rekonstruieren."*
→ **Falsifiziert**, wenn die Aggregation in Trockenmühle oder Kooperative die Auflösung unter 95 % drückt. Wahrscheinlichster Ausgang: **teilweise falsifiziert** — Auflösung bis Kooperative gelingt, bis Parzelle nicht. Genau das muss man wissen, bevor man skaliert.

**H2 — Betriebliche Tragfähigkeit.**
*„Die Erfassung kostet die Röstmannschaft ≤2 Minuten je Charge, und die Erfassungsquote liegt nach 8 Wochen ohne Nachfassen bei ≥95 %."*
→ **Falsifiziert**, wenn nach Wochen die Erfassung schleift. **Dies ist die Hypothese, die am häufigsten scheitert und am seltensten gemessen wird.** Messung: Erfassungsquote wöchentlich, ohne Ankündigung, ohne Erinnerung.

**H3 — Beschaffbarkeit der Herkunftsdaten.**
*„Die Kooperative liefert Parzellendaten in der geforderten Qualität ohne Zusatzvergütung über den bestehenden Preis hinaus."*
→ **Falsifiziert**, wenn Nachvergütung oder externer Kartierungsdienstleister nötig wird. Bestimmt direkt die Skalierungskosten (`08`).

**H4 — Zahlungsbereitschaft (kommerziell).**
*„Mindestens ein B2B-Kunde ist bereit, für den Zugang zu chargengenauen Herkunfts- und CO₂-Daten einen benannten Aufpreis oder eine Vertragsbindung zu geben."*
→ **Falsifiziert**, wenn alle Kunden nach der Referenznummer fragen und sonst nichts. **Wenn H4 falsifiziert wird, entfällt die Geschäftsgrundlage für Phase 2 vollständig.**

Zusatzmessung ohne Hypothesencharakter: **QR-Scanrate** je verkaufter Einheit. Erwartung im niedrigen einstelligen Prozentbereich **[geschätzt]**. Sie entscheidet nicht über Phase 2, aber über das Marketingbudget.

### Erfolgskriterien und Abbruchkriterien Phase 1

| | |
|---|---|
| **Weiter zu 1b (Blend + weitere Herkünfte)** | H1 ≥80 % (auf mindestens Kooperativenebene), H2 bestätigt, H3 mit kalkulierbaren Kosten |
| **Anpassen** | H1 nur auf Exporteurebene erreichbar → Anspruch senken, Genauigkeitsgrad offen ausweisen statt Kette behaupten |
| **Abbruch Phase 1** | H2 falsifiziert und auch nach einer Iteration der Erfassung nicht zu retten. Ohne betriebliche Tragfähigkeit ist alles Weitere Datenmüll. |
| **Phase 2 sperren** | H4 falsifiziert |

---

## 3. Roadmap

```
2026        Q3 ──────── Q4 ────────────────────┤ 30.12. EUDR-Pflicht
            │  Phase 0: Compliance (Pflicht)   │
            │  Rollenklärung · Geodaten · SaaS · TRACES · Referenznummern
            
2027        Q1 ──── Q2 ──── Q3 ──── Q4 ────────┤
            │ 1a: Pilot     │ 1b: Blend +      │ 1c: Rollout
            │ 1 Herkunft    │ mehrere Herkünfte│ alle SKUs
            │ 1 SKU         │ CO₂ Scope 1/2    │ B2B-API
            │ Event Store   │ DPP alle Piloten │ Audit-Pack
            │ Evidence Grad.│                  │
            
2028+       ┌──────────────────────────────────┐
            │ Phase 2 — NUR bei Auslösekriterium│
            └──────────────────────────────────┘
```

### Auslösekriterium Phase 2 (kryptografische Verankerung)

Phase 2 startet **nur**, wenn **mindestens eine** der folgenden Bedingungen eintritt:

1. Ein benannter B2B-Kunde fordert verifizierbare Nachweisführung **vertraglich** (nicht: findet sie interessant).
2. Eine Regulierungsänderung verlangt Nachweis der Zeitgleichheit über einen qualifizierten Zeitstempel hinaus.
3. Mindestens zwei externe Parteien sollen in denselben Datenbestand **schreiben** und einander nicht vertrauen.
4. Ein Schadensfall (Rückruf, Betrugsvorwurf) hat gezeigt, dass die eigene Dokumentation extern nicht als glaubwürdig akzeptiert wurde.

**Fehlen alle vier, wird Phase 2 nicht gestartet — auch nicht „für später schon mal".** Die Vorbereitung beschränkt sich auf das, was ohnehin nützlich ist: Tages-Merkle-Root und austauschbare Verankerungssenke (`04`, Abschn. 2).

---

## 4. Abhängigkeiten und Reihenfolgezwänge

| Vorher muss stehen | Sonst |
|---|---|
| Rollenklärung (0.1) | Man beschafft Geodaten für Lots, für die man gar nicht zuständig ist — oder umgekehrt |
| Geodaten (0.6) | Kein DDS, keine Ware, kein Piloten-Ausgangspunkt |
| Segregations-Entscheidung im Lager (`05`, Abschn. 6) | Chargenzuordnung wird zur Fiktion, H1 ist nicht mehr testbar |
| Gaszähler-Nachrüstung | Kein chargengenauer Scope 1, CO₂ bleibt Monatsdurchschnitt |
| Röstchargen strukturiert erfasst (Röstsoftware o. Cropster) | Massenbilanz muss aus Excel rekonstruiert werden — der teuerste Weg |
| H4 geprüft | Phase 2 wäre eine Wette ohne Nachfrager |

**Die größte ungenannte Abhängigkeit:** eine benannte, dauerhaft verantwortliche Person für Datenqualität. Ohne sie zerfällt das System binnen eines Jahres, unabhängig von der Architektur. Das ist keine Projektrolle, sondern eine Linienfunktion.
