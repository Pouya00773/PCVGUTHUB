/**
 * Design-System für die Kaffee-Traceability-Präsentation.
 *
 * Enthält Palette, Typografie, Maße und alle Layout-Bausteine.
 * Inhalte stehen in inhalt_teil1..4.js — hier steht nur, wie es aussieht.
 *
 * Wichtig (pptxgenjs-Eigenheiten):
 *  - Farben ohne '#', niemals 8-stellig.
 *  - Optionsobjekte werden von pptxgenjs in-place mutiert. Deshalb liefert
 *    jede Helferfunktion ein FRISCHES Objekt statt einer geteilten Konstante.
 *  - Jeder addText-Aufruf braucht isTextBox: true.
 *
 * Jede Textbox wird über fitFont() dimensioniert. Die Schätzformel ist
 * absichtlich identisch mit der in scripts/pptx_qa.py, damit Generator und
 * Prüfung nicht auseinanderlaufen.
 */

// ---------------------------------------------------------------------------
// Palette — themenbezogen: Wald (Entwaldung) dominant, Bohnen-Amber als Akzent
// ---------------------------------------------------------------------------
const C = {
  FOREST: '1B3A2F',
  FOREST_2: '24503F',
  MOSS: '97BC62',
  AMBER: 'C9762F',
  AMBER_L: 'F2E3D0',
  CREAM: 'F7F6F2',
  WHITE: 'FFFFFF',
  INK: '17241F',
  MUTED: '6B7A72',
  LINE: 'DDE3DE',
  RED: 'A6352B',
  RED_L: 'F6E4E2',
  MOSS_TXT: 'CBDCC9',
};

// Schriften von der Safe-List: rendern maßstabsgetreu in der Prüfung
const F = { HEAD: 'Cambria', BODY: 'Calibri' };

// Maße (Zoll) — LAYOUT_WIDE = 13.33 x 7.5
const M = {
  W: 13.333,
  H: 7.5,
  PAD: 0.7,
  get CW() { return this.W - 2 * this.PAD; },   // 11.93
  TITLE_Y: 0.50,
  TITLE_H: 1.16,
  BODY_Y: 1.82,
  FOOT_Y: 6.94,
  TAKE_Y: 6.16,        // Oberkante der Kernaussage-Leiste
  TAKE_H: 0.56,
};

const shadowSoft = () => ({
  type: 'outer', color: '000000', blur: 10, offset: 2, angle: 90, opacity: 0.10,
});

// ---------------------------------------------------------------------------
// Auto-Fit
// ---------------------------------------------------------------------------
const CHAR_W = 0.53;   // mittlere Zeichenbreite als Anteil der Schriftgröße
const CHAR_W_BOLD = 0.58;  // fetter Text läuft breiter
const LINE_H = 1.22;   // Zeilenhöhe als Faktor der Schriftgröße

function neededHeight(text, widthIn, pt, bold = false) {
  if (!text) return 0;
  const charWIn = (pt * (bold ? CHAR_W_BOLD : CHAR_W)) / 72;
  const perLine = Math.max(1, Math.floor(widthIn / charWIn));
  let lines = 0;
  for (const para of String(text).split('\n')) {
    lines += Math.max(1, Math.ceil(para.length / perLine));
  }
  return (lines * pt * LINE_H) / 72;
}

/** Größte Schriftgröße zwischen minPt und startPt, bei der der Text passt. */
function fitFont(text, widthIn, heightIn, startPt, minPt = 9.5, bold = false) {
  let pt = startPt;
  while (pt > minPt && neededHeight(text, widthIn - 0.06, pt, bold) > heightIn) pt -= 0.5;
  return pt;
}

/** Textbox mit automatisch angepasster Schriftgröße. */
function fitText(slide, text, box, opts = {}) {
  const { x, y, w, h } = box;
  const start = opts.fontSize || 13;
  const bold = !!opts.bold;
  const size = fitFont(text, w, h, start, opts.minSize || 9.5, bold);
  slide.addText(text, {
    x, y, w, h,
    fontFace: opts.fontFace || F.BODY,
    fontSize: size,
    bold: !!opts.bold,
    italic: !!opts.italic,
    color: opts.color || C.INK,
    align: opts.align || 'left',
    valign: opts.valign || 'top',
    charSpacing: opts.charSpacing,
    lineSpacingMultiple: opts.lineSpacingMultiple || 1.06,
    isTextBox: true,
    margin: 0,
  });
  // Tatsächlich benötigte Höhe — Aufrufer positionieren Folgeelemente darunter,
  // damit ein zweizeiliger Umbruch nichts überdeckt.
  return { size, height: Math.min(h, neededHeight(text, w - 0.06, size, bold)) };
}

// ---------------------------------------------------------------------------
// Grundgerüst
// ---------------------------------------------------------------------------
const lightBg = (slide) => { slide.background = { color: C.CREAM }; };
const darkBg = (slide) => { slide.background = { color: C.FOREST }; };

/**
 * Kopfzeile einer Inhaltsfolie: kleine Rubrik, darunter der Titel.
 * Bewusst OHNE Farbbalken und ohne Linie unter dem Titel — beides liest sich
 * als generische Vorlage. Getrennt wird über Weißraum.
 */
function slideHead(slide, { kicker, title }) {
  const tw = M.CW - 1.4;
  if (kicker) {
    slide.addText(kicker.toUpperCase(), {
      x: M.PAD, y: M.TITLE_Y - 0.30, w: M.CW, h: 0.26,
      fontFace: F.BODY, fontSize: 11, bold: true, charSpacing: 1.6,
      color: C.AMBER, isTextBox: true, margin: 0,
    });
  }
  fitText(slide, title, { x: M.PAD, y: M.TITLE_Y, w: tw, h: M.TITLE_H }, {
    fontFace: F.HEAD, fontSize: 30, minSize: 21, bold: true,
    color: C.FOREST, lineSpacingMultiple: 1.0,
  });
}

function sourceNote(slide, text) {
  fitText(slide, text, { x: M.PAD, y: M.FOOT_Y, w: M.CW, h: 0.3 }, {
    fontSize: 9, minSize: 7.5, italic: true, color: C.MUTED,
  });
}

function speakerBadge(slide, n) {
  if (!n) return;
  slide.addShape('ellipse', {
    x: M.W - M.PAD - 0.34, y: M.TITLE_Y - 0.02, w: 0.34, h: 0.34,
    fill: { color: C.MOSS }, line: { color: C.MOSS },
  });
  slide.addText(String(n), {
    x: M.W - M.PAD - 0.34, y: M.TITLE_Y - 0.02, w: 0.34, h: 0.34,
    fontFace: F.BODY, fontSize: 13, bold: true, color: C.FOREST,
    align: 'center', valign: 'middle', isTextBox: true, margin: 0,
  });
}

/** Kernaussage am unteren Rand des Inhaltsbereichs, auf Amber-Tint. */
function keyTakeaway(slide, text) {
  slide.addShape('roundRect', {
    x: M.PAD, y: M.TAKE_Y, w: M.CW, h: M.TAKE_H, rectRadius: 0.06,
    fill: { color: C.AMBER_L }, line: { color: C.AMBER_L },
  });
  fitText(slide, text, {
    x: M.PAD + 0.24, y: M.TAKE_Y + 0.05, w: M.CW - 0.48, h: M.TAKE_H - 0.10,
  }, { fontSize: 13, minSize: 10, bold: true, color: C.FOREST, valign: 'middle' });
}

function numCircle(slide, { x, y, d = 0.5, label, fill = C.FOREST, color = C.WHITE, size = 16 }) {
  slide.addShape('ellipse', { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
  slide.addText(String(label), {
    x, y, w: d, h: d,
    fontFace: F.BODY, fontSize: size, bold: true, color,
    align: 'center', valign: 'middle', isTextBox: true, margin: 0,
  });
}

function card(slide, { x, y, w, h, fill = C.WHITE, radius = 0.08, shadow = true, line = C.LINE }) {
  slide.addShape('roundRect', {
    x, y, w, h, rectRadius: radius,
    fill: { color: fill }, line: { color: line, width: 0.75 },
    ...(shadow ? { shadow: shadowSoft() } : {}),
  });
}

/** Unterkante des Inhaltsbereichs — abhängig davon, ob eine Kernaussage folgt. */
const bodyBottom = (d) => (d.takeaway ? M.TAKE_Y - 0.14 : M.FOOT_Y - 0.10);

// ---------------------------------------------------------------------------
// Layouts
// ---------------------------------------------------------------------------

function layoutTitle(slide, d) {
  darkBg(slide);
  slide.addShape('ellipse', {
    x: 9.6, y: -1.5, w: 5.6, h: 5.6, fill: { color: C.FOREST_2 }, line: { color: C.FOREST_2 },
  });
  slide.addShape('ellipse', {
    x: 11.1, y: 4.4, w: 3.4, h: 3.4, fill: { color: C.FOREST_2 }, line: { color: C.FOREST_2 },
  });
  slide.addText(d.eyebrow.toUpperCase(), {
    x: M.PAD, y: 1.62, w: 9.0, h: 0.3,
    fontFace: F.BODY, fontSize: 12, bold: true, charSpacing: 2,
    color: C.MOSS, isTextBox: true, margin: 0,
  });
  fitText(slide, d.title, { x: M.PAD, y: 2.06, w: 9.1, h: 2.10 }, {
    fontFace: F.HEAD, fontSize: 38, minSize: 28, bold: true,
    color: C.WHITE, lineSpacingMultiple: 1.04,
  });
  fitText(slide, d.subtitle, { x: M.PAD, y: 4.34, w: 8.7, h: 0.92 }, {
    fontSize: 15, minSize: 12, color: C.MOSS, lineSpacingMultiple: 1.14,
  });
  fitText(slide, d.meta, { x: M.PAD, y: 6.42, w: 9.2, h: 0.4 }, {
    fontSize: 11.5, minSize: 10, color: 'A9BFAE',
  });
}

function layoutDivider(slide, d) {
  darkBg(slide);
  slide.addShape('ellipse', {
    x: 10.3, y: 1.05, w: 5.4, h: 5.4, fill: { color: C.FOREST_2 }, line: { color: C.FOREST_2 },
  });
  numCircle(slide, { x: M.PAD, y: 2.56, d: 0.92, label: d.num, fill: C.AMBER, size: 30 });
  fitText(slide, d.title, { x: M.PAD, y: 3.72, w: 9.0, h: 1.0 }, {
    fontFace: F.HEAD, fontSize: 34, minSize: 26, bold: true, color: C.WHITE,
  });
  fitText(slide, d.subtitle, { x: M.PAD, y: 4.80, w: 8.7, h: 0.86 }, {
    fontSize: 15, minSize: 12, color: C.MOSS, lineSpacingMultiple: 1.14,
  });
  const foot = d.minutes
    ? `Sprecher:in ${d.speaker}  ·  ca. ${d.minutes} Minuten`
    : `Sprecher:in ${d.speaker}`;
  slide.addText(foot, {
    x: M.PAD, y: 6.30, w: 8.0, h: 0.34,
    fontFace: F.BODY, fontSize: 12, bold: true, color: C.AMBER,
    isTextBox: true, margin: 0,
  });
}

function layoutAgenda(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  const n = d.items.length, gap = 0.16;
  const avail = M.FOOT_Y - 0.10 - M.BODY_Y;
  const rowH = (avail - gap * (n - 1)) / n;
  let y = M.BODY_Y;
  d.items.forEach((it, i) => {
    card(slide, { x: M.PAD, y, w: M.CW, h: rowH });
    numCircle(slide, {
      x: M.PAD + 0.28, y: y + (rowH - 0.46) / 2, d: 0.46, label: i + 1, size: 15,
    });
    fitText(slide, it.title, { x: M.PAD + 0.95, y: y + 0.14, w: 6.6, h: 0.34 }, {
      fontFace: F.HEAD, fontSize: 16, minSize: 13, bold: true, color: C.FOREST,
    });
    fitText(slide, it.desc, { x: M.PAD + 0.95, y: y + 0.50, w: 7.5, h: 0.30 }, {
      fontSize: 11.5, minSize: 9.5, color: C.MUTED,
    });
    slide.addText(`Sprecher:in ${it.speaker}`, {
      x: M.W - M.PAD - 2.4, y: y + 0.16, w: 2.1, h: 0.28,
      fontFace: F.BODY, fontSize: 11.5, bold: true, color: C.AMBER,
      align: 'right', isTextBox: true, margin: 0,
    });
    slide.addText(it.minutes, {
      x: M.W - M.PAD - 2.4, y: y + 0.48, w: 2.1, h: 0.28,
      fontFace: F.BODY, fontSize: 11, color: C.MUTED,
      align: 'right', isTextBox: true, margin: 0,
    });
    y += rowH + gap;
  });
}

function layoutBullets(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const hasAside = !!d.aside;
  const listW = hasAside ? 7.5 : M.CW;
  const bottom = bodyBottom(d);
  const avail = bottom - M.BODY_Y;
  const slotH = avail / d.bullets.length;

  let y = M.BODY_Y;
  d.bullets.forEach((b) => {
    const [head, sub] = Array.isArray(b) ? b : [b, null];
    slide.addShape('ellipse', {
      x: M.PAD + 0.02, y: y + 0.12, w: 0.15, h: 0.15,
      fill: { color: C.AMBER }, line: { color: C.AMBER },
    });
    const headBox = sub ? Math.min(0.62, slotH * 0.44) : slotH - 0.10;
    const h1 = fitText(slide, head, { x: M.PAD + 0.36, y, w: listW - 0.36, h: headBox }, {
      fontSize: 15, minSize: 11.5, bold: true, color: C.INK, lineSpacingMultiple: 1.02,
    });
    if (sub) {
      const subY = y + h1.height + 0.06;
      const subH = y + slotH - 0.12 - subY;
      fitText(slide, sub, { x: M.PAD + 0.36, y: subY, w: listW - 0.36, h: subH }, {
        fontSize: 12.5, minSize: 9, color: C.MUTED,
      });
    }
    y += slotH;
  });

  if (hasAside) {
    const ax = M.PAD + 7.9, aw = M.CW - 7.9;
    const ah = Math.min(4.0, avail);
    card(slide, { x: ax, y: M.BODY_Y, w: aw, h: ah, fill: C.FOREST, line: C.FOREST });
    slide.addText(d.aside.label.toUpperCase(), {
      x: ax + 0.32, y: M.BODY_Y + 0.30, w: aw - 0.64, h: 0.28,
      fontFace: F.BODY, fontSize: 10.5, bold: true, charSpacing: 1.4,
      color: C.MOSS, isTextBox: true, margin: 0,
    });
    fitText(slide, d.aside.text, {
      x: ax + 0.32, y: M.BODY_Y + 0.68, w: aw - 0.64, h: ah - 0.96,
    }, {
      fontFace: F.HEAD, fontSize: d.aside.size || 17, minSize: 11,
      bold: true, color: C.WHITE, lineSpacingMultiple: 1.12,
    });
  }
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutCards(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const cols = d.cols || 3;
  const rows = Math.ceil(d.cards.length / cols);
  const gx = 0.26, gy = 0.24;
  const cw = (M.CW - gx * (cols - 1)) / cols;
  const availH = bodyBottom(d) - M.BODY_Y;
  const ch = (availH - gy * (rows - 1)) / rows;

  // Innenaufbau der Karte
  const bd = 0.38;                 // Durchmesser Nummernkreis
  const padIn = 0.26;
  const titleY = 0.62;
  const titleH = Math.min(0.50, ch * 0.26);

  // Eine gemeinsame Schriftgröße für alle Karten der Folie — unterschiedlich
  // große Kartentexte wirken unruhig.
  const innerW = cw - 2 * padIn;
  const titleSize = Math.min(...d.cards.map(
    (c) => fitFont(c.title, innerW, titleH, 15, 11.5, true)));
  const bodyRoom = ch - (titleY + titleH + 0.08) - 0.14;
  const textSize = Math.min(...d.cards.map(
    (c) => fitFont(c.text, innerW, bodyRoom, 12, 9)));

  d.cards.forEach((c, i) => {
    const cx = M.PAD + (i % cols) * (cw + gx);
    const cy = M.BODY_Y + Math.floor(i / cols) * (ch + gy);
    const accent = c.tone === 'bad' ? C.RED : c.tone === 'good' ? C.MOSS : C.FOREST;
    card(slide, { x: cx, y: cy, w: cw, h: ch });
    numCircle(slide, {
      x: cx + padIn, y: cy + 0.18, d: bd, label: c.badge || i + 1,
      fill: accent, color: c.tone === 'good' ? C.FOREST : C.WHITE, size: 13,
    });
    slide.addText(c.title, {
      x: cx + padIn, y: cy + titleY, w: innerW, h: titleH,
      fontFace: F.HEAD, fontSize: titleSize, bold: true, color: C.FOREST,
      valign: 'top', lineSpacingMultiple: 1.0, isTextBox: true, margin: 0,
    });
    const tH = Math.max(neededHeight(c.title, innerW - 0.06, titleSize, true), 0.26);
    const tY = cy + titleY + tH + 0.08;
    slide.addText(c.text, {
      x: cx + padIn, y: tY, w: innerW, h: cy + ch - 0.14 - tY,
      fontFace: F.BODY, fontSize: textSize, color: C.MUTED,
      valign: 'top', lineSpacingMultiple: 1.06, isTextBox: true, margin: 0,
    });
  });
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutCompare(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const n = d.columns.length, gx = 0.28;
  const cw = (M.CW - gx * (n - 1)) / n;
  const ch = bodyBottom(d) - M.BODY_Y;
  const headH = 0.88;

  d.columns.forEach((col, i) => {
    const cx = M.PAD + i * (cw + gx);
    const hi = !!col.highlight;
    card(slide, {
      x: cx, y: M.BODY_Y, w: cw, h: ch,
      line: hi ? C.AMBER : C.LINE, shadow: hi,
    });
    slide.addShape('roundRect', {
      x: cx, y: M.BODY_Y, w: cw, h: headH, rectRadius: 0.08,
      fill: { color: hi ? C.FOREST : C.LINE }, line: { color: hi ? C.FOREST : C.LINE },
    });
    fitText(slide, col.head, { x: cx + 0.22, y: M.BODY_Y + 0.10, w: cw - 0.44, h: 0.34 }, {
      fontFace: F.HEAD, fontSize: 15, minSize: 11.5, bold: true,
      color: hi ? C.WHITE : C.FOREST,
    });
    fitText(slide, col.sub, { x: cx + 0.22, y: M.BODY_Y + 0.46, w: cw - 0.44, h: 0.34 }, {
      fontSize: 11, minSize: 9, color: hi ? C.MOSS : C.MUTED,
    });

    const rows = col.rows.filter((r) => r !== '');
    const listTop = M.BODY_Y + headH + 0.16;
    const listH = ch - headH - 0.30;
    const slot = listH / rows.length;
    let y = listTop;
    rows.forEach((r) => {
      const isVerdict = r.startsWith('=');
      const txt = isVerdict ? r.slice(1).trim() : r;
      fitText(slide, txt, { x: cx + 0.22, y, w: cw - 0.44, h: slot - 0.06 }, {
        fontSize: isVerdict ? 12.5 : 12, minSize: 9,
        bold: isVerdict, color: isVerdict ? C.FOREST : C.MUTED,
      });
      y += slot;
    });
  });
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutStats(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const n = d.stats.length, gx = 0.28;
  const cw = (M.CW - gx * (n - 1)) / n;
  const ch = 2.42;
  d.stats.forEach((s, i) => {
    const cx = M.PAD + i * (cw + gx);
    card(slide, { x: cx, y: M.BODY_Y, w: cw, h: ch });
    fitText(slide, s.value, { x: cx + 0.16, y: M.BODY_Y + 0.26, w: cw - 0.32, h: 0.92 }, {
      fontFace: F.HEAD, fontSize: s.size || 38, minSize: 20, bold: true,
      color: C.AMBER, align: 'center', valign: 'middle',
    });
    fitText(slide, s.label, { x: cx + 0.16, y: M.BODY_Y + 1.24, w: cw - 0.32, h: 0.36 }, {
      fontFace: F.HEAD, fontSize: 14, minSize: 11, bold: true,
      color: C.FOREST, align: 'center',
    });
    fitText(slide, s.sub, { x: cx + 0.20, y: M.BODY_Y + 1.64, w: cw - 0.40, h: ch - 1.82 }, {
      fontSize: 11.5, minSize: 9, color: C.MUTED, align: 'center',
    });
  });
  if (d.note) {
    const noteTop = M.BODY_Y + ch + 0.26;
    fitText(slide, d.note, { x: M.PAD, y: noteTop, w: M.CW, h: bodyBottom(d) - noteTop }, {
      fontSize: 13, minSize: 10, color: C.INK, lineSpacingMultiple: 1.1,
    });
  }
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutFlow(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const n = d.steps.length;
  const gap = 0.24, arrow = 0.28;
  const bw = (M.CW - (n - 1) * (gap + arrow)) / n;
  const bottom = bodyBottom(d);

  // Alle Kastenhöhen aus dem Text ableiten, statt den restlichen Platz
  // aufzufüllen — sonst entstehen große leere Flächen in den Kästen.
  let breaksBlock = 0, breakBoxH = 0, breakBwid = 0;
  if (d.breaks) {
    const bn = d.breaks.items.length;
    breakBwid = (M.CW - 0.22 * (bn - 1)) / bn;
    const need = Math.max(...d.breaks.items.map(
      (t) => neededHeight(t, breakBwid - 0.34, 11)));
    breakBoxH = Math.min(1.15, Math.max(0.62, need + 0.24));
    breaksBlock = 0.26 + 0.30 + breakBoxH;
  }
  // Kästen nutzen den verfügbaren Platz (gedeckelt), ihr Text wird darin
  // vertikal zentriert — das vermeidet sowohl Überlauf als auch leere Flächen.
  const room = bottom - M.BODY_Y - breaksBlock;
  const bh = Math.max(1.5, Math.min(room - 0.30, 3.4));
  const by = M.BODY_Y + Math.min(0.28, Math.max(0.10, (room - bh) / 2));
  const stepTextSize = Math.min(...d.steps.map(
    (s) => fitFont(s.text, bw - 0.28, bh - 0.90, 11, 8.5)));

  d.steps.forEach((s, i) => {
    const bx = M.PAD + i * (bw + gap + arrow);
    const dark = !!s.emph;
    card(slide, {
      x: bx, y: by, w: bw, h: bh,
      fill: dark ? C.FOREST : C.WHITE, line: dark ? C.FOREST : C.LINE,
    });
    // Titel + Text als Gruppe vertikal zentrieren
    const tNeed = neededHeight(s.title, bw - 0.34, 13.5, true);
    const xNeed = neededHeight(s.text, bw - 0.34, 11);
    const top = by + Math.max(0.16, (bh - (tNeed + 0.14 + xNeed)) / 2);
    const t = fitText(slide, s.title, {
      x: bx + 0.14, y: top, w: bw - 0.28, h: Math.min(0.62, tNeed + 0.08),
    }, {
      fontFace: F.HEAD, fontSize: 13.5, minSize: 10.5, bold: true,
      color: dark ? C.WHITE : C.FOREST, align: 'center', lineSpacingMultiple: 1.0,
    });
    const txY = top + t.height + 0.14;
    slide.addText(s.text, {
      x: bx + 0.14, y: txY, w: bw - 0.28, h: by + bh - 0.14 - txY,
      fontFace: F.BODY, fontSize: stepTextSize, color: dark ? C.MOSS : C.MUTED,
      align: 'center', valign: 'top', lineSpacingMultiple: 1.06,
      isTextBox: true, margin: 0,
    });
    if (i < n - 1) {
      slide.addText('→', {
        x: bx + bw + gap / 2 - 0.06, y: by + bh / 2 - 0.24, w: arrow + 0.12, h: 0.48,
        fontFace: F.BODY, fontSize: 20, bold: true, color: C.AMBER,
        align: 'center', valign: 'middle', isTextBox: true, margin: 0,
      });
    }
  });

  if (d.breaks) {
    const lblY = by + bh + 0.22;
    slide.addText(d.breaks.label.toUpperCase(), {
      x: M.PAD, y: lblY, w: M.CW, h: 0.24,
      fontFace: F.BODY, fontSize: 10.5, bold: true, charSpacing: 1.4,
      color: C.RED, isTextBox: true, margin: 0,
    });
    const boxY = lblY + 0.30;
    d.breaks.items.forEach((t, i) => {
      const x = M.PAD + i * (breakBwid + 0.22);
      slide.addShape('roundRect', {
        x, y: boxY, w: breakBwid, h: breakBoxH, rectRadius: 0.06,
        fill: { color: C.RED_L }, line: { color: C.RED_L },
      });
      fitText(slide, t, {
        x: x + 0.14, y: boxY + 0.10, w: breakBwid - 0.28, h: breakBoxH - 0.20,
      }, { fontSize: 11, minSize: 8.5, color: C.RED });
    });
  }
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutDecision(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const qw = 7.4, qx = (M.W - qw) / 2, qy = M.BODY_Y;
  const qh = 0.82;
  slide.addShape('roundRect', {
    x: qx, y: qy, w: qw, h: qh, rectRadius: 0.10,
    fill: { color: C.FOREST }, line: { color: C.FOREST }, shadow: shadowSoft(),
  });
  fitText(slide, d.question, { x: qx + 0.22, y: qy + 0.06, w: qw - 0.44, h: qh - 0.12 }, {
    fontFace: F.HEAD, fontSize: 15.5, minSize: 12, bold: true,
    color: C.WHITE, align: 'center', valign: 'middle',
  });

  const by = qy + qh + 0.46;
  const bh = bodyBottom(d) - by;
  const bw = (M.CW - 0.5) / 2;
  d.branches.forEach((b, i) => {
    const bx = M.PAD + i * (bw + 0.5);
    slide.addText('▼', {
      x: bx + bw / 2 - 0.2, y: qy + qh + 0.04, w: 0.4, h: 0.34,
      fontFace: F.BODY, fontSize: 13, color: C.AMBER,
      align: 'center', isTextBox: true, margin: 0,
    });
    const headH = 0.90;
    card(slide, { x: bx, y: by, w: bw, h: bh });
    slide.addShape('roundRect', {
      x: bx, y: by, w: bw, h: headH, rectRadius: 0.08,
      fill: { color: i === 0 ? C.AMBER : C.MOSS },
      line: { color: i === 0 ? C.AMBER : C.MOSS },
    });
    const hc = i === 0 ? C.WHITE : C.FOREST;
    fitText(slide, b.cond, { x: bx + 0.22, y: by + 0.09, w: bw - 0.44, h: 0.30 }, {
      fontSize: 11.5, minSize: 9.5, bold: true, color: hc,
    });
    fitText(slide, b.role, { x: bx + 0.22, y: by + 0.42, w: bw - 0.44, h: 0.40 }, {
      fontFace: F.HEAD, fontSize: 16, minSize: 12, bold: true, color: hc,
    });
    const listTop = by + headH + 0.18;
    const slot = (bh - headH - 0.32) / b.duties.length;
    let y = listTop;
    b.duties.forEach((t) => {
      slide.addShape('ellipse', {
        x: bx + 0.24, y: y + 0.09, w: 0.12, h: 0.12,
        fill: { color: C.AMBER }, line: { color: C.AMBER },
      });
      fitText(slide, t, { x: bx + 0.50, y, w: bw - 0.74, h: slot - 0.04 }, {
        fontSize: 12, minSize: 9.5, color: C.MUTED,
      });
      y += slot;
    });
  });
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutTimeline(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const n = d.phases.length, gx = 0.28;
  const cw = (M.CW - gx * (n - 1)) / n;
  const py = M.BODY_Y + 0.68;
  const ph = bodyBottom(d) - py;
  const phaseSize = Math.min(...d.phases.map(
    (p) => fitFont(p.text, cw - 0.44, ph - 1.18, 11.5, 8.5)));

  d.phases.forEach((p, i) => {
    const px = M.PAD + i * (cw + gx);
    numCircle(slide, {
      x: px + cw / 2 - 0.26, y: M.BODY_Y, d: 0.52, label: p.num,
      fill: p.emph ? C.AMBER : C.FOREST, size: 16,
    });
    card(slide, {
      x: px, y: py, w: cw, h: ph,
      fill: p.emph ? C.AMBER_L : C.WHITE, line: p.emph ? C.AMBER_L : C.LINE,
    });
    fitText(slide, p.title, { x: px + 0.22, y: py + 0.22, w: cw - 0.44, h: 0.42 }, {
      fontFace: F.HEAD, fontSize: 15.5, minSize: 11.5, bold: true,
      color: C.FOREST, lineSpacingMultiple: 1.0,
    });
    fitText(slide, p.when, { x: px + 0.22, y: py + 0.66, w: cw - 0.44, h: 0.28 }, {
      fontSize: 11.5, minSize: 9.5, bold: true, color: C.AMBER,
    });
    slide.addText(p.text, {
      x: px + 0.22, y: py + 0.98, w: cw - 0.44, h: ph - 1.18,
      fontFace: F.BODY, fontSize: phaseSize, color: C.MUTED,
      valign: 'top', lineSpacingMultiple: 1.06, isTextBox: true, margin: 0,
    });
  });
  if (d.takeaway) keyTakeaway(slide, d.takeaway);
  if (d.source) sourceNote(slide, d.source);
}

function layoutTable(slide, d) {
  lightBg(slide);
  slideHead(slide, { kicker: d.kicker, title: d.title });
  speakerBadge(slide, d.speaker);

  const head = d.head.map((h) => ({
    text: h,
    options: {
      fill: { color: C.FOREST }, color: C.WHITE, bold: true,
      fontFace: F.BODY, fontSize: 11.5, valign: 'middle', margin: 0.08,
    },
  }));
  const body = d.rows.map((r, ri) => r.map((cell, ci) => ({
    text: cell,
    options: {
      fill: { color: ri % 2 ? C.WHITE : 'EFEEE9' },
      color: ci === 0 ? C.FOREST : C.INK,
      bold: ci === 0,
      fontFace: F.BODY, fontSize: d.rows.length > 8 ? 9.5 : 10.5,
      valign: 'top', margin: 0.08,
    },
  })));
  // Zeilenhöhe über den Inhaltsbereich verteilen, damit die Tabelle die Folie
  // ausfüllt statt oben zu kleben. Kopfzeile etwas flacher als die Datenzeilen.
  const avail = M.FOOT_Y - 0.12 - M.BODY_Y;
  const headH = 0.38;
  const rowH = Math.max(0.30, (avail - headH) / d.rows.length);
  slide.addTable([head, ...body], {
    x: M.PAD, y: M.BODY_Y, w: M.CW,
    colW: d.colW,
    rowH: [headH, ...d.rows.map(() => rowH)],
    border: { type: 'solid', color: C.LINE, pt: 0.5 },
    autoPage: false,
  });
  if (d.source) sourceNote(slide, d.source);
}

function layoutStatement(slide, d) {
  darkBg(slide);
  slide.addShape('ellipse', {
    x: 10.9, y: -1.2, w: 4.4, h: 4.4, fill: { color: C.FOREST_2 }, line: { color: C.FOREST_2 },
  });
  if (d.kicker) {
    slide.addText(d.kicker.toUpperCase(), {
      x: M.PAD, y: 1.24, w: M.CW - 1.0, h: 0.3,
      fontFace: F.BODY, fontSize: 11.5, bold: true, charSpacing: 1.8,
      color: C.AMBER, isTextBox: true, margin: 0,
    });
  }
  const hasPoints = !!d.points;
  const stH = hasPoints ? 2.40 : 3.4;
  fitText(slide, d.statement, { x: M.PAD, y: 1.72, w: 10.6, h: stH }, {
    fontFace: F.HEAD, fontSize: d.size || 30, minSize: 20, bold: true,
    color: C.WHITE, lineSpacingMultiple: 1.10,
  });
  if (hasPoints) {
    const top = 1.72 + stH + 0.22;
    const bottom = d.source ? M.FOOT_Y - 0.16 : M.H - 0.5;
    const slot = (bottom - top) / d.points.length;
    let y = top;
    d.points.forEach((p) => {
      slide.addShape('ellipse', {
        x: M.PAD + 0.02, y: y + 0.11, w: 0.14, h: 0.14,
        fill: { color: C.MOSS }, line: { color: C.MOSS },
      });
      fitText(slide, p, { x: M.PAD + 0.36, y, w: 10.4, h: slot - 0.04 }, {
        fontSize: 13.5, minSize: 10, color: C.MOSS_TXT,
      });
      y += slot;
    });
  }
  if (d.source) {
    fitText(slide, d.source, { x: M.PAD, y: M.FOOT_Y, w: M.CW, h: 0.3 }, {
      fontSize: 9, minSize: 7.5, italic: true, color: '8FA894',
    });
  }
}

const LAYOUTS = {
  title: layoutTitle,
  divider: layoutDivider,
  agenda: layoutAgenda,
  bullets: layoutBullets,
  cards: layoutCards,
  compare: layoutCompare,
  stats: layoutStats,
  flow: layoutFlow,
  decision: layoutDecision,
  timeline: layoutTimeline,
  table: layoutTable,
  statement: layoutStatement,
};

module.exports = { C, F, M, LAYOUTS, fitFont, neededHeight };
