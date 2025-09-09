<template>
  <v-container fluid class="pa-0" style="padding: 40px 24px;">
    <h2 class="text-h5 font-weight-bold mb-6">
      <v-icon left>mdi-eye</v-icon> View Note
    </h2>

    <div style="margin-bottom: 16px;">
      <h3 class="text-h6 mb-2">Title</h3>
      <p style="padding: 12px; background: #f5f5f5;">{{ note.title }}</p>
    </div>

    <div style="margin-bottom: 16px;">
      <h3 class="text-h6 mb-2">Content</h3>
      <p style="padding: 12px; background: #f5f5f5; white-space: pre-wrap;">{{ note.content }}</p>
    </div>

    <div style="margin-bottom: 16px;">
      <h3 class="text-h6 mb-2">Summary</h3>
      <p style="padding: 12px; background: #f5f5f5;">{{ note.summary }}</p>
    </div>

    <div style="margin-bottom: 16px;">
      <h3 class="text-h6 mb-2">Created Date</h3>
      <p style="padding: 12px; background: #f5f5f5;">{{ formatDate(note.created_at) }}</p>
    </div>

    <v-btn color="indigo" @click="$router.push('/notes')">
      <v-icon left>mdi-arrow-left</v-icon> Back to Notes
    </v-btn>
  </v-container>
</template>

<script>
import { getNote } from '../api'

export default {
  name: 'NoteViewer',
  props: { id: { type: String, required: true } },
  data() {
    return {
      note: { title: '', content: '', summary: '' }
    }
  },
  async mounted() {
    try {
      const response = await getNote(this.id)
      this.note = response.data
      this.note.title = this.note.title || ''
      this.note.content = this.note.content || ''
      this.note.summary = this.note.summary || ''
    } catch (error) {
      console.error('Failed to load note:', error)
    }
  },
  methods: {
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
