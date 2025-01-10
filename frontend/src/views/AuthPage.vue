<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const router = useRouter();

const useStore = useUserStore()

const username = ref<string>("")
const password = ref<string>("")

const errorWindowActive = ref<boolean>(false);
const errorTitle = ref<string>("")

const auth = async () => {
  try {
    const json = {
      username: username.value,
      password: password.value
    }
    const { data } = await axios.post("/users/auth/", json);
    if (typeof data === "string") {
      errorTitle.value = data;
      errorWindowActive.value = true;
    } else {
      useStore.userToken = data.token
      localStorage.setItem("userToken", JSON.stringify(data.token));
      router.push("/")
    }
  } catch (err) {
    console.log(err);
  }
}
</script>

<template>
<div class="min-h-screen bg-no-repeat bg-bottom bg-[url('/wave.svg')]"></div>
<div class="fixed top-0 left-0 flex items-center gap-2 px-3 py-1">
  <img src="/favicon.ico" alt="icon" class="h-16" />
  <b class="text-lg">TesTrackV2</b>
</div>
<div class="h-96 w-1/3 bg-white fixed left-1/2 -translate-x-1/2 top-52 rounded-2xl p-10 flex flex-col items-center justify-center shadow-2xl max-xl:w-2/4 max-md:w-3/4 max-sm:w-full">
  <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="mb-2 min-h-12">
    <circle cx="12" cy="9" r="3" stroke="#22c55e" stroke-width="1.5"/>
    <circle cx="12" cy="12" r="10" stroke="#22c55e" stroke-width="1.5"/>
    <path d="M17.9691 20C17.81 17.1085 16.9247 15 11.9999 15C7.07521 15 6.18991 17.1085 6.03076 20" stroke="#22c55e" stroke-width="1.5" stroke-linecap="round"/>
  </svg>
  <b class="text-lg mb-3">Войдите в ваш аккаунт</b>
  <div v-if="errorWindowActive" class="mb-6 flex items-center gap-2 p-3 rounded-lg border-solid border-red-400 border-2 bg-red-100">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#991b1b" class="size-6">
      <path stroke-linecap="round" stroke-linejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
    </svg>
    <p class="text-red-800">{{ errorTitle }}</p>
  </div>
  <div class="relative z-0 w-3/4 mb-5 group">
    <input v-model="username" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
    <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Логин</label>
  </div>
  <div class="relative z-0 w-3/4 mb-8 group">
    <input v-model="password" type="password" name="floating_password" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
    <label for="floating_password" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Пароль</label>
  </div>
  <button @click="auth" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
    Вход
  </button>
</div>
</template>
