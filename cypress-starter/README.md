# Cypress-Startgerüst

Fertiges Projekt mit drei Tests gegen die Übungsseite `the-internet.herokuapp.com/login`.
Gedacht für den Cypress-Block der Interviewvorbereitung – damit die Zeit in die Tests geht
und nicht in die Einrichtung.

## Starten

```bash
cd cypress-starter
npm install          # lädt Cypress inkl. Binary (~1-2 Min.)
npm run cy:open      # öffnet die Oberfläche: E2E Testing -> Browser -> login.cy.js
```

Alternativ ohne Fenster: `npm run cy:run`

Voraussetzung: Node.js ab Version 18.

## Was drin ist

`cypress/e2e/login.cy.js` – drei Testfälle:

| Test | Prüft |
|---|---|
| gültige Zugangsdaten | Weiterleitung nach `/secure` + Erfolgsmeldung |
| falsches Passwort | bleibt auf `/login` + Fehlermeldung |
| leeres Formular | Fehlermeldung – der Edge Case, den Anforderungen oft offenlassen |

## Womit du im Gespräch arbeiten kannst

- **Aufbau eines Tests:** `cy.visit` (Vorbedingung) → `cy.get().type()/.click()` (Schritte) →
  `.should()` (erwartetes Ergebnis). Das ist derselbe Dreischritt wie in deinen manuellen
  Testfällen – nur ausführbar.
- **Selektoren:** hier `#username` per ID. In echten Projekten nimmt man eigene Attribute wie
  `data-cy="username"`, weil IDs und CSS-Klassen sich beim Refactoring ändern und Tests dann
  ohne echten Fehler rot werden.
- **Warum drei statt einem Test:** ein Positivfall, ein Negativfall, ein Randfall. Genau die
  Aufteilung, die du aus der manuellen Arbeit kennst.
- **Was man automatisiert:** stabile, wiederkehrende Abläufe wie diesen Login – als
  Regressionstest bei jedem Release. Explorative Prüfungen und selten geänderte Bereiche
  bleiben manuell.

## Nächster Schritt, falls Zeit bleibt

Einen vierten Test ergänzen: nach dem Login auf „Logout“ klicken und prüfen, dass wieder
`/login` erscheint.
