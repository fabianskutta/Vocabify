<template>
  <!-- Navigationsleiste einfügen -->
  <Nav/>
  <!-- Login-Formular -->
  <div v-if="isFormRendered" class="login">
      <form class="container" @submit.prevent="signIn(userData)">
          <h2>Login</h2>
          <!-- Eingabefeld für E-Mail -->
          <label for="email"><b>E-Mail</b></label>
          <input v-model="userData.email" type="email" name="email" required>
          <!-- Eingabefeld für Passwort -->
          <label for="password"><b>Password</b></label>
          <input v-model="userData.password" type="password" name="password" required>
          <!-- Fehlermeldung anzeigen -->
          <p v-if="userData.errorMsg">{{ userData.errorMsg }}</p>
          <!-- Login-Schaltfläche -->
          <button type="submit">Login</button>
          <!-- Links für Formulare -->
          <div class="form-links">
              <nuxt-link to="/register">Du hast noch kein Konto? Registriere Dich!</nuxt-link>
          </div>
      </form>
      <!-- Glanzeffekt im Hintergrund -->
      <div class="glow"></div>
  </div>
</template>

<style lang="scss" scoped>
/* Stile für Überschrift */
h2 {
  margin-bottom: 0;
  text-align: center;
}

/* Stile für Glanzeffekt */
.glow {
  background-image: linear-gradient(45deg, #ff4141, #ff4141);
  opacity: 0.2;
  filter: blur(100px);
  width: 400px;
  height: 400px;
  position: absolute;
  z-index: -1;
}

/* Stile für Formular-Links */
.form-links {
  display: flex;
  justify-content: space-evenly;
  margin-top: 20px;
  a {
      color: #7a7a7a;
      font-size: 12px;
  }
}

/* Stile für das Login-Formular */
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* Stile für den Container des Formulars */
.container {
  background-color: var(--background1);
  display: flex;
  width: 400px;
  padding: 1.5rem;
  justify-content: center;
  flex-direction: column;
  border-color: #ffffff17;
  border-style: solid;
  border-width: 1px;
  border-radius: 20px;
  height: fit-content;
  z-index: 200;
}

/* Stile für Eingabefelder */
input, select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #333333;
  background-color: var(--input);
  color: var(--text1);
  border-radius: 4px;
  resize: vertical;
}

/* Stile für Schaltfläche */
button[type=submit] {
  background-color: var(--accent1);
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
  margin-top: 20px;
}

/* Stile für Fokuszustand der Eingabefelder */
textarea:focus, input:focus {
  outline: none;
  border: 1px solid #7a7a7a;
}

/* Stile für Labels */
label {
  padding: 12px 12px 12px 0;
  display: inline-block;
  font-size: 14px;
  color: #7a7a7a;
  font-weight: 300;
}

/* Stile für Paragraphen */
p {
  font-size: 14px;
}
</style>

<script setup lang="js">
// Importieren von Supabase-Client-Funktionen und Routing-Werkzeugen
const client = useSupabaseClient();
const router = useRouter();

// Benutzerdaten-Reaktivität
const userData = ref({
  email: "", // E-Mail-Adresse
  password: "", // Passwort
  errorMsg: "", // Fehlermeldung
});

// Anmeldefunktion
async function signIn() {
  try {
      const { error } = await client.auth.signInWithPassword({
          email: userData.value.email, // E-Mail-Adresse
          password: userData.value.password // Passwort
      });
      if (error) throw error;
      router.push("/"); // Weiterleitung nach erfolgreichem Login
  } catch (error) {
      userData.value.errorMsg = error.message; // Fehlermeldung anzeigen
  }
}

// Reaktivität für die Anzeige des Formulars
const isFormRendered = ref(false);

// Nach dem Laden der Komponente das Formular anzeigen
onMounted(() => {
  isFormRendered.value = true;
});
</script>
