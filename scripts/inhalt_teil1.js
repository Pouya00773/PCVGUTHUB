/**
 * Inhalt Teil 1 — Titel, Agenda, Block A (Sprecher:in 1), Block B (Sprecher:in 2).
 *
 * `notes` ist der ausformulierte Sprechtext, nicht Stichworte.
 * Richtwert: ~120 Wörter pro Minute.
 */

const TITEL_UND_AGENDA = [
  {
    layout: 'title',
    eyebrow: 'Hochschulprojekt · Verifizierbare Lieferketten',
    title: 'Rückverfolgbarer Kaffee:\nEUDR, Herkunftsnachweis\nund CO₂ je Charge',
    subtitle: 'Umsetzungsplan für eine Kaffeerösterei — abgeleitet aus dem Kakao-Piloten\nvon Hashgraph Group, Merck und PwC Germany',
    meta: 'Gruppenarbeit · fünf Vortragende · Rechercheschluss 09.09.2026',
    notes:
      'Guten Tag zusammen. Wir stellen heute einen Umsetzungsplan für eine Kaffeerösterei vor. '
      + 'Die Aufgabe war: ein System entwerfen für rückverfolgbare Herkunft, für die Konformität mit der EU-Entwaldungsverordnung und für produktgebundene CO₂-Daten. '
      + 'Als Vorbild diente ein Pilotprojekt, das die Hashgraph Group, Merck und PwC Germany im September 2026 für Kakao angekündigt haben — mit digitalem Produktpass, Blockchain-Verankerung und physischen Sicherheitsmarkern.\n\n'
      + 'Wir sagen gleich zu Beginn, wohin die Reise geht: Wir haben den Referenzfall nicht kopiert, sondern geprüft — und an vier Stellen kommen wir zu einem anderen Ergebnis als die Aufgabenstellung nahelegte. Einer dieser Befunde streicht einen kompletten Baustein, den digitalen Produktpass. Ein zweiter stellt die Blockchain selbst in Frage.\n\n'
      + 'Eine Vorbemerkung zur Ehrlichkeit unserer Zahlen: Die Rösterei ist ein konstruiertes Fallunternehmen. '
      + 'Alle Annahmen sind als solche gekennzeichnet. Und jede Aussage in unseren Unterlagen trägt eine Markierung — recherchiert mit Quelle, angenommen oder geschätzt. '
      + 'Dazu später mehr.\n\n'
      + 'Ich übergebe zunächst an die Agenda.',
  },
  {
    layout: 'agenda',
    kicker: 'Ablauf',
    title: 'Fünf Blöcke, fünf Vortragende',
    items: [
      { title: 'Ausgangslage und Vorgehen', desc: 'Referenzfall, Fallunternehmen, warum Kaffee anders ist als Kakao', speaker: 1, minutes: 'ca. 10 Min.' },
      { title: 'Regulatorik', desc: 'EUDR nach der Revision, Rollenfrage — und was überraschend nicht gilt', speaker: 2, minutes: 'ca. 10 Min.' },
      { title: 'Lieferkette und Datenmodell', desc: 'Akteure, Bruchstellen, GS1-Standard, Datenschutz, Evidence Grading', speaker: 3, minutes: 'ca. 10 Min.' },
      { title: 'Architektur und Massenbilanz', desc: 'Drei Optionen, die Gegenthese zur Blockchain, Röstverlust und Blends', speaker: 4, minutes: 'ca. 10 Min.' },
      { title: 'CO₂, Umsetzung und Risiken', desc: 'Bilanzierung ohne Scheingenauigkeit, MVP, Roadmap, Empfehlung', speaker: 5, minutes: 'ca. 10 Min.' },
    ],
    notes:
      'Wir haben den Vortrag in fünf Blöcke geteilt, jeder von uns übernimmt einen. '
      + 'Der erste Block — meiner — klärt die Ausgangslage: Was war der Referenzfall, mit welchem Unternehmen arbeiten wir, und warum kann man eine Kakao-Lösung nicht einfach auf Kaffee übertragen. '
      + 'Ich erkläre außerdem, wie wir methodisch vorgegangen sind, weil das für die Bewertung unserer Ergebnisse wichtig ist.\n\n'
      + 'Der zweite Block behandelt die Regulatorik — der Teil mit der größten Überraschung. Im dritten geht es um die Lieferkette und das Datenmodell. Der vierte ist der technische Kern: drei Architekturoptionen und die Prüfung, ob man überhaupt eine Blockchain braucht. Der fünfte bringt CO₂, Zeitplan, Kosten, Risiken und unsere Empfehlung.\n\n'
      + 'Wir haben rund fünfzig Minuten eingeplant und halten am Ende Zeit für Ihre Fragen frei. '
      + 'Damit starte ich in den ersten Block.',
  },
];

const BLOCK_A = [
  {
    layout: 'divider',
    num: 'A',
    title: 'Ausgangslage und Vorgehen',
    subtitle: 'Was war der Auftrag, mit welchem Unternehmen arbeiten wir,\nund warum ist Kaffee nicht Kakao?',
    speaker: 1,
    minutes: 10,
    notes:
      'Beginnen wir mit der Ausgangslage. Ich möchte Ihnen in diesem Block vier Dinge mitgeben: '
      + 'erstens, was der Referenzfall aus der Kakaobranche eigentlich beinhaltet; '
      + 'zweitens, welches Unternehmen wir betrachten und welche Annahmen wir dafür getroffen haben; '
      + 'drittens — und das ist der inhaltlich wichtigste Punkt —, an welchen Stellen sich Kaffee grundlegend von Kakao unterscheidet; '
      + 'und viertens, wie wir methodisch gearbeitet haben.',
  },
  {
    layout: 'cards',
    kicker: 'Der Referenzfall',
    title: 'Kakao-Pilot: Hashgraph Group, Merck und PwC Germany',
    speaker: 1,
    cols: 3,
    cards: [
      { badge: '1', title: 'TrackTrace', text: 'Plattform der Hashgraph Group für digitale Produktpässe. Erzeugt pro Charge einen digitalen Zwilling und erfasst Ereignisse an definierten Prüfpunkten.' },
      { badge: '2', title: 'M-Trust™ von Merck', text: 'Unsichtbare Sicherheitsmarker auf Pigmentbasis in Produkt oder Verpackung. Verifikation über ein Handlesegerät vor Ort.' },
      { badge: '3', title: 'Hedera als Ledger', text: 'Über den Consensus Service werden ausschließlich Hashes von Ereignissen und Dokumenten verankert — keine vertraulichen Inhalte. Beweist Zeitgleichheit.' },
      { badge: '4', title: 'PwC Germany', text: 'Geschäftsprozesse, Governance, Rollenmodell und Schulung. Der Teil, der in Technikprojekten regelmäßig unterschätzt wird.' },
      { badge: '5', title: 'Evidence Grading', text: 'Daten werden als „Verified" oder „Declared" klassifiziert, statt schwächere Daten abzulehnen. Wir übernehmen dieses Prinzip vollständig.' },
      { badge: '6', title: 'Tokenisierte Massenbilanz', text: 'Bei Transformation werden Input-Token gesperrt statt verbrannt, Output-Token neu geprägt. Erzwungen wird: Input ≥ Output + Verlust.' },
    ],
    takeaway: 'Angekündigt am 08.09.2026 — der Auslöser ist die EUDR-Frist zum 30.12.2026 und Bußgelder bis 4 % des Jahresumsatzes.',
    source: 'Quelle: Pressemitteilung The Hashgraph Group / Merck / PwC Germany, 08.09.2026 [recherchiert]',
    notes:
      'Das ist der Referenzfall. Im September 2026 haben die Hashgraph Group, das Wissenschafts- und Technologieunternehmen Merck und PwC Germany einen Piloten für Kakao-Rückverfolgbarkeit angekündigt. '
      + 'Sechs Bausteine, die Sie hier sehen.\n\n'
      + 'TrackTrace ist die Plattform: Sie legt für jede Charge einen digitalen Zwilling an und protokolliert Ereignisse an definierten Prüfpunkten. '
      + 'M-Trust von Merck ist der physische Teil — unsichtbare Pigmentmarker, die man mit einem Handgerät auslesen kann. '
      + 'Hedera ist die Ledger-Ebene, und hier ist ein Detail wichtig: Es werden nur Hashes verankert, keine Dokumente. '
      + 'Der Zweck ist der Nachweis der Zeitgleichheit — man kann Belege später nicht zurechtlegen. '
      + 'PwC bringt Prozesse und Governance ein.\n\n'
      + 'Zwei Bausteine haben uns fachlich besonders überzeugt. '
      + 'Das Evidence Grading: Daten werden nicht abgelehnt, wenn sie schwach sind, sondern gekennzeichnet — verifiziert oder erklärt. '
      + 'Und die tokenisierte Massenbilanz mit ihrer erzwungenen Ungleichung: Was hineingeht, muss mindestens dem entsprechen, was herauskommt, plus dem Verlust.\n\n'
      + 'Der Auslöser ist regulatorischer Druck: Ab dem 30. Dezember 2026 gilt die Entwaldungsverordnung, mit Bußgeldern bis vier Prozent des Jahresumsatzes. Dieser Druck trifft die Kaffeebranche in identischer Weise.',
  },
  {
    layout: 'stats',
    kicker: 'Das Fallunternehmen',
    title: 'Unsere Rösterei — konstruiert, aber realistisch',
    speaker: 1,
    stats: [
      { value: '> 1.000 t', label: 'Grünkaffee pro Jahr', sub: 'Damit kein KMU nach EU-Definition — die Frist ist der 30.12.2026, nicht Juni 2027' },
      { value: '> 50', label: 'Mitarbeitende', sub: 'Eigene IT-Landschaft mit ERP und Warenwirtschaft, aber keine Röstsoftware' },
      { value: 'Mischform', label: 'Beschaffung', sub: 'Teils Direct-Trade-Eigenimport, teils Zukauf über EU-Importeure — beide Wege parallel' },
    ],
    note: 'Alle drei Angaben sind gesetzte Annahmen, keine Erhebung. Sie sind so gewählt, dass der interessanteste Fall entsteht: ein Unternehmen, das gleichzeitig zwei regulatorische Rollen trägt und dem die kürzere der beiden Fristen zugewiesen ist.',
    takeaway: 'Genau diese Kombination erzeugt die zentrale Schwierigkeit des gesamten Projekts — dazu gleich mehr.',
    source: 'Rahmenbedingungen [angenommen] · Größenklassen und Fristen nach VO (EU) 2025/2650 [recherchiert]',
    notes:
      'Damit zu unserem Fallunternehmen. Wir betrachten eine Rösterei mit mehr als tausend Tonnen Grünkaffee im Jahr und über fünfzig Mitarbeitenden. '
      + 'Sie hat ein ERP und eine Warenwirtschaft, aber keine spezialisierte Röstsoftware. '
      + 'Und sie beschafft in Mischform: einen Teil importiert sie selbst im Direct Trade, einen anderen Teil kauft sie über europäische Grünkaffeehändler zu.\n\n'
      + 'Diese Angaben sind gesetzt, nicht erhoben — aber nicht beliebig, sondern so, dass der lehrreichste Fall entsteht.\n\n'
      + 'Warum? Zwei Konsequenzen ergeben sich unmittelbar. '
      + 'Erstens: Mit dieser Größe ist das Unternehmen nach EU-Definition kein Klein- oder Kleinstunternehmen. '
      + 'Damit gilt für sie die frühere der beiden Fristen — Ende Dezember 2026 statt Mitte 2027. '
      + 'Zweitens: Die Mischform bedeutet, dass die Rösterei regulatorisch nicht eine Rolle hat, sondern zwei. '
      + 'Für die selbst importierten Partien ist sie etwas völlig anderes als für die zugekauften. '
      + 'Mein Kollege wird das im nächsten Block im Detail auflösen.\n\n'
      + 'Halten Sie bitte im Kopf: Ende Dezember 2026, und zwei Rollen gleichzeitig.',
  },
  {
    layout: 'bullets',
    kicker: 'Der Kern unserer Analyse',
    title: 'Warum Kaffee nicht Kakao ist — Teil 1: der Prozess',
    speaker: 1,
    bullets: [
      ['Röstverlust von 15 bis 20 Prozent',
        'Beim Rösten verdampft Wasser, das Silberhäutchen löst sich. Aus 100 kg Grünkaffee werden rund 82 kg Röstkaffee. Kakao kennt diesen Masseverlust in dieser Größenordnung nicht — die Massenbilanz muss ihn abbilden.'],
      ['Der Verlustfaktor wird selbst zum Angriffspunkt',
        'Wer den Verlust hoch deklariert, kann Ware unbekannter Herkunft einschleusen, ohne dass die Bilanz auffällt. Bei tausend Tonnen entsprechen zwei Prozentpunkte rund zwanzig Tonnen im Jahr.'],
      ['Blends mischen mehrere Herkünfte, chargenweise nachjustiert',
        'Ein Hausblend enthält vier oder fünf Ursprünge in variablen Anteilen. Das ist eine n-zu-1-Transformation — und eine Falle für die Herkunftskommunikation.'],
    ],
    aside: {
      label: 'Die Formel, die daraus folgt',
      text: 'Σ Input\n=\nΣ Output\n+ Verlust\n+ Ausschuss\n+ Muster\n+ Toleranz',
      size: 19,
    },
    takeaway: 'Entscheidend ist: Der Verlust wird gemessen, nicht deklariert. Er ist die Restgröße aus Ein- und Auswaage — nie ein Eingabefeld.',
    source: 'Röstverlust 15–20 % [recherchiert, Branchenwissen] · Rechenbeispiel [geschätzt]',
    notes:
      'Jetzt zum inhaltlichen Kern meines Blocks: Warum kann man die Kakao-Lösung nicht einfach übertragen? '
      + 'Ich nenne Ihnen sechs Unterschiede, aufgeteilt auf zwei Folien. Zuerst drei, die den Produktionsprozess betreffen.\n\n'
      + 'Der erste ist der Röstverlust. Beim Rösten verliert Kaffee fünfzehn bis zwanzig Prozent seiner Masse — Wasser verdampft, das Silberhäutchen löst sich ab. '
      + 'Aus hundert Kilogramm Grünkaffee werden rund zweiundachtzig Kilogramm Röstkaffee. '
      + 'Eine Massenbilanz, die das nicht abbildet, schlägt bei jeder einzelnen Charge Alarm.\n\n'
      + 'Der zweite Punkt ist der eigentlich interessante, und er hat uns am längsten beschäftigt. '
      + 'Der Verlustfaktor ist nicht nur ein technischer Parameter — er ist ein Manipulationsvektor. '
      + 'Wer einen zu hohen Verlust deklariert, schafft in der Bilanz Platz für Ware, die nie ordnungsgemäß eingekauft wurde. '
      + 'Rechnen Sie mit: Bei tausend Tonnen im Jahr entsprechen zwei Prozentpunkte rund zwanzig Tonnen Grünkaffee, die verschwinden dürfen, ohne dass die Formel verletzt wird. '
      + 'Das ist keine theoretische Lücke.\n\n'
      + 'Unsere Antwort darauf steht rechts unten und ist bewusst unspektakulär: Der Verlust wird gemessen, nicht deklariert. '
      + 'Ein- und Auswaage kommen von der Waage, der Verlust ist die Restgröße. '
      + 'Ein Eingabefeld für den Verlustfaktor gibt es in unserem Entwurf schlicht nicht. Mein Kollege im vierten Block vertieft das.\n\n'
      + 'Der dritte Unterschied sind Blends. Ein Hausblend mischt vier oder fünf Herkünfte, und die Anteile werden chargenweise nachjustiert — je nach Ernte, Verfügbarkeit und Verkostung. '
      + 'Das ist technisch eine n-zu-1-Transformation, und kommunikativ eine Falle, auf die ich gleich noch zurückkomme.',
  },
  {
    layout: 'bullets',
    kicker: 'Der Kern unserer Analyse',
    title: 'Warum Kaffee nicht Kakao ist — Teil 2: Kette und Recht',
    speaker: 1,
    bullets: [
      ['Die Kette ist tief, und die Rösterei kauft nie am Feld',
        'Kleinbauer, Kooperative, Trockenmühle, Exporteur, Importeur, erst dann die Rösterei. Wer erfasst die Geokoordinaten? Nicht wir — die Kooperative. Das verschiebt den Vertrauensanker.'],
      ['Zwei regulatorische Rollen gleichzeitig',
        'Durch die Mischform ist die Rösterei bei einem Lot voller Betreiber mit Sorgfaltspflicht und bei dem Lot daneben nur nachgelagerter Akteur. Entschieden wird je Lot, nicht je Unternehmen.'],
      ['Parzellen-Koordinaten sind personenbeziehbare Daten',
        'Eine Parzelle hat einen Bewirtschafter. Damit greift die DSGVO — und ihr Löschrecht kollidiert frontal mit der Unveränderlichkeit eines Ledgers.'],
    ],
    aside: {
      label: 'Und der Marker?',
      text: 'Merck markiert Verpackungen.\n\nGrünkaffee steckt in Jutesäcken, die umgepackt werden.\n\nWir streichen den Marker — mit Begründung.',
      size: 15,
    },
    takeaway: 'Drei von sechs Unterschieden betreffen nicht die Technik, sondern Recht, Vertrauen und Datenschutz. Genau dort scheitern solche Projekte.',
    source: 'DSGVO-Einordnung [angenommen, vorsichtige Auslegung] · Rollenlogik nach VO (EU) 2025/2650 [recherchiert]',
    notes:
      'Die zweite Hälfte der Unterschiede betrifft nicht den Prozess, sondern die Kette und das Recht.\n\n'
      + 'Vierter Unterschied: die Tiefe der Lieferkette. Zwischen dem Kaffeebauern und uns stehen mindestens eine Kooperative, eine Trockenmühle, ein Exporteur und häufig ein Importeur. '
      + 'Die Rösterei kauft praktisch nie am Feld. '
      + 'Das hat eine unbequeme Konsequenz für die Geodaten, die die Verordnung verlangt: Wir erfassen sie nicht. Die Kooperative erfasst sie. '
      + 'Damit verschiebt sich der Vertrauensanker von uns weg — und keine Technologie holt ihn zurück.\n\n'
      + 'Fünfter Unterschied: die Rollenfrage. Ich hatte es angedeutet — durch die Mischform ist unser Unternehmen bei der einen Partie voll sorgfaltspflichtig und bei der Partie daneben fast pflichtfrei. '
      + 'Und zwar gleichzeitig, im selben Lager. Das muss ein System abbilden können.\n\n'
      + 'Sechster Unterschied, und der ist juristisch heikel: GPS-Koordinaten von Kleinbauernparzellen sind personenbeziehbare Daten. '
      + 'Eine Parzelle hat einen Bewirtschafter, und bei einer Kooperative mit Mitgliederregister ist die Zuordnung trivial. '
      + 'Damit greift die Datenschutzgrundverordnung — und deren Löschrecht steht in direktem Widerspruch zur Unveränderlichkeit einer Blockchain. '
      + 'Diesen Konflikt löst der Referenzfall nicht sichtbar auf. Wir tun es im dritten Block.\n\n'
      + 'Rechts noch ein siebter Punkt: Mercks Marker sitzt auf Verpackungen — Grünkaffee reist in Jutesäcken, die umgepackt werden. Wir streichen diesen Baustein; mein Kollege begründet das im vierten Block.',
  },
  {
    layout: 'flow',
    kicker: 'Methodik',
    title: 'Wie wir vorgegangen sind',
    speaker: 1,
    steps: [
      { title: '1 · Prämissen prüfen', text: 'Zuerst die Aufgabenstellung selbst hinterfragt: Gilt jede geforderte Pflicht überhaupt?' },
      { title: '2 · Primärquellen', text: 'EUR-Lex und Kommissionsdokumente vor Kanzlei- und Branchentexten. Rechercheschluss 09.09.2026.', emph: true },
      { title: '3 · Entwerfen', text: 'Datenmodell, Architekturoptionen und Massenbilanz aus den geprüften Anforderungen abgeleitet.' },
      { title: '4 · Gegenthese', text: 'Die eigene Lösung bewusst angegriffen: Geht es auch ohne Blockchain? Was streichen wir?' },
    ],
    takeaway: 'Die Prämissenprüfung stand bewusst vor dem Entwurf — sonst hätten wir eine Pflicht erfüllt, die es nicht gibt.',
    notes:
      'Bevor ich an meinen Kollegen übergebe, kurz zur Methodik. Das ist kein Pflichtabschnitt, sondern erklärt, warum wir an manchen Stellen von der Aufgabenstellung abweichen.\n\n'
      + 'Wir sind in vier Schritten vorgegangen. Der erste war, die Aufgabenstellung selbst zu prüfen. '
      + 'Wir haben nicht gefragt „wie erfüllen wir diese Anforderung", sondern zuerst „gilt diese Anforderung überhaupt". '
      + 'Diese Reihenfolge hat sich ausgezahlt — Sie werden im zweiten Block sehen, warum.\n\n'
      + 'Zweiter Schritt: Recherche. Wir haben grundsätzlich Primärquellen genutzt, also die Verordnungstexte auf EUR-Lex und die Dokumente der Europäischen Kommission, und erst danach Sekundärquellen wie Kanzleianalysen und Branchenpresse. '
      + 'Unser Rechercheschluss ist der 9. September 2026.\n\n'
      + 'Warum diese Sorgfalt? Weil die EU-Entwaldungsverordnung innerhalb von zwei Jahren zweimal verschoben und mehrfach inhaltlich geändert wurde. '
      + 'Wer hier mit Wissen von vor einem Jahr arbeitet, arbeitet mit falschem Recht. '
      + 'Wir haben deshalb auch keinem Lehrbuchstand vertraut, sondern jede Frist und jede Pflicht am aktuellen Verordnungstext geprüft.\n\n'
      + 'Dritter Schritt war der eigentliche Entwurf — Datenmodell, Architektur, Massenbilanz.\n\n'
      + 'Und der vierte Schritt war, unseren eigenen Entwurf anzugreifen. Wir haben bewusst die Gegenthese formuliert: Braucht es für diese Aufgabe überhaupt eine Blockchain? '
      + 'Und wir haben systematisch gefragt, welche Bausteine des Referenzfalls wir streichen können. '
      + 'Ein kürzerer, ehrlicher Plan ist uns lieber als ein vollständiger, der Aufwand rechtfertigt.',
  },
  {
    layout: 'cards',
    kicker: 'Methodik',
    title: 'Jede Aussage trägt ihre Belastbarkeit im Text',
    speaker: 1,
    cols: 3,
    cards: [
      { badge: 'R', title: 'recherchiert', tone: 'good', text: 'Belegt durch eine benannte Quelle mit Link. Gilt für alle Fristen, Rechtsnormen, Marktpreise und Studienwerte. Nachprüfbar, ohne uns fragen zu müssen.' },
      { badge: 'A', title: 'angenommen', text: 'Bewusst gesetzt, weil die Information fehlt — etwa die Kennzahlen unseres Fallunternehmens oder eine juristische Auslegung, die noch aussteht.' },
      { badge: 'G', title: 'geschätzt', text: 'Von uns gerechnet oder hergeleitet, ohne belastbare Quelle. Vor allem Kosten und Mengengerüste. Immer als Bandbreite, nie als Punktwert.' },
    ],
    takeaway: 'Der Sinn dahinter: Wer unsere Empfehlung prüft, soll sofort sehen, worauf sie ruht — und wo sie am dünnsten ist.',
    notes:
      'Ein zweites methodisches Prinzip, das sich durch alle unsere Unterlagen zieht: Wir kennzeichnen jede Aussage danach, wie belastbar sie ist. Drei Stufen.\n\n'
      + 'Recherchiert heißt: Es gibt eine benannte Quelle mit Link. Das betrifft alle Fristen, alle Rechtsnormen, Marktpreise und Werte aus Studien. '
      + 'Sie können das nachprüfen, ohne uns zu fragen.\n\n'
      + 'Angenommen heißt: Wir haben etwas gesetzt, weil die Information nicht vorlag. '
      + 'Dazu gehören die Kennzahlen unseres Fallunternehmens, aber auch juristische Auslegungen, die noch nicht geklärt sind.\n\n'
      + 'Geschätzt heißt: Wir haben gerechnet oder hergeleitet, ohne belastbare Quelle. '
      + 'Das betrifft vor allem Kosten und Mengengerüste — und dort geben wir grundsätzlich Bandbreiten an, keine Punktwerte. '
      + 'Eine Kostenschätzung mit einer Nachkommastelle wäre eine Behauptung, keine Schätzung.\n\n'
      + 'Der Zweck: Wer unsere Empfehlung bewerten will, soll sehen, worauf sie ruht — und wo sie am dünnsten ist.\n\n'
      + 'Damit übergebe ich an meine Kollegin beziehungsweise meinen Kollegen für die Regulatorik. Und ich kündige an: Dort wartet der Befund, der unser Projekt am stärksten verändert hat.',
  },
];

module.exports = { TITEL_UND_AGENDA, BLOCK_A };
