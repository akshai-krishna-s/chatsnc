<template>
  <div class="text-gray-light h-full flex-1 flex flex-col">
    <div class="flex-1 overflow-hidden">
      <div class="relative h-full">
        <div class="flex h-full flex-col items-center justify-center">
          <form class="flex flex-col gap-3 bg-gray-medium items-center px-10 py-8 rounded-md" @submit.prevent="registerUser">
            <p class="text-center text-2xl font-medium mb-3">Register to ChatSNC</p>
            <div class="flex flex-col gap-1">
              <label for="email" class="text-base">Email</label>
              <input type="email" id="email" name="email" class="bg-transparent border h-8 rounded-md w-60 pl-2 focus:outline-none focus:ring-1 ring-slate-300" v-model="data.email" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="password" class="text-base">Password</label>
              <input type="password" id="password" name="password" class="bg-transparent border h-8 rounded-md w-60 pl-2 focus:outline-none focus:ring-1 ring-slate-300" v-model="data.password" />
            </div>
            <button class="text-gray-medium text-base bg-gray-light w-fit px-4 py-1 font-medium rounded-md">Register</button>
            <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
            <p class="text-sm">Don't have an account? <router-link class="text-blue-primary" to="/register">Login</router-link></p>
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
  email: '',
  password: '',
})

const error = ref('')

async function registerUser() {
  try {
    const response = await axios.post('users/', {
      email: data.value.email,
      password: data.value.password,
    })

    error.value = ''
    // redirect to login page
    router.push('/login')
  } catch (e: any) {
    if (e.response.status === 403 || e.response.status === 400) {
      error.value = e.response.data.detail
    }
    if (e.response.status === 422) {
      error.value = 'Enter a valid email and password'
    }
  }
}
</script>
