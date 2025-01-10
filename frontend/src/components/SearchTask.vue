<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'

const emits = defineEmits(["changeTasks"])

const taskId = ref<string>('')

const searchTask = async () => {
  try {
    const { data } = await axios.get("/taskbase/task/" + taskId.value);
    emits("changeTasks", data)
  } catch (err) {
    console.log(err);
  }
}

</script>

<template>
<div class="flex flex-col items-center">
  <div class="relative z-0 w-3/4 mb-5 group">
    <input v-model="taskId" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
    <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Номер задачи</label>
  </div>
  <button @click="searchTask" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
    Показать задачу
  </button>
</div>
</template>
