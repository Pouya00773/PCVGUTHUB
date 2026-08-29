// Login der Übungsseite the-internet.herokuapp.com/login
// Gültige Zugangsdaten der Seite: tomsmith / SuperSecretPassword!
//
// Aufbau wie ein Testfall im Testplan:
// Vorbedingung -> Schritte -> erwartetes Ergebnis

describe("Login", () => {
  beforeEach(() => {
    cy.visit("/login");
  });

  it("meldet sich mit gültigen Zugangsdaten an", () => {
    cy.get("#username").type("tomsmith");
    cy.get("#password").type("SuperSecretPassword!");
    cy.get("button[type=submit]").click();

    cy.url().should("include", "/secure");
    cy.get("#flash").should("contain", "You logged into a secure area");
  });

  it("weist ein falsches Passwort ab", () => {
    cy.get("#username").type("tomsmith");
    cy.get("#password").type("falschesPasswort");
    cy.get("button[type=submit]").click();

    cy.url().should("include", "/login");
    cy.get("#flash").should("contain", "Your password is invalid");
  });

  // Edge Case: leeres Formular - der Fall, den eine Anforderung oft nicht beschreibt
  it("weist ein leeres Formular ab", () => {
    cy.get("button[type=submit]").click();

    cy.get("#flash").should("contain", "Your username is invalid");
  });
});
