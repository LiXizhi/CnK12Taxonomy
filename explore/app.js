const SUBJECTS = [
  "语文", "数学", "英语", "科学", "信息科技",
  "道德与法治", "历史", "地理", "体育与健康", "艺术", "劳动",
  "物理", "化学", "生物学",
];
const COLORS = {
  语文: 0xf472b6,
  数学: 0x60a5fa,
  英语: 0x34d399,
  科学: 0xfbbf24,
  信息科技: 0xa78bfa,
  道德与法治: 0xfb7185,
  历史: 0xfb923c,
  地理: 0x2dd4bf,
  体育与健康: 0x84cc16,
  艺术: 0xe879f9,
  劳动: 0xa8a29e,
  物理: 0x38bdf8,
  化学: 0x22d3ee,
  生物学: 0x4ade80,
};
const XUEDUAN = {
  1: "第一学段 1–2 年级",
  2: "第二学段 3–4 年级",
  3: "第三学段 5–6 年级",
  4: "第四学段 7–9 年级",
  5: "高中 10–12 年级",
};
const TYPES = {
  CONCEPTUAL: "观念",
  PROCEDURAL: "技能",
  REPRESENTATIONAL: "表征",
  LANGUAGE: "语言",
  META: "元认知",
};

const $ = (sel) => document.querySelector(sel);
const hash01 = (s) => {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619);
  return (h >>> 0) / 4294967296;
};

const state = {
  topics: [],
  byId: new Map(),
  deps: [],
  prereqOf: new Map(),
  unlocksOf: new Map(),
  enabled: new Set(SUBJECTS),
  maxGrade: 9,
  selected: null,
  pathIds: null,
  pathEdges: null,
  hover: null,
};

const domainsBySubject = new Map();

function gradeRadiusScale(grade) {
  const progress = THREE.MathUtils.clamp((grade - 1) / 11, 0, 1);
  return 0.38 + 0.62 * Math.pow(progress, 0.72);
}

function layout(t) {
  const si = Math.max(0, SUBJECTS.indexOf(t.subject));
  const sector = ((si + 0.5) / SUBJECTS.length) * Math.PI * 2;
  const domains = domainsBySubject.get(t.subject) ?? [];
  const di = Math.max(0, domains.indexOf(t.domain));
  const grade = (t.gradeStart + t.gradeEnd) / 2;
  const r = (9 + di * 1.7 + hash01(t.id) * 2.4) * gradeRadiusScale(grade);
  const spread = ((Math.PI * 2) / SUBJECTS.length) * 0.7;
  const angle = sector + (hash01(t.id + "a") - 0.5) * spread;
  const y = (grade - 1) * 3.15 + (hash01(t.id + "y") - 0.5) * 0.85;
  return new THREE.Vector3(Math.cos(angle) * r, y, Math.sin(angle) * r);
}

function ancestors(id) {
  const out = [];
  const seen = new Set([id]);
  const q = [id];
  while (q.length) {
    const cur = q.shift();
    for (const e of state.prereqOf.get(cur) ?? []) {
      if (seen.has(e.prerequisiteId)) continue;
      seen.add(e.prerequisiteId);
      out.push(e);
      q.push(e.prerequisiteId);
    }
  }
  return out;
}

async function load() {
  const [topicsDoc, depsDoc] = await Promise.all([
    fetch("../data/topics.json").then((r) => {
      if (!r.ok) throw new Error("topics");
      return r.json();
    }),
    fetch("../data/dependencies.json").then((r) => {
      if (!r.ok) throw new Error("deps");
      return r.json();
    }),
  ]);
  state.topics = topicsDoc.topics;
  state.deps = depsDoc.dependencies;
  state.byId = new Map(state.topics.map((t) => [t.id, t]));
  state.prereqOf = new Map();
  state.unlocksOf = new Map();
  for (const e of state.deps) {
    if (!state.prereqOf.has(e.topicId)) state.prereqOf.set(e.topicId, []);
    state.prereqOf.get(e.topicId).push(e);
    if (!state.unlocksOf.has(e.prerequisiteId)) state.unlocksOf.set(e.prerequisiteId, []);
    state.unlocksOf.get(e.prerequisiteId).push(e);
  }
}

function renderChrome() {
  const box = $("#subjects");
  box.innerHTML = "";
  for (const s of SUBJECTS) {
    const b = document.createElement("button");
    b.style.setProperty("--c", `#${COLORS[s].toString(16).padStart(6, "0")}`);
    b.dataset.subject = s;
    b.innerHTML = `${s} <span class="subject-count"></span>`;
    b.addEventListener("click", () => {
      if (state.enabled.has(s) && state.enabled.size === 1) return;
      if (state.enabled.has(s)) state.enabled.delete(s);
      else state.enabled.add(s);
      b.classList.toggle("off", !state.enabled.has(s));
      applyFilters();
    });
    box.appendChild(b);
  }

  const maxGrade = $("#max-grade");
  maxGrade.value = String(state.maxGrade);
  maxGrade.addEventListener("change", () => {
    state.maxGrade = Number(maxGrade.value);
    const selectedTopic = state.byId.get(state.selected);
    if (selectedTopic && !visible(selectedTopic)) clearSelect();
    else applyFilters();
    updateVisibleCounts();
    $("#q").dispatchEvent(new Event("input"));
  });
  updateVisibleCounts();
}

function visible(t) {
  return state.enabled.has(t.subject) && t.gradeStart <= state.maxGrade;
}

function updateVisibleCounts() {
  const topics = state.topics.filter((t) => t.gradeStart <= state.maxGrade);
  const visibleIds = new Set(topics.map((t) => t.id));
  const dependencyCount = state.deps.filter(
    (e) => visibleIds.has(e.prerequisiteId) && visibleIds.has(e.topicId),
  ).length;
  $("#counts").textContent = `${topics.length.toLocaleString("zh-CN")} 个微主题 · ${dependencyCount.toLocaleString("zh-CN")} 条先修`;
  document.querySelectorAll("[data-subject]").forEach((button) => {
    const count = topics.filter((t) => t.subject === button.dataset.subject).length;
    button.querySelector(".subject-count").textContent = count;
  });
}

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x0b1020, 0.012);
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 320);
camera.position.set(36, 28, 36);

const renderer = new THREE.WebGLRenderer({ canvas: $("#canvas"), antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.setClearColor(0x0b1020, 1);

const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.35;
controls.minDistance = 8;
controls.maxDistance = 110;
controls.target.set(0, 18, 0);

scene.add(new THREE.AmbientLight(0xffffff, 0.55));
const key = new THREE.DirectionalLight(0xffffff, 0.85);
key.position.set(12, 30, 10);
scene.add(key);

const ringMat = new THREE.MeshBasicMaterial({ color: 0x1f2937, side: THREE.DoubleSide });
function makeLabel(text) {
  const c = document.createElement("canvas");
  c.width = 256;
  c.height = 64;
  const ctx = c.getContext("2d");
  ctx.clearRect(0, 0, 256, 64);
  ctx.fillStyle = "rgba(154,163,181,0.95)";
  ctx.font = "28px 'Microsoft YaHei', sans-serif";
  ctx.textAlign = "right";
  ctx.textBaseline = "middle";
  ctx.fillText(text, 248, 32);
  const tex = new THREE.CanvasTexture(c);
  tex.encoding = THREE.sRGBEncoding;
  const spr = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false }));
  spr.scale.set(6.4, 1.6, 1);
  return spr;
}

for (const g of [1, 3, 5, 7, 9, 11]) {
  const y = (g - 1) * 3.15;
  const ringRadius = 22.5 * gradeRadiusScale(g);
  const ringGeo = new THREE.RingGeometry(ringRadius, ringRadius + 0.15, 96);
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = -Math.PI / 2;
  ring.position.y = y;
  scene.add(ring);
  const lab = makeLabel(`${g} 年级`);
  lab.position.set(-24.5, y, 0);
  scene.add(lab);
}

let dots, lines, positions = [];
const indexById = new Map();
const dummy = new THREE.Object3D();
const color = new THREE.Color();

function buildGraph() {
  domainsBySubject.clear();
  for (const t of state.topics) {
    if (!domainsBySubject.has(t.subject)) domainsBySubject.set(t.subject, []);
    const arr = domainsBySubject.get(t.subject);
    if (!arr.includes(t.domain)) arr.push(t.domain);
  }
  positions = state.topics.map(layout);
  indexById.clear();
  state.topics.forEach((t, i) => indexById.set(t.id, i));

  const geo = new THREE.SphereGeometry(0.16, 14, 14);
  const mat = new THREE.MeshStandardMaterial({
    roughness: 0.35,
    metalness: 0.05,
    emissive: 0x111111,
    emissiveIntensity: 0.35,
  });
  dots = new THREE.InstancedMesh(geo, mat, state.topics.length);
  dots.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  scene.add(dots);

  const edgePos = new Float32Array(state.deps.length * 6);
  const edgeCol = new Float32Array(state.deps.length * 6);
  const lineGeo = new THREE.BufferGeometry();
  lineGeo.setAttribute("position", new THREE.BufferAttribute(edgePos, 3));
  lineGeo.setAttribute("color", new THREE.BufferAttribute(edgeCol, 3));
  const lineMat = new THREE.LineBasicMaterial({
    vertexColors: true,
    transparent: true,
    opacity: 0.22,
    depthWrite: false,
  });
  lines = new THREE.LineSegments(lineGeo, lineMat);
  scene.add(lines);

  applyFilters();
}

function applyFilters() {
  const show = state.topics.map(visible);
  for (let i = 0; i < state.topics.length; i++) {
    const t = state.topics[i];
    const p = positions[i];
    dummy.position.copy(p);
    const sel = state.selected === t.id;
    const inPath = state.pathIds?.has(t.id);
    const s = sel ? 2.1 : inPath ? 1.45 : 0.85 + (t.centrality ?? 0.2);
    dummy.scale.setScalar(show[i] ? s : 0.0001);
    dummy.updateMatrix();
    dots.setMatrixAt(i, dummy.matrix);
    const c = color.setHex(COLORS[t.subject] ?? 0xffffff);
    if (state.selected && !sel && !inPath) c.multiplyScalar(0.22);
    dots.setColorAt(i, c);
  }
  dots.instanceMatrix.needsUpdate = true;
  if (dots.instanceColor) dots.instanceColor.needsUpdate = true;

  const pos = lines.geometry.getAttribute("position");
  const col = lines.geometry.getAttribute("color");
  const path = state.pathIds ?? new Set();
  let w = 0;
  for (const e of state.deps) {
    const a = state.byId.get(e.prerequisiteId);
    const b = state.byId.get(e.topicId);
    if (!a || !b || !visible(a) || !visible(b)) continue;
    const ia = indexById.get(a.id);
    const ib = indexById.get(b.id);
    const pa = positions[ia];
    const pb = positions[ib];
    const hot = state.pathEdges
      ? state.pathEdges.has(`${e.topicId}|${e.prerequisiteId}`)
      : path.has(a.id) && path.has(b.id);
    if (state.selected && !hot) continue;
    pos.setXYZ(w, pa.x, pa.y, pa.z);
    pos.setXYZ(w + 1, pb.x, pb.y, pb.z);
    const ca = color.setHex(COLORS[a.subject]);
    if (!hot && state.selected) ca.multiplyScalar(0.15);
    col.setXYZ(w, ca.r, ca.g, ca.b);
    const cb = color.setHex(COLORS[b.subject]);
    if (!hot && state.selected) cb.multiplyScalar(0.15);
    col.setXYZ(w + 1, cb.r, cb.g, cb.b);
    w += 2;
  }
  // hide unused
  for (let i = w; i < pos.count; i++) pos.setXYZ(i, 0, 0, 0);
  pos.needsUpdate = true;
  col.needsUpdate = true;
  lines.geometry.setDrawRange(0, w);
  lines.material.opacity = state.selected ? 0.85 : 0.18;
}

function select(id) {
  state.selected = id;
  const ups = ancestors(id);
  const priorIds = new Set([id, ...ups.map((e) => e.prerequisiteId)]);
  const directDown = (state.unlocksOf.get(id) ?? []).map((e) => e.topicId);
  state.pathIds = new Set([...priorIds, ...directDown]);
  state.pathEdges = new Set();
  for (const e of state.deps) {
    if (priorIds.has(e.topicId) && priorIds.has(e.prerequisiteId)) {
      state.pathEdges.add(`${e.topicId}|${e.prerequisiteId}`);
    }
  }
  for (const e of state.unlocksOf.get(id) ?? []) {
    state.pathEdges.add(`${e.topicId}|${e.prerequisiteId}`);
  }
  applyFilters();
  openPanel(id, ups);
  const t = state.byId.get(id);
  const i = indexById.get(id);
  if (i != null) {
    controls.autoRotate = false;
    controls.target.copy(positions[i]);
  }
}

function clearSelect() {
  state.selected = null;
  state.pathIds = null;
  state.pathEdges = null;
  applyFilters();
  $("aside").classList.remove("open");
  controls.autoRotate = true;
}

function openPanel(id, ups) {
  const t = state.byId.get(id);
  const aside = $("aside");
  aside.classList.add("open");
  const hex = `#${(COLORS[t.subject] ?? 0xffffff).toString(16).padStart(6, "0")}`;
  const prereqs = (state.prereqOf.get(id) ?? []).slice().sort((a, b) => {
    const ga = state.byId.get(a.prerequisiteId)?.gradeStart ?? 0;
    const gb = state.byId.get(b.prerequisiteId)?.gradeStart ?? 0;
    return ga - gb;
  });
  const unlocks = (state.unlocksOf.get(id) ?? []).slice(0, 12);
  const directIds = new Set(prereqs.map((e) => e.prerequisiteId));
  const earlier = ups
    .map((e) => state.byId.get(e.prerequisiteId))
    .filter((p) => p && !directIds.has(p.id))
    .sort((a, b) => a.gradeStart - b.gradeStart || a.name.localeCompare(b.name, "zh"));
  aside.innerHTML = `
    <button class="close" type="button" aria-label="关闭">×</button>
    <div class="kicker" style="color:${hex}">${t.subject} · ${t.domain}</div>
    <h2>${t.name}</h2>
    <div class="en">${t.nameEn ?? ""}</div>
    <div class="meta">
      <span class="chip">${t.gradeStart}–${t.gradeEnd} 年级</span>
      <span class="chip">${XUEDUAN[t.xueduan] ?? ""}</span>
      <span class="chip">${TYPES[t.type] ?? t.type}</span>
    </div>
    <p>${t.description}</p>
    <h3>掌握证据</h3>
    <ul>${(t.evidence ?? []).map((e) => `<li>${e}</li>`).join("")}</ul>
    <h3>先修（${prereqs.length} 条直接）</h3>
    <ul>${
      prereqs.length
        ? prereqs
            .map((e) => {
              const p = state.byId.get(e.prerequisiteId);
              return `<li><button class="linkish" data-id="${p.id}">${p.name}</button>
                <span class="reason">${e.strength === "hard" ? "硬依赖" : "软依赖"} · ${e.reason ?? ""}</span></li>`;
            })
            .join("")
        : "<li>没有记录的先修。</li>"
    }</ul>
    ${
      earlier.length
        ? `<h3>此前还需掌握（${earlier.length}）</h3>
        <ul>${earlier
          .map(
            (p) =>
              `<li><button class="linkish" data-id="${p.id}">${p.name}</button>
                <span class="reason">${p.subject} · ${p.gradeStart}–${p.gradeEnd}年级</span></li>`,
          )
          .join("")}</ul>`
        : ""
    }
    <h3>随后可学</h3>
    <ul>${
      unlocks.length
        ? unlocks
            .map((e) => {
              const p = state.byId.get(e.topicId);
              return `<li><button class="linkish" data-id="${p.id}">${p.name}</button></li>`;
            })
            .join("")
        : "<li>暂无后续边。</li>"
    }</ul>
    <h3>课标代码</h3>
    <ul>${(t.standards ?? []).map((s) => `<li><code>${s}</code></li>`).join("")}</ul>
  `;
  aside.querySelector(".close").onclick = clearSelect;
  aside.querySelectorAll("[data-id]").forEach((btn) => {
    btn.addEventListener("click", () => select(btn.dataset.id));
  });
}

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
const tooltip = $("#tooltip");

function pick(ev) {
  const rect = renderer.domElement.getBoundingClientRect();
  pointer.x = ((ev.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((ev.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(pointer, camera);
  const hit = raycaster.intersectObject(dots)[0];
  if (!hit || hit.instanceId == null) return null;
  const t = state.topics[hit.instanceId];
  return visible(t) ? t : null;
}

renderer.domElement.addEventListener("pointermove", (ev) => {
  const t = pick(ev);
  state.hover = t?.id ?? null;
  if (t) {
    tooltip.style.display = "block";
    tooltip.style.left = `${ev.clientX}px`;
    tooltip.style.top = `${ev.clientY}px`;
    tooltip.textContent = `${t.name} · ${t.subject} ${t.gradeStart}–${t.gradeEnd}年级`;
    renderer.domElement.style.cursor = "pointer";
  } else {
    tooltip.style.display = "none";
    renderer.domElement.style.cursor = "grab";
  }
});

renderer.domElement.addEventListener("click", (ev) => {
  const t = pick(ev);
  if (t) select(t.id);
});

window.addEventListener("keydown", (ev) => {
  if (ev.key === "Escape") clearSelect();
});

window.addEventListener("resize", () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

function bindSearch() {
  const input = $("#q");
  const hits = $("#hits");
  const run = () => {
    const q = input.value.trim();
    if (!q) {
      hits.classList.remove("open");
      hits.innerHTML = "";
      return;
    }
    const found = state.topics
      .filter((t) => visible(t) && (`${t.name}${t.nameEn}${t.domain}${t.subject}`.includes(q) || t.id.includes(q)))
      .slice(0, 20);
    hits.innerHTML = found
      .map(
        (t) =>
          `<button type="button" data-id="${t.id}">${t.name}<small>${t.subject} · ${t.gradeStart}–${t.gradeEnd}年级</small></button>`,
      )
      .join("");
    hits.classList.toggle("open", found.length > 0);
    hits.querySelectorAll("button").forEach((b) => {
      b.onclick = () => {
        select(b.dataset.id);
        hits.classList.remove("open");
      };
    });
  };
  input.addEventListener("input", run);
  input.addEventListener("focus", run);
}

function tick() {
  controls.update();
  renderer.render(scene, camera);
  requestAnimationFrame(tick);
}

try {
  await load();
  renderChrome();
  buildGraph();
  bindSearch();
  tick();
} catch (err) {
  console.error(err);
  $("#counts").textContent = "无法加载 data/*.json。请在仓库根目录运行 npm run explore 后再打开 /explore/";
}
