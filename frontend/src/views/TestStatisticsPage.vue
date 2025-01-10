<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useUserStore } from '@/stores/user.ts'
import HeaderMain from '@/components/HeaderMain.vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

type resultsType = {
  user: string,
  result: string[],
}

const route = useRoute();
const useStore = useUserStore()

const tasksId = ref<string[]>([]);

const results = ref<Array<resultsType>>([]);

onMounted(async () => {
  try {
    const { data } = await axios.get("/results/test/" + useStore.userToken + "/" + String(route.params.id));
    tasksId.value = data.slice(0, 1)[0]
    results.value = data.slice(1)
  } catch (err) {
    console.log(err);
  }
})
</script>

<template>
<div class="flex flex-col justify-center items-center w-full">
  <div class="mt-5 flex flex-col items-center w-full justify-center">
    <HeaderMain />
    <h3 class="mt-16 font-bold text-lg">Статистика по тесту:</h3>
    <div class="bg-white shadow-2xl rounded-2xl w-2/4 max-sm:w-full p-5 flex flex-col items-center justify-center">
      <div class="relative overflow-x-auto rounded-lg shadow-2xl mt-5 w-full">
        <table class="w-full text-sm text-left rtl:text-right">
          <thead class="text-xs text-white uppercase bg-green-500">
          <tr>
            <th scope="col" class="px-6 py-3">
              Пользователь
            </th>
            <th
              scope="col" class="px-6 py-3"
              v-for="task in tasksId"
              :key="Number(task)"
            >
              {{ task }}
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
            class="bg-white border-b hover:bg-gray-50"
            v-for="result in results"
            :key="result.user"
          >
            <th
              scope="row" class="px-6 py-4 font-medium whitespace-nowrap"
            >
              {{ result.user }}
            </th>
            <th
              scope="row" class="px-6 py-4 font-medium whitespace-nowrap"
              v-for="item in result.result"
              :key="item"
            >
              <img v-if="item == '0'" src="/close_2.svg" alt="close" class="w-7 h-7" />
              <img v-if="item != '0'" src="/checked.svg" alt="close" class="w-7 h-7" />
            </th>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>
