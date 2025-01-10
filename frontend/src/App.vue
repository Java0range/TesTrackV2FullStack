<script setup lang="ts">
import { RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user.ts'
import axios from 'axios'

const userStore = useUserStore()

onMounted(async () => {
  const localCart = localStorage.getItem("userToken");
  userStore.userToken = localCart ? JSON.parse(localCart) : [];
})

axios.defaults.baseURL = "http://82.148.30.194/api"
</script>

<template>
  <RouterView />
</template>
