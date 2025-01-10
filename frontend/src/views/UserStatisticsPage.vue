<script setup lang="ts">
import HeaderMain from '@/components/HeaderMain.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user.ts'

type resultType = {
  user: string,
  test: string,
  result: string[]
}

const route = useRoute();
const useStore = useUserStore()

const results = ref<Array<resultType>>([
  {
    "user": "student",
    "test": "Новый тест",
    "result": [
      "0",
      "0",
      "0",
      "1"
    ]
  }
])

onMounted(async () => {
  try {
    const { data } = await axios.get("/results/user/" + useStore.userToken + "/" + String(route.params.id));
    results.value = data
  } catch (err) {
    console.log(err);
  }
})
</script>

<template>
<div class="flex flex-col justify-center items-center w-full">
  <div class="mt-5 flex flex-col items-center w-full justify-center">
    <HeaderMain />
    <h3 class="mt-16 font-bold text-lg">Статистика по пользователю</h3>
    <div class="bg-white shadow-2xl rounded-2xl w-2/4 max-sm:w-full p-5 flex flex-col items-center justify-center">
      <div class="relative overflow-x-auto rounded-lg shadow-2xl mt-5 w-full">
        <table class="w-full text-sm text-left rtl:text-right">
          <thead class="text-xs text-white uppercase bg-green-500">
          <tr>
            <th scope="col" class="px-6 py-3">
              Пользователь
            </th>
            <th scope="col" class="px-6 py-3">
              Тест
            </th>
            <th scope="col" class="px-6 py-3">
              <span class="sr-only">Edit</span>
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
            >
              {{ result.test }}
            </th>
            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
              <div class="flex items-center justify-between">
                <div
                  v-for="item in result.result"
                  :key="item"
                >
                  <img v-if="item == '0'" src="/close_2.svg" alt="close" class="w-7 h-7" />
                  <img v-if="item != '0'" src="/checked.svg" alt="close" class="w-7 h-7" />
                </div>
              </div>
            </th>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>
