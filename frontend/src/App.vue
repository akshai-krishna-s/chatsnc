<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Nav from './components/Nav.vue'
</script>

<template>
  <div class="relative h-full flex w-full text-gray-light overflow-hidden font-open">
    <div class="flex-1 h-full max-w-full flex flex-col relative">
      <Nav />
      <div class="relative h-full w-full flex-1 overflow-auto transition-width">
        <RouterView />
      </div>
    </div>
  </div>
</template>
