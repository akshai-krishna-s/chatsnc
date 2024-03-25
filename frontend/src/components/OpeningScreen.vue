<template>
  <div class="flex h-full flex-col items-center justify-center">
    <div class="flex flex-col px-4 md:px-0 items-center gap-6">
      <p class="text-2xl md:text-2xl mb-4 text-center text-gray-light font-medium">
        Ask about the website content of <a href="https://snckollam.ac.in/" target="_blank" class="transition text-blue-200 hover:underline hover:text-gray-light">SN College</a>
      </p>
      <div class="flex flex-col md:flex-row gap-2">
        <button
          v-for="query in randomQueries"
          :key="String(query)"
          class="text-orange-100 text-base pl-6 pr-6 hover:shadow-md transition hover:shadow-gray py-5 border text-left border-orange-100 rounded-3xl flex align-top font-normal"
          @click="$emit('submitSampleQuery', query)"
        >
          >> {{ query }}
        </button>
      </div>
      <p class="text-sm text-gray-light">- Please do not enter any private or sensitive information.</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
const sampleQueries = [
  'What is the minimum attendance required in SN College?',
  'Who was the first HOD of physics department?',
  'What are the courses provided in Biotechnology Department?',
  'How to Apply for E-Grantz and who can apply?',
  'What are the facilities available in the Hostel?',
  'What are the scholarships available for students?',
  'Who are the current principal and manager of SN College?',
  'where is Multi Gym located in SN College?',
]

const randomQueries = sampleQueries.sort(() => Math.random() - Math.random()).slice(0, 3)
</script>
