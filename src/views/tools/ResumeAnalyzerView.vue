<script setup lang="ts">
import { ref } from 'vue'
import { analyzeResume } from '../../services/api'

const selectedFile = ref<File | null>(null)
const feedback = ref('')
const loading = ref(false)
const error = ref('')

function onFileChange(e: Event) {
  const input = e.target as HTMLInputElement | null
  selectedFile.value = input?.files?.[0] ?? null
}

async function submit() {
  if (!selectedFile.value) return
  loading.value = true
  error.value = ''
  try {
    const res = await analyzeResume(selectedFile.value)
    feedback.value = res.feedback
  } catch (e:any) {
    error.value = e.message || 'Request failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="tool">
    <h2>AI Resume Analyzer</h2>
    <input type="file" @change="onFileChange" accept=".pdf,.txt" />
    <button @click="submit" :disabled="loading || !selectedFile">{{ loading ? 'Analyzing…' : 'Analyze Now' }}</button>
    <div v-if="error" class="err">Error: {{ error }}</div>
    <pre v-if="feedback" class="out">{{ feedback }}</pre>
  </div>
</template>

<style scoped>
.tool { padding: 1rem; display:flex; flex-direction:column; gap:.75rem; }
button { align-self:flex-start; padding:.6rem 1rem; background:#0f172a; color:#fff; border:0; border-radius:10px; cursor:pointer; }
.out { white-space: pre-wrap; background:#f8fafc; padding:1rem; border-radius:10px; }
</style>
