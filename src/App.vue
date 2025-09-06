<script setup lang="ts">
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'
import HeroSection from './components/HeroSection.vue'
import ToolCards from './components/ToolCards.vue'
import HistorySection from './components/HistorySection.vue'
</script>

<template>
  <div class="dashboard-wrapper">
    <Sidebar />
    <div class="dashboard-content">
      <Navbar />
      <div class="dashboard-scroll">
        <HeroSection />
        <ToolCards />
        <HistorySection />
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-wrapper {
  display: flex;
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
}
.dashboard-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  background: #fff;
  min-width: 0;
  box-shadow: 0 0 16px rgba(0,0,0,0.04);
  height: 100vh;
  overflow-y: auto;
}
.dashboard-scroll {
  flex: 1;
  padding: 2rem;
  background: #fff;
}
</style>
