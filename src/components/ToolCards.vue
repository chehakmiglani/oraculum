<script setup lang="ts">
const tools = [
  { icon: '💬', title: 'AI Career Q&A Chat', desc: 'Ask career questions', cta: 'Ask Now', to: '/tools/chat' },
  { icon: '📄', title: 'AI Resume Analyzer', desc: 'Improve your resume', cta: 'Analyze Now', to: '/tools/resume' },
  { icon: '🧭', title: 'Career Roadmap Generator', desc: 'Build your roadmap', cta: 'Generate Now', to: '/tools/roadmap' },
  { icon: '✉️', title: 'Cover Letter Generator', desc: 'Write a cover letter', cta: 'Create Now', to: '/tools/cover-letter' },
]
</script>

<template>
  <section>
    <h2 class="section-title">Available AI Tools</h2>
    <p class="section-sub">Start building and shape your career with these exclusive AI tools</p>
    <div class="grid">
      <article class="card" v-for="t in tools" :key="t.title">
        <div class="card-head">
          <div class="icon">{{ t.icon }}</div>
          <div>
            <h3>{{ t.title }}</h3>
            <p class="muted">{{ t.desc }}</p>
          </div>
        </div>
  <RouterLink class="primary" :to="t.to">{{ t.cta }}</RouterLink>
      </article>
    </div>
  </section>
</template>

<style scoped>
.section-title { font-size: 1.125rem; font-weight: 800; margin: .25rem 0 0; }
.section-sub { color: #64748b; margin: 0 0 1rem; }
.grid { display:grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; }
.card { border:1px solid #eef2f7; border-radius: 14px; padding: 1rem; display:flex; flex-direction:column; justify-content:space-between; gap:.75rem; }
.card-head { display:flex; gap:.75rem; align-items:center; }
.icon { width:40px; height:40px; border-radius:10px; background:#f1f5f9; display:flex; align-items:center; justify-content:center; font-size: 1.25rem; }
.card h3 { margin: 0; font-size: 1rem; }
.muted { color:#6b7280; margin: .25rem 0 0; font-size: .9rem; }
.primary { align-self:flex-start; background:#0f172a; color:#fff; border:0; border-radius:10px; padding:.6rem 1rem; font-weight:700; cursor:pointer; text-decoration: none; display:inline-block; }
@media (max-width: 1100px){ .grid{ grid-template-columns: repeat(2, 1fr);} }
@media (max-width: 640px){ .grid{ grid-template-columns: 1fr;} }
</style>
