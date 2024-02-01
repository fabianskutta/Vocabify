<template>
    <Nav logout="true"/>
    <div class="padding">
        <br><br><br><br>
        <Nuxt-link @click="addBox()" class="btn">Sammlung erstellen</Nuxt-link>
    
        <div class="boxes">
                <BoxSnaek v-for="box of boxes" :box="box" :key="box.id"/>
        </div>
    
        <p v-if="!boxes[0]">Du hast noch keine Sammlung erstellt!</p>
    </div>
    </template>
    
    <style scoped>
    .boxes {
        margin-top: 2rem;
        display: flex;
        flex-wrap: wrap;
    }
    
    body {
        margin: 2rem;
    }
    </style>
    
    <script setup>
    const client = useSupabaseClient();
    const user = useSupabaseUser()
    const router = useRouter();
    
    const { data: boxes, refresh: refreshBoxes } = await useAsyncData('boxes', async () => {
      const { data } = await client.from('boxes').select('*').order('created_at')
    
      return data
    })
    
    async function addBox() {
        const { data, error } = await client.from('boxes').insert([
        { name: 'Neue Sammlung', user_id: user.value.id},
      ])
      .select()
      refreshBoxes();
    }
    </script>