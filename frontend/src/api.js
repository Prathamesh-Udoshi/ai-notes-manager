import axios from 'axios';

const API_BASE_URL = 'https://ai-notes-backend-ef9c.onrender.com'; // Adjust if backend runs on different port or host

export const getNotes = () => {
  return axios.get(`${API_BASE_URL}/notes/`);
};

export const getNote = (id) => {
  return axios.get(`${API_BASE_URL}/notes/${id}`);
};

export const createNote = (note) => {
  return axios.post(`${API_BASE_URL}/notes/`, note);
};

export const updateNote = (id, note) => {
  return axios.put(`${API_BASE_URL}/notes/${id}`, note);
};

export const deleteNote = (id) => {
  return axios.delete(`${API_BASE_URL}/notes/${id}`);
};

export const summarizeText = (text) => {
  return axios.post(`${API_BASE_URL}/ai/summarize`, { text });
};
