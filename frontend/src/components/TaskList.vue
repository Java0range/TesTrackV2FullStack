<script setup lang="ts">
import TaskCart from '@/components/TaskCart.vue'

type filesType = {
  url: string,
  name: string,
  user_id: string
}

type itemsType = {
  task_id: number,
  difficulty: string,
  number_task: number,
  files: Array<filesType>,
  img: Array<string>,
  otv: string,
  text: string,
  writer_link: string,
  writer_name: string,
  table: Array<string[]>
}

defineProps({
  items: Array<itemsType>,
})
</script>

<template>
<div class="flex flex-col justify-center items-center gap-5 max-w-full">
  <TaskCart
    v-for="item in items"
    :key="item.task_id"
    :difficulty="item.difficulty"
    :number-task="item.number_task"
    :img="item.img"
    :task-id="item.task_id"
    :text="item.text"
    :writer-link="item.writer_link"
    :writer-name="item.writer_name"
    :table="item.table"
    :files="item.files"
    :otv="item.otv"
    type="taskbase"
  />
</div>
</template>
