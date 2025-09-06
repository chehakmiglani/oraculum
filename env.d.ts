/// <reference types="vite/client" />

// Vue SFC shim for TypeScript so imports like './Component.vue' type-check
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}
