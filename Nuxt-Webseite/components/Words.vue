<template>
    {{ word.term }} - {{ word.definition }} <br>
</template>

<script setup lang="ts">
    defineProps<{word: Word;}>();
</script>