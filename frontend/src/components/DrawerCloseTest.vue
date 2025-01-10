<script setup lang="ts">
defineProps<{
  closeClicked: () => void;
  closeTestClicked: () => void;
  saveButtonActive: boolean;
}>()
</script>

<template>
<div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
<div class="fixed left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 bg-white w-96 z-20 p-8 rounded-2xl">
  <div>
    <h3>Вы уверены что хотите завершить тест?</h3>
    <div class="flex justify-center items-center mt-3 gap-5">
      <button @click="closeClicked" class="bg-white border-dashed border-2 border-green-500 hover:border-green-400 text-green-500 min-w-20 font-bold py-2 px-4 rounded-full transition-all">
        Нет
      </button>
      <button :disabled="!saveButtonActive" @click="closeTestClicked" class="hover:bg-green-400 hover:border-green-400 border-solid border-2 border-green-500 bg-green-500 text-white min-w-20 font-bold py-2 px-2 rounded-full transition-all disabled:bg-slate-400 disabled:border-slate-400">
        Да
      </button>
    </div>
  </div>
</div>
</template>
