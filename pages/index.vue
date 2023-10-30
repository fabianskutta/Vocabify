<template>
    <br><br>
    <a @click="signOut()" class="btn">Logout</a>

    <div class="boxes">
            <BoxSnaek v-for="box of boxes" :box="box" :key="box.id"/>
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
const router = useRouter();

async function signOut() {
    const { error } = await client.auth.signOut();
    router.push("/login");
}

const { data: boxes } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').order('created_at')

  return data
})

console.log(boxes.value);
</script>