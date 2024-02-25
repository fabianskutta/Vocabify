<template>
  <!-- Navigationsleiste mit Schaltfläche zur Box-Seite -->
  <Nav :box="box" btn="toBox"/>
  <!-- Container für die Karte -->
  <div v-if="word" class="card-container">
      <!-- Kartelement -->
      <div class="card" @click="flipCard">
          <!-- Karteninhalt -->
          <div class="card-inner" :class="{ flipped: isFlipped }">
              <!-- Vorderseite der Karte mit Begriff -->
              <div class="card-face front">
                  <h2>{{ word.term }}</h2>
              </div>
              <!-- Rückseite der Karte mit Definition -->
              <div class="card-face back">
                  <h2>{{ word.definition }}</h2>
              </div>
          </div>
      </div>
      <!-- Schaltflächen für "Gewusst" und "Nicht gewusst" -->
      <div class="btns">
          <div @click="yes(word.id, word.level)" class="btn yes">Gewusst</div>
          <div @click="no(word.id, word.level)" class="btn no">Nicht gewusst</div>
      </div>
  </div>
  <!-- Nachricht, wenn keine Wörter verfügbar sind -->
  <div v-if="!word" class="card-container">
      <img src="https://i.gifer.com/origin/02/02326e71d0adc41645bff3f07d930343_w200.gif" alt="">
      <p>Du hast genug gelernt. Gönn Dir mal eine Pause!</p>
  </div>
</template>

<script setup>

// Importieren der Reactivity-Funktionen für die Komponente
const isFlipped = ref(false); // Reaktive Variable für den Kartenflip-Zustand

// Funktion zum Umschalten des Kartenflip-Zustands
const flipCard = () => {
  isFlipped.value = !isFlipped.value;
};

// Verwendung des Supabase-Clients
const client = useSupabaseClient(); // Supabase-Client

// Extrahieren der ID aus den Routenparametern
const { id } = useRoute().params;

// Abrufen der Daten der Box aus der Datenbank
const { data: box } = await useAsyncData('boxes', async () => {
  const { data } = await client.from('boxes').select('*').eq('id', id);
  return data[0];
});

// Abrufen der Daten des Wortes aus der Datenbank
const { data: word, refresh: refreshWords } = await useAsyncData("words", async () => {
  const { data } = await client.from("words").select("*").eq("box_id", id);
  const currentDate = new Date();

  for (const wordItem of data) {
    const level = wordItem.level;

    if (level === null) {
      return wordItem;
    }

    const lastLearnedDate = new Date(wordItem.LastLearned);
    const intervalDays = Math.pow(level, 2);

    const nextDueDate = new Date(lastLearnedDate);
    nextDueDate.setDate(lastLearnedDate.getDate() + intervalDays);

    if (currentDate > nextDueDate) {
      return wordItem;
    }
  }
});

// Funktion zum Aktualisieren des Lernlevels eines Wortes
async function updateLevel(id, levelChange) {
  const newLevel = Math.min(Math.max(1, levelChange), 16);
  const { data, error } = await client
    .from('words')
    .update({ level: newLevel, LastLearned: new Date() })
    .eq('id', id)
    .select();
  refreshWords();
  isFlipped.value = false;
}

// Funktion für die Aktion "Ja" auf einem Wort
async function yes(id, level) {
  await updateLevel(id, level + 1); // Erhöhe das Lernlevel um 1
  confetti(); // Starte die Konfetti-Animation
}

// Funktion für die Aktion "Nein" auf einem Wort
async function no(id, level) {
  await updateLevel(id, level - 1); // Verringere das Lernlevel um 1
}

 </script>
 
 <style lang="scss">
      /* Stile für den Kartencontainer */
     .card-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }

    /* Stile für die Schaltflächen */
    .btns {
      margin-top: 2rem;
      display: flex;

      .btn {
        margin: 0.5rem;
      }

      /* Stile für die Schaltfläche "Gewusst" */
      .yes {
        background-color: #63fd55;
        color: #000000;
      }

      /* Stile für die Schaltfläche "Nicht gewusst" */
      .no {
        background-color: #ff4141;
      }
    }

    /* Stile für die Karte */
    .card {
      position: relative;
      width: 500px;
      height: 300px;
      perspective: 1000px;
      cursor: pointer;
    }

    /* Stile für das Innere der Karte */
    .card-inner {
      position: absolute;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.5s;
    }

    /* Stile für die umgedrehte Karte */
    .flipped {
      transform: rotateY(180deg);
    }

    /* Stile für die Vorder- und Rückseite der Karte */
    .card-face {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
      border: 1px solid #ffffff17;
      border-radius: 20px;
      box-sizing: border-box;
      color: var(--text1);
    }

    /* Stile für die Vorderseite der Karte */
    .front {
      background-color: var(--card);
    }

    /* Stile für die Rückseite der Karte */
    .back {
      background-color: var(--cardbg);
      transform: rotateY(180deg);
    }
 </style>