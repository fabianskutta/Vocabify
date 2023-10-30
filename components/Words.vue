<template>
<div class="words-container">

</div>


{{ word.term }}
{{ word.definition }}
</template>

<script setup lang="ts">
defineProps<{word: Word;}>();
</script>