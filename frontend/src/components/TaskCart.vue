<script setup lang="ts">
import TitleView from '@/components/TitleView.vue'
import { ref } from 'vue'

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
const viewOtv = ref<boolean>(false);
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
        :key="row"
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
    <button v-if="type === 'taskbase'" @click="viewOtv = !viewOtv" class="mt-3 bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
      {{ viewOtv ? otv : "Показать ответ" }}
    </button>
  </div>
</template>

<style scoped>
</style>
