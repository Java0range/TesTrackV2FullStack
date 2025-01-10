<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { useRouter } from 'vue-router';

defineProps({
  isActive: String
})

const router = useRouter();

const useStore = useUserStore()

const quit = () => {
  useStore.userToken = ''
  localStorage.setItem("userToken", JSON.stringify(""));
  router.push('/auth')
}
</script>

<template>
  <div class="w-3/4 max-sm:w-full flex justify-between items-center">
    <div class="flex items-center">
      <img src="/favicon.ico" alt="logo" class="w-8 h-8" />
      <b>TesTrackV2 Beta</b>
    </div>
    <div class="flex max-sm:flex-col items-center gap-3 uppercase opacity-70 text-base">
      <router-link to="/tests" class="hover:opacity-100 cursor-pointer hover:font-medium transition-all" :class="isActive === 'Тесты' ? 'font-bold' : ''">Тесты</router-link>
      <router-link to="/" class="hover:opacity-100 cursor-pointer hover:font-medium transition-all" :class="isActive === 'Главная' ? 'font-bold' : ''">Главная</router-link>
      <router-link to="/tasks" class="hover:opacity-100 cursor-pointer hover:font-medium transition-all" :class="isActive === 'База Заданий' ? 'font-bold' : ''">База Заданий</router-link>
    </div>
    <div>
      <button @click="quit" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
        Выход
      </button>
    </div>
  </div>
</template>
