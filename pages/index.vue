<template>
<div class="padding">
    <img class="logo2" src="/Vocabify.png" alt="">
    <br><br>
    <Nuxt-link @click="signOut()" class="btn">Logout</Nuxt-link> <Nuxt-link @click="addBox()" class="btn">Box erstellen</Nuxt-link>

    <div class="boxes">
            <BoxSnaek v-for="box of boxes" :box="box" :key="box.id"/>
    </div>

    <p v-if="!boxes[0]">Du hast noch keine Boxen erstellt!</p>
</div>
</template>

<style scoped>
.boxes {
    display: flex;
    margin-top: 2rem;
}

body {
    margin: 2rem;
}
</style>

<script setup>
const client = useSupabaseClient();
const user = useSupabaseUser()
const router = useRouter();

async function signOut() {
    const { error } = await client.auth.signOut();
    router.push("/login");
}

const { data: boxes, refresh: refreshBoxes } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').order('created_at')

  return data
})

async function addBox() {
    const { data, error } = await client.from('boxes').insert([
    { name: 'New Box', user_id: user.value.id},
  ])
  .select()
  refreshBoxes();
}
</script>