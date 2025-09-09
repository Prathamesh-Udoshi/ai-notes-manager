<template>
  <v-container fluid class="pa-0" style="min-height: 100vh; padding: 40px 24px;">
    <div class="d-flex align-center justify-space-between mb-6">
      <h2 class="text-h5 font-weight-bold">
        <v-icon left>mdi-note-multiple</v-icon> My Notes
      </h2>
      <v-btn color="indigo" @click="$router.push('/notes/new')">
        <v-icon left>mdi-plus</v-icon> Create Note
      </v-btn>
    </div>

    <div v-if="notes.length === 0" class="text-center pa-8">
      <v-icon size="64" color="grey" class="mb-4">mdi-note-off</v-icon>
      <h3 class="text-h6 grey--text">No notes yet</h3>
      <p class="body-1 grey--text">Create your first note to get started!</p>
    </div>

    <div v-else>
      <div
        v-for="note in notes"
        :key="note.id"
        style="border-bottom: 1px solid #ddd; padding: 16px 0;"
      >
        <h3 class="text-h6 font-weight-bold mb-2">{{ note.title || 'Untitled' }}</h3>
        <p class="mb-2" style="font-size: 0.95rem; color: #333;">
          {{ getNoteSubtitle(note) }}
        </p>
        <p class="mb-3" style="font-size: 0.85rem; color: #666;">
          Created on: {{ formatDate(note.created_at) }}
        </p>
        <div class="d-flex" style="gap: 12px;">
          <v-btn small color="blue" @click.stop="viewNote(note.id)">
            <v-icon left>mdi-eye</v-icon> View
          </v-btn>
          <v-btn small color="orange" @click.stop="editNote(note.id)">
            <v-icon left>mdi-pencil</v-icon> Edit
          </v-btn>
          <v-btn small color="red" @click.stop="deleteNote(note.id)">
            <v-icon left>mdi-delete</v-icon> Delete
          </v-btn>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script>
import { getNotes, deleteNote } from '../api'

export default {
  name: 'NoteList',
  data() {
    return { notes: [] }
  },
  async mounted() {
    await this.loadNotes()
  },
  methods: {
    async loadNotes() {
      try {
        const response = await getNotes()
        this.notes = response.data
      } catch (error) {
        console.error('Failed to load notes:', error)
      }
    },
    async deleteNote(id) {
      if (confirm('Are you sure you want to delete this note?')) {
        try {
          await deleteNote(id)
          await this.loadNotes()
        } catch (error) {
          console.error('Failed to delete note:', error)
        }
      }
    },
    editNote(id) {
      this.$router.push(`/notes/${id}/edit`)
    },
    viewNote(id) {
      this.$router.push(`/notes/${id}/view`)
    },
    getNoteSubtitle(note) {
      return note.summary || (note.content ? note.content.substring(0, 100) + '...' : 'No content')
    },
    formatDate(dateString) {
      if (!dateString) return 'Unknown'
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>
