<template>
  <div class="h-full w-full overflow-y-auto">
    <div class="flex flex-col gap-6 px-4 py-4 md:px-0">
      <div v-for="message in chat" :key="message.content" class="flex flex-col">
        <div class="flex flex-col">
          <p class="font-semibold">{{ message.role === 'user' ? 'You' : 'ChatSNC' }}</p>
          <p class="whitespace-pre-wrap">{{ message.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
type Chat = {
  content: string
  role: string
}

defineProps({
  chat: {
    type: Array<Chat>,
    required: true,
  },
})
</script>
