<template>
  <v-container fluid class="pa-0" style="padding: 40px 24px;">
    <h2 class="text-h5 font-weight-bold mb-6">
      <v-icon left>mdi-note-edit</v-icon>
      {{ isEditMode ? 'Edit Note' : 'Create Note' }}
    </h2>

    <v-form ref="form" v-model="valid">
      <v-text-field
        v-model="note.title"
        label="Title (optional - will be auto-generated if empty)"
        placeholder="Enter a title or leave blank for AI-generated title"
        full-width
      ></v-text-field>

      <v-textarea
        v-model="note.content"
        label="Content"
        :rules="[v => !!v || 'Content is required']"
        rows="10"
        required
        full-width
      ></v-textarea>

      <v-textarea
        v-model="note.summary"
        label="Summary"
        rows="4"
        readonly
        full-width
      ></v-textarea>

      <div class="mt-4 d-flex" style="gap: 16px;">
        <v-btn color="indigo" @click="saveNote" :disabled="!note.content.trim()">
          {{ isEditMode ? 'Update' : 'Create' }}
        </v-btn>
        <v-btn color="grey darken-1" @click="summarize" :disabled="!note.content.trim()">
          <v-icon left>mdi-brain</v-icon> Summarize
        </v-btn>
        <v-btn text @click="$router.push('/notes')">Cancel</v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<script>
import { createNote, getNote, updateNote, summarizeText } from '../api'

export default {
  name: 'NoteEditor',
  props: { id: { type: String, default: null } },
  data() {
    return {
      note: { title: '', content: '', summary: '' },
      valid: false,
      isEditMode: false
    }
  },
  async mounted() {
    if (this.id) {
      this.isEditMode = true
      try {
        const response = await getNote(this.id)
        this.note = response.data
        this.note.title = this.note.title || ''
        this.note.content = this.note.content || ''
        this.note.summary = this.note.summary || ''
      } catch (error) {
        console.error('Failed to load note:', error)
      }
    }
  },
  methods: {
    async saveNote() {
      if (!this.$refs.form.validate()) return
      try {
        if (this.isEditMode) {
          await updateNote(this.id, this.note)
        } else {
          await createNote(this.note)
        }
        this.$router.push('/notes')
      } catch (error) {
        console.error('Failed to save note:', error)
      }
    },
    async summarize() {
      try {
        const response = await summarizeText(this.note.content)
        this.note.summary = response.data.summary || ''
      } catch (error) {
        console.error('Failed to summarize:', error)
      }
    }
  }
}
</script>
