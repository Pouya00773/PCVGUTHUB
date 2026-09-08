# 04 — Architektur- und Stack-Optionen, Build vs. Buy

---

## 1. Drei bewertete Optionen

### Option A — „Zukauf": Compliance-SaaS + ERP, kein Ledger

```
Kooperative/Exporteur ──(CSV/GeoJSON/Portal)──▶ EUDR-Compliance-SaaS ──(DDS)──▶ TRACES
                                                        │
                                                        ├──(API/CSV)──▶ ERP (Chargen, Bestände)
                                                        └──▶ Referenznummern-Register
```

| | |
|---|---|
| **Was es kann** | Volle EUDR-Konformität für beide Pfade. Geodatenaufnahme, Risikoscreening gegen Waldverlustdaten, DDS-Einreichung, Referenznummernverwaltung, Audit-Export |
| **Was es nicht kann** | Chargengenaue Verknüpfung über Röstung und Blend, CO₂ je Charge, DPP, kryptografische Nachweisführung |
| **Zeit bis produktiv** | **6–10 Wochen** **[geschätzt]** — als einzige Option innerhalb der Frist |
| **Risiko** | Anbieterbindung; Chargenlogik bleibt im ERP, evtl. mit Lücken über den Röstprozess |
| **Urteil** | **Zwingend. Das ist Phase 0.** Auch wenn ihr später B oder C baut, braucht ihr das jetzt. |

### Option B — Hybrid: Zukauf Compliance + schlanker Eigenbau Daten-/DPP-Schicht *(Empfehlung)*

```
                          ┌──────────────────────────────────────────┐
Compliance-SaaS ──────────▶│  Event Store (Append-only, EPCIS 2.0)    │
ERP / Warenwirtschaft ────▶│  · signierte Ereignisse                  │──▶ DPP-Renderer (QR)
Röstsoftware / Waage ─────▶│  · Merkle-Root je Tag                    │──▶ B2B-API
Gas-/Stromzähler ─────────▶│  · Evidence Grading                      │──▶ Audit-Pack-Export
                          └──────────────────────────────────────────┘
                                          │ (optional, Phase 2)
                                          ▼  Merkle-Root → externer Zeitstempel
```

| | |
|---|---|
| **Was es kann** | Alles aus A, plus durchgängige Chargenkette, CO₂ je Röstcharge, freiwilliger DPP, Rückruf-Trace, Evidence Grading, und — **als abtrennbarer Zusatz** — Verankerung |
| **Kern der Sparsamkeit** | Der Event Store ist eine Postgres-Datenbank mit Append-only-Disziplin und EPCIS-2.0-JSON. Kein Framework, keine Chain, keine Workflow-Engine. Der teure Teil sind die **Konnektoren**, nicht der Speicher. |
| **Zeit bis produktiv** | 4–8 Monate nach Phase 0 **[geschätzt]** |
| **Risiko** | Ihr betreibt Software. Ohne benannte interne Verantwortung verrottet sie. |
| **Urteil** | **Empfehlung für Phase 1.** Die Verankerung wird vorbereitet (Merkle-Root wird ohnehin gebildet), aber nicht aktiviert. |

### Option C — Referenzfall-Klon: TrackTrace / Hedera / DIDs / VCs / Token

| | |
|---|---|
| **Was es kann** | Alles aus B, plus verteilte Schreibrechte für misstrauische Parteien, plus kryptografischer Nachweis der Zeitgleichheit gegenüber Dritten, plus Token-Ownership |
| **Was es zusätzlich kostet** | Schlüsselverwaltung über Organisationsgrenzen hinweg, Onboarding jedes Partners, Betriebs-Know-how, Anbieterbindung an einen jungen Markt, Rechtsklärung der DSGVO-Konstruktion (`03`, 4.3) |
| **Zeit bis produktiv** | 12–24 Monate mit Partner-Onboarding **[geschätzt]** |
| **Urteil** | **Heute nicht begründbar.** Es fehlt der Nachfrager. Auslösekriterium in `07`. |

---

## 2. Die Gegenthese, ernsthaft geprüft

> *Reicht eine signierte, extern testierte Datenbank mit Merkle-Tree und regelmäßigem Timestamping?*

**Antwort: Für euren Fall ja.** Die Begründung ist nicht Kostenersparnis.

**Was ein Ledger tatsächlich leistet:** Er beweist, dass ein Datensatz zu einem Zeitpunkt existierte (Zeitgleichheit), und er erlaubt mehreren Parteien, die einander nicht vertrauen, in denselben Bestand zu schreiben, ohne dass eine von ihnen die Reihenfolge kontrolliert.

**Was davon braucht ihr?**

| Eigenschaft | Braucht ihr sie? | Ohne Chain erreichbar? |
|---|---|---|
| Zeitgleichheitsnachweis („der Beleg lag am Tag X vor") | **Ja** — genau das ist der Kern des EUDR-Nachweises | **Ja.** Merkle-Root je Tag + qualifizierter Zeitstempel nach eIDAS (RFC 3161) oder OpenTimestamps. Beweiskraft eines qualifizierten Zeitstempels vor einem EU-Gericht ist **höher** als die einer Chain-Transaktion. |
| Manipulationsschutz gegen euch selbst | Ja | **Ja.** Append-only + externer Zeitstempel + Wirtschaftsprüfer-Testat der Kontrollen. |
| Schreibrechte für misstrauische Dritte | **Nein.** Ihr seid der einzige Schreiber; alle anderen liefern euch Daten. | entfällt |
| Öffentliche Verifizierbarkeit ohne euch | Nein — niemand fragt danach | (Chain-Vorteil, ungenutzt) |
| Token-Ownership für Endkunden | Nein | entfällt |

**Die Kosten sind nicht das Argument.** Hedera hat den Preis für `ConsensusSubmitMessage` zum Januar 2026 von 0,0001 auf **0,0008 USD** je Nachricht angehoben (fixer USD-Preis) **[recherchiert]** ([Hedera, Preisänderung Jan. 2026](https://hedera.com/blog/price-update-to-consensussubmitmessage-in-consensus-service-january-2026/)). Rechnung für euch:

| Verankerungsgranularität | Ereignisse/Jahr **[geschätzt]** | Kosten/Jahr |
|---|---|---|
| Je Ereignis (Rohdaten) | ~500.000 | **~400 USD** |
| Je Charge (Röst-/Blend-/Packcharge) | ~20.000 | ~16 USD |
| Je Tages-Merkle-Root | 365 | ~0,30 USD |

*Basis: >1.000 t/Jahr, angenommene Chargengröße 60 kg, rund 17.000 Röstchargen, zzgl. Blend-, Pack- und Wareneingangsereignisse.* **[geschätzt]**

Wer sagt, Blockchain sei zu teuer, hat nicht gerechnet. **Die realen Kosten liegen bei Integration, Schlüsselverwaltung und Betrieb — und die entstehen unabhängig vom Transaktionspreis.** Genau darum ist die Empfehlung: Merkle-Root bilden (das ist billig und nützlich), Verankerungsziel offenlassen. Der Wechsel von einer RFC-3161-TSA auf Hedera ist später eine Konfigurationsänderung, kein Umbau — **wenn** ihr die Verankerung von Anfang an als austauschbare Senke baut. Das ist die eine Architekturvorgabe, die Phase 1 aus Phase 2 mitnehmen muss.

**Empfohlene Verankerungsstrategie in Phase 1:** Tages-Merkle-Root, qualifizierter eIDAS-Zeitstempel, zusätzlich (kostenlos) OpenTimestamps. Latenz: bis 24 h — für EUDR-Nachweiszwecke völlig ausreichend, da die Beweisfrage „lag der Beleg vor der Einfuhr vor?" auf Tagesebene entschieden wird, nicht auf Sekundenebene.

---

## 3. Build vs. Buy — der Markt löst Phase 0 bereits

**Kaufen, nicht bauen.** Für EUDR-Compliance existiert 2026 ein funktionierender Anbietermarkt; ein Eigenbau wäre in 16 Wochen weder fertig noch auditierbar.

| Anbieter | Deckt ab | Bewertung |
|---|---|---|
| **Cropster** | Röstsoftware mit Chargenverwaltung, Grünkaffee-Kontraktmanagement (Dokumente, Ereignisse, Vorwärts-Traceability auf Lot-Ebene) **und EUDR-Tooling** **[recherchiert]** ([Cropster Produktankündigung](https://www.cropster.com/blog-post/beyond-the-roast-episode-1/)) | **Stärkster Kandidat für Phase 0+1 zugleich.** Ihr habt es heute nicht — das ist die größte einzelne Lücke in eurer Systemlandschaft, weil bei euch die Röstchargendaten nicht strukturiert anfallen. Prüfen, ob EUDR-Modul beide Pfade (Primär + Downstream) abdeckt. |
| **Koltiva** | Polygonkartierung im Feld (KoltiTrace), Lieferantenerfassung, Risikoscreening, DDS-Einreichung, API/ERP-Integration **[recherchiert]** ([Koltiva EUDR](https://www.koltiva.com/eudrcompliance)) | Stark **upstream**, dort wo euer Engpass ist. Kandidat, wenn Kooperativen noch nicht kartiert sind. |
| **Meridia, Sourcemap, Fairfood** | Lieferkettenkartierung und Rückverfolgbarkeit | Etablierte Alternativen, je nach Ursprungsland unterschiedliche Feldpräsenz |
| **Fairtrade Fairtrace** | Kostenlose Geolokationserfassung für Fairtrade-Kooperativen, Weitergabe an Importeure ab Okt. 2026 **[recherchiert]** ([Daily Coffee News](https://dailycoffeenews.com/2026/06/16/fairtrade-launches-free-eudr-geolocation-tool-for-coffee-cooperatives/)) | **Zuerst prüfen.** Kostet nichts, deckt evtl. einen Teil eurer Herkünfte ab. |
| **TRACES (EU)** | Amtliches Informationssystem für DDS-Einreichung; Funktionsweise durch Kommissionsmaßnahme vom 13.07.2026 festgelegt **[recherchiert]** | Kein Anbieter, sondern Pflichtziel. Jede Software muss dorthin liefern. |
| **The Hashgraph Group TrackTrace** | DPP + Traceability auf Hedera, Referenzfall | Nur relevant, wenn Option C. Bewertung: junger Anbieter, starke Bindung. |

**Was ihr selbst bauen solltet (und nur das):**

1. Konnektoren ERP ↔ Compliance-SaaS ↔ Röstdaten
2. Event Store + Evidence Grading
3. DPP-Renderer und B2B-API
4. Energiedatenerfassung je Charge

Das ist der differenzierende Teil, und es ist wenig Code. **Alles, was Regulatorik interpretiert (Risikoscreening, DDS-Formate, TRACES-Anbindung), wird gekauft** — dort ändert sich die Anforderung schneller, als ihr nachpflegen könnt.

---

## 4. Physische Authentifizierung: ehrliche Bewertung

Der Referenzfall setzt Mercks M-Trust™ ein — unsichtbare Pigmentmarker in Produkt oder Verpackung, verifiziert per Handgerät.

| Ansatz | Bei Grünkaffee (Jutesack) | Bei Endverbraucherverpackung | Urteil |
|---|---|---|---|
| **Pigmentmarker (M-Trust o. ä.)** | Sack ist austauschbar, wird oft umgepackt; Marker sagt nichts über den Inhalt | Technisch machbar | **Streichen.** Löst Fälschungsschutz — ein Problem, das ihr nicht habt. Ein Kaffee-Fälscher fälscht nicht eure Tüte, er verkauft billigeren Kaffee als teuren. |
| **Manipulationssichere Siegel + Sack-/Liner-IDs** (GrainPro/Videplast mit fortlaufender Nr., Siegelnummer im Ereignis erfasst) | **Machbar, günstig** | machbar | **Empfehlung.** Beweist Unversehrtheit zwischen zwei erfassten Punkten. Reicht für den realistischen Bedrohungsfall (Umpacken auf dem Transport). |
| **Stabilisotopen-/Spurenelementanalyse** (Labor) | **Der einzige Ansatz, der die Herkunft am Kaffee selbst prüft** — Isotopensignatur korreliert mit Geologie und Klima der Anbauregion | dito | **Als Stichprobe empfohlen.** Regionale Auflösung, nicht parzellenscharf; braucht eine Referenzdatenbank. Kosten je Probe im niedrigen dreistelligen Bereich **[geschätzt]**. 5–10 Proben/Jahr als Kontrollinstrument sind wirksamer als jeder Marker. |
| **Sensorik/NIR-Spektroskopie** | begrenzt aussagekräftig zur Herkunft | dito | Für Qualität nützlich, für Herkunft schwach |
| **Ganz verzichten** | — | — | **Vertretbar.** Wenn Siegel-Disziplin plus Stichprobenanalyse steht, ist der Grenznutzen eines Markers gering. |

> **Empfehlung: Marker streichen, Siegel + Isotopen-Stichprobe.** Das kostet einen Bruchteil und adressiert das reale Risiko — Substitution — statt des dekorativen.

---

## 5. Ausdrücklich gestrichene Referenzfall-Bestandteile

| Gestrichen | Begründung |
|---|---|
| **jBPM / BPMN-Workflow-Engine** | Eure Prozesse sind linear und wenige. Eine Workflow-Engine erzeugt Modellierungs- und Betriebsaufwand ohne Gegenwert. Statusfelder im Event Store genügen. |
| **Keycloak / Enterprise-SSO** | Bei <100 internen Nutzenden reicht die Rechteverwaltung des ERP und des SaaS. Ein zusätzlicher IdP ist eine zusätzliche Ausfallquelle. |
| **ERC-1155-Token-Ownership für Endkunden** | Kein Kaffeekäufer will Token-Eigentümer werden. Erzeugt zudem regulatorische Fragen (Wertpapier-/Geldwäscherecht), die man ohne Not nicht aufwirft. |
| **DIDs/VCs für einzelne Kleinbauern** | Onboarding-Hürde unrealistisch; erzeugt Scheinverifikation. Stellvertretende Erfassung, ehrlich als *Declared* gekennzeichnet, ist der bessere Weg (`03`, Abschn. 5). |
| **Physische Sicherheitsmarker** | siehe Abschn. 4 |
| **Consumer-App** | Ein QR-Code, der auf eine Webseite führt, ist ausreichend. Eine App, die niemand installiert, ist teurer Stillstand. |

**Behalten:** Evidence Grading, Hash-Verankerung als *optionale* Senke, Massenbilanz-Logik (als Buchhaltung, nicht als Token), Audit-Pack-Export, Trace-Abfrage für Rückrufe.

---

## 6. Konkreter Stack-Vorschlag für Option B

| Baustein | Technologie | Begründung |
|---|---|---|
| Event Store | PostgreSQL, Append-only-Tabellen, EPCIS-2.0-JSON in `jsonb`, PostGIS für Geometrien | Ein System für relationale Daten, Dokumente und Geodaten. Kein Spezialstore nötig. |
| Signatur | Ed25519, Schlüssel je Organisation/Gerät, Signatur über kanonisiertes JSON (JCS) | Klein, schnell, gut unterstützt |
| Integritätskette | Tages-Merkle-Root, RFC-3161-Zeitstempel + OpenTimestamps | Austauschbare Senke (Abschn. 2) |
| Konnektoren | schlanke Jobs (Python/TypeScript), Dateiimport + REST | Kein ESB, kein iPaaS bei dieser Zahl von Schnittstellen |
| DPP-Frontend | serverseitig gerenderte Seiten, GS1 Digital Link als URL-Schema | Muss Jahre stabil bleiben; kein SPA-Framework-Risiko |
| Energiedaten | Impulszähler Gas/Strom → Modbus/MQTT → Event Store | Siehe `06` |
| Compliance | zugekauft (Abschn. 3) | |

**Nicht im Stack:** Message Broker, Kubernetes, Data Lake, Workflow-Engine, Chain. Wenn eine dieser Komponenten später zwingend wird, war die Anforderung vorher unklar.
