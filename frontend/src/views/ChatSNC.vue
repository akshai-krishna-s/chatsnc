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
          <div class="md:mx-auto px-4 py-4 md:px-0">
            <div v-for="message in chat" :key="message.content" class="flex flex-col">
              <div class="flex flex-col">
                <p class="font-semibold">{{ message.role === 'user' ? 'You' : 'ChatSNC' }}</p>
                <p class="whitespace-pre-wrap">{{ message.content }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full pt-2 md:pt-0">
      <form class="mx-2 flex flex-row gap-3 stretch last:mb-auto md:mx-4 md:last:mb-6 lg:mx-auto lg:w-9/12" @submit.prevent="loading ? null : sendMessage()">
        <div class="relative flex h-full flex-1 items-stretch md:flex-col">
          <div class="flex w-full items-center">
            <div
              class="overflow-hidden flex w-full flex-grow relative border rounded-full border-gray items-center gap-2 [&:has(input:focus)]:border-gray-light [&:has(input:focus)]:shadow-[0_2px_6px_rgba(0,0,0,.05)]"
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

              <span class="cursor-pointer" @click="loading ? null : sendMessage()">
                <svg width="50" height="50" viewBox="0 0 66 67" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g filter="url(#filter0_d_46_17)">
                    <circle cx="32.9531" cy="33.5" r="29.375" fill="#282A36" />
                  </g>
                  <path
                    d="M46.8221 32.918L24.4553 22.2529C24.2301 22.145 23.9792 22.1041 23.732 22.1351C23.4847 22.166 23.2512 22.2675 23.0587 22.4278C22.8662 22.588 22.7227 22.8004 22.6447 23.0402C22.5668 23.28 22.5577 23.5372 22.6186 23.782L25.1697 34.1245L22.6186 44.4669C22.5572 44.7118 22.5658 44.9693 22.6436 45.2094C22.7213 45.4494 22.8649 45.6621 23.0576 45.8225C23.2503 45.9829 23.484 46.0844 23.7316 46.1151C23.9791 46.1458 24.2301 46.1045 24.4553 45.996L46.8221 35.3309C47.0482 35.2233 47.2393 35.0527 47.3732 34.839C47.507 34.6254 47.5781 34.3775 47.5781 34.1245C47.5781 33.8714 47.507 33.6235 47.3732 33.4099C47.2393 33.1963 47.0482 33.0256 46.8221 32.918ZM25.8433 42.3859L26.9472 37.9105L34.4204 34.1245L26.9472 30.3384L25.8433 25.8631L43.1711 34.1245L25.8433 42.3859Z"
                    fill="#C3CADB"
                  />
                  <defs>
                    <filter id="filter0_d_46_17" x="0.378125" y="0.925" width="65.15" height="65.15" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                      <feFlood flood-opacity="0" result="BackgroundImageFix" />
                      <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha" />
                      <feMorphology radius="1" operator="dilate" in="SourceAlpha" result="effect1_dropShadow_46_17" />
                      <feOffset />
                      <feGaussianBlur stdDeviation="1.1" />
                      <feComposite in2="hardAlpha" operator="out" />
                      <feColorMatrix type="matrix" values="0 0 0 0 0.76328 0 0 0 0 0.790296 0 0 0 0 0.859766 0 0 0 0.37 0" />
                      <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_46_17" />
                      <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_46_17" result="shape" />
                    </filter>
                  </defs>
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
import { ref } from 'vue'
import type { Ref } from 'vue'

const base_url = import.meta.env.VITE_API_ENDPOINT

const router = useRouter()

const chat_id: Ref<Number> = ref(0)

type Chat = {
  content: string
  role: string
}

const loading = ref(false)

const chat: Ref<Chat[]> = ref([])
const message = ref('')

async function createChat() {
  try {
    // const response = await axios.post('chat/', {
    //   headers: {
    //     Authorization: 'Bearer ' + localStorage.getItem('token'),
    //   },
    // })
    // console.log(response.data)
    const response = await fetch(`${base_url}chat/`, {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + localStorage.getItem('token'),
      },
    })
    const data = await response.json()
    return data.id
  } catch (e: any) {}
}

async function updateChat(chat_history: any) {
  try {
    // const response = await axios.put(`chat/${chat_id}`, {
    //   headers: {
    //     'Content-Type': 'application/json',
    //     Authorization: 'Bearer ' + localStorage.getItem('token'),
    //   },
    //   data: JSON.stringify(chat_history),
    // })
    const response = await fetch(`${base_url}chat/${chat_id.value}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + localStorage.getItem('token'),
      },
      body: JSON.stringify(chat_history),
    })
  } catch (e: any) {}
}

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
    if (chat.value.length === 1) {
      chat_id.value = await createChat()
    }
    const response = await fetch(
      `${base_url}chat/generate?` +
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

              // Update the chat after the assistant has finished sending data
              loading.value = false

              updateChat(chat.value)
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
  }
}

onMounted(() => {
  const token = localStorage.getItem('token')
  if (!token || isTokenExpired(token)) {
    router.push('/login')
  }
})
</script>
