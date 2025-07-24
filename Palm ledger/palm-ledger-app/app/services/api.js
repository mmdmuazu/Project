// services/api.js
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api"; // Change to hosted IP when deploying

export const register = (data) =>
  axios.post(`${BASE_URL}/auth/register/`, data);
export const login = (data) => axios.post(`${BASE_URL}/auth/login/`, data);

export const getTransactions = (token) =>
  axios.get(`${BASE_URL}/transactions/`, {
    headers: { Authorization: `Token ${token}` },
  });

export const addTransaction = (data, token) =>
  axios.post(`${BASE_URL}/transactions/`, data, {
    headers: { Authorization: `Token ${token}` },
  });
