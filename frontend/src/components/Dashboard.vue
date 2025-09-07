<template>
  <div>
    <h1>Dashboard</h1>
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
          <v-card-title>Actions</v-card-title>
          <v-card-text>
            <v-btn color="primary" @click="$router.push('/notes')">Go to Notes</v-btn>
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
