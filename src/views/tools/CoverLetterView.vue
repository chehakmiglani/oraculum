<script setup lang="ts">
import { ref } from 'vue'
import { generateCoverLetter } from '../../services/api'

const jd = ref('')
const resumeText = ref('')
const letter = ref('')
const loading = ref(false)

async function submit() {
  if (!jd.value.trim()) return
  loading.value = true
  try {
    const res = await generateCoverLetter(jd.value, resumeText.value)
    letter.value = res.letter
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="tool">
    <h2>Cover Letter Generator</h2>
    <textarea v-model="jd" placeholder="Paste Job Description" rows="6" />
    <textarea v-model="resumeText" placeholder="Paste Resume (optional)" rows="6" />
    <button @click="submit" :disabled="loading">{{ loading ? 'Creating…' : 'Create Now' }}</button>
    <pre v-if="letter" class="out">{{ letter }}</pre>
  </div>
</template>

<style scoped>
.tool { padding: 1rem; display:flex; flex-direction:column; gap:.75rem; }
textarea { width:100%; padding:.6rem .8rem; border:1px solid #e5e7eb; border-radius:10px; font-family: inherit; }
button { align-self:flex-start; padding:.6rem 1rem; background:#0f172a; color:#fff; border:0; border-radius:10px; cursor:pointer; }
.out { white-space: pre-wrap; background:#f8fafc; padding:1rem; border-radius:10px; }
</style>
