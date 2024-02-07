<template>
  <div class="w-full px-4 md:px-16 flex sticky top-0 z-10 min-h-[40px] shadow-md shadow-shadow py-3 justify-between items-center">
    <p class="text-xl font-bold">ChatSNC</p>
    <div v-if="isUserInHomePage()" class="cursor-pointer" @click="logoutUser">
      <svg width="36" height="36" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="25" cy="25" r="24" stroke="#C3CADB" stroke-width="2" />
        <path
          d="M15 37V12H27.5V14.7778H17.7778V34.2222H27.5V37H15ZM33.0556 31.4444L31.1458 29.4306L34.6875 25.8889H23.3333V23.1111H34.6875L31.1458 19.5694L33.0556 17.5556L40 24.5L33.0556 31.4444Z"
          fill="#C3CADB"
        />
      </svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// check if user is in home page
function isUserInHomePage() {
  return router.currentRoute.value.path === '/'
}

function logoutUser() {
  localStorage.removeItem('token')
  axios.defaults.headers.common['Authorization'] = ''
  router.push('/login')
}
</script>
