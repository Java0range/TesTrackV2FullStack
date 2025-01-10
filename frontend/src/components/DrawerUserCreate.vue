<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user.ts'

const isAdmin = ref(false)

const userStore = useUserStore()

const props = defineProps<{
  drawerClose: () => void;
  usersUpdate: () => void;
}>();

const username = ref<string>("")
const password = ref<string>("")

const CreateUser = async () => {
  try {
    const json = {
      "username": username.value,
      "password": password.value,
      "is_admin": isAdmin.value,
      "token": userStore.userToken
    }
    await axios.post("/users/create", json);
    props.usersUpdate();
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
    <h3 class="font-bold text-lg">Создание пользователя</h3>
    <div class="relative z-0 mb-5 group mt-5 w-3/4">
      <input v-model="username" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
      <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Логин</label>
    </div>
    <div class="relative z-0 mb-8 group w-3/4">
      <input v-model="password" type="password" name="floating_password" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
      <label for="floating_password" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Пароль</label>
    </div>
    <div class="flex justify-between items-center w-full">
      <button @click="isAdmin = !isAdmin" :class="isAdmin ? 'bg-green-500 text-white' : 'bg-white'" class="p-2 rounded-2xl hover:opacity-70 border-dashed border-2 border-green-500 transition-all">
        Админ
      </button><button @click="CreateUser" class="border-solid border-2 border-green-500 bg-green-500 hover:bg-green-400 text-white font-bold p-2 rounded-2xl transition-all">
        Создать
      </button>
    </div>
  </div>
</div>
</template>
