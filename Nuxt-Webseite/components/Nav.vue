<template>
    <nav id="nav">
        <div v-if="$colorMode.value == 'light'" id="logo"><img src="/Vocabify-w.png" alt=""></div>
        <div v-if="$colorMode.value !== 'light'" id="logo"><img src="/Vocabify.png" alt=""></div>
        <div v-if="box"><h3>{{ box.name }}</h3></div>
        <div><Nuxt-link v-if="logout" @click="signOut()" class="btn">Logout</Nuxt-link><Nuxt-link v-if="back" :to="`/box/${box.id}`" class="btn">Zurück</Nuxt-link><Nuxt-link v-if="home" :to="`/`" class="btn">Zurück</Nuxt-link></div>
    </nav>
</template>

<script setup lang="ts">
defineProps<{box: Box; back:Back; home:Home; logout:Logout;}>();

const client = useSupabaseClient();
const user = useSupabaseUser()
const router = useRouter();
    
async function signOut() {
    const { error } = await client.auth.signOut();
    router.push("/login");
}
</script>

<style lang="scss" scoped>

nav {
    position: fixed;
    padding: 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    left:0;
    right:0;
    top: 0;
    box-sizing: border-box;
    z-index: 600;
    background-color: var(--background1);
    font-weight: 600;

    #logo img {
        height: 60px;
    }
    }
</style>