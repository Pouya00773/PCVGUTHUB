# 00 — Executive Summary

**Stand:** 08.09.2026 · **Adressat:** Geschäftsführung · **Entscheidungsbedarf:** Freigabe Phase 0 (sofort), Grundsatzentscheid Phase 1/2 (Q4 2026)

---

## Die Lage in vier Sätzen

Ihr seid mit >1.000 t Grünkaffee und >50 Mitarbeitenden **kein KMU**, also gilt die EU-Entwaldungsverordnung für euch ab dem **30.12.2026** — das sind ab heute rund **16 Wochen**. Weil ihr in Mischform beschafft, seid ihr **gleichzeitig** voller Betreiber (für eure Direct-Trade-Eigenimporte, mit voller Sorgfaltspflicht und Parzellen-Geolokation) und erster Downstream-Betreiber (für Ware von EU-Importeuren, mit stark reduzierten Pflichten). Der im Referenzfall beschriebene Blockchain-Stack löst diese Pflicht **nicht** und ist in 16 Wochen auch nicht produktiv zu bekommen. Wer jetzt ein DLT-Projekt startet statt Lieferantendaten zu beschaffen, verfehlt die Frist mit einer schönen Architektur.

## Vier Befunde, die den Auftrag verändern

**1. Für Kaffee gibt es keine DPP-Pflicht. [recherchiert]** Die Ökodesign-Verordnung (ESPR, VO (EU) 2024/1781) nimmt Lebensmittel in Art. 1 Abs. 2 ausdrücklich aus dem Anwendungsbereich; der Arbeitsplan 2025–2030 priorisiert Stahl, Textilien, Reifen, Aluminium, Möbel, Matratzen. Ein Digitaler Produktpass für euren Kaffee ist damit **freiwilliges Marketing**, kein Compliance-Projekt. Verpflichtend wird nur die Verpackungskennzeichnung nach PPWR — und die betrifft Recycling, nicht Herkunft. Wer den DPP als Pflicht verkauft, verkauft euch etwas Falsches. *(Details: `01-regulatorik.md`)*

**2. Der Engpass liegt upstream, nicht in der IT.** Das teure, langsame und riskante Element ist die Beschaffung belastbarer Parzellen-Geodaten von Kooperativen und Exporteuren in den Ursprungsländern — nicht die Software, die sie später speichert. Jede Architekturdiskussion, die vor der Beschaffungsfrage geführt wird, ist verfrüht. *(Details: `02-stakeholder-und-prozesse.md`)*

**3. Fairtrade-/Rainforest-Massenbilanz ersetzt EUDR nicht.** Zertifizierungssysteme erlauben die Vermischung zertifizierter und nicht-zertifizierter Ware; die EUDR verlangt Geolokation der Parzellen, aus denen die **tatsächlich gelieferte** Charge stammt. Die beiden Logiken sind nicht substituierbar. Ihr braucht beides, und die Zertifikate nehmen euch die EUDR-Arbeit nicht ab. *(Details: `01`, `05`)*

**4. Für die kryptografische Verankerung gibt es heute keinen zahlenden Nachfrager.** Die Ledger-Kosten sind irrelevant (Hedera: 0,0008 USD je Nachricht **[recherchiert]**, bei 500.000 Ereignissen/Jahr rund 400 USD **[geschätzt]**). Die relevanten Kosten sind Schlüsselverwaltung, Betrieb, Integration und Anbieterbindung. Solange kein B2B-Kunde Verifizierbarkeit vertraglich fordert, ist eine signierte Append-only-Datenbank mit Merkle-Root und externem Timestamping funktional gleichwertig und deutlich billiger. *(Details: `04-architektur-optionen.md`)*

## Empfehlung: drei Phasen, streng getrennt

| Phase | Zeitraum | Zweck | Charakter |
|---|---|---|---|
| **0 — Compliance** | jetzt → 30.12.2026 | EUDR-Fähigkeit: Lieferantenmanagement, Geodaten, Risikobewertung, DDS in TRACES, Referenznummern-Register | **Pflicht.** Muss auch dann stehen, wenn alles andere gestrichen wird. Zugekaufte Software, kein Eigenbau, kein Ledger. |
| **1 — Datenqualität** | 2027 | Chargen-Datenmodell nach GS1 EPCIS 2.0, Evidence Grading, CO₂ Scope 1/2 je Röstcharge, freiwilliger DPP für eine Pilot-SKU | **Freiwilliger Mehrwert.** Zahlt auf Einkauf, Qualitätssicherung, Rückruffähigkeit und B2B-Vertrieb ein. |
| **2 — Verankerung** | frühestens 2028, begründungspflichtig | Kryptografische Nachweisbarkeit der Zeitgleichheit | **Optional.** Nur starten, wenn ein benannter Abnehmer sie fordert oder mehrere misstrauische Parteien denselben Datenbestand schreiben. |

Phase 2 startet **nicht automatisch** nach Phase 1. Das Auslösekriterium steht in `07-mvp-und-roadmap.md`.

## Was wir aus dem Referenzfall streichen — und warum

- **Physische Sicherheitsmarker (M-Trust) für Grünkaffee** — gestrichen. Jutesäcke sind kein markierbarer Träger, und euer Problem ist Herkunftsnachweis, nicht Produktfälschung. Für die Endverbraucherverpackung wäre der Marker technisch machbar, löst aber ein Problem, das ihr nicht habt. *(Bewertung inkl. Alternativen: `04`)*
- **ERC-1155-Token-Ownership für Endkunden** — gestrichen. Ein Kaffeekäufer will nicht Eigentümer eines Tokens werden. Die Massenbilanz-Logik behalten wir, sie braucht aber keine Chain. *(`05`)*
- **jBPM / Keycloak / Enterprise-SSO / BPMN-Workflow-Engine** — gestrichen. Bei eurer Größe ist das Overhead ohne Gegenwert. *(`04`)*

Behalten wird ausdrücklich das **Evidence Grading** (Verified/Declared): Es ist der intelligenteste Teil des Referenzfalls, kostet fast nichts und funktioniert ohne jede Blockchain.

## Der ehrliche Satz zum Schluss

Wenn ihr am Ende dieses Projekts sauberes Lieferantenmanagement, verlässliche Parzellendaten, ein durchgängiges Chargen-Datenmodell und eine testierte Auswertung habt — dann habt ihr 90 % des Nutzens, und zwar unabhängig davon, ob je ein Hash auf einem Ledger landet. Die Verankerung ist das letzte Prozent, und sie ist erst dann sinnvoll, wenn jemand dafür zahlt.

---

## Quellen zu dieser Seite

Vollständige Quellenangaben in den Detaildokumenten. Die vier Befunde stützen sich auf:

- EUDR-Fristen und Rollenlogik: [VO (EU) 2025/2650, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502650) · [Rat der EU, 18.12.2025](https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/) → `01`
- ESPR-Ausnahme für Lebensmittel: [VO (EU) 2024/1781, Art. 1 Abs. 2](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202401781) → `01`
- Fairtrade-Geolokationstool für Kooperativen: [Daily Coffee News, 16.06.2026](https://dailycoffeenews.com/2026/06/16/fairtrade-launches-free-eudr-geolocation-tool-for-coffee-cooperatives/) → `01`, `02`
- Hedera-Transaktionspreis ab Januar 2026: [Hedera Blog](https://hedera.com/blog/price-update-to-consensussubmitmessage-in-consensus-service-january-2026/) → `04`, `08`

---

*Kennzeichnung der Aussagen in allen Dokumenten: **[recherchiert]** mit Quelle · **[angenommen]** · **[geschätzt]**.*
