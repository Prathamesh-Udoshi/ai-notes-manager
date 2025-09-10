<template>
  <v-container fluid class="pa-0" style="min-height: 100vh;">
    <!-- Hero Section -->
    <section style="background: #1a237e; color: white; padding: 60px 24px; text-align: center;">
      <h1 class="text-h3 font-weight-bold mb-4">Welcome to Smart Notes</h1>
      <p class="text-h6 mb-3">Your intelligent note-taking companion powered by AI</p>
      <p class="text-body-1 mb-8" style="max-width: 600px; margin: 0 auto;">
        Create, organize, and manage your notes with automatic summarization and smart title generation.
      </p>
      <v-btn size="large" color="white" variant="outlined" class="px-8" @click="$router.push('/notes/new')">
        <v-icon left>mdi-plus</v-icon>
        Create Your First Note
      </v-btn>
    </section>

    <!-- Features Section -->
    <section style="padding: 60px 24px; background: #f5f5f5;">
      <h2 class="text-h4 text-center mb-12 font-weight-bold">Features</h2>
      <v-row justify="center">
        <v-col cols="12" md="4" class="text-center pa-4">
          <v-card flat class="pa-6" style="height: 100%;">
            <v-icon size="56" color="indigo" class="mb-4">mdi-brain</v-icon>
            <h3 class="text-h6 font-weight-bold mb-3">AI-Powered Summarization</h3>
            <p class="text-body-1">Automatically generate concise summaries of your notes using advanced AI models.</p>
          </v-card>
        </v-col>
        <v-col cols="12" md="4" class="text-center pa-4">
          <v-card flat class="pa-6" style="height: 100%;">
            <v-icon size="56" color="indigo" class="mb-4">mdi-lightbulb-on</v-icon>
            <h3 class="text-h6 font-weight-bold mb-3">Smart Title Generation</h3>
            <p class="text-body-1">Get intelligent title suggestions based on your note content.</p>
          </v-card>
        </v-col>
        <v-col cols="12" md="4" class="text-center pa-4">
          <v-card flat class="pa-6" style="height: 100%;">
            <v-icon size="56" color="indigo" class="mb-4">mdi-note-edit</v-icon>
            <h3 class="text-h6 font-weight-bold mb-3">Easy Note Management</h3>
            <p class="text-body-1">Create, edit, delete, and organize your notes with a clean, intuitive interface.</p>
          </v-card>
        </v-col>
      </v-row>
    </section>

    <!-- Notes Summary -->
    <section style="padding: 60px 24px;">
      <h2 class="text-h4 text-center mb-12 font-weight-bold">Dashboard</h2>
      <v-row justify="center">
        <v-col cols="12" md="5" class="pa-4">
          <v-card flat class="pa-6 text-center" style="height: 100%;">
            <v-icon size="48" color="indigo" class="mb-4">mdi-chart-pie</v-icon>
            <h3 class="text-h6 font-weight-bold mb-4">Notes Summary</h3>
            <div class="mb-3">
              <p class="text-h5 font-weight-bold indigo--text">{{ notes.length }}</p>
              <p class="text-body-2">Total Notes</p>
            </div>
            <div>
              <p class="text-body-1 font-weight-medium">{{ lastNoteTitle }}</p>
              <p class="text-body-2 text--secondary">Last Note</p>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md="5" class="pa-4">
          <v-card flat class="pa-6 text-center" style="height: 100%;">
            <v-icon size="48" color="indigo" class="mb-4">mdi-flash</v-icon>
            <h3 class="text-h6 font-weight-bold mb-6">Quick Actions</h3>
            <v-row>
              <v-col cols="12" class="pa-2">
                <v-btn block size="large" color="indigo" variant="elevated" class="mb-3" @click="$router.push('/notes')">
                  <v-icon left>mdi-view-list</v-icon>
                  View All Notes
                </v-btn>
              </v-col>
              <v-col cols="12" class="pa-2">
                <v-btn block size="large" color="grey darken-1" variant="elevated" @click="$router.push('/notes/new')">
                  <v-icon left>mdi-plus</v-icon>
                  Create New Note
                </v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </section>

    <!-- Credits Section -->
    <section style="padding: 40px 24px; background: #f8f9fa; border-top: 1px solid #e9ecef;">
      <div class="text-center">
        <p class="text-body-2 text--secondary mb-2">Made with ❤️ by</p>
        <p class="text-h6 font-weight-bold indigo--text">@Prathamesh</p>
      </div>
    </section>
  </v-container>
</template>

<script>
import { getNotes } from '../api'

export default {
  name: 'Dashboard',
  data() {
    return { notes: [] }
  },
  computed: {
    lastNoteTitle() {
      if (this.notes.length === 0) return 'No notes yet'
      return this.notes[this.notes.length - 1].title || 'Untitled'
    }
  },
  async mounted() {
    try {
      const response = await getNotes()
      this.notes = response.data
    } catch (error) {
      console.error('Failed to load notes:', error)
    }
  }
}
</script>
