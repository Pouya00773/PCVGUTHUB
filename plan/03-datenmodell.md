# 03 — Datenmodell, Identität und Datenschutz

---

## 1. Standardentscheid: GS1 EPCIS 2.0, kein Eigenformat

**Empfehlung: EPCIS 2.0 als Ereignismodell, GS1-Identifikatoren als Schlüssel.** **[recherchiert]**

Begründung:

- EPCIS 2.0 bildet genau das ab, was hier gebraucht wird: Ereignisse mit *what / when / where / why*, Aggregation (Sack → Palette), Transformation (Grünkaffee → Röstkaffee) und Ownership-Transfer. Es verbindet Ursprungsereignisse auf Feldebene — Erntestandort, Geolokation, Datum — über Aggregation, Verarbeitung und Export in einer durchgehenden Kette. ([GS1 EPCIS](https://www.gs1.org/standards/epcis) · [EPCIS/CBV Implementation Guideline](https://ref.gs1.org/guidelines/epcis-cbv/))
- Version 2.0 bietet REST/JSON-LD statt SOAP/XML — integrierbar ohne Speziallisten.
- **Für EUDR existiert bereits eine Umsetzungshilfe:** GS1 Germany EUDR Implementation Guideline (v1.11), und der GS1-EUDR-Provisional-Standard referenziert EPCIS als Mechanismus zur Übermittlung von Referenz- und Verifikationsnummern. ([GS1 Germany EUDR Guideline PDF](https://www.gs1-germany.de/fileadmin/gs1/fachpublikationen/GS1_Germany_EUDR_Guideline_V1.11.pdf))
- Eure Handelspartner im LEH sprechen ohnehin GS1. Ein Eigenformat müsstet ihr an jeder Schnittstelle übersetzen.

**Ehrliche Einschränkung:** EPCIS ist für den Feldbereich schwergewichtig. Kooperativen werden **kein** EPCIS senden. Die Umsetzung ist deshalb zweigeteilt: einfache Aufnahmeformate (CSV, GeoJSON, Excel) upstream — EPCIS als internes kanonisches Modell ab Wareneingang. Wer EPCIS bis zum Kleinbauern durchdrücken will, blockiert das Projekt. **[angenommen]**

---

## 2. Entitäten

| Entität | ID-Schema | Schlüsselattribute | Quelle |
|---|---|---|---|
| **Parzelle** (`Plot`) | interne UUID + Kooperativen-Referenz | Geometrie (Polygon >4 ha / Punkt), Fläche, Land, Erzeuger-Pseudonym, Landnutzungs-Legalitätsnachweis | Kooperative |
| **Erntecharge** (`HarvestLot`) | Kooperativen-Lot-Nr. | n Parzellen, Erntezeitraum, Menge kg cherry/parchment, Aufbereitungsart, Varietät | Kooperative |
| **Exportlot** (`ExportLot`) | ICO-Marks + Exporteur-Lot-Nr. | n Erntechargen, Sackzahl, Nettogewicht, Qualitätsanalyse, Phyto-/Ursprungszeugnis, Container-Nr. | Exporteur |
| **Grünkaffeepartie** (`GreenLot`) | **GTIN + Chargennummer**, intern `GRN-JJJJ-nnn` | Exportlot-Referenz, Einlagerungsgewicht, Lagerort, Feuchte, **EUDR-Rolle (A/B)**, **DDS-Referenznummer**, Zertifizierungsstatus | ihr / Importeur |
| **Röstcharge** (`RoastBatch`) | `RST-JJJJMMTT-nnn` | 1 GreenLot (oder n bei Pre-Blend), Einwaage, Auswaage, Röstprofil, Start/Ende, Röster-ID, Gasverbrauch, Stromverbrauch | Röstsoftware + Waage |
| **Blend** (`BlendBatch`) | `BLD-JJJJMMTT-nnn` | n Röstchargen mit Ist-Massen, Rezeptur-Soll, Auswaage | Produktion |
| **Verpackungseinheit** (`PackagedUnit`) | **GTIN + Los**, Umkarton **SSCC** | Blend- oder Röstchargen-Referenz, Füllgewicht, MHD, Verpackungsspezifikation | Abpackung |
| **Standort** | **GLN** | Rösterei, Lager, Kooperative, Exporteur | Stammdaten |

**Grundregel:** Jede Entität hat **genau einen** verantwortlichen Erfasser und **genau einen** Zeitstempel der Erfassung. Ohne diese beiden Felder funktioniert das Evidence Grading (`09`, Abschnitt Evidence) nicht.

---

## 3. Ereignistypen (EPCIS-Mapping)

| Fachlicher Vorgang | EPCIS-Ereignis | `bizStep` (CBV) | Anmerkung |
|---|---|---|---|
| Ernte auf Parzelle | ObjectEvent | `commissioning` | mit `sourceLocation` = Parzellengeometrie |
| Ablieferung Kooperative | AggregationEvent | `receiving` | Bruchstelle: Sammelbehälter |
| Aufbereitung / Trocknung | TransformationEvent | `commissioning` | Masseverlust cherry→parchment |
| Trockenmühle / Sortierung | TransformationEvent | `commissioning` | **Hauptbruchstelle**, `02` Abschn. 3 |
| Export / Verschiffung | ObjectEvent | `shipping` | Container, B/L |
| Wareneingang Rösterei | ObjectEvent | `receiving` | hier entsteht die `GreenLot` |
| **Rösten** | **TransformationEvent** | `commissioning` | 1:1 mit Masseverlust — Kernfall, `05` |
| **Blenden** | **TransformationEvent** | `commissioning` | n:1 — Kernfall, `05` |
| Mahlen | TransformationEvent | `commissioning` | geringer Verlust |
| Abpacken | AggregationEvent | `packing` | VE entsteht |
| Verkauf / Versand | ObjectEvent | `shipping` | Weitergabe DDS-Referenznummer |
| Rückruf | ObjectEvent | `holding` | rückwärts über Trace-Abfrage |

**Ergänzende Ereignisse, die nicht in CBV stehen und als Erweiterung geführt werden:** `EUDRDeclarationEvent` (DDS eingereicht, Referenznummer erhalten), `EnergyReadingEvent` (Gas-/Stromzählerstand je Röstcharge).

---

## 4. Datenschutz: der Konflikt, und wie er aufgelöst wird

### 4.1 Die Rechtslage

**GPS-Koordinaten kleinbäuerlicher Parzellen sind personenbeziehbare Daten**, sobald sie sich einer identifizierbaren natürlichen Person zuordnen lassen — und genau das tun sie, denn eine Parzelle hat einen Bewirtschafter. Bei einer Kooperative mit veröffentlichtem Mitgliederregister ist die Zuordnung trivial. Damit greift die DSGVO, einschließlich Art. 17 (Löschung). **[angenommen — dies ist die vorsichtige Auslegung; sie ist die einzige, die sich verteidigen lässt, und sollte datenschutzrechtlich bestätigt werden, siehe `10`]**

Gleichzeitig **verlangt** die EUDR die Übermittlung genau dieser Geolokation an das EU-Informationssystem. Der Konflikt ist also nicht „darf man" — man muss —, sondern: **was davon darf in ein unveränderliches System.**

### 4.2 Die Drei-Zonen-Regel

| Zone | Was liegt dort | Löschbar? |
|---|---|---|
| **Off-chain, zugriffsbeschränkt** (eure Datenbank / SaaS) | Parzellengeometrien, Erzeugernamen, Landtitel, Verträge, Preise, alle Dokumente | **Ja.** Vollständig, DSGVO-konform. |
| **Off-chain, veröffentlicht** (DPP, QR-Seite) | Land, Region, Kooperative, Höhenlage, Varietät, Aufbereitung, Erntejahr — **niemals Parzellengeometrie, niemals Erzeugername** | Ja |
| **On-chain / verankert** (nur in Phase 2) | **Ausschließlich Hashes** — nie ein Dokument, nie eine Koordinate, nie ein Name, nie ein Pseudonym mit Wiedererkennungswert | Nein — deshalb Abschn. 4.3 |

Diese Regel ist nicht verhandelbar. Ein einziges personenbezogenes Datum in einem unveränderlichen Ledger ist ein dauerhafter, nicht heilbarer Verstoß.

### 4.3 Auflösung des Konflikts Art. 17 DSGVO vs. Unveränderlichkeit: Crypto-Shredding

Ein blanker Hash über eine Koordinate ist **nicht** anonym: Der Suchraum von Koordinaten ist klein genug, um ihn per Brute Force zu durchsuchen. Ein Hash allein reicht also nicht.

**Verfahren:**

1. Je Parzelle (bzw. je Datensatz) wird ein zufälliges **Salt** erzeugt und **ausschließlich off-chain** in der löschbaren Zone gespeichert.
2. Verankert wird `H(salt || datensatz)`.
3. Prüfung durch Dritte ist möglich, solange ihr Salt und Datensatz vorlegt.
4. **Löschverlangen nach Art. 17:** Ihr löscht Datensatz **und** Salt. Zurück bleibt ein Hash, der ohne Salt nicht mehr auf eine Person zurückführbar und praktisch nicht mehr brute-forcebar ist — er ist damit nach herrschender Auffassung anonym geworden. Die Prüfbarkeit dieses einen Datensatzes ist danach dauerhaft verloren. **Das ist der Preis, und er ist zu akzeptieren.** **[angenommen — juristisch nicht abschließend geklärt; die Konstruktion ist etabliert, aber nicht höchstrichterlich bestätigt. Vor Phase 2 zwingend prüfen lassen.]**

**Konsequenz für die Architektur:** Solange Phase 2 nicht startet, existiert der Konflikt gar nicht. Ein weiterer Grund, die Verankerung nicht vorzuziehen.

### 4.4 Was ihr zusätzlich braucht

- **Rechtsgrundlage** für die Verarbeitung der Erzeugerdaten: rechtliche Verpflichtung (Art. 6 Abs. 1 lit. c DSGVO) für den EUDR-Teil; für die freiwillige DPP-Nutzung ein eigener Grund — Einwilligung ist bei Kleinbauern praktisch schwer sauber einzuholen. → `10`
- **Drittlandtransfer** in umgekehrter Richtung ist unkritisch (Daten fließen in die EU), aber SaaS-Anbieter mit Servern außerhalb der EU sind zu prüfen.
- **Auftragsverarbeitungsverträge** mit jedem Kartierungs- und Compliance-Dienstleister.

---

## 5. Identitäts- und Signaturkonzept — abgestuft nach Realität

Der Referenzfall vergibt DIDs und Verifiable Credentials an Personen, Prozesse und Geräte. Für euch ist das **nach Akteursklasse zu differenzieren**, sonst wird es Theater.

| Akteur | Was realistisch geht | Warum |
|---|---|---|
| **Rösterei, Geräte, Mitarbeitende** | **Volle Signatur.** Schlüssel auf Firmengeräten, Erfassung signiert, Zeitstempel aus vertrauenswürdiger Quelle. → Datenstufe **Verified** | Ihr kontrolliert die Geräte. Hier ist Kryptografie sinnvoll und billig. |
| **Exporteur, Importeur, größere Kooperative** | **Signatur möglich**, wenn vertraglich vereinbart. Einfachstes tragfähiges Mittel: Signatur auf Organisationsebene (ein Schlüssel je Organisation), nicht je Person. | Institutionen mit Bestandsinteresse. DID/VC-Infrastruktur ist hier vertretbar, aber Vertragsdurchsetzung ist wirksamer als Technik. |
| **Kleinbauer ohne Smartphone** | **Keine eigene Signatur.** Stellvertretende Erfassung durch die Kooperative, mit Kennzeichnung „erfasst durch X am Y". → Datenstufe **Declared** | Alles andere ist Fiktion. |

> **Der ehrliche Satz, der im Referenzfall fehlt:** Stellvertretende Erfassung **verschiebt** den Vertrauensanker von der Person auf die Institution — sie schafft ihn nicht. Wenn die Kooperative falsch erfasst, ist das Ergebnis kryptografisch einwandfrei und inhaltlich falsch. Deshalb ist die Bezeichnung als *Declared* nicht kosmetisch, sondern der Kern der Aussage. Siehe `09`, Risiko „Garbage in".

**Widerrufslogik:** Eine Sperrliste (Revocation List) je Organisationsschlüssel, geführt von euch, mit Gültigkeitsprüfung zum **Ereigniszeitpunkt**, nicht zum Prüfzeitpunkt — sonst entwertet ein Schlüsselwechsel rückwirkend die gesamte Historie. Für die Größenordnung reicht eine einfache Statusliste; W3C StatusList2021 ist der Standardweg, aber kein Muss.

**Streichung:** Enterprise-SSO (Keycloak), Rollen- und Berechtigungsmodelle auf Konzernniveau, eine BPMN-Engine (jBPM). Bei <100 internen Nutzenden ist das reiner Betriebsaufwand. Die Rechteverwaltung eures ERP plus die des Compliance-SaaS reicht. Begründung ausführlich in `04`.

---

## 6. Der DPP: freiwillig, deshalb selbst zu definieren

Weil ESPR nicht gilt (`01`, Abschn. 3), gibt es keinen Pflichtfeldkatalog. Empfohlene **Container/Content-Trennung**:

- **Container** = stabile, druckbare Adresse auf der Verpackung (GS1 Digital Link auf GTIN + Los). Ändert sich nie.
- **Content** = die aufgelöste Information, serverseitig, versioniert und änderbar. Trägt später auch die PPWR-Pflichtangaben (`01`, Abschn. 4) — **ein** Code, **eine** Datenbasis.

**Sichtbarkeitsstufen:**

| Stufe | Zielgruppe | Inhalt |
|---|---|---|
| Öffentlich | Endkunde | Land, Region, Kooperative (Name, wenn sie zustimmt), Höhe, Varietät, Aufbereitung, Erntejahr, Röstdatum, CO₂-Angabe mit Unsicherheitsband, Evidence-Kennzeichnung. **Keine Koordinaten. Keine Erzeugernamen.** |
| B2B (Login/Token) | Handelskunde | zusätzlich: DDS-Referenznummer, Chargenverknüpfung, Zertifikatsstatus, detaillierte CO₂-Aufschlüsselung |
| Behörde / Audit | zuständige Behörde | Audit-Pack: vollständige Kette inkl. Geodaten, Dokumente, Prüfprotokolle — **nicht öffentlich**, Export auf Anforderung |

**Blends im DPP — die heikle Stelle:**

Ein Hausblend mit vier Herkünften und chargenweise nachjustierten Anteilen darf **nicht** so dargestellt werden, dass eine einzelne Herkunft als *die* Herkunft erscheint. Regeln:

1. Alle Bestandteile werden genannt, absteigend nach Anteil.
2. Anteile werden als **Ist-Wert der konkreten Charge** ausgewiesen, nicht als Rezeptur-Soll — die Charge weiß, was in ihr ist. Ein Anteilsband („55–65 %") ist nur zulässig, wenn die Ist-Werte technisch nicht vorliegen, und muss dann als Band gekennzeichnet sein.
3. Bestandteile unter einer Bagatellgrenze (Vorschlag: 5 %) werden trotzdem genannt, nicht weggerundet.
4. Ändert sich die Zusammensetzung von Charge zu Charge, ändert sich der DPP-Inhalt — deshalb ist die Losnummer im Code zwingend, nicht optional.
5. **Keine Bauerngeschichte zu einem Blend**, wenn der Bauer 12 % beiträgt. Das ist der klassische Irreführungsfall.

---

## 7. Was das Datenmodell nicht kann

- Es kann die Aggregation in der Trockenmühle nicht auflösen (`02`, Abschn. 3). Es kann sie nur **dokumentieren** — mit einer Genauigkeitsangabe („Charge stammt aus 3 Kooperativen, Parzellenauflösung nur auf Kooperativenebene").
- Es kann falsche Eingangsdaten nicht erkennen. Plausibilitätsprüfungen (Ertrag pro Hektar, Polygon-Überlappung, Erntezeitfenster) fangen grobe Fehler, keine geschickten. `09`.
