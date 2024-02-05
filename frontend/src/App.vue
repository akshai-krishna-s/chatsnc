<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Nav from './components/Nav.vue'
</script>

<template>
  <div class="w-full h-full flex flex-col bg-gray-dark text-gray-light font-roboto font-medium">
    <Nav />
    <RouterView />
  </div>
</template>
