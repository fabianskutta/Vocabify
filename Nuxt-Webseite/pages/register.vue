<template>
  <!-- Navigationsleiste einfügen -->
  <Nav/>
  <!-- Registrierungsformular -->
  <div class="register">
      <form class="container" @submit.prevent="signUp(userData)">
          <h2>Register</h2>
          <!-- Eingabefeld für E-Mail -->
          <label for="email"><b>E-Mail</b></label>
          <input v-model="userData.email" type="email" name="email" required>
          <!-- Eingabefeld für Passwort -->
          <label for="password"><b>Password</b></label>
          <input v-model="userData.password" type="password" name="password" required>
          <!-- Fehlermeldung anzeigen -->
          <p v-if="userData.errorMsg">{{ userData.errorMsg }}</p>
          <!-- Erfolgsmeldung anzeigen -->
          <p v-if="!userData.errorMsg && userData.successMsg">{{ userData.successMsg }}</p>
          <!-- Registrierungsschaltfläche -->
          <button type="submit">Register</button>
          <!-- Links für Formulare -->
          <div class="form-links">
              <nuxt-link to="/login">Du hast bereits ein Konto?</nuxt-link>
          </div>
      </form>
      <!-- Glanzeffekt im Hintergrund -->
      <div class="glow"></div>
  </div>
</template>

<style lang="scss">
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

/* Stile für das Registrierungsformular */
.register {
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
}

/* Stile für Eingabefelder */
input, select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #333333;
  background-color: #171717;
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
// Importieren von Supabase-Client-Funktionen
const client = useSupabaseClient();

// Reaktivität für Benutzerdaten
const userData = ref({
  email: "", 
  password: "",
  errorMsg: "",
  successMsg: "",
});

// Funktion für die Registrierung
async function signUp() {
  try {
      const { data, error } = await client.auth.signUp({
          email: userData.value.email, // E-Mail-Adresse
          password: userData.value.password // Passwort
      });
      if (error) throw error;
      userData.value.successMsg = "Check your E-Mail to confirm your account."; // Erfolgsmeldung setzen
  } catch (error) {
      userData.value.errorMsg = error.message; // Fehlermeldung setzen
  }
}
</script>
