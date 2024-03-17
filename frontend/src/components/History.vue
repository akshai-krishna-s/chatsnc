<template>
  <div class="w-full md:w-4/12 hidden md:flex self-start text-gray-light border border-gray mt-8 rounded-md shadow-lg py-3 px-4">
    <div class="flex w-full flex-col gap-1">
      <h1 class="text-lg font-bold">Recent Chats</h1>
      <div class="flex w-full flex-col">
        <div
          v-for="(item, index) in history.slice(0, 10)"
          class="flex w-full cursor-pointer py-2 pl-1 hover:bg-gray-medium transition flex-col gap-2 border-b border-gray hover:border-l-4 hover:border-orange-300"
          :key="index"
          @click="$emit('getChat', item.id)"
        >
          <div class="flex flex-row w-full">
            <div class="text-sm w-full overflow-ellipsis overflow-hidden whitespace-nowrap">{{ displayString(item.chats) }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onRenderTriggered } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'

type Chat = {
  content: string
  role: string
}

type History = {
  id: number
  chats: Chat[]
}

const history: Ref<History[]> = ref([])

function displayString(item: any) {
  return item[0].content
}

async function getChats() {
  try {
    const response = await axios.get('chat/', {
      headers: {
        Authorization: 'Bearer ' + localStorage.getItem('token'),
      },
    })
    console.log(response.data)
    for (const item of response.data) {
      if (item.history) {
        history.value.push({
          id: item.id,
          chats: item.history,
        })
      }
    }
    console.log(history.value)
  } catch (e: any) {}
}

onMounted(() => {
  getChats()
})

onRenderTriggered(() => {
  getChats()
})
</script>
