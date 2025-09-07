<template>
  <div>
    <v-row>
      <v-col cols="12" md="8" offset-md="2">
        <v-card>
          <v-card-title>
            <span v-if="isEditMode">Edit Note</span>
            <span v-else>Create Note</span>
          </v-card-title>
          <v-card-text>
            <v-form ref="form" v-model="valid">
              <v-text-field
                v-model="note.title"
                label="Title"
                :rules="[v => !!v || 'Title is required']"
                required
              ></v-text-field>
              <v-textarea
                v-model="note.content"
                label="Content"
                :rules="[v => !!v || 'Content is required']"
                rows="10"
                required
              ></v-textarea>
              <v-textarea
                v-model="note.summary"
                label="Summary"
                rows="4"
                readonly
              ></v-textarea>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="saveNote" :disabled="!valid">
              {{ isEditMode ? 'Update' : 'Create' }}
            </v-btn>
            <v-btn color="secondary" @click="summarize" :disabled="!note.content">
              Summarize
            </v-btn>
            <v-btn text @click="$router.push('/notes')">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { createNote, getNote, updateNote, summarizeText } from '../api'

export default {
  name: 'NoteEditor',
  props: {
    id: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      note: {
        title: '',
        content: '',
        summary: ''
      },
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
        // Ensure properties are defined
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
