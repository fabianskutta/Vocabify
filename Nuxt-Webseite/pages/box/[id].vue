<template>
  <!-- Navigationsleiste mit Zurück-Schaltfläche zur Startseite -->
  <Nav :box="box" btn="home"/>
  <!-- Platzhalter für den Abstand oben -->
  <div class="nav-dummy"></div>
  <!-- Bereich mit Innenabstand -->
  <div class="padding">
    <!-- Schaltflächen zum Bearbeiten und Lernen der Box -->
    <Nuxt-link :to="`/box-edit/${id}`" class="btn">Bearbeiten</Nuxt-link> <Nuxt-link :to="`/learn/${id}`" class="btn">Lernen</Nuxt-link>
    <!-- Titel der Box -->
    <h1>{{ box.name }}</h1>
     <!-- Liste der Wörter -->
    <Words v-for="word of words" :word="word" :key="word.id"/>
  </div>
</template>

<style>
/* Titel der Box */
h1 {
  color: var(--text1);
}
</style>

<script setup>
// Importieren der Supabase-Funktionen und Nutzung des Routings
const client = useSupabaseClient();
const { id } = useRoute().params;

// Abrufen der Daten für die aktuelle Box und die zugehörigen Wörter
const { data: box } = await useAsyncData('boxes', async () => {
    const { data } = await client.from('boxes').select('*').eq('id', id)
    return data[0]
})

const { data: words } = await useAsyncData('words', async () => {
    const { data } = await client.from('words').select('*').eq('box_id', id)
    return data
})
</script>