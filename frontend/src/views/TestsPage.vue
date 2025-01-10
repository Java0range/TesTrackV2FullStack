<script setup lang="ts">
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user.ts'
import Header from '@/components/HeaderMain.vue'

const useStore = useUserStore()

const tests = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get("/tests/testsForUser/" + useStore.userToken);
    tests.value = data;
  } catch (err) {
    console.log(err);
  }
})
</script>

<template>
<div class="flex flex-col justify-center items-center w-full">
  <div class="mt-5 flex flex-col items-center w-full justify-center">
    <Header is-active="Тесты"></Header>
    <div class="bg-white mt-16 shadow-2xl rounded-2xl w-2/4 max-sm:w-full p-5 flex flex-col items-center justify-center">
      <h3>Доступные тесты:</h3>
      <div v-if="tests.length == 0" class="flex flex-col items-center justify-center w-full">
        <h3 class="mt-5 font-bold text-lg">К сожалению у вас нет доступных тестов</h3>
        <img src="/emoji-2.png" alt="emoji" class="mt-1 w-20" />
      </div>
      <div v-if="tests.length != 0" class="relative overflow-x-auto rounded-lg shadow-2xl mt-5 w-full">
        <table class="w-full text-sm text-left rtl:text-right">
          <thead class="text-xs text-white uppercase bg-green-500">
          <tr>
            <th scope="col" class="px-6 py-3">
              Название
            </th>
            <th scope="col" class="px-6 py-3">
              <span class="sr-only">Edit</span>
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
            class="bg-white border-b hover:bg-gray-50"
            v-for="item in tests"
            :key="item[0]"
          >
            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
              {{ item[1] }}
            </th>
            <td class="px-6 py-4 text-right">
              <div class="flex items-center justify-center gap-2">
                <router-link :to="'/test/'  + item[0]"><img src="/checked.svg" alt="checked" class="h-8 w-8 opacity-60 hover:opacity-100 cursor-pointer transition-all"></router-link>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>
