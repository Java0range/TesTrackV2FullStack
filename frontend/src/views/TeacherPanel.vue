<script setup lang="ts">
import Header from '@/components/HeaderMain.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user.ts'
import DrawerUserCreate from '@/components/DrawerUserCreate.vue'
import DrawerTestCreate from '@/components/DrawerTestCreate.vue'

const useStore = useUserStore()

const slider = ref<boolean>(true);

const sliderNext = () => {
  slider.value = false
}
const sliderBack = () => {
  slider.value = true
}

const tests = ref([])

const users = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get("/tests/tests/" + useStore.userToken);
    tests.value = data;
  } catch (err) {
    console.log(err);
  }
  try {
    const { data } = await axios.get("/users/users/" + useStore.userToken);
    users.value = data;
  } catch (err) {
    console.log(err);
  }
})

const updateUsers = async () => {
  try {
    const { data } = await axios.get("/users/users/" + useStore.userToken);
    users.value = data;
  } catch (err) {
    console.log(err);
  }
}

const updateTests = async () => {
  try {
    const { data } = await axios.get("/tests/tests/" + useStore.userToken);
    tests.value = data;
  } catch (err) {
    console.log(err);
  }
}

const deleteUser = async (id:number) => {
  const json = {
    "id": id,
    "token": useStore.userToken
  }
  try {
    await axios.delete("/users/delete", {
      headers: {},
      data: json
    });
    updateUsers();
  } catch (err) {
    console.log(err);
  }
}

const deleteTest = async (id:number) => {
  const json = {
    "id": id,
    "token": useStore.userToken
  }
  try {
    await axios.delete("/tests/delete", {
      headers: {},
      data: json
    });
    updateTests();
  } catch (err) {
    console.log(err);
  }
}

const drawerTestCreateWindow = ref<boolean>(false)

const drawerTestCreateWindowClose = () => {
  drawerTestCreateWindow.value = false
}

const drawerUserCreateWindow = ref<boolean>(false)

const drawerUserCreateClose = () => {
  drawerUserCreateWindow.value = false
}
</script>

<template>
<DrawerTestCreate v-if="drawerTestCreateWindow" :drawer-close="drawerTestCreateWindowClose" :update-tests="updateTests"/>
<DrawerUserCreate v-if="drawerUserCreateWindow" :drawer-close="drawerUserCreateClose" :users-update="updateUsers" />
<div class="mt-5 flex flex-col items-center w-full justify-center">
  <Header></Header>
  <div class="shadow-2xl p-7 rounded-2xl mt-16 w-1/2 max-sm:w-full bg-white">
    <div class="flex items-center justify-between w-full">
      <h3 class="font-bold text-lg">Панель Учителя</h3>
      <button @click="slider ? drawerUserCreateWindow = true : drawerTestCreateWindow = true" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
        Создать
      </button>
    </div>
    <div class="flex gap-2 mt-5 justify-center items-center w-full">
      <button @click="sliderBack" :class="slider ? 'bg-green-500 text-white' : 'bg-white'" class="min-w-40 p-3 rounded-2xl hover:opacity-70 border-dashed border-2 border-green-500 transition-all">Пользователи</button>
      <button @click="sliderNext" :class="slider ? 'bg-white' : 'bg-green-500 text-white'" class="min-w-40 p-3 rounded-2xl hover:opacity-70 border-dashed border-2 border-green-500 transition-all">Тесты</button>
    </div>
    <div v-if="!slider" class="relative overflow-x-auto rounded-lg shadow-2xl mt-5">
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
              <router-link :to="'/statistics/test/' + item[0]"><img src="/checked.svg" alt="checked" class="h-6 w-6 opacity-60 hover:opacity-100 cursor-pointer transition-all"></router-link>
              <img @click="deleteTest(item[0])" src="/delete.png" alt="delete" class="h-6 w-6 opacity-60 hover:opacity-100 cursor-pointer transition-all">
            </div>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div v-if="slider" class="relative overflow-x-auto rounded-lg shadow-2xl mt-5">
      <table class="w-full text-sm text-left rtl:text-right">
        <thead class="text-xs text-white uppercase bg-green-500">
        <tr>
          <th scope="col" class="px-6 py-3">
            Имя
          </th>
          <th scope="col" class="px-6 py-3">
            Админ
          </th>
          <th scope="col" class="px-6 py-3">
            <span class="sr-only">Edit</span>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr
          class="bg-white border-b hover:bg-gray-50"
          v-for="item in users"
          :key="item[0]"
        >
          <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
            {{ item[1] }}
          </th>
          <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
            <img v-if="item[2] === 0" src="/close.svg" alt="not" class="h-6 w-6">
            <img v-if="item[2] === 1" src="/check.svg" alt="yes" class="h-6 w-6">
          </th>
          <td class="px-6 py-4 text-right">
            <div class="flex items-center justify-center gap-2">
              <router-link :to="'/statistics/user/' + item[0]"><img src="/checked.svg" alt="checked" class="h-6 w-6 opacity-60 hover:opacity-100 cursor-pointer transition-all"></router-link>
              <img @click="deleteUser(item[0])" src="/delete.png" alt="delete" class="h-6 w-6 opacity-60 hover:opacity-100 cursor-pointer transition-all">
            </div>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>
