<template>
  <Nav :box="box" :back="true"/>
  <div class="padding main-container">
    <h1>Welches Fach möchtest du lernen?</h1>
    <div class="learn-container">
      <Nuxt-link :to="`/learn/${id}?tray=1`" class="fach fach-1"><h2 class="number">1</h2><p class="description">Neue Vokabeln lernen</p></Nuxt-link>
      <Nuxt-link :to="`/learn/${id}?tray=2`" class="fach fach-2"><h2 class="number">2</h2><p class="description">Üben und festigen</p></Nuxt-link>
      <Nuxt-link :to="`/learn/${id}?tray=3`" class="fach fach-3"><h2 class="number">3</h2><p class="description">Wiederholen für Vertiefung</p></Nuxt-link>
      <Nuxt-link :to="`/learn/${id}?tray=4`" class="fach fach-4"><h2 class="number">4</h2><p class="description">Sicher beherrscht</p></Nuxt-link>
    </div>
  </div>
</template>

<style lang="scss">
.main-container {
  display: flex;
  align-items: center;
  justify-content: center ;
  flex-direction: column;
  height: 100vh;
}

.learn-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.fach {
  background-color: #171717;
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

  .number {
    text-align: center;
    font-weight: 900;
    font-size: 4rem; 
    margin: 0;
  }

  .description {
    text-align: center;
    color: #7a7a7a;
  }
}

.fach-1 {
  .number {
    color: #ff4141;
  }
}

.fach-2 {
  .number {
    color: #ff7d41;
  }
}

.fach-3 {
  .number {
    color: #fcff41;
  }
}
.fach-4 {
  .number {
    color: #57ff41;
  }
}
</style>

<script setup>
const client = useSupabaseClient();
const { id } = useRoute().params;

const { data: box } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').eq('id', id)

  return data[0]
})

</script>