<script setup lang="ts">
import { ref } from 'vue'
import { askChat } from '../../services/api'

const question = ref('')
const answer = ref('')
const loading = ref(false)
const provider = ref('')
const model = ref('')
const error = ref('')

async function submit() {
  if (!question.value.trim()) return
  loading.value = true
  error.value = ''
  try {
    const res = await askChat(question.value)
    answer.value = res.answer
    provider.value = res.provider || ''
    model.value = res.model || ''
  } catch (e:any) {
    error.value = e.message || 'Request failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="tool">
    <h2>AI Career Q&A Chat</h2>
    <div class="row">
      <input v-model="question" placeholder="Ask a career question" />
      <button @click="submit" :disabled="loading">{{ loading ? 'Asking…' : 'Ask Now' }}</button>
    </div>
  <div v-if="error" class="err">Error: {{ error }}</div>
  <div v-if="provider && !error" class="meta">Model: {{ provider }} / {{ model }}</div>
  <pre v-if="answer" class="out">{{ answer }}</pre>
  </div>
</template>

<style scoped>
.tool { padding: 1rem; }
.row { display:flex; gap:.5rem; }
input { flex:1; padding:.6rem .8rem; border:1px solid #e5e7eb; border-radius:10px; }
button { padding:.6rem 1rem; background:#0f172a; color:#fff; border:0; border-radius:10px; cursor:pointer; }
.out { white-space: pre-wrap; background:#f8fafc; padding:1rem; border-radius:10px; margin-top: .75rem; }
.meta { font-size:.75rem; color:#64748b; margin-top:.5rem; }
</style>
