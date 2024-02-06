<template>
  <div class="text-gray-light h-full flex-1 flex flex-col">
    <div class="flex-1 overflow-hidden">
      <div class="relative h-full">
        <div class="flex h-full flex-col items-center justify-center">
          <form class="flex flex-col gap-3 mt- bg-gray-medium items-center px-10 py-8 rounded-md" @submit.prevent="loginUser">
            <p class="text-center text-2xl font-medium mb-3">Login to ChatSNC</p>
            <div class="flex flex-col gap-1">
              <label for="email" class="text-base">Email</label>
              <input type="email" id="username" name="username" class="bg-transparent border h-8 rounded-md w-60 pl-2 focus:outline-none focus:ring-1 ring-slate-300" v-model="data.username" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="password" class="text-base">Password</label>
              <input type="password" id="password" name="password" class="bg-transparent border h-8 rounded-md w-60 pl-2 focus:outline-none focus:ring-1 ring-slate-300" v-model="data.password" />
            </div>
            <button class="text-gray-medium flex justify-center text-base bg-gray-light w-fit px-4 py-1 font-medium rounded-md">
              <p v-if="!loading">Login</p>
              <div v-else>
                <svg class="w-6 h-6 text-gray-medium animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-10" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              </div>
            </button>
            <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
            <p class="text-sm">Don't have an account? <router-link class="text-blue-primary" to="/register">Register</router-link></p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const data = ref({
  username: '',
  password: '',
})

const loading = ref(false)

const error = ref('')

async function loginUser() {
  try {
    loading.value = true
    const response = await axios.post(
      'login',
      {
        username: data.value.username,
        password: data.value.password,
      },
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    )
    error.value = ''
    console.log(response.data)
    localStorage.setItem('token', response.data.access_token)
    router.push('/')
  } catch (e: any) {
    if (e.response.status === 403) {
      error.value = e.response.data.detail
    }
    if (e.response.status === 422) {
      error.value = 'Enter a valid email and password'
    }
  } finally {
    loading.value = false
  }
}
</script>
