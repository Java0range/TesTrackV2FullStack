<template>
  <div>
    <div v-html="renderedContent" class="text-lg"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const props = defineProps({
  text: {
    type: String,
    required: true,
  },
});

const renderedContent = ref('');

watch(
  () => props.text,
  (newText) => {
    try {
      // Заменяем LaTeX выражения на отрендеренные HTML
      const latexRegex = /\\\((.*?)\\\)/g; // Регулярное выражение для поиска LaTeX
      const renderedText = newText.replace(latexRegex, (_, latex) => {
        return katex.renderToString(latex, {
          throwOnError: false,
        });
      });
      renderedContent.value = renderedText;
    } catch (error) {
      console.error('Error rendering LaTeX:', error);
      renderedContent.value = 'Ошибка при рендеринге выражения';
    }
  },
  { immediate: true }
);
</script>
