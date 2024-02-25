<template>
    <!-- Verlinkung zur Box-Seite -->
    <nuxt-link :to="`/box/${box.id}`" class="box-sneak">
        <!-- Container für die Box -->
        <div class="box-container">
            <!-- Titel der Box -->
            <h3>{{ box.name }}</h3>
        </div>
    </nuxt-link>
</template>

<script setup lang="ts">
    // Definiert die Eigenschaften des Komponentenprops
    defineProps<{box: Box;}>();
</script>

<style lang="scss">

/* "box-sneak" */
.box-sneak {
    background-color: var(--input);
    display: flex;
    width: 300px;
    padding: 1.5rem;
    justify-content: center;
    flex-direction: column;
    border-color: #ffffff17;
    border-style: solid;
    border-width: 1px;
    border-radius: 20px;
    margin: 1.5rem;
    text-decoration: none;

    /* Box Titel */
    h3 {
    font-weight: 800;
    font-size: 1.5rem; 
    margin: 0;
    color: var(--text1);
    text-align: center;
  }
    }
</style>