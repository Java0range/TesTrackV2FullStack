<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import Header from '@/components/HeaderMain.vue'
import SearchAllTasks from '@/components/SearchAllTasks.vue'
import SearchTask from '@/components/SearchTask.vue'
import TaskList from '@/components/TaskList.vue'

type filesType = {
  url: string,
  name: string,
  user_id: string
}

type itemsType = {
  task_id: number,
  difficulty: string,
  number_task: number,
  files: Array<filesType>,
  img: Array<string>,
  otv: string,
  text: string,
  writer_link: string,
  writer_name: string,
  table: Array<string[]>
}

const slider = ref<boolean>(true);

const sliderNext = () => {
  slider.value = false
}
const sliderBack = () => {
  slider.value = true
}

const selectedNumber = ref<string>("1")

const items = ref<Array<itemsType>>([])

const onChangeNumber = (selected: string) => {
  selectedNumber.value = selected;
}

const searchTasks = async () => {
  try {
    const { data } = await axios.get("/taskbase/tasks/" + selectedNumber.value);
    items.value = data;
  } catch (err) {
    console.log(err);
  }
}

const changeTasks = (tasks: Array<itemsType>) => {
  items.value = tasks;
}
</script>

<template>
<div class="flex flex-col justify-center items-center w-full">
  <div class="mt-5 flex flex-col items-center w-full justify-center">
    <Header is-active="База Заданий"></Header>
    <div class="flex gap-2 mt-5">
      <button @click="sliderBack" :class="slider ? 'bg-green-500 text-white' : 'bg-white'" class="p-3 rounded-2xl hover:opacity-70 border-dashed border-2 border-green-500 transition-all">По типу задания</button>
      <button @click="sliderNext" :class="slider ? 'bg-white' : 'bg-green-500 text-white'" class="p-3 rounded-2xl hover:opacity-70 border-dashed border-2 border-green-500 transition-all">По номеру задания</button>
    </div>
    <div class="shadow-2xl p-7 rounded-2xl mt-5 w-1/3 max-sm:w-full">
      <SearchAllTasks v-if="slider" @search-task-clicked="searchTasks" @on-change-number="onChangeNumber" />
      <SearchTask v-if="!slider" @change-tasks="changeTasks" />
    </div>
    <div class="overflow-hidden z-10 float-left">
      <TaskList :items="items" />
    </div>
  </div>
</div>
</template>
