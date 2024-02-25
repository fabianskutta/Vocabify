<template>
    <!-- Navigationsleiste -->
    <nav id="nav">
        <!-- Logo je nach Farbmodus anzeigen -->
        <div v-if="$colorMode.value == 'light'" id="logo"><img src="/Vocabify-w.png" alt=""></div>
        <div v-if="$colorMode.value !== 'light'" id="logo"><img src="/Vocabify.png" alt=""></div>

        <!-- Boxname anzeigen, wenn vorhanden -->
        <div v-if="box"><h3>{{ box.name }}</h3></div>

        <div>
            <!-- Abmelden-Schaltfläche, wenn btn='logout' -->
            <Nuxt-link v-if="btn=='logout'" @click="signOut()" class="btn">Abmelden</Nuxt-link>
            <!-- Zurück-Schaltfläche zur Box-Seite, wenn btn='toBox' -->
            <Nuxt-link v-if="btn=='toBox'" :to="`/box/${box.id}`" class="btn">Zurück</Nuxt-link>
            <!-- Zurück-Schaltfläche zur Startseite, wenn btn='home' -->
            <Nuxt-link v-if="btn=='home'" :to="`/`" class="btn">Zurück</Nuxt-link>
        </div>
    </nav>
</template>

<script setup lang="ts">
// Definiert die Eigenschaften der Komponentenprops
defineProps<{btn: Btn; box: Box}>();

// Importieren der Supabase-Funktionen und des Routers
const client = useSupabaseClient();
const user = useSupabaseUser()
const router = useRouter();

// Funktion zum Abmelden des Benutzers
async function signOut() {
    const { error } = await client.auth.signOut();
    router.push("/login");
}
</script>

<style lang="scss" scoped>

/* Navigationsleiste */
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

    /* Logo */
    #logo img {
        height: 60px;
    }
    }
</style>