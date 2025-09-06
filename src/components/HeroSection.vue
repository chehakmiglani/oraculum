<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { APP_NAME, APP_TAGLINE } from '@/constants/branding'
</script>

<template>
  <section class="hero">
    <div class="copy">
  <h1>{{ APP_NAME }} — {{ APP_TAGLINE }}</h1>
  <p>Smarter career decisions start here — get tailored advice, real-time market insights, and a roadmap built just for you.</p>
  <RouterLink class="cta" :to="{ name: 'chat' }">Let's Get Started</RouterLink>
    </div>
  </section>
</template>

<style scoped>
.hero {
  width: 100%;
  border-radius: 16px;
  padding: 28px;
  background: linear-gradient(90deg, #ec4899, #6366f1);
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}
.copy { max-width: 860px; }
.hero h1 { font-size: 1.75rem; line-height: 1.2; margin: 0 0 .5rem; }
.hero p { opacity: .95; margin: 0 0 1rem; }
.cta { background: #fff; color: #111827; border: 0; border-radius: 10px; padding: .6rem 1rem; font-weight: 700; cursor: pointer; }
</style>
