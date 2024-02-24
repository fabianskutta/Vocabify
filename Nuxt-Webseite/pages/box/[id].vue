<template>
   <Nav :box="box" :home="true"/>
<div class="padding">
  <br><br><br><br>
<Nuxt-link :to="`/box-edit/${id}`" class="btn">Bearbeiten</Nuxt-link> <Nuxt-link :to="`/learn/${id}`" class="btn">Lernen</Nuxt-link>
<h1>{{ box.name }}</h1>


<Words v-for="word of words" :word="word" :key="word.id"/>
</div>
</template>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #ffffff17;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #171717;
}
</style>

<script setup>
const client = useSupabaseClient();
const { id } = useRoute().params;

const { data: box } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').eq('id', id)

  return data[0]
})

const { data: words } = await useAsyncData('words', async () => {
  const { data } = await client.from('words').select('*').eq('box_id', id)

  return data
})
</script>