<template>
  <!-- Navigationsleiste mit Abmelden-Schaltfläche -->
  <Nav btn="logout"/>
  <!-- Hauptinhalt -->
  <div class="padding">
      <br><br><br><br>
      <!-- Schaltfläche zum Erstellen einer neuen Sammlung -->
      <Nuxt-link @click="addBox()" class="btn">Sammlung erstellen</Nuxt-link>
  
      <!-- Container für die Sammlungen -->
      <div class="boxes">
          <!-- Iteration über vorhandene Sammlungen -->
          <BoxSnaek v-for="box of boxes" :box="box" :key="box.id"/>
      </div>
  
      <!-- Nachricht, wenn keine Sammlungen vorhanden sind -->
      <p v-if="!boxes[0]">Du hast noch keine Sammlung erstellt!</p>
  </div>
</template>
    
    <style scoped>
    /* Stile für den Container der Sammlungen */
        .boxes {
        margin-top: 2rem;
        display: flex;
        flex-wrap: wrap;
    }

    /* Stile für den gesamten Körper */
    body {
        margin: 2rem;
    }
    </style>
    
<script setup>
// Importieren von Supabase-Client-Funktionen und Routing-Werkzeugen
const client = useSupabaseClient();
const user = useSupabaseUser();
const router = useRouter();

// Abfrage der Benutzersammlungen
const { data: boxes, refresh: refreshBoxes } = await useAsyncData('boxes', async () => {
    const { data } = await client.from('boxes').select('*').order('created_at');

    return data;
});

// Funktion zum Hinzufügen einer neuen Sammlung
async function addBox() {
    const { data, error } = await client.from('boxes').insert([
        { name: 'Neue Sammlung', user_id: user.value.id },
    ]).select();
    
    refreshBoxes();
}
</script>