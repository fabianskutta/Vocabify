<template>
  <Nav :box="box" btn="toBox"/>
  <!-- Platzhalter für den Abstand oben -->
  <div class="nav-dummy"></div>
  <!-- Bereich mit Innenabstand -->
  <div class="padding">
    <!-- Eingabefelder für den Boxnamen und Dateiupload -->
    <div class="inputs">
      <input @blur="name => changeBoxname(name)" :value="box.name" type="text" name="name" required>
      <input type="file" @change="handleFileUpload">
    </div>
    <br><br>

 <!-- Liste der Wörter -->
  <div v-for="word of words" :word="word" :key="word.id">
  <div class="wordsEdit-container">
    <form class="wordsEdit-input-container">
        <div class="wordsEdit-input">
            <label for="term"><b>Begriff</b></label>
            <input @blur="term => changeTerm(term, `${word.id}`)" :value="word.term" type="text" name="term" required>
        </div>
        <div class="wordsEdit-input">
            <label for="definition"><b>Definition</b></label>
            <input @blur="definition => changeDefinition(definition, `${word.id}`)" :value="word.definition" type="text" name="definition" required>
        </div>
        <div class="wordsEdit-btn">
            <Nuxt-link @click="deleteWord(`${word.id}`)" class="btn">Löschen</Nuxt-link>
        </div>
    </form>
</div>
</div>
<br>
<!-- Schaltfläche zum Hinzufügen eines Wortes -->
<Nuxt-link @click="addWord()" class="btn">Karte hinzufügen</Nuxt-link>
<br><br><br>
<!-- Schaltfläche zum Löschen der Box -->
<Nuxt-link @click="deleteBox()" class="btn">Box löschen</Nuxt-link>
  </div>
</template>

<style>
/* Stile für die Eingabefelder */
.inputs {
  display: flex;

  input {
    margin-right: 2rem;
  }
}

/* Stile für den Container der Wortbearbeitung */
.wordsEdit-container {
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 4px;
    background-color: var(--background2);
}

/* Stile für das Wortbearbeitungsformular */
.wordsEdit-input-container {
    display: flex;
    justify-content: space-between;
}

/* Stile für die Eingabefelder im Wortbearbeitungsformular */
.wordsEdit-input {
    width: 100%;
    margin-right: 2rem;
}

/* Stile für die Schaltflächen im Wortbearbeitungsformular */
.wordsEdit-btn {
    flex-direction: column;
    display: flex;
    justify-content: flex-end;
}

/* Allgemeine Stile für Eingabefelder */
input, select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #333333;
  background-color: var(--input);
  color: var(--text1);
  border-radius: 4px;
  resize: vertical;
}

/* Stile für die Schaltflächen */
button[type=submit] {
  background-color: var(--accent1);
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
  margin-top: 0px;
  font-size: 1rem;
}

/* Stile für das Fokussieren von Eingabefeldern */
textarea:focus, input:focus{
    outline: none;
    border: 1px solid #7a7a7a;
  }

  /* Stile für die Beschriftungen */
  label {
  padding: 12px 12px 12px 0;
  display: inline-block;
  font-size: 14px;
  color: #7a7a7a;
  font-weight: 300;
}
</style>

<script setup>
// Importieren der Supabase-Funktionen
const client = useSupabaseClient()

// Parameter aus dem Routenobjekt extrahieren
const { id } = useRoute().params;

// Daten für die aktuelle Box und die zugehörigen Wörter abrufen
const userData = ref({
    NewTerm: "",
    newDefinition: "",
  });

// Funktionen für die Bearbeitung von Begriffen und Definitionen sowie das Hinzufügen und Löschen von Wörtern und Boxen definieren
const { data: box, refresh: refreshBox } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').eq('id', id)

  return data[0]
})

const { data: words, refresh: refreshWords } = await useAsyncData('words', async () => {
  const { data } = await client.from('words').select('*').eq('box_id', id)
  return data
})

async function changeTerm(term, id) {
    let value = term.target.value;
    const { data, error } = await client.from('words').update({ term: value }).eq('id', id).select();
}

async function changeBoxname(name) {
    let value = name.target.value;
    const { data, error } = await client.from('boxes').update({ name: value }).eq('id', id).select();
    refreshBox();
}

async function changeDefinition(definition, id) {
    let value = definition.target.value;
    const { data, error } = await client.from('words').update({ definition: value }).eq('id', id).select();
}

async function deleteWord(id) {
    const { data, error } = await client.from('words').delete().eq('id', id);
    refreshWords();
}

async function deleteBox() {
    const { data2, error2 } = await client.from('words').delete().eq('box_id', id);
    const { data, error } = await client.from('boxes').delete().eq('id', id);
    await navigateTo('/')
}

async function addWord() {
    const { data, error } = await client.from('words').insert([
    { box_id: id, level: 1 },
  ])
  .select()
    refreshWords();
}

// Funktion zum Verarbeiten des Dateiuploads
import Papa from 'papaparse';

async function handleFileUpload(event) {
  const file = event.target.files[0];

  if (file) {
    Papa.parse(file, {
      encoding: 'UTF-8',
      complete: async (result) => {
        const header = result.data[0];
        const termIndex = header.indexOf('term');
        const definitionIndex = header.indexOf('definition');

        if (termIndex !== -1 && definitionIndex !== -1) {
          const wordsToInsert = result.data.slice(1).filter(row => row[termIndex] && row[definitionIndex]).map((row) => {
            return {
              box_id: id,
              term: row[termIndex],
              definition: row[definitionIndex],
              level: 1,
            };
          });

          if (wordsToInsert.length > 0) {
            const { data, error } = await client.from('words').insert(wordsToInsert).select();
            refreshWords();
          } else {
            console.error('Die CSV-Datei enthält keine gültigen Daten.');
          }
        } else {
          console.error('CSV-Datei muss die Spalten "term" und "definition" enthalten.');
        }
      },
    });
  }
}

</script>