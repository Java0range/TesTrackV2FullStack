<script setup lang="ts">
import Header from '@/components/HeaderMain.vue'
import { useRouter } from 'vue-router'

const router = useRouter();

const openPanel = () => {
  router.push('/teacher')
}
</script>

<template>
<div class="flex flex-col items-center w-full">
  <div class="mt-5 flex flex-col items-center w-full justify-center">
    <Header is-active="Главная"></Header>
    <div class="bg-white shadow-2xl flex p-5 rounded-3xl mt-40 gap-3 max-sm:flex-col w-1/2 max-sm:w-full md:w-3/4 xl:w-1/2">
      <img src="/favicon.ico" alt="logo" class="h-full w-full max-sm:h-12 max-sm:w-12 md:w-1/2" />
      <div>
        <h3 class="text-xl"><b>TesTrackV2 Beta</b> - это OpenSource Web приложение для проведения пробников ЕГЭ по информатике, нацеленное в первую очередь на повышение навыков для сдачи экзамена</h3>
        <button @click="openPanel" class="bg-green-500 hover:bg-green-400 text-white font-bold py-3 px-4 rounded-full transition-all mt-3 text-base">
          Панель учителя
        </button>
      </div>
    </div>
  </div>
</div>
</template>
