#!/usr/bin/env node
/**
 * Erzeugt output/Kaffee_Traceability_EUDR.pptx
 *
 *   node scripts/build_kaffee_praesentation.js
 *
 * Aufbau: Design-System in pptx_theme.js, Inhalte in inhalt_teil1..4.js.
 * Wer Texte ändern will, fasst nur die Inhaltsdateien an.
 *
 * Am Ende gibt das Skript eine Zeitprobe aus: Wortzahl der Sprechernotizen
 * je Block, geteilt durch 120 Wörter pro Minute.
 */

const path = require('path');
const PptxGenJS = require('pptxgenjs');
const { LAYOUTS } = require('./pptx_theme');

const { TITEL_UND_AGENDA, BLOCK_A } = require('./inhalt_teil1');
const { BLOCK_B } = require('./inhalt_teil2');
const { BLOCK_C, BLOCK_D } = require('./inhalt_teil3');
const { BLOCK_E, BACKUP } = require('./inhalt_teil4');

const OUT = path.join(__dirname, '..', 'output', 'Kaffee_Traceability_EUDR.pptx');
const WPM = 120; // Sprechgeschwindigkeit für die Zeitprobe

const SLIDES = [
  ...TITEL_UND_AGENDA,
  ...BLOCK_A,
  ...BLOCK_B,
  ...BLOCK_C,
  ...BLOCK_D,
  ...BLOCK_E,
  ...BACKUP,
];

function countWords(s) {
  return (s || '').trim().split(/\s+/).filter(Boolean).length;
}

function build() {
  const pres = new PptxGenJS();
  pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5 — muss vor addSlide gesetzt sein
  pres.author = 'Projektgruppe';
  pres.title = 'Rückverfolgbarer Kaffee: EUDR, Herkunftsnachweis und CO₂ je Charge';
  pres.subject = 'Umsetzungsplan für eine Kaffeerösterei';

  SLIDES.forEach((d, i) => {
    const render = LAYOUTS[d.layout];
    if (!render) throw new Error(`Unbekanntes Layout "${d.layout}" auf Folie ${i + 1}`);
    const slide = pres.addSlide();
    render(slide, d);
    if (d.notes) slide.addNotes(d.notes);
  });

  return pres.writeFile({ fileName: OUT });
}

function report() {
  const blocks = [
    ['Titel + Agenda', TITEL_UND_AGENDA],
    ['A — Ausgangslage (Sprecher:in 1)', BLOCK_A],
    ['B — Regulatorik (Sprecher:in 2)', BLOCK_B],
    ['C — Kette und Daten (Sprecher:in 3)', BLOCK_C],
    ['D — Architektur (Sprecher:in 4)', BLOCK_D],
    ['E — Umsetzung (Sprecher:in 5)', BLOCK_E],
  ];

  console.log(`\nFolien gesamt: ${SLIDES.length}  (davon Backup: ${BACKUP.length})\n`);
  console.log('Zeitprobe der Sprechernotizen:');
  let total = 0;
  blocks.forEach(([name, arr]) => {
    const w = arr.reduce((s, d) => s + countWords(d.notes), 0);
    total += w;
    console.log(`  ${name.padEnd(36)} ${String(w).padStart(5)} Wörter  ≈ ${(w / WPM).toFixed(1)} Min.`);
  });
  console.log(`  ${'VORTRAG GESAMT'.padEnd(36)} ${String(total).padStart(5)} Wörter  ≈ ${(total / WPM).toFixed(1)} Min.`);

  // Folien ohne bzw. mit zu kurzen Notizen melden
  const thin = SLIDES
    .map((d, i) => ({ nr: i + 1, layout: d.layout, w: countWords(d.notes) }))
    .filter((s) => s.w < 80 && s.layout !== 'table' && s.layout !== 'divider');
  if (thin.length) {
    console.log('\nFolien mit weniger als 80 Wörtern Sprechtext:');
    thin.forEach((s) => console.log(`  Folie ${s.nr} (${s.layout}): ${s.w} Wörter`));
  } else {
    console.log('\nAlle Inhaltsfolien haben mindestens 80 Wörter Sprechtext.');
  }
  console.log('');
}

build()
  .then((f) => {
    console.log(`Geschrieben: ${f}`);
    report();
  })
  .catch((e) => {
    console.error('Fehler beim Erzeugen:', e);
    process.exit(1);
  });
