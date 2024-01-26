<template>
    <Nav :box="box" :back="true"/>
    <div v-if="word" class="card-container">
      <div class="card" @click="flipCard">
    <div class="card-inner" :class="{ flipped: isFlipped }">
      <div class="card-face front">
        <h2>{{ word.term }}</h2>
      </div>
      <div class="card-face back">
        <h2>{{ word.definition }}</h2>
      </div>
    </div>
  </div>
  <div class="btns">
    <div @click="yes(word.id, word.level)" class="btn yes">Gewusst</div>
    <div @click="no(word.id, word.level)" class="btn no">Nicht gewusst</div>
  </div>
  </div>
 </template>

<script setup>

const isFlipped = ref(false);

const flipCard = () => {
  isFlipped.value = !isFlipped.value;
};

 const client = useSupabaseClient();
 const { id } = useRoute().params;
 const tray = useRoute().query.tray;
 
 const { data: box } = await useAsyncData('boxes', async () => {
   const { data } = await client.from('boxes').select('*').eq('id', id)
   return data[0]
 })
 
 const { data: word, refresh: refreshWords } = await useAsyncData('words', async () => {
   const { data } = await client.from('words').select('*').eq('box_id', id).eq('level', tray)
 
   return data[0]
 })

 async function yes(id, level) {
  if (level != 4) {
    level++;
  }
    const { data, error } = await client.from('words').update({ level: level }).eq('id', id).select();
    refreshWords();
    isFlipped.value = false;
    confetti();
}

async function no(id, level) {
  if (level != 1) {
    level--;
  }
    const { data, error } = await client.from('words').update({ level: level }).eq('id', id).select();
    refreshWords();
}
 </script>
 
 <style lang="scss">
     .card-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }

    .btns {
      margin-top: 2rem;
      display: flex;

      .btn {
        margin: 0.5rem;
      }

      .yes {
        background-color: #63fd55;
        color: #000000;
      }

      .no {
        background-color: #ff4141;
      }
    }

    .card {
      position: relative;
      width: 500px;
      height: 300px;
      perspective: 1000px;
      cursor: pointer;
    }

    .card-inner {
      position: absolute;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.5s;
    }

    .flipped {
      transform: rotateY(180deg);
    }

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
      color: white;
    }

    .front {
      background-color: #171717;
    }

    .back {
      background-color: #303030; /* Hintergrundfarbe der Rückseite anpassen */
      transform: rotateY(180deg);
    }
 </style>