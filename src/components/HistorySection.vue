<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { getHistory } from '../services/api';

type HistoryRow = { icon: string; title: string; date: string }
const rows = ref<HistoryRow[]>([])
const loading = ref(false)
const error = ref<string | null>(null)

onMounted(async () => {
  loading.value = true
  try {
    const res = await getHistory()
    rows.value = (res.items || []).map((it: any) => ({
      icon: it.tool?.includes('Resume') ? '📄' : it.tool?.includes('Roadmap') ? '🧭' : it.tool?.includes('Cover') ? '✉️' : '💬',
      title: it.tool || 'Unknown',
      date: new Date().toLocaleString(),
    }))
  } catch (e) {
    console.error(e)
    error.value = 'Could not load history. Is the backend running?'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="history">
    <h2 class="section-title">Previous History</h2>
    <p class="section-sub">What you previously worked on, you can find here</p>

    <div v-if="loading">Loading…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <ul v-else class="list">
      <li v-for="h in rows" :key="h.title + h.date" class="row">
        <span class="bullet">{{ h.icon }}</span>
        <span class="name">{{ h.title }}</span>
        <span class="time">{{ h.date }}</span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.history { margin-top: 1.5rem; }
.list { list-style:none; padding:0; margin: .75rem 0 0; display:flex; flex-direction:column; gap:.5rem; }
.row { display:grid; grid-template-columns: 24px 1fr auto; align-items:center; gap:.5rem; padding:.5rem .75rem; border:1px solid #eef2f7; border-radius:10px; }
.bullet { color:#6366f1; text-align:center; }
.name { font-weight:700; }
.time { color:#64748b; font-size:.85rem; }
.error { color: #b91c1c; }
</style>
