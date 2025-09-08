<template>
  <div>
    <v-row>
      <v-col cols="12" md="8" offset-md="2">
        <v-card>
          <v-card-title>
            View Note
          </v-card-title>
          <v-card-text>
            <v-text-field
              v-model="note.title"
              label="Title"
              readonly
            ></v-text-field>
            <v-textarea
              v-model="note.content"
              label="Content"
              rows="10"
              readonly
            ></v-textarea>
            <v-textarea
              v-model="note.summary"
              label="Summary"
              rows="4"
              readonly
            ></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="$router.push('/notes')">Back to Notes</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { getNote } from '../api'

export default {
  name: 'NoteViewer',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      note: {
        title: '',
        content: '',
        summary: ''
      }
    }
  },
  async mounted() {
    try {
      const response = await getNote(this.id)
      this.note = response.data
      // Ensure properties are defined
      this.note.title = this.note.title || ''
      this.note.content = this.note.content || ''
      this.note.summary = this.note.summary || ''
    } catch (error) {
      console.error('Failed to load note:', error)
    }
  }
}
</script>
