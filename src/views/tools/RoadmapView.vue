<script setup lang="ts">
import { ref } from 'vue'
import { generateRoadmap } from '../../services/api'

const role = ref('Data Scientist')
const level = ref('junior')
const steps = ref<string[]>([])
const loading = ref(false)

async function submit() {
  loading.value = true
  try {
    const res = await generateRoadmap(role.value, level.value)
    steps.value = res.steps || []
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="tool">
    <h2>Career Roadmap Generator</h2>
    <div class="row">
      <input v-model="role" placeholder="Target role" />
      <select v-model="level">
        <option>junior</option>
        <option>mid</option>
        <option>senior</option>
      </select>
      <button @click="submit" :disabled="loading">{{ loading ? 'Generating…' : 'Generate Now' }}</button>
    </div>
    <ol v-if="steps.length" class="out">
      <li v-for="s in steps" :key="s">{{ s }}</li>
    </ol>
  </div>
</template>

<style scoped>
.tool { padding: 1rem; }
.row { display:flex; gap:.5rem; }
input, select { padding:.6rem .8rem; border:1px solid #e5e7eb; border-radius:10px; }
button { padding:.6rem 1rem; background:#0f172a; color:#fff; border:0; border-radius:10px; cursor:pointer; }
.out { margin-top:.75rem; display:flex; flex-direction:column; gap:.4rem; }
</style>
