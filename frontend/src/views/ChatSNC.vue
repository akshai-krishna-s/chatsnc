<template>
  <div class="flex h-full md:px-12 gap-8">
    <div class="text-gray-light h-full flex-1 flex flex-col">
      <div class="flex-1 overflow-hidden">
        <div class="relative h-full" v-if="chat.length === 0">
          <StartScreen :sampleQueries="sampleQueries" @submitSampleQuery="submitSampleQuery" />
        </div>
        <div class="relative h-full md:mt-4" v-else>
          <ChatDisplay :chat="chat" />
        </div>
      </div>

      <div class="w-full pt-2 md:pt-0">
        <form class="stretch mx-2 flex flex-row gap-3 last:mb-2 md:last:mb-6 lg:max-w-2xl xl:max-w-3xl" @submit.prevent="loading ? null : sendMessage()">
          <div class="relative flex h-full flex-1 items-stretch md:flex-col">
            <div class="flex w-full items-center">
              <div
                class="overflow-hidden flex w-full flex-grow relative border rounded-full border-gray items-center gap-2 [&:has(input:focus)]:border-gray-light [&:has(input:focus)]:shadow-[0_2px_6px_rgba(0,0,0,.05)]"
              >
                <span class="cursor-pointer" @click="clearChat">
                  <IconNew />
                </span>
                <input
                  placeholder="Type your message here..."
                  class="w-full h-7 resize-none border-0 bg-transparent focus:ring-offset-0 focus:outline-none placeholder:font-normal placeholder-gray-light focus:ring-0 focus-visible:ring-0"
                  style="overflow-y: hidden"
                  v-model="message"
                />

                <span class="cursor-pointer" @click="loading ? null : sendMessage()">
                  <IconSent />
                </span>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
    <History @getChat="getChat" :key="historyKey" />
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { isTokenExpired } from '../utils'
import { ref } from 'vue'
import type { Ref } from 'vue'
import StartScreen from './../components/OpeningScreen.vue'
import ChatDisplay from './../components/ChatDisplay.vue'
import History from './../components/History.vue'
import IconNew from './../components/Icon/New.vue'
import IconSent from './../components/Icon/Sent.vue'
import axios from 'axios'

const base_url = import.meta.env.VITE_API_ENDPOINT

const router = useRouter()

const chat_id: Ref<Number> = ref(0)

type Chat = {
  content: string
  role: string
}

const sampleQueries = ['What is the minimum attendance required in SN College?', 'Who was the first HOD of physics department?', 'What are the courses provided in Biotechnology Department?']

const loading = ref(false)

const chat: Ref<Chat[]> = ref([])
const message = ref('')

const historyKey = ref(0)

const forceHistoryRerender = () => {
  historyKey.value += 1
}

function submitSampleQuery(query: string) {
  message.value = query
  sendMessage()
}

function clearChat() {
  chat.value = []
  forceHistoryRerender()
}

async function createChat() {
  try {
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
        push()
      },
    })
  } catch (e: any) {
    console.log(e)
  } finally {
  }
}

async function getChat(id: number) {
  try {
    const response = await axios.get(`chat/${id}`, {
      headers: {
        Authorization: 'Bearer ' + localStorage.getItem('token'),
      },
    })
    chat.value = response.data
    chat_id.value = id
  } catch (e: any) {}
}

onMounted(() => {
  const token = localStorage.getItem('token')
  if (!token || isTokenExpired(token)) {
    router.push('/login')
  }
})
</script>
