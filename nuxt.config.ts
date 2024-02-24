// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/supabase',
    '@nuxtjs/color-mode'
  ],
  css: [
    '@/assets/css/main.scss',
  ],
  supabase: {
    redirectOptions: {
      login: '/login',
      callback: '/confirm',
      exclude: [
        '/register',
        '/resetPassword',
        '/updatePassword',
      ],
    }
  }
})
