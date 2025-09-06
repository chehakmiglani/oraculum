<script setup lang="ts">
import logo from '../assets/logo.svg';
import { APP_NAME } from '@/constants/branding'
</script>

<template>
  <header class="navbar">
    <div class="left">
      <img class="logo" :alt="APP_NAME" :src="logo" />
      <span class="brand">{{ APP_NAME.toUpperCase() }}</span>
    </div>
    <div class="center">
      <input class="search" type="search" placeholder="Search" />
    </div>
    <div class="right">
      <button class="pill">Join Our AI Career Community</button>
      <div class="avatar">S</div>
    </div>
  </header>
</template>

<style scoped>
.navbar {
  height: 64px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 1rem;
  padding: 0 1rem;
  border-bottom: 1px solid #eef2f7;
  background: #ffffffcc;
  backdrop-filter: saturate(180%) blur(8px);
  position: sticky;
  top: 0;
  z-index: 10;
}
.left { display: flex; align-items: center; gap: .5rem; }
.logo { width: 28px; height: 28px; }
.brand { font-weight: 700; letter-spacing: .5px; color: #0f172a; }
.center { max-width: 560px; width: 100%; }
.search {
  width: 100%;
  height: 38px;
  padding: 0 .875rem;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
  outline: none;
}
.right { display: flex; align-items: center; gap: .75rem; }
.pill {
  height: 36px; padding: 0 .875rem; border-radius: 999px; border: 0; cursor: pointer;
  background: #f1f5f9; color: #0f172a; font-weight: 600;
}
.avatar { width: 32px; height: 32px; border-radius: 50%; background: #111827; color: #fff; display:flex; align-items:center; justify-content:center; font-weight:700; }
</style>
