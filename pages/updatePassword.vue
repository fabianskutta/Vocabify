<template>
  <div class="register">
      <form class="container" @submit.prevent="updatePassword(userData)">
        <label for="password"><b>New Password</b></label>
        <input v-model="userData.password" type="password" name="password" required>
  
        <p v-if="userData.errorMsg"> {{ userData.errorMsg }}</p>
        <p v-if="!userData.errorMsg && userData.successMsg">{{ userData.successMsg }}</p>
  
        <button type="submit">Update Password</button>
        <div class="form-links">
          <nuxt-link to="/login">Already have an account? Login</nuxt-link>
        </div>
      </form>
  </div>
  
  </template>
  
  <style lang="scss">
  .form-links {
    display: flex;
    justify-content: space-evenly;
    margin-top: 20px;
    a {
      color: #7a7a7a;
      font-size: 12px;
    }
  }
  
  
  .register {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
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
  
  input, select, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #333333;
    background-color: #171717;
    color: var(--text1);
    border-radius: 4px;
    resize: vertical;
  }
  
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
  
  textarea:focus, input:focus{
      outline: none;
      border: 1px solid #7a7a7a;
    }
  
  label {
    padding: 12px 12px 12px 0;
    display: inline-block;
    font-size: 14px;
    color: #7a7a7a;
    font-weight: 300;
  }
  
  p {
    font-size: 14px;
  }
  </style>
  
  <script setup lang="js">
  const client = useSupabaseClient();
  const router = useRouter();
  
  const userData = ref({
      email: "",
      errorMsg: "",
      successMsg: "",
    });
  
    async function updatePassword() {
    try {
      const { data, error } = await client.auth.updateUser({
        password: userData.value.password
      });
      if (error) throw error;
      router.push("/");
    } catch (error) {
      userData.value.errorMsg = error.message;
    }
  }
  </script>