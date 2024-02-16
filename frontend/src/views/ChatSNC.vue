<template>
  <div class="text-gray-light h-full flex-1 flex flex-col">
    <div class="flex-1 overflow-hidden">
      <div class="relative h-full" v-if="chat.length === 0">
        <div class="absolute left-0 right-0"><div class="h-1.5"></div></div>
        <div class="flex h-full flex-col items-center justify-center">
          <div class="text-2xl font-medium">Ask about SN College...</div>
        </div>
      </div>
      <div class="relative h-full" v-else>
        <div class="h-full w-full overflow-y-auto">
          <div class="flex flex-col gap-6 md:w-3/6 md:mx-auto px-4 py-4 md:px-0">
            <div v-for="message in chat" :key="message.content" class="flex flex-col">
              <div class="flex flex-col">
                <p class="font-semibold">{{ message.role === 'user' ? 'You' : 'ChatSNC' }}</p>
                <p class="">{{ message.content }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full pt-2 md:pt-0">
      <form class="stretch mx-2 flex flex-row gap-3 last:mb-2 md:mx-4 md:last:mb-6 lg:mx-auto lg:max-w-2xl xl:max-w-3xl" @submit.prevent="sendMessage">
        <div class="relative flex h-full flex-1 items-stretch md:flex-col">
          <div class="flex w-full items-center">
            <div
              class="overflow-hidden flex w-full flex-grow relative border rounded-full border-gray items-center pr-4 gap-2 [&:has(input:focus)]:border-gray-light [&:has(input:focus)]:shadow-[0_2px_6px_rgba(0,0,0,.05)]"
            >
              <span class="cursor-pointer" @click="chat = []">
                <svg width="50" height="50" viewBox="0 0 66 67" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g filter="url(#filter0_d_29_32)">
                    <circle cx="33.1875" cy="33.5" r="29.375" fill="#282A36" />
                  </g>
                  <path d="M33.1875 24.3203V42.6797" stroke="#C3CADB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                  <path d="M24.0078 33.5H42.3672" stroke="#C3CADB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                  <defs>
                    <filter id="filter0_d_29_32" x="0.6125" y="0.925" width="65.15" height="65.15" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                      <feFlood flood-opacity="0" result="BackgroundImageFix" />
                      <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha" />
                      <feMorphology radius="1" operator="dilate" in="SourceAlpha" result="effect1_dropShadow_29_32" />
                      <feOffset />
                      <feGaussianBlur stdDeviation="1.1" />
                      <feComposite in2="hardAlpha" operator="out" />
                      <feColorMatrix type="matrix" values="0 0 0 0 0.76328 0 0 0 0 0.790296 0 0 0 0 0.859766 0 0 0 0.37 0" />
                      <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_29_32" />
                      <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_29_32" result="shape" />
                    </filter>
                  </defs>
                </svg>
              </span>
              <input
                placeholder="Type your message here..."
                class="w-full h-7 resize-none border-0 bg-transparent focus:ring-offset-0 focus:outline-none placeholder:font-normal placeholder-gray-light focus:ring-0 focus-visible:ring-0"
                style="overflow-y: hidden"
                v-model="message"
              />
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
import { ref } from 'vue'
import type { Ref } from 'vue'

const base_url = import.meta.env.VITE_API_ENDPOINT

const router = useRouter()

type Chat = {
  content: string
  role: string
}

const loading = ref(false)

const chat: Ref<Chat[]> = ref([])
const message = ref('')

async function sendMessage() {
  try {
    loading.value = true
    const message_copy = message.value
    message.value = ''
    const chat_to_send = chat.value.slice()
    chat.value.push({
      role: 'user',
      content: message_copy,
    })

    const response = await fetch(
      `${base_url}chatsnc/generate?` +
        new URLSearchParams({
          query: message_copy,
        }),
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + localStorage.getItem('token'),
        },
        body: JSON.stringify(chat_to_send),
      }
    )

    // stream
    const reader = response.body?.getReader()

    const stream = new ReadableStream({
      start(controller) {
        chat.value.push({
          content: '',
          role: 'assistant',
        })
        // The following function handles each data chunk
        function push() {
          // "done" is a Boolean and value a "Uint8Array"
          reader?.read().then(({ done, value }) => {
            // Is there no more data to read?
            if (done) {
              // Tell the browser that we have finished sending data
              controller.close()
              return
            }
            // Get the data and send it to the browser via the controller
            const text = new TextDecoder().decode(value)
            chat.value[chat.value.length - 1].content += text
            controller.enqueue(value)

            // Continue pushing data
            push()
          })
        }
        console.log(chat.value)
        push()
      },
    })
  } catch (e: any) {
    console.log(e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  const token = localStorage.getItem('token')
  if (!token || isTokenExpired(token)) {
    router.push('/login')
  }
})
</script>
