<script setup lang="ts">
import { RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user.ts'
import axios from 'axios'

const userStore = useUserStore()

onMounted(async () => {
  const localCart = localStorage.getItem("userToken");
  userStore.userToken = localCart ? JSON.parse(localCart) : "";
})

axios.defaults.baseURL = "http://127.0.0.1:8000";
</script>

<template>
  <RouterView />
</template>
