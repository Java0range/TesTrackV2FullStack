<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted, ref, watch } from 'vue'
import { useUserStore } from '@/stores/user.ts'
import TaskCart from '@/components/TaskCart.vue'
import axios from 'axios'
import DrawerCloseTest from '@/components/DrawerCloseTest.vue'

type filesType = {
  url: string,
  name: string,
  user_id: string
};

type activeTestType = {
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
};

const route = useRoute();
const useStore = useUserStore();

type testType = [number, string, string[]] | [];

const test = ref<testType>([]);

const otv = ref<string[]>([]);

const otvInput = ref<string>("");

const activeTestId = ref<string>("");

const activeTest = ref<activeTestType>({
  task_id: 0,
  difficulty: "",
  number_task: 0,
  files: [],
  img: [],
  otv: "",
  text: "",
  writer_link: "",
  writer_name: "",
  table: []
});

const resultsListActive = ref<boolean>(false);

const resultsList = ref<Array<string>>([]);

const drawerActive = ref<boolean>(false);

const saveButtonActive = ref<boolean>(true);

const openDrawer = () => {
  drawerActive.value = true
}

const closeDrawer = () => {
  drawerActive.value = false
}

const closeTest = async () => {
  saveButtonActive.value = false;
  const json = {
    test_id: test.value[0],
    result: otv.value,
    token: useStore.userToken
  }
  try {
    const { data } = await axios.post("/results/save", json);
    drawerActive.value = false;
    resultsList.value = data;
    resultsListActive.value = true;
  } catch (err) {
    console.log(err);
  }
}

onMounted(async () => {
  try {
    const { data } = await axios.get("/tests/testForUser/" + useStore.userToken + "/" + String(route.params.id));
    test.value = data;
  } catch (err) {
    console.log(err);
  }
  activeTestId.value = test.value[2][0];
  for (let i = 0; i < test.value[2].length; i++) {
    otv.value.push("")
  }
  try {
    const { data } = await axios.get("/taskbase/task/" + activeTestId.value);
    activeTest.value = data[0];
  } catch (err) {
    console.log(err);
  }
})

watch(activeTestId, async () => {
  try {
    const { data } = await axios.get("/taskbase/task/" + activeTestId.value);
    activeTest.value = data[0];
  } catch (err) {
    console.log(err);
  }
})
</script>

<template>
<DrawerCloseTest v-if="drawerActive" :close-clicked="closeDrawer" :close-test-clicked="closeTest" :save-button-active="saveButtonActive" />
<div class="flex flex-col justify-center items-center w-full">
  <div v-if="resultsListActive" class="mt-5 flex flex-col items-center w-2/4 max-sm:w-full justify-center">
    <div class="bg-white shadow-2xl rounded-lg flex flex-col items-center justify-center p-5">
      <h3>Результаты:</h3>
      <div class="relative overflow-x-auto rounded-lg shadow-2xl mt-5 w-full">
        <table class="w-full text-sm text-left rtl:text-right">
          <thead class="text-xs text-white uppercase bg-green-500">
          <tr>
            <th scope="col" class="px-6 py-3">
              Номер
            </th>
            <th scope="col" class="px-6 py-3">
              Результат
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
            class="bg-white border-b hover:bg-gray-50"
            v-for="i in resultsList.length"
            :key="resultsList[i - 1]"
          >
            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
              {{ i }}
            </th>
            <td class="px-6 py-4 text-right">
              <img v-if="resultsList[i - 1] == '0'" src="/close_2.svg" alt="close" class="w-6 h-6" />
              <img v-if="resultsList[i - 1] != '0'" src="/checked.svg" alt="close" class="w-6 h-6" />
            </td>
          </tr>
          </tbody>
        </table>
      </div>
      <router-link to="/tests"><button class="mt-5 bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
        Выйти
      </button></router-link>
    </div>
  </div>
  <div v-if="!resultsListActive" class="mt-5 flex flex-col items-center w-2/4 max-sm:w-full justify-center">
    <div class="grid grid-cols-8 gap-3">
      <div
        class="p-3 flex cursor-pointer justify-center items-center border-solid border-2 border-gray-300 rounded-lg h-9 w-9 shadow-xl hover:-translate-y-2 transition-all"
        v-for="task in test[2]"
        :key="test[2].indexOf(task)"
        @click="activeTestId = task"
        :class="otv[test[2].indexOf(task)] == '' ? 'border-gray-300' : 'border-green-500 shadow-lg shadow-green-500'"
      >
        <p>{{ test[2].indexOf(task) + 1 }}</p>
      </div>
    </div>
    <div class="mt-5 flex flex-col items-center justify-center bg-white p-3 rounded-xl shadow-2xl">
      <div class="flex flex-col items-center justify-center">
        <TaskCart
          :difficulty="activeTest.difficulty"
          :number-task="activeTest.number_task"
          :img="activeTest.img"
          :task-id="activeTest.task_id"
          :text="activeTest.text"
          :writer-link="activeTest.writer_link"
          :writer-name="activeTest.writer_name"
          :table="activeTest.table"
          :files="activeTest.files"
          :otv="activeTest.otv"
        />
        <div class="relative z-0 w-3/4 mb-5 mt-7 group">
          <input v-model="otvInput" type="text" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-green-500 peer" placeholder=" " required />
          <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-green-500 peer-focus:dark:text-green-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Ваш ответ</label>
        </div>
        <div class="flex items-center justify-center gap-9">
          <button @click="otv[test[2].indexOf(activeTestId)] = otvInput" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
            Сохранить
          </button>
          <button @click="openDrawer" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
            Завершить
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
