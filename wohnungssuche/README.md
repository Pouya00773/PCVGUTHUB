# Wohnungssuche Berlin – automatisierte Bewerbungen über ImmoScout24

Antwort auf die Frage: *„Kann eine KI wie Traumwohnung.ai für mich automatisch Wohnungs-
bewerbungen verschicken, welches Abo brauche ich, und kann Claude das für mich einrichten?"*

**Kurzfassung:**
1. Ja, solche Dienste existieren und funktionieren (Traumwohnung.ai, Wohnly.ai, Immobilien-Bot).
   Sie brauchen aber deine ImmoScout24-Zugangsdaten – das ist der Haken (siehe
   [`anbieter-und-abos.md`](anbieter-und-abos.md)).
2. Das Abo, das den größten *nachweisbaren* Vorteil bringt, ist **ImmoScout24 SuchenPlus**
   (früher „MieterPlus") – wegen Bewerbermappe und TOP-Bewerber-Siegel, nicht wegen der KI.
3. **Nein, ich kann dich nicht selbst bei ImmoScout24 anmelden** – drei harte Gründe unten.
4. Was ich stattdessen gemacht habe: alle Inhalte fertig vorbereitet, damit dein manueller
   Teil auf **ca. 45–60 Minuten** schrumpft.

---

## 1. Warum ich die Anmeldung nicht selbst machen kann

Das ist keine Bequemlichkeit, sondern drei echte Blocker:

| Blocker | Details |
|---|---|
| **Netzwerk** | `immobilienscout24.de`, `traumwohnung.ai` und `wohnly.ai` sind vom Egress-Proxy dieser Umgebung blockiert. Ich habe es getestet – die Anfragen werden abgewiesen, bevor sie das Netz verlassen. Ich habe keinen Browser auf die Seite. |
| **Zugangsdaten** | Ich habe deine nicht, und du solltest sie mir auch nicht geben. Sie würden im Klartext im Chat-Verlauf und potenziell im Git-Repo landen. Dasselbe gilt für die KI-Dienste: dort trägst du deine Zugangsdaten selbst ein, nicht ich. |
| **AGB & Verifizierung** | Die ImmoScout24-Nutzungs-AGB verbieten automatisierte Abfragen per Skript, Bot oder Crawler ausdrücklich. Die Registrierung verlangt zudem E-Mail-/SMS-Bestätigung und für die verifizierte Bewerbermappe eine Bankkonto-Anbindung (Kontoblick/Ident). Das ist bewusst nicht delegierbar. |

**Realistische Arbeitsteilung:** Ich mache die Inhalte (Anschreiben, Selbstauskunft,
Dokumenten-Logistik, Anbieter-Entscheidung). Du machst die drei Klicks, die eine
verifizierte Identität erfordern.

---

## 2. Was ich dafür von dir brauche

Vollständige Liste in [`profil_daten.md`](profil_daten.md) – das ist ein ausfüllbarer
Fragebogen. Die wichtigsten Felder, ohne die keine Bewerbung rausgehen kann:

- Nettoeinkommen (Werkstudent AKG + ggf. BAföG/Unterstützung)
- Wunsch-Bezirke, max. Warmmiete, Zimmerzahl, Einzugstermin
- Bürge (Eltern?) inkl. deren Bereitschaft, Bonitätsunterlagen beizulegen
- WG oder Single-Wohnung, Haustiere, Raucher
- SCHUFA-Status (schon vorhanden? wie alt?)

Trag das direkt in `profil_daten.md` ein oder schreib es mir in den Chat – dann fülle ich
die Dokumente final aus und committe die fertigen Dateien.

---

## 3. Ablauf und realistische Dauer

### Phase 0 – schon erledigt (von mir)
Anbieter-Recherche, Anschreiben-Bausteine, Selbstauskunft-Vorlage, Dokumenten-Checkliste,
Generator-Skript. → `output/`

### Phase 1 – dein manueller Teil (**45–60 Min. aktiv**)
1. ImmoScout24-Konto anlegen bzw. einloggen, Profil vollständig ausfüllen (15 Min.)
2. SuchenPlus buchen, falls du dich dafür entscheidest (5 Min.)
3. Bewerbermappe befüllen: Selbstauskunft hochladen, Bankkonto für Einkommensverifikation
   verbinden (15 Min.)
4. SCHUFA-BonitätsCheck bestellen (10 Min. – **Ergebnis digital meist sofort bis 3 Werktage**)
5. Falls KI-Dienst: dort registrieren, Suchprofil + Anschreiben hinterlegen (15 Min.)

### Phase 2 – Wartezeiten, die du nicht beschleunigen kannst
| Baustein | Dauer |
|---|---|
| SCHUFA-BonitätsCheck | sofort (digital) bis ca. 3 Werktage |
| Elternbürgschaft + deren Unterlagen | 1–3 Tage (hängt an deinen Eltern) |
| Arbeitgeberbescheinigung AKG | 1–5 Werktage (HR anschreiben – Textbaustein liegt bei) |

### Phase 3 – laufender Betrieb
Ab dem Moment, wo Mappe + Automatisierung stehen, laufen Bewerbungen **rund um die Uhr
ohne dein Zutun**. Der Zeitvorteil ist der eigentliche Produktnutzen: in Berlin entscheidet
oft, wer in den ersten Minuten nach Inseratsschaltung antwortet.

### Ehrliche Gesamterwartung
- **Bis alles scharf geschaltet ist:** 3–7 Tage (Engpass ist fast immer die SCHUFA oder die Bürgschaft, nicht die Technik)
- **Bis zur ersten Besichtigungseinladung:** typisch 1–3 Wochen
- **Bis zum unterschriebenen Mietvertrag in Berlin:** realistisch **4–12 Wochen**

Kein Dienst verkürzt Phase 3 zuverlässig auf Tage. Wer das verspricht, verkauft Hoffnung.
Was Automatisierung real leistet: sie erhöht die *Anzahl* der Bewerbungen und deine
*Antwortgeschwindigkeit* – und damit die Trefferwahrscheinlichkeit pro Woche.

---

## 4. Meine Empfehlung

**Zweistufig, mit dem risikoarmen Teil zuerst:**

**Stufe 1 (sofort, geringes Risiko):** ImmoScout24 SuchenPlus im 6-Monats-Abo + vollständig
verifizierte Bewerbermappe + Suchagent mit Sofort-Benachrichtigung aufs Handy. Das ist
ImmoScout24s eigenes Produkt, verstößt gegen nichts, und das TOP-Bewerber-Siegel wirkt genau
dort, wo der Vermieter aussortiert. Mit fertigen Textbausteinen bist du manuell in unter
2 Minuten pro Inserat – das schlägt einen Bot mit halbfertiger Mappe.

**Stufe 2 (nur wenn Stufe 1 nach ~3 Wochen nicht reicht):** einen KI-Dienst dazunehmen.
Dann bewusst und mit offenen Augen: Zugangsdaten-Weitergabe und AGB-Konflikt sind real,
das Risiko ist eine Account-Sperre. Details und Anbietervergleich in
[`anbieter-und-abos.md`](anbieter-und-abos.md).

---

## 5. Dateien in diesem Ordner

| Datei | Inhalt |
|---|---|
| `README.md` | dieses Dokument – Überblick, Zeitplan, Empfehlung |
| [`anbieter-und-abos.md`](anbieter-und-abos.md) | Anbietervergleich, Preise, AGB-/Risikoanalyse |
| [`profil_daten.md`](profil_daten.md) | Fragebogen: was ich von dir brauche |
| `../scripts/build_wohnungsbewerbung.py` | erzeugt die DOCX-Dateien |

**Erzeugte Dokumente** (in `../output/`):
- `Mieter-Selbstauskunft.docx`
- `Wohnungs-Anschreiben_Vorlage.docx` (3 Varianten: Portal-Kurznachricht, Standard, mit Bürgschaft)
- `Bewerbermappe_Deckblatt.docx` (Deckblatt + Dokumenten-Checkliste)

```bash
pip install python-docx
python3 scripts/build_wohnungsbewerbung.py
```
