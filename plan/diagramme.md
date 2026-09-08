# Diagramme

Vier Mermaid-Diagramme. Sie rendern in GitHub, GitLab und jedem Markdown-Viewer mit Mermaid-Unterstützung.

---

## 1. Datenfluss vom Erzeuger zum Endkunden, mit Vertrauensankern

Jeder Knoten trägt die Belastbarkeit seines Vertrauensankers im Label. Gestrichelte Kanten markieren die vier Stellen, an denen die Kette in der Praxis bricht; doppelte Kanten den Warenfluss zu euch.

```mermaid
flowchart TD
    subgraph URSPRUNG["Ursprungsland"]
        P["Parzelle<br/>Geometrie, Erzeuger<br/>Anker: schwach"]
        K["Kooperative / Washing Station<br/>Erntecharge, Polygonerfassung<br/>Anker: mittel, Institution"]
        E["Exporteur / Trockenmuehle<br/>Exportlot, Dokumente<br/>Anker: mittel"]
    end

    subgraph EU["EU-Markt"]
        I["Importeur / Gruenkaffeehaendler<br/>PRIMAERBETREIBER bei Pfad B<br/>liefert nur DDS-Referenznummer"]
        R["ROESTEREI<br/>Wareneingang, Roestung, Blend, Abpackung<br/>Anker: stark, eigene Geraete"]
    end

    subgraph SENKEN["Nachweisziele"]
        T["TRACES<br/>DDS-Einreichung"]
        B2B["B2B-Kunde<br/>Referenznummer + CO2-Daten"]
        B2C["Endkunde<br/>QR / DPP"]
    end

    P -.->|"Ablieferung in Sammelbehaelter<br/>BRUCHSTELLE 2"| K
    K -->|"Erntecharge, Polygone<br/>Declared"| E
    E -.->|"Aggregation mehrerer Kooperativen<br/>BRUCHSTELLE 1"| I
    E ==>|"Pfad A: Direct Trade<br/>ihr seid Zollanmelder"| R
    I ==>|"Pfad B: Zukauf<br/>nur Referenznummer"| R

    R -->|"Pfad A: eigene DDS"| T
    I -->|"Pfad B: DDS des Importeurs"| T
    R --> B2B
    R --> B2C

    R -.->|"Blend n zu 1<br/>BRUCHSTELLE 3"| R
    R -.->|"Silo-Vermischung<br/>BRUCHSTELLE 4"| R
```

**Lesehilfe:** Die vier Bruchstellen sind in `02-stakeholder-und-prozesse.md`, Abschnitt 3 erläutert. Kein Ledger repariert sie — er dokumentiert sie nur unveränderlich.

---

## 2. EUDR-Rollenentscheidung je Lot

Die Entscheidung fällt **je Lot**, nicht je Unternehmen. Bei Mischform-Beschaffung laufen beide Zweige parallel.

```mermaid
flowchart TD
    START["Neues Gruenkaffee-Lot"] --> Q1{"Wer ist Anmelder<br/>auf der Zollanmeldung<br/>bei der Einfuhr in die EU?"}

    Q1 -->|"Wir"| PRIM["PRIMAERBETREIBER"]
    Q1 -->|"EU-Importeur / Haendler"| DOWN["ERSTER DOWNSTREAM-BETREIBER"]
    Q1 -->|"unklar"| KLAER["Klaerung Zoll und Recht<br/>siehe 10-offene-fragen A1"]
    KLAER --> Q1

    PRIM --> PA1["Geolokation aller Parzellen<br/>Polygon ab 4 ha, sonst Punkt"]
    PA1 --> PA2["Erntezeitraum + Legalitaetsnachweise"]
    PA2 --> PA3["Risikobewertung gegen<br/>Waldverlustdaten, Stichtag 31.12.2020"]
    PA3 --> PA4{"Risiko<br/>vernachlaessigbar?"}
    PA4 -->|"nein"| PA5["Risikominderung<br/>dokumentiert"]
    PA5 --> PA3
    PA4 -->|"ja"| PA6["DDS in TRACES einreichen<br/>VOR Inverkehrbringen"]
    PA6 --> REF["Referenznummer erhalten"]

    DOWN --> DA1["DDS-Referenznummer<br/>vom Importeur einholen"]
    DA1 --> DA2{"Nummer<br/>vorhanden?"}
    DA2 -->|"nein"| STOP["Ware NICHT weitergeben<br/>Vertragsfall, siehe 10 A4"]
    DA2 -->|"ja"| REF

    REF --> WEITER["Referenznummer aufbewahren<br/>und an eigene Abnehmer weitergeben"]
    WEITER --> OFFEN{"Loest Roesten ein erneutes<br/>Inverkehrbringen aus?<br/>Rechtsfrage offen"}
    OFFEN -->|"nein, herrschende Lesart"| ENDE["Weitergabe genuegt"]
    OFFEN -->|"falls ja"| NEU["Eigene DDS auch fuer<br/>Pfad-B-Ware noetig"]
```

**Hinweis:** Der Zweig `OFFEN` ist die in `01-regulatorik.md`, Abschnitt 2.4 beschriebene ungeklärte Rechtsfrage. Das Datenmodell trägt beide Ausgänge.

---

## 3. Massenbilanz beim Blenden — n zu 1 mit Verlust

```mermaid
flowchart LR
    subgraph INPUT["Input: n Roestchargen"]
        R1["RST-001<br/>Herkunft Aethiopien<br/>m_ist = 42,0 kg"]
        R2["RST-002<br/>Herkunft Kolumbien<br/>m_ist = 30,5 kg"]
        R3["RST-003<br/>Herkunft Brasilien<br/>m_ist = 12,0 kg"]
    end

    MIX(["Transformationsereignis<br/>BLENDEN"])

    R1 -->|"anteil_ist 49,6 %<br/>soll 50 % plus minus 5 pp"| MIX
    R2 -->|"anteil_ist 36,0 %<br/>soll 35 % plus minus 5 pp"| MIX
    R3 -->|"anteil_ist 14,2 %<br/>soll 15 % plus minus 5 pp"| MIX

    MIX --> OUT["BLD-2027-014<br/>Auswaage m_blend = 84,0 kg"]
    MIX --> VERL["Prozessverlust 0,3 kg<br/>Handling, Mischerrest"]
    MIX --> EPS["Messtoleranz 0,2 kg<br/>innerhalb 0,5 % Grenze"]

    OUT --> CHK{"Pruefung<br/>Summe Input = 84,5 kg<br/>Summe Output + Verlust = 84,5 kg"}
    CHK -->|"erfuellt"| OK["Buchung frei<br/>Inputs auf locked gesetzt<br/>Rezepturzeilen geschrieben"]
    CHK -->|"verletzt"| ALARM["Buchung blockiert<br/>Begruendung erforderlich"]

    OK --> DPP["DPP-Anzeige speist sich<br/>aus anteil_ist dieser Charge,<br/>NIE aus der Rezeptur"]
```

**Kernregeln:** Inputs werden gesperrt, nicht gelöscht. `anteil_ist` ist die Wahrheit, `anteil_soll` nur Abweichungskontrolle. Details in `05-massenbilanz-und-token.md`.

---

## 4. Systemarchitektur Option B — die Empfehlung

Die gestrichelte Box ist Phase 2 und wird nur bei Eintritt eines Auslösekriteriums aktiviert. Sie hängt an einer austauschbaren Senke.

```mermaid
flowchart TB
    subgraph Q["Datenquellen"]
        SAAS["EUDR-Compliance-SaaS<br/>zugekauft"]
        ERP["ERP / Warenwirtschaft<br/>vorhanden"]
        ROAST["Roestsoftware + Waage<br/>Cropster oder gleichwertig"]
        METER["Gas- und Stromzaehler<br/>Modbus / MQTT"]
    end

    subgraph CORE["Event Store, Eigenbau, PostgreSQL + PostGIS"]
        EV["Append-only Ereignisse<br/>EPCIS 2.0 als JSON"]
        SIG["Signatur Ed25519<br/>je Organisation und Geraet"]
        GRADE["Evidence Grading<br/>Verified / Declared / Imported / Estimated"]
        MB["Massenbilanz-Constraints<br/>Summe Input groesser gleich Output plus Verlust"]
        MERKLE["Merkle-Root je Tag"]
    end

    subgraph OUT["Ausgaben"]
        DPP["DPP-Renderer<br/>GS1 Digital Link, QR"]
        API["B2B-API<br/>Referenznummern, CO2-Aufschluesselung"]
        AUDIT["Audit-Pack-Export<br/>fuer Behoerde"]
        TRACE["Trace-Abfrage<br/>Rueckruf"]
    end

    subgraph ANCHOR["Phase 2 — nur bei Ausloesekriterium"]
        TSA["eIDAS-Zeitstempel<br/>RFC 3161"]
        OTS["OpenTimestamps<br/>kostenlos"]
        HCS["Hedera HCS<br/>0,0008 USD je Nachricht"]
    end

    SAAS --> EV
    ERP --> EV
    ROAST --> EV
    METER --> EV

    EV --> SIG --> GRADE
    EV --> MB
    GRADE --> MERKLE

    GRADE --> DPP
    GRADE --> API
    EV --> AUDIT
    EV --> TRACE

    MERKLE -.->|"austauschbare Senke"| TSA
    MERKLE -.-> OTS
    MERKLE -.-> HCS

    SAAS -->|"DDS"| TRACES["TRACES<br/>EU-Informationssystem"]
```

**Die eine Architekturvorgabe, die Phase 1 aus Phase 2 mitnehmen muss:** Der Merkle-Root wird immer gebildet, die Senke bleibt austauschbar. Der Wechsel von einer Zeitstempelstelle auf einen Ledger ist dann Konfiguration, kein Umbau. Begründung in `04-architektur-optionen.md`, Abschnitt 2.
