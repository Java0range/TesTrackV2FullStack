<script setup lang="ts">
import TitleView from '@/components/TitleView.vue'

type filesType = {
  url: string,
  name: string,
  user_id: string
}

defineProps({
  numberTask: Number,
  taskId: Number,
  writerName: String,
  writerLink: String,
  difficulty: String,
  text: String,
  img: Array<string>,
  table: Array<string[]>,
  files: Array<filesType>,
  otv: String,
  type: String
})
</script>

<template>
  <div :class="type === 'taskbase' ? 'w-1/2' : 'w-full'" class="shadow-2xl p-7 rounded-2xl mt-5 w-1/2 max-sm:w-full bg-white">
    <div class="flex gap-2 items-center mb-2">
      <div class="p-1 border-solid border-2 flex items-center justify-center w-9 h-9 rounded-lg"><h3>{{ numberTask }}</h3></div>
      <p v-if="type === 'taskbase'">#{{ taskId }}</p>
      <a v-if="writerName && type === 'taskbase'" :href="writerLink" class="text-green-500">{{ writerName }}</a>
      <p>Уровень: {{ difficulty }}</p>
    </div>
    <TitleView :text="text" />
    <img
      v-for="i in img"
      :key="i"
      :src="i"
      alt="img"
    >
    <table class="table-auto">
      <tbody>
      <tr
        v-for="row in table"
        :key="Number(row)"
      >
        <td
          class="border-solid border-2 border-black p-1 min-w-12"
          v-for="cell in row"
          :key="cell"
        >{{ cell }}</td>
      </tr>
      </tbody>
    </table>
    <div class="mt-3">
      <a
        class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all"
        v-for="item in files"
        :key="item.name"
        :href="'https://kompege.ru' + item.url"
      >
        {{ item.name }}
      </a>
    </div>
      <details v-if="type === 'taskbase'" class="p-4 [&_svg]:open:-rotate-180">
        <summary class="flex cursor-pointer list-none items-center gap-4">
            <svg class="rotate-0 transform text-green-500 transition-all duration-300" fill="none" height="20" width="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          <h3>Показать ответ</h3>
        </summary>
        <b>{{ otv }}</b>
      </details>
  </div>
</template>

<style scoped>
</style>
