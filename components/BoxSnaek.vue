<template>
    <nuxt-link :to="`/box/${box.id}`" class="box-sneak">
        <div class="box-container">
            <h3>{{ box.name }}</h3>
        </div>
    </nuxt-link>
</template>

<script setup lang="ts">
    defineProps<{box: Box;}>();
</script>

<style lang="scss">
.box-sneak {
    padding: 1rem;
    margin: 0.25rem;
    color: #fff;
    text-decoration: none;
    background: #171717;
    border-radius: 4px;
    }
</style>