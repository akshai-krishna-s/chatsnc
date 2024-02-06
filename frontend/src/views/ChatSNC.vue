<template>
  <div class="text-gray-light h-full flex-1 flex flex-col">
    <div class="flex-1 overflow-hidden">
      <!-- <div class="relative h-full">
        <div class="absolute left-0 right-0"><div class="h-1.5"></div></div>
        <div class="flex h-full flex-col items-center justify-center">
          <div class="text-2xl font-medium">Ask about SN College...</div>
        </div>
      </div> -->
      <div class="relative h-full">
        <div class="h-full w-full overflow-y-auto">
          <div class="flex flex-col gap-6 md:w-3/6 md:mx-auto px-4 py-4 md:px-0">
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">You</p>
              <p class="font-light text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit?</p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">ChatSNC</p>
              <p class="font-light text-sm text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi odit, minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis Excepturi odit,
                minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis placeat similique id ipsam. Asperiores, laborum saepe?
              </p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">You</p>
              <p class="font-light text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit?</p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">ChatSNC</p>
              <p class="font-light text-sm">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi odit, minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis Excepturi odit,
                minus, alias blanditiis pariatur modi
              </p>
            </div>
            <div>
              <p class="font-medium text-sm">You</p>
              <p class="font-light text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit?</p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">ChatSNC</p>
              <p class="font-light text-sm">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi odit, minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis Excepturi odit,
                minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis placeat similique id ipsam. Asperiores, laborum saepe?
              </p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">You</p>
              <p class="font-light text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit?</p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">ChatSNC</p>
              <p class="font-light text-sm">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi odit, minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis Excepturi odit,
                minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis placeat similique id ipsam. Asperiores, laborum saepe?
              </p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">You</p>
              <p class="font-light text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit?</p>
            </div>
            <div class="flex flex-col gap-1">
              <p class="font-medium text-sm">ChatSNC</p>
              <p class="font-light text-sm">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi odit, minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis Excepturi odit,
                minus, alias blanditiis pariatur modi, culpa fugit dignissimos nobis iusto facere a corporis placeat similique id ipsam. Asperiores, laborum saepe?
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full pt-2 md:pt-0">
      <form class="stretch mx-2 flex flex-row gap-3 last:mb-2 md:mx-4 md:last:mb-6 lg:mx-auto lg:max-w-2xl xl:max-w-3xl">
        <div class="relative flex h-full flex-1 items-stretch md:flex-col">
          <div class="flex w-full items-center">
            <div
              class="overflow-hidden flex w-full flex-grow relative border rounded-full border-gray items-center pl-4 pr-1 gap-2 [&:has(input:focus)]:border-gray-light [&:has(input:focus)]:shadow-[0_2px_6px_rgba(0,0,0,.05)]"
            >
              <input
                placeholder="Type your message here..."
                class="w-full h-7 resize-none border-0 bg-transparent focus:ring-offset-0 focus:outline-none placeholder:font-light placeholder-gray-light focus:ring-0 focus-visible:ring-0"
                style="overflow-y: hidden"
              />
              <span>
                <svg width="55" height="55" viewBox="0 0 60 59" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="30.1875" cy="29.5" r="29.375" fill="#282A36" />
                  <path d="M30.1875 20.3203V38.6797" stroke="#C3CADB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                  <path d="M21.0078 29.5H39.3672" stroke="#C3CADB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </span>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { isTokenExpired } from '../utils'

const router = useRouter()

onMounted(() => {
  const token = localStorage.getItem('token')
  if (!token || isTokenExpired(token)) {
    router.push('/login')
  }
})
</script>
