<script setup lang="ts">
import { RouterLink } from 'vue-router'
import bot from '../assets/bot.svg';
import { APP_NAME, APP_TAGLINE } from '@/constants/branding'
</script>

<template>
  <aside class="sidebar">
    <div class="brand-row">
  <img class="emoji" :src="bot" alt="bot" />
      <div class="brand-text">
        <div class="title">{{ APP_NAME.toUpperCase() }}</div>
        <div class="subtitle">{{ APP_TAGLINE }}</div>
      </div>
    </div>

    <nav class="nav">
      <RouterLink class="item" :to="{ name: 'dashboard' }">Workspace</RouterLink>
      <RouterLink class="item" :to="{ name: 'chat' }">AI Tools</RouterLink>
      <RouterLink class="item" :to="{ name: 'about' }">My History</RouterLink>
      <a class="item" href="#">Billing</a>
      <a class="item" href="#">Profile</a>
    </nav>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 240px;
  background: #ffffff;
  border-right: 1px solid #eef2f7;
  padding: 1rem .75rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.brand-row { display:flex; gap:.75rem; align-items:center; padding:.25rem .5rem; }
.emoji { width: 36px; height: 36px; }
.brand-text .title { font-weight:800; letter-spacing:.3px; }
.brand-text .subtitle { font-size:.8rem; color:#64748b; margin-top:-2px; }
.nav { display:flex; flex-direction:column; gap:.25rem; }
.item { padding:.6rem .75rem; border-radius: 10px; color:#0f172a; text-decoration:none; font-weight:600; display:block; }
.item:hover { background:#f1f5f9; }
.item.active { background:#e2e8f0; }
</style>
