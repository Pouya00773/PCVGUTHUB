# Anbieter, Abos und Risiken

Stand der Recherche: August 2026. Wo ich Preise **nicht** verifizieren konnte, steht das
ausdrücklich dabei – die Seiten von Traumwohnung.ai, Wohnly.ai und ImmoScout24 selbst sind
aus dieser Umgebung heraus nicht abrufbar (Egress-Proxy), ich konnte also nur über
Suchergebnisse und Drittquellen arbeiten. **Preise bitte vor dem Buchen selbst gegenprüfen.**

---

## 1. Die vier Kategorien

Es hilft, nicht alles in einen Topf zu werfen. Die Dienste unterscheiden sich vor allem darin,
**wie tief sie in deinen ImmoScout24-Account greifen** – und daran hängt das Risiko.

### Kategorie A – ImmoScout24s eigenes Produkt (kein Risiko)

**ImmoScout24 SuchenPlus** (früher „MieterPlus")

| Laufzeit | Preis pro Monat |
|---|---|
| 12 Monate | 12,99 € |
| 6 Monate | 19,99 € |
| 2 Monate | 29,99 € |

Was drin ist:
- **Bewerbermappe** mit Mieter-Selbstauskunft, Einkommensnachweis, Mietzahlungsbestätigung
  und Identitätsprüfung. Einkommen und Identität werden über eine **Bankkonto-Anbindung**
  verifiziert – das ist der Punkt, der die Mappe für Vermieter glaubwürdig macht, weil die
  Daten von ImmoScout24 bestätigt sind und nicht von dir behauptet.
- **TOP-Bewerber-Siegel**, sobald die Mappe vollständig ist.
- **Früherer Zugriff** auf einen Teil der privaten Inserate (zeitlich begrenzter Vorsprung).
- **Bis zu 40 % Rabatt** auf den SCHUFA-BonitätsCheck.

Was **nicht** drin ist: die SCHUFA-Auskunft selbst (separat zu bestellen) und jede Form von
automatischem Bewerben. SuchenPlus verschickt nichts für dich.

Kritische Einordnung aus unabhängigen Tests: Der einzige wirklich belegbare Vorteil ist der
zeitlich begrenzte Frühzugriff auf einen Teil der Inserate. Der Rest ist Komfort und
Signalwirkung – wobei die Signalwirkung der verifizierten Mappe bei Berliner Massenbesichtigungen
real etwas taugt.

---

### Kategorie B – Benachrichtigungs-Bots (geringes Risiko)

**Immobilien-Bot.de** – 2,99 € für 7 Tage oder 7,99 € pro Monat, davor 7 Tage kostenlos
(Testphase startet mit der ersten Suche).

Der Bot durchsucht ImmoScout24, Immowelt, Kleinanzeigen, immobilien.de, LEG u. a. rund um die
Uhr und schickt dir eine **Echtzeit-Push-Benachrichtigung**, sobald ein passendes Inserat
online geht. **Bewerben tust du dich selbst.**

Das ist der pragmatische Mittelweg: Du bekommst den Geschwindigkeitsvorteil, gibst aber keine
Zugangsdaten aus der Hand, und dein Account tut nichts Automatisiertes. Mit einer fertigen
Textbaustein-Bibliothek (liegt in `../output/` bereit) bist du nach der Push in unter zwei
Minuten beworben – das reicht in den meisten Fällen.

---

### Kategorie C – Voll-Automaten (funktioniert, aber mit Preis)

**Traumwohnung.ai** und **Wohnly.ai** – beide versprechen dasselbe Grundprinzip: Kriterien
einmal hinterlegen, der KI-Agent durchsucht ImmoScout24, Immowelt und Immonet parallel und
verschickt binnen Sekunden eine **personalisierte Bewerbung**, 24/7.

Preise, soweit belegbar:
- **Traumwohnung.ai**: kostenloser Einstieg mit 50 Nachrichten-Guthaben, dann „Traumwohnung+"
  als Monatsabo mit **kostenpflichtiger 7-Tage-Testphase**. Achtung, das ist die Konstruktion,
  bei der Leute in die Falle laufen: Es fällt ein einmaliges Testentgelt an, und **das Abo
  verlängert sich nach der Testphase automatisch monatlich**, wenn du nicht vor Ablauf kündigst.
  Abrechnung über Stripe. Den konkreten Monatspreis konnte ich nicht verifizieren – er wird
  erst im Checkout ausgewiesen.
- **Wohnly.ai**: Preise nicht verifizierbar. Auf Trustpilot 4 Sterne, aber nur eine Handvoll
  Bewertungen – das ist statistisch nichts. Gilt genauso für Traumwohnung.

**Das eigentliche Problem dieser Kategorie:** Damit der Dienst *in deinem Namen* auf
ImmoScout24 bewerben kann, braucht er Zugriff auf deinen Account. Es gibt keine offizielle
ImmoScout24-API für Mieterbewerbungen – die Dienste automatisieren also die normale Website.
Praktisch heißt das: deine Zugangsdaten liegen bei einem Dritten.

---

### Kategorie D – Selbstbau (nicht empfohlen)

Auf **Apify** gibt es einen fertigen „ImmoScout24 Apply Bot – Auto Applications". Technisch
könnte man den mieten oder etwas Vergleichbares selbst schreiben.

Ich rate davon ab und baue dir das auch nicht: In dem Moment bist **du** der Betreiber des
Bots. Die AGB-Verletzung ist dann unmittelbar deine, nicht die eines Dienstleisters, und der
Account, der gesperrt wird, ist deiner – mitten in der Wohnungssuche. Der Aufwand steht in
keinem Verhältnis zum Nutzen gegenüber Kategorie A + B.

---

## 2. Die AGB-Lage – nüchtern

Die ImmoScout24-Nutzungs-AGB sind eindeutig: **Automatisierte Abfragen mittels Skripten, Bots,
Crawlern und ähnlichen Maßnahmen sind untersagt**, insbesondere Data Mining und Data Extraction.
Zulässig ist ausdrücklich nur, über die bereitgestellten Online-Suchmasken einzelne Datensätze
sichtbar zu machen. Ebenfalls untersagt: die gewonnenen Daten zum Aufbau einer eigenen Datenbank
zu verwenden.

**Was das konkret bedeutet:**

- Das ist **Zivilrecht, kein Strafrecht**. Du machst dich nicht strafbar. Die realistische
  Konsequenz ist eine **Sperrung deines ImmoScout24-Accounts** – im ungünstigsten Moment, nämlich
  wenn du gerade mitten in Bewerbungen steckst.
- Das Risiko trägt **dein** Account, auch wenn der Dienstleister den Bot betreibt. Er verliert
  einen Kunden, du verlierst deinen Zugang und deine Bewerbungshistorie.
- Die Weitergabe von Zugangsdaten an Dritte ist zusätzlich ein Punkt, den du bei einem
  Datenleck des Anbieters ausbaden würdest. Nutze dort **in jedem Fall ein eigenes,
  einmaliges Passwort**, das du nirgends sonst verwendest.
- Nebenbei: ImmoScout24 lehnt automatisierte Bewerbungen ohnehin ab, wenn das Profil
  unvollständig ist. Ein Bot auf einem halbfertigen Profil ist rausgeworfenes Geld – die
  vollständige Mappe ist die Voraussetzung, nicht die Kür.

Ich sage dir nicht, dass du Kategorie C nicht nutzen darfst – das ist deine Entscheidung, und
viele tun es. Ich sage dir, dass der Trade-off lautet: *mehr Tempo gegen das Risiko, den
Account zu verlieren, plus ein Abo mit automatischer Verlängerung.*

---

## 3. Kostenrechnung für drei Monate Suche

| Variante | Posten | Summe 3 Monate |
|---|---|---|
| **Sparsam** | SCHUFA-BonitätsCheck (~30 €) + Immobilien-Bot (3 × 7,99 €) | **≈ 54 €** |
| **Empfohlen** | SuchenPlus 6-Mon.-Abo (3 × 19,99 €) + SCHUFA mit Rabatt (~20 €) + Immobilien-Bot (3 × 7,99 €) | **≈ 104 €** |
| **Voll-Automat** | wie „Empfohlen" + Traumwohnung+/Wohnly (Monatspreis unbekannt, Schätzung 20–40 €/Mon.) | **≈ 165–225 €** |

Zum Vergleich: Eine einzige Wohnung, die du wegen zu langsamer Antwort verpasst, kostet dich
in Berlin mehr als der Unterschied zwischen diesen Zeilen. Aber ein Voll-Automat auf einer
unvollständigen Mappe bringt gar nichts. **Erst die Mappe, dann das Tempo.**

---

## 4. Wenn du dich für Kategorie C entscheidest – Schutzmaßnahmen

1. **Eigenes Passwort** für ImmoScout24, nirgendwo sonst verwendet.
2. **Kalendereintrag auf Tag 6** der Testphase – vor der automatischen Verlängerung kündigen,
   falls es nicht überzeugt.
3. **Zahlung über PayPal oder Kreditkarte**, nicht Lastschrift – leichter zu stoppen.
4. **Bewerbungen stichprobenartig kontrollieren.** Ein generisches oder fehlerhaftes
   KI-Anschreiben in deinem Namen schadet mehr, als es nutzt. Hinterlege dort deine eigenen
   Textbausteine aus `../output/Wohnungs-Anschreiben_Vorlage.docx`, statt der KI freie Hand
   zu lassen.
5. **Erst starten, wenn die Bewerbermappe vollständig ist** – siehe oben.

---

## Quellen

- [ImmoScout24 – Nutzungs-AGB](https://www.immobilienscout24.de/agb/nutzungsagb.html)
- [ImmoScout24 – SuchenPlus Mitgliedschaft Mieten](https://www.immobilienscout24.de/suchende/suchenplus-mitgliedschaft-mieten.html)
- [ImmoScout24 – MeinPlus+ Bewerbermappe](https://www.immobilienscout24.de/meinplus/vorteile/mieterplus/bewerbermappe)
- [ImmoScout24 – Wohnungsbewerbung: Anschreiben, Unterlagen und Tipps](https://www.immobilienscout24.de/wissen/mieten/wohnungsbewerbung-tipps.html)
- [Wohnticker – ImmoScout MieterPlus: Kosten, Nutzen & Kündigung (2026)](https://wohnticker.de/ratgeber/immoscout-mieterplus-kosten)
- [Immobilien-Ranking – Lohnt sich ImmoScout Plus? MieterPlus/SuchenPlus im Check](https://www.immobilien-ranking.de/lohnt-sich-immoscout-plus-2026-mieterplus-suchenplus-check/)
- [ZEIT & WERT Immobilien – Was taugt die MieterPlus Mitgliedschaft](https://zeitundwert.de/aktuelles/was-taugt-die-mieterplus-mitgliedschaft-von-immoscout)
- [Traumwohnung.ai – AGB](https://traumwohnung.ai/agb/)
- [Traumwohnung.ai – Wohnungssuche Berlin](https://traumwohnung.ai/wohnungssuche-berlin/)
- [Wohnly – Traumwohnung AI Alternative im Vergleich](https://wohnly.ai/ratgeber/traumwohnung-ai-alternative)
- [Immobilien Bot](https://immobilien-bot.de/en/) · [AGB](https://immobilien-bot.de/agb/)
- [Apify – ImmoScout24 Apply Bot](https://apify.com/clearpath/immoscout24-apply-bot)
- [Berliner MieterGemeinschaft – Wohnungsbewerbung](https://www.bmgev.de/mietrecht/tipps-a-z/artikel/wohnungsbewerbung/)
- [DeinZimmer – Wohnungsbewerbung als Student:in](https://www.deinzimmer.de/artikel/wohnungsbewerbung-als-studentin)
