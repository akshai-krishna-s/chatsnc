<template>
  <div class="text-gray-light h-full flex-1 flex flex-col">
    <div class="flex-1 overflow-hidden">
      <div class="relative h-full">
        <div class="flex h-full flex-col items-center justify-center">
          <form class="flex flex-col gap-3 bg-gray-medium items-center px-10 py-8 rounded-md">
            <p class="text-center text-2xl font-medium mb-3">Login to ChatSNC</p>
            <div class="flex flex-col gap-1">
              <label for="email" class="text-base">Email</label>
              <input type="email" id="email" class="bg-transparent border h-8 rounded-md w-60" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="password" class="text-base">Password</label>
              <input type="password" id="password" class="bg-transparent border h-8 rounded-md w-60" />
            </div>
            <button class="text-gray-medium text-base bg-gray-light w-fit px-4 py-1 font-medium rounded-md">Login</button>
            <p class="text-sm">Don't have an account? <router-link class="text-blue-primary" to="/register">Register</router-link></p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup></script>
