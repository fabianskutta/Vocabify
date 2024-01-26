<template>
  <div>
    <NuxtPage/>
  </div>
</template>

<script setup>
    useHead({
  titleTemplate: () => `Vocabify`,
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  script: [
    {
      src: 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js',
      type: "text/javascript",
      async: true,
    },
  ],
});
  </script>