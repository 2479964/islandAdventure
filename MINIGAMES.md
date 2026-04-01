## Minigames for “The Golden Trio’s Wild Ride”

This document adds lightweight, browser-friendly minigames at natural tension/decision beats in the existing Ren’Py story without rewriting the narrative.

### Placement Overview
- **White House intro (start label):** Searching for the “little black book” memory match.
- **Jet scene (jet_scene label):** Turbulence quick-time reflex check.
- **Island scene (island_scene label):** Parrot squawk logic/code-breaking.
- **Tel Aviv scene (tel_scene label):** Falafel peace-treaty dialogue choice.

---

### Minigame 1: Little Black Book Memory
**Integration:** Right after Trump asks Epstein for the “little black book” in the White House intro, before the first menu choice.

**Description:** Player flips cards to find matching “contact” pairs before staffers walk in. Fits the secrecy/panic of hiding the book.

**Rules:**
- Objective: Match all pairs within the time limit.
- Win: All pairs matched before timer hits 0.
- Lose: Timer expires with unmatched pairs.

**Outcome:**
- **Win →** Keeps reputation intact; unlocks a bonus line (“Crisis averted. Tremendous filing skills.”) but story menus proceed as written.
- **Lose →** Embarrassing quip triggers (“Staffer saw everything.”) before returning to the existing menu; no branch change.

**Implementation (simplified):**
```html
<div id="memory-grid"></div>
<div id="timer"></div>
<script>
const contacts = ['deal','ally','press','law'];           // base cards (duplicated on next line via spread operator)
const deck = shuffle([...contacts, ...contacts]);
let flipped = [], solved = 0, time = 45, timerInterval = null, lock = false, finished = false;
function shuffle(arr){
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
const grid = document.getElementById('memory-grid');
deck.forEach((c,i) => {
  const card = document.createElement('button');
  card.textContent = '?'; card.dataset.value = c;
  card.onclick = () => {
    if (lock || flipped.length === 2 || card.disabled || finished) return;
    card.textContent = c;
    card.disabled = true;
    flipped.push(card);
    if (flipped.length === 2) {
      const [a,b] = flipped;
      if (a.dataset.value === b.dataset.value) { solved += 2; flipped=[]; }
      else {
        lock = true;
        setTimeout(() => {
          a.textContent='?';
          b.textContent='?';
          a.disabled=false;
          b.disabled=false;
          flipped=[];
          lock = false;
        }, 600);
      }
      if (solved === deck.length) end(true);
    }
  };
  grid.appendChild(card);
});
const timer = document.getElementById('timer');
timerInterval = setInterval(()=>{
  time--;
  timer.textContent=`Time: ${time}s`;
  if(time<=0) end(false);
},1000);
function end(win){
  if (finished) return;
  finished = true;
  if (timerInterval) clearInterval(timerInterval);
  alert(win?'Win!':'Lose.');
}
</script>
```

---

### Minigame 2: Jet Turbulence QTE
**Integration:** Midway through `jet_scene`, when Yahu threatens to jump if “massage chair” is mentioned again.

**Description:** Quick-time event tapping highlighted seats to steady drinks during turbulence. Reflects urgency on the jet.

**Rules:**
- Objective: Click the highlighted target within a short window, 5 times.
- Win: 5 successes before 3 misses.
- Lose: 3 misses first.

**Outcome:**
- **Win →** Keeps everyone calm; adds a confident line before proceeding to the existing menu.
- **Lose →** Minor spill gag appears; menu choices remain unchanged.

**Implementation (simplified):**
```html
<div id="qte-target"></div><div id="score"></div>
<script>
let hits=0, misses=0, active=false;
const target=document.getElementById('qte-target');
function flash(){
  active=true; target.classList.add('on');
  setTimeout(()=>{ if(active){ misses++; update(); } stop(); }, 900);
}
function stop(){ active=false; target.classList.remove('on'); if (misses>=3) end(false); else if (hits>=5) end(true); else setTimeout(flash,500); }
target.onclick=()=>{ if(active){ hits++; update(); stop(); } };
function update(){ document.getElementById('score').textContent=`Hits ${hits}/5 | Misses ${misses}/3`; }
function end(win){ alert(win?'Smooth flight!':'Spilled drinks!'); }
flash();
</script>
```

---

### Minigame 3: Parrot Cipher Logic
**Integration:** In `island_scene` after the parrot squawks “Little black book!”, before the ending/tel menu.

**Description:** Decode the parrot’s squawk by ordering colored feathers to reveal the safe code. Fits the secretive island vibe.

**Rules:**
- Objective: Arrange 4 feathers in the correct order using provided clues.
- Win: Correct permutation submitted.
- Lose: Three incorrect submissions.

**Outcome:**
- **Win →** Adds a humorous “found the snacks” reward line; menu continues unchanged.
- **Lose →** Parrot mocks the team; proceed to menu normally.

**Implementation (simplified):**
```html
<div id="feathers"></div><div id="attempt"></div><button id="submit">Submit</button>
<div id="feedback"></div>
<script>
const answer=['red','blue','green','gold'];
const feathers=document.getElementById('feathers');
const feedback=document.getElementById('feedback');
const attemptDisplay=document.getElementById('attempt');
['red','blue','green','gold'].forEach(color=>{
  const btn=document.createElement('button');
  btn.textContent=color; btn.onclick=()=>select(color); feathers.appendChild(btn);
});
let attempt=[];
let attemptsLeft=3;
function renderAttempt(){ attemptDisplay.textContent = attempt.length ? attempt.join(' → ') : 'No picks yet'; }
function select(c){
  if(attempt.length>=4 || attempt.includes(c)) return;
  attempt.push(c);
  renderAttempt();
}
renderAttempt();
document.getElementById('submit').onclick=()=>{
  const guess = attempt.join(',');
  const target = answer.join(',');
  if(guess===target){ end(true); return; }
  attemptsLeft--;
  attempt=[];
  feedback.textContent=`Nope. You tried: ${guess || 'nothing'}. ${attemptsLeft} tries left.`;
  renderAttempt();
  if(!attemptsLeft) end(false);
};
function end(win){
  feedback.textContent=win?'Code cracked!':'Parrot wins.';
  attempt=[];
  renderAttempt();
}
</script>
```

---

### Minigame 4: Falafel Treaty Dialogue
**Integration:** In `tel_scene` during the “Falafel peace treaty” discussion, before jumping to `ending`.

**Description:** Dialogue choice puzzle; pick the most diplomatic responses to reach a positive tally. Ties to negotiation theme.

**Rules:**
- Objective: Choose the best of three responses in three turns.
- Win: Score ≥ 2 good choices.
- Lose: Score ≤ 1.

**Outcome:**
- **Win →** Extra upbeat line before the ending; no branch change.
- **Lose →** Lighthearted bickering line before the ending.

**Implementation (simplified):**
```html
<div id="dialogue"></div>
<script>
const dialogue=document.getElementById('dialogue');
const prompts=[
 {q:'Pick a toast line', opts:[
   {t:'To mutual profit!', v:1},
   {t:'To mystery flights!', v:0},
   {t:'To plausible deniability!', v:-1}]},
 {q:'Choose a table topic', opts:[
   {t:'Mutual security cooperation', v:1},
   {t:'Unscheduled island tour', v:-1},
   {t:'Neutral weather small-talk', v:0}]},
 {q:'Seal the deal', opts:[
   {t:'Handshake and hummus', v:1},
   {t:'Whispered side deal', v:-1},
   {t:'Group selfie', v:0}]}
];
let score=0, i=0;
function render(){
  if(i>=prompts.length) return finish();
  const p=prompts[i]; dialogue.innerHTML=`<p>${p.q}</p>`;
  p.opts.forEach(o=>{
    const b=document.createElement('button'); b.textContent=o.t;
    b.onclick=()=>{ score+=o.v; i++; render(); }; dialogue.appendChild(b);
  });
}
function finish(){ alert(score>=2?'Treaty sealed!':'Awkward silence.'); }
render();
</script>
```

---

### Integration Notes
- Each minigame injects immediately before the existing menu or transition listed above, preserving original branching and dialogue.
- Outcomes only add flavor lines; they do **not** alter the story’s structure or endings, keeping pacing intact.
- All snippets are plain HTML/CSS/JS placeholders suitable for embedding in a web layer; visuals can be skinned to match existing assets without heavy frameworks.
