<template>
  <div>
    <v-row justify="space-between" align="center" class="mb-4">
      <v-col cols="auto">
        <h1>Notes</h1>
      </v-col>
      <v-col cols="auto">
        <v-btn color="primary" @click="$router.push('/notes/new')">Create Note</v-btn>
      </v-col>
    </v-row>

    <v-list>
      <v-list-item
        v-for="note in notes"
        :key="note.id"
        @click="editNote(note.id)"
        class="note-item"
      >
        <v-list-item-content>
          <v-list-item-title>{{ note.title || 'Untitled' }}</v-list-item-title>
          <v-list-item-subtitle>{{ getNoteSubtitle(note) }}</v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-btn icon @click.stop="deleteNote(note.id)">
            <v-icon color="red">mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import { getNotes, deleteNote } from '../api'

export default {
  name: 'NoteList',
  data() {
    return {
      notes: []
    }
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
    getNoteSubtitle(note) {
      return note.summary || (note.content ? note.content.substring(0, 100) + '...' : 'No content')
    }
  }
}
</script>

<style scoped>
.note-item {
  cursor: pointer;
}
</style>
