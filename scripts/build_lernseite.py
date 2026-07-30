#!/usr/bin/env python3
"""
Erzeugt aus lernskript/karteikarten.md eine eigenstaendige Lernseite:
output/lernseite.html

Die Karten werden als JSON in die Seite eingebettet, damit die Datei ohne
Netzwerkzugriff funktioniert. Aufruf:  python3 scripts/build_lernseite.py
"""
import json
import re
from pathlib import Path

from karten import lies_karten, lies_marker, pruefe, kapitel_code

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "lernskript"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

def md_inline(text):
    """**fett** und `code` nach HTML, alles andere escapen."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


CSS = """
:root{
  --paper:#F2F3EF; --paper-2:#E9EBE3; --ink:#1A1D17; --ink-2:#585D4E;
  --rule:#C7CBBC; --rule-soft:#DDE0D5;
  --accent:#5C8F00; --accent-bright:#75B800; --accent-soft:#EDF3DE;
  --signal:#A8760A; --signal-soft:#FBF0D5;
  --grid:rgba(26,29,23,.045);
  --shadow:0 1px 2px rgba(26,29,23,.06),0 8px 28px rgba(26,29,23,.07);
}
@media (prefers-color-scheme:dark){
  :root{
    --paper:#12150F; --paper-2:#1A1E15; --ink:#E8EAE3; --ink-2:#9AA08D;
    --rule:#333829; --rule-soft:#262B1E;
    --accent:#93D613; --accent-bright:#A8E82B; --accent-soft:#1F2A0C;
    --signal:#E0A800; --signal-soft:#2C2408;
    --grid:rgba(232,234,227,.045);
    --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 32px rgba(0,0,0,.45);
  }
}
:root[data-theme="dark"]{
  --paper:#12150F; --paper-2:#1A1E15; --ink:#E8EAE3; --ink-2:#9AA08D;
  --rule:#333829; --rule-soft:#262B1E;
  --accent:#93D613; --accent-bright:#A8E82B; --accent-soft:#1F2A0C;
  --signal:#E0A800; --signal-soft:#2C2408;
  --grid:rgba(232,234,227,.045);
  --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 32px rgba(0,0,0,.45);
}
:root[data-theme="light"]{
  --paper:#F2F3EF; --paper-2:#E9EBE3; --ink:#1A1D17; --ink-2:#585D4E;
  --rule:#C7CBBC; --rule-soft:#DDE0D5;
  --accent:#5C8F00; --accent-bright:#75B800; --accent-soft:#EDF3DE;
  --signal:#A8760A; --signal-soft:#FBF0D5;
  --grid:rgba(26,29,23,.045);
  --shadow:0 1px 2px rgba(26,29,23,.06),0 8px 28px rgba(26,29,23,.07);
}

*{box-sizing:border-box}

body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  font-size:16px; line-height:1.55;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),
                   linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:28px 28px;
  -webkit-text-size-adjust:100%;
}

.mono{font-family:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace}

.wrap{max-width:760px;margin:0 auto;padding:20px 18px 56px;
  display:flex;flex-direction:column;gap:18px}

/* ---- Kopf ---- */
header{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 14px;
  padding-bottom:12px;border-bottom:2px solid var(--ink)}
h1{margin:0;font-size:1.16rem;font-weight:700;letter-spacing:-.015em;
  text-wrap:balance}
.sub{font-size:.7rem;text-transform:uppercase;letter-spacing:.13em;
  color:var(--ink-2);margin-left:auto}

/* ---- Steuerleiste ---- */
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.seg{display:flex;border:1px solid var(--rule);border-radius:2px;
  overflow:hidden;background:var(--paper-2)}
.seg button{appearance:none;background:transparent;border:0;
  padding:7px 13px;font:inherit;font-size:.72rem;color:var(--ink-2);
  cursor:pointer;letter-spacing:.09em;text-transform:uppercase;
  border-right:1px solid var(--rule-soft)}
.seg button:last-child{border-right:0}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.seg button:hover:not([aria-pressed="true"]){color:var(--ink)}

select,.btn{appearance:none;font:inherit;font-size:.72rem;
  letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2);
  background:var(--paper-2);border:1px solid var(--rule);border-radius:2px;
  padding:7px 13px;cursor:pointer}
select{text-transform:none;letter-spacing:0;font-size:.78rem;color:var(--ink)}
.btn:hover,select:hover{color:var(--ink);border-color:var(--ink-2)}

:where(button,select,a):focus-visible{outline:2px solid var(--accent-bright);
  outline-offset:2px}

/* ---- Fortschrittsbalken ---- */
.progress{height:3px;background:var(--rule-soft);position:relative;overflow:hidden}
.progress i{position:absolute;inset:0 auto 0 0;background:var(--accent-bright);
  transition:width .3s ease}
@media (prefers-reduced-motion:reduce){.progress i{transition:none}}

/* ---- Karte ---- */
.stage{perspective:1600px;display:flex;align-items:flex-start}
.card{width:100%;display:grid;transform-style:preserve-3d;
  transition:transform .5s cubic-bezier(.2,.7,.2,1);cursor:pointer;
  border:0;padding:0;background:none;font:inherit;color:inherit;text-align:left}
.card.flip{transform:rotateY(180deg)}
@media (prefers-reduced-motion:reduce){.card{transition:none}}

.face{grid-area:1/1;backface-visibility:hidden;-webkit-backface-visibility:hidden;
  background:var(--paper-2);border:1px solid var(--rule);
  box-shadow:var(--shadow);display:flex;flex-direction:column;min-height:230px}
.face.back{transform:rotateY(180deg)}

.face-body{flex:1;padding:26px 24px 22px;display:flex;flex-direction:column;gap:14px}

.tagrow{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.tag{font-size:.63rem;letter-spacing:.14em;text-transform:uppercase;
  padding:3px 8px;border:1px solid var(--rule);color:var(--ink-2);border-radius:2px}
.tag.klausur{border-color:var(--signal);color:var(--signal);
  background:var(--signal-soft);font-weight:600}
.tag.seite{border-color:var(--accent);color:var(--accent);background:var(--accent-soft)}
.tag.verwandt{border-color:var(--ink-2);color:var(--ink-2)}
.legende{font-size:.72rem;line-height:1.5;color:var(--ink-2);
  border-left:2px solid var(--rule);padding-left:12px}
.legende b{color:var(--ink);font-weight:600}

.q{font-size:1.24rem;line-height:1.35;font-weight:650;letter-spacing:-.012em;
  text-wrap:balance;margin:0}
.a{font-size:1rem;line-height:1.62;margin:0}
.a strong{font-weight:650}
code{font-family:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  font-size:.9em;background:var(--accent-soft);color:var(--accent);
  padding:1px 5px;border-radius:2px}

.hint{margin-top:auto;padding-top:10px;font-size:.68rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink-2)}

/* Schriftfeld, wie im Stromlaufplan */
.schriftfeld{display:grid;grid-template-columns:1fr 1fr auto;
  border-top:1px solid var(--rule)}
.schriftfeld div{padding:7px 12px;border-right:1px solid var(--rule);
  font-size:.63rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.schriftfeld div:last-child{border-right:0;font-variant-numeric:tabular-nums;
  color:var(--ink)}
.schriftfeld b{color:var(--ink);font-weight:600}

/* ---- Bewertung ---- */
.rate{display:flex;gap:8px}
.rate button{flex:1;padding:13px;font-size:.74rem;letter-spacing:.1em;
  text-transform:uppercase;border:1px solid var(--rule);background:var(--paper-2);
  color:var(--ink-2);cursor:pointer;border-radius:2px;font-family:inherit}
.rate button:hover{color:var(--ink);border-color:var(--ink-2)}
.rate .ok:hover{border-color:var(--accent);color:var(--accent);background:var(--accent-soft)}
.rate .again:hover{border-color:var(--signal);color:var(--signal);background:var(--signal-soft)}

.stats{display:flex;gap:18px;font-size:.68rem;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ink-2);font-variant-numeric:tabular-nums}
.stats b{color:var(--ink);font-weight:600}

.empty{padding:40px 24px;text-align:center;color:var(--ink-2);
  border:1px dashed var(--rule);background:var(--paper-2)}

@media (max-width:560px){
  .wrap{padding:14px 12px 40px}
  .q{font-size:1.1rem}
  .sub{margin-left:0;width:100%}
  .schriftfeld{grid-template-columns:1fr auto}
  .schriftfeld div:nth-child(2){display:none}
}
"""

JS = """
const $=s=>document.querySelector(s);
const cards=window.KARTEN;
let filter='alle', kapFilter='', order=[], pos=0, flipped=false;
const seen=new Set(), known=new Set();

function pool(){
  return cards.map((c,i)=>i).filter(i=>{
    const c=cards[i];
    if(filter==='belegt'&&c.stufe!=='belegt') return false;
    if(filter==='verwandt'&&c.stufe!=='verwandt') return false;
    if(filter==='offen'&&known.has(i)) return false;
    if(kapFilter&&c.kap!==kapFilter) return false;
    return true;
  });
}
function rebuild(keep){
  const cur=order[pos];
  order=pool();
  if(keep&&order.includes(cur)) pos=order.indexOf(cur);
  else pos=0;
  render();
}
function shuffle(){
  for(let i=order.length-1;i>0;i--){const j=Math.random()*(i+1)|0;
    [order[i],order[j]]=[order[j],order[i]];}
  pos=0;render();
}
function step(d){
  if(!order.length) return;
  pos=(pos+d+order.length)%order.length;
  flipped=false;render();
}
function flip(){ if(order.length){flipped=!flipped;paint();} }

function rate(ok){
  const i=order[pos];
  if(i===undefined) return;
  seen.add(i);
  if(ok) known.add(i); else known.delete(i);
  if(filter==='offen'&&ok){rebuild(false);return;}
  step(1);
}

function paint(){
  $('#card').classList.toggle('flip',flipped);
  $('#card').setAttribute('aria-label',
    flipped?'Antwort. Zum Umdrehen aktivieren.':'Frage. Zum Umdrehen aktivieren.');
}

function render(){
  const total=order.length;
  $('#stage').hidden=!total;
  $('#empty').hidden=!!total;
  $('#rate').hidden=!total;
  if(!total){$('#bar-i').style.width='0%';paintStats();return;}
  const c=cards[order[pos]];
  $('#q').innerHTML=c.q;
  $('#a').innerHTML=c.a;
  for(const side of ['f','b']){
    $('#kap-'+side).innerHTML='<b>'+c.code+'</b>';
    $('#src-'+side).textContent=c.src||'Foliensatz';
    $('#nr-'+side).textContent=(pos+1)+' / '+total;
  }
  for(const side of ['f','b']){
    const el=$('#stufe-'+side);
    el.hidden=!c.stufe;
    el.textContent=c.stufe==='belegt'?'★ Belegt markiert':'◆ Verwandtes Thema';
    el.className='tag '+(c.stufe==='belegt'?'klausur':'verwandt');
  }
  $('#bar-i').style.width=(total?((pos+1)/total*100):0)+'%';
  paint();paintStats();
}
function paintStats(){
  $('#s-known').textContent=known.size;
  $('#s-total').textContent=cards.length;
  $('#s-star').textContent=cards.filter((c,i)=>c.stufe==='belegt'&&known.has(i)).length
    +' / '+cards.filter(c=>c.stufe==='belegt').length;
}

addEventListener('keydown',e=>{
  if(e.target.tagName==='SELECT') return;
  if(e.key===' '||e.key==='Enter'){e.preventDefault();flip();}
  if(e.key==='ArrowRight')step(1);
  if(e.key==='ArrowLeft')step(-1);
  if(e.key==='j')rate(true);
  if(e.key==='n')rate(false);
});

let x0=null;
$('#stage').addEventListener('touchstart',e=>{x0=e.touches[0].clientX},{passive:true});
$('#stage').addEventListener('touchend',e=>{
  if(x0===null)return;
  const dx=e.changedTouches[0].clientX-x0;
  if(Math.abs(dx)>55){step(dx<0?1:-1);}
  x0=null;
},{passive:true});

document.querySelectorAll('.seg button').forEach(b=>{
  b.onclick=()=>{
    document.querySelectorAll('.seg button').forEach(o=>o.setAttribute('aria-pressed',o===b));
    filter=b.dataset.f;flipped=false;rebuild(false);
  };
});
$('#kap').onchange=e=>{kapFilter=e.target.value;flipped=false;rebuild(false);};
$('#shuffle').onclick=shuffle;
$('#card').onclick=flip;
$('#ok').onclick=()=>rate(true);
$('#again').onclick=()=>rate(false);

rebuild(false);
"""


def build():
    positiv, _ = lies_marker()
    roh = lies_karten(marker=(positiv, set()))
    stat = pruefe(roh, positiv)

    karten = [{"kap": k["kapitel"], "code": kapitel_code(k["kapitel"]),
               "q": md_inline(k["frage"]), "a": md_inline(k["antwort"]),
               "src": k["quelle"], "stufe": k["stufe"]} for k in roh]
    kapitel = sorted({k["kap"] for k in karten}, key=lambda s: (len(s), s))

    optionen = "".join(f'<option value="{k}">{k}</option>' for k in kapitel)

    html = f"""<title>Karteikarten — Grundlagen der Automation</title>
<style>{CSS}</style>
<div class="wrap">
  <header>
    <h1>Grundlagen der Automation</h1>
    <span class="sub mono">{stat['karten']} Karten · {stat['belegt']} belegt · {stat['verwandt']} verwandt</span>
  </header>

  <div class="bar">
    <div class="seg" role="group" aria-label="Kartenauswahl">
      <button data-f="alle" aria-pressed="true">Alle</button>
      <button data-f="belegt" aria-pressed="false">★ Belegt</button>
      <button data-f="verwandt" aria-pressed="false">◆ Verwandt</button>
      <button data-f="offen" aria-pressed="false">Offen</button>
    </div>
    <select id="kap" aria-label="Kapitel filtern">
      <option value="">Alle Kapitel</option>{optionen}
    </select>
    <button class="btn" id="shuffle">Mischen</button>
  </div>

  <p class="legende">
    <b>★ belegt</b> — auf genau dieser Folie steht ein handschriftlicher
    Klausurhinweis, {stat['marker_gesamt']} Folien insgesamt.
    <b>◆ verwandt</b> — gleiches Thema wie eine markierte Folie, aber ohne
    eigenen Hinweis; das ist eine Einschätzung, kein Beleg.
    Die Hinweise stammen aus eigener Mitschrift und grenzen den Stoff nicht ab —
    Karten ohne Zeichen können genauso drankommen.
  </p>

  <div class="progress"><i id="bar-i"></i></div>

  <div class="stage" id="stage">
    <button class="card" id="card" aria-live="polite">
      <div class="face front">
        <div class="face-body">
          <div class="tagrow">
            <span class="tag" id="stufe-f" hidden></span>
          </div>
          <p class="q" id="q"></p>
          <span class="hint mono">Tippen oder Leertaste zum Umdrehen</span>
        </div>
        <div class="schriftfeld mono">
          <div id="kap-f"></div><div id="src-f"></div><div id="nr-f"></div>
        </div>
      </div>
      <div class="face back">
        <div class="face-body">
          <div class="tagrow">
            <span class="tag seite">Antwort</span>
            <span class="tag" id="stufe-b" hidden></span>
          </div>
          <p class="a" id="a"></p>
        </div>
        <div class="schriftfeld mono">
          <div id="kap-b"></div><div id="src-b"></div><div id="nr-b"></div>
        </div>
      </div>
    </button>
  </div>

  <div class="empty" id="empty" hidden>
    Keine Karten in dieser Auswahl. Filter zurücksetzen oder Kapitel wechseln.
  </div>

  <div class="rate" id="rate">
    <button class="again" id="again">Nochmal <span class="mono">(N)</span></button>
    <button class="ok" id="ok">Sitzt <span class="mono">(J)</span></button>
  </div>

  <div class="stats mono">
    <span>Gewusst <b id="s-known">0</b> von <b id="s-total">0</b></span>
    <span>Klausurkarten <b id="s-star">0</b></span>
  </div>
</div>
<script>window.KARTEN={json.dumps(karten, ensure_ascii=False)};</script>
<script>{JS}</script>
"""
    pfad = OUT / "lernseite.html"
    pfad.write_text(html, encoding="utf-8")
    print(f"geschrieben: {pfad.relative_to(ROOT)} "
          f"({pfad.stat().st_size/1024:.0f} KB, {stat['karten']} Karten, "
          f"{len(kapitel)} Kapitel, belegt {stat['belegt']}, "
          f"verwandt {stat['verwandt']})")
    return pfad


if __name__ == "__main__":
    build()
