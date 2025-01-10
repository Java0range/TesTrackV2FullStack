<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user.ts'


const props = defineProps<{
  drawerClose: () => void;
  updateTests: () => void;
}>();

const useStore = useUserStore()

const testName = ref<string>("")

const tasks = ref<Array<string>>([])

const taskInput = ref<string>("")

const createTask = () => {
  tasks.value.push(taskInput.value)
}

const deleteTask = (task:string) => {
  tasks.value.splice(tasks.value.indexOf(task), 1)
}

const createTest = async () => {
  const json = {
    "name": testName.value,
    "taskIdList": tasks.value,
    "token": useStore.userToken
  }
  try {
    await axios.post("/tests/create", json);
    props.updateTests();
    props.drawerClose();
  } catch (err) {
    console.log(err);
  }
}

</script>

<template>
<div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
<div class="fixed left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 bg-white w-96 z-20 p-8 rounded-2xl">
  <img @click="props.drawerClose" src="/close_2.svg" alt="Close" class="absolute top-4 left-full -translate-x-12 cursor-pointer opacity-60 hover:opacity-100 transition-all" />
  <div class="flex flex-col justify-center items-center">
    <h3 class="font-bold text-lg">Создание теста</h3>
    <div class="relative z-0 mb-5 group mt-5 w-3/4">
      <input v-model="testName" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
      <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Имя теста</label>
    </div>
    <div class="flex justify-center items-center gap-2 w-full">
      <div class="relative z-0 mb-5 group mt-5 w-full">
        <input v-model="taskInput" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
        <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Номер задания</label>
      </div>
      <img @click="createTask" src="/plus.svg" alt="plus" class="h-7 w-7 opacity-70 hover:opacity-100 cursor-pointer transition-all" />
    </div>
    <div
      class="flex flex-col justify-center items-center w-full"
      v-for="task in tasks"
      :key="task"
    >
      <div class="mt-2 flex justify-between items-center gap-2 w-full border-solid border-2 border-gray-300 p-1 rounded-lg">
        <p>{{ task }}</p>
        <img @click="deleteTask(task)" src="/delete.png" alt="delete" class="h-6 w-6 opacity-60 hover:opacity-100 cursor-pointer transition-all" />
      </div>
    </div>
    <button @click="createTest" class="mt-2 border-solid border-2 border-green-500 bg-green-500 hover:bg-green-400 text-white font-bold p-2 rounded-2xl transition-all">
      Создать
    </button>
  </div>
</div>
</template>
