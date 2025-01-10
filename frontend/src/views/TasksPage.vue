<script setup lang="ts">
import { provide, ref } from 'vue'
import axios from 'axios'
import Header from '@/components/HeaderMain.vue'
import SearchAllTasks from '@/components/SearchAllTasks.vue'
import SearchTask from '@/components/SearchTask.vue'
import TaskList from '@/components/TaskList.vue'

const slider = ref<boolean>(true);

const sliderNext = () => {
  slider.value = false
}
const sliderBack = () => {
  slider.value = true
}

const selectedNumber = ref<string>("1")

const items = ref<Array<any>>([])

const onChangeNumber = (event) => {
  selectedNumber.value = event.target.value
}

const searchTasks = async () => {
  try {
    const { data } = await axios.get("/taskbase/tasks/" + selectedNumber.value);
    items.value = data;
  } catch (err) {
    console.log(err);
  }
}
provide("tasksbase", {
  items
});
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
      <SearchAllTasks v-if="slider" :search-task-clicked="searchTasks" :on-change-number="onChangeNumber" />
      <SearchTask v-if="!slider" />
    </div>
    <div class="overflow-hidden z-10 float-left">
      <TaskList :items="items" />
    </div>
  </div>
</div>
</template>
