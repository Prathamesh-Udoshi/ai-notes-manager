<template>
  <div>
    <!-- Hero Section -->
    <v-row justify="center" class="mb-8">
      <v-col cols="12" md="10" lg="8">
        <v-card class="pa-6 text-center" color="primary" dark>
          <v-card-title class="text-h3 mb-4">Welcome to Smart Notes</v-card-title>
          <v-card-text class="text-h6">
            Your intelligent note-taking companion powered by AI
          </v-card-text>
          <v-card-text class="text-body-1">
            Create, organize, and manage your notes with automatic summarization and smart title generation.
          </v-card-text>
          <v-btn size="large" color="white" variant="outlined" @click="$router.push('/notes/new')" class="mt-4">
            <v-icon left>mdi-plus</v-icon>
            Create Your First Note
          </v-btn>
        </v-card>
      </v-col>
    </v-row>

    <!-- Features Section -->
    <v-row justify="center" class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 text-center mb-6">Features</h2>
      </v-col>
      <v-col cols="12" md="4">
        <v-card class="pa-4 text-center h-100">
          <v-icon size="64" color="primary" class="mb-4">mdi-brain</v-icon>
          <v-card-title>AI-Powered Summarization</v-card-title>
          <v-card-text>
            Automatically generate concise summaries of your notes using advanced AI models.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card class="pa-4 text-center h-100">
          <v-icon size="64" color="primary" class="mb-4">mdi-lightbulb-on</v-icon>
          <v-card-title>Smart Title Generation</v-card-title>
          <v-card-text>
            Get intelligent title suggestions based on your note content.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card class="pa-4 text-center h-100">
          <v-icon size="64" color="primary" class="mb-4">mdi-note-edit</v-icon>
          <v-card-title>Easy Note Management</v-card-title>
          <v-card-text>
            Create, edit, delete, and organize your notes with a clean, intuitive interface.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Notes Summary -->
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Notes Summary</v-card-title>
          <v-card-text>
            <p>Total Notes: {{ notes.length }}</p>
            <p>Last Note Title: {{ lastNoteTitle }}</p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Quick Actions</v-card-title>
          <v-card-text>
            <v-btn color="primary" @click="$router.push('/notes')" class="mr-2">
              <v-icon left>mdi-view-list</v-icon>
              View All Notes
            </v-btn>
            <v-btn color="secondary" @click="$router.push('/notes/new')">
              <v-icon left>mdi-plus</v-icon>
              Create Note
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { getNotes } from '../api'

export default {
  name: 'Dashboard',
  data() {
    return {
      notes: []
    }
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
