<script setup lang="ts">
defineProps({
  searchTaskClicked: Function,
  onChangeNumber: Function
})
</script>

<template>
<div class="flex gap-5 max-sm:flex-col">
  <div class="flex items-center justify-center gap-2">
    <h3>Тип:</h3>
    <select @change="onChangeNumber" class="px-3 py-2 border rounded-md outline-none w-full">
      <option value="1">1. Анализ информационных моделей</option>
      <option value="2">2. Таблицы истинности логических выражений</option>
      <option value="3">3. Поиск и сортировка в базах данных</option>
      <option value="4">4. Кодирование и декодирование данных. Условие Фано</option>
      <option value="5">5. Анализ алгоритмов для исполнителей</option>
      <option value="6">6. Циклические алгоритмы для Исполнителя</option>
      <option value="7">7. Кодирование графической и звуковой информации</option>
      <option value="8">8. Комбинаторика</option>
      <option value="9">9. Обработка числовой информации в электронных таблицах</option>
      <option value="10">10. Поиск слова в текстовом документе</option>
      <option value="11">11. Вычисление количества информации</option>
      <option value="12">12. Алгоритмы для исполнителей с циклами и ветвлениями</option>
      <option value="13">13. IP адреса и маски</option>
      <option value="14">14. Позиционные системы счисления</option>
      <option value="15">15. Истинность логического выражения</option>
      <option value="16">16. Вычисление значения рекурсивной функции</option>
      <option value="17">17. Обработка целочисленных данных. Проверка делимости</option>
      <option value="18">18. Динамическое программирование в электронных таблицах</option>
      <option value="19">19-21. Теория игр</option>
      <option value="22">22. Многопоточные вычисления</option>
      <option value="23">23. Динамическое программирование (количество программ)</option>
      <option value="24">24. Обработка символьных строк</option>
      <option value="25">25. Обработка целочисленных данных. Поиск делителей</option>
      <option value="26">26. Обработка данных с помощью сортировки</option>
      <option value="27">27. Анализ данных</option>
    </select>
  </div>
  <div class="flex items-center justify-center gap-2">
    <h3>Сложность:</h3>
    <select class="px-3 py-2 border rounded-md outline-none">
      <option value="name">Сначала новые</option>
      <option value="price">Сначала старые</option>
      <option value="-price">Сначала простые</option>
      <option value="-price">Сначала сложные</option>
    </select>
  </div>
</div>
<div class="flex items-center justify-center mt-2">
  <button @click="searchTaskClicked" class="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 rounded-full transition-all">
    Найти все задачи
  </button>
</div>
</template>
