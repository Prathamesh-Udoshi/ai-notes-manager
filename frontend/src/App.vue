<template> <v-app> <v-app-bar app color="primary" dark> <v-toolbar-title>Smart Notes</v-toolbar-title>
      <v-spacer></v-spacer> <v-btn to="/" text>Home</v-btn> <v-btn to="/notes" text>Notes</v-btn> </v-app-bar> <v-main>
      <v-container> <router-view /> </v-container> </v-main> </v-app> </template>
<script>export default { name: 'App' } </script>