import React, { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";
import {
  login,
  register,
  getTransactions,
  addTransaction,
} from "../services/api"; // ✅

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const res = await login({ username, password });
      const token = res.data.token;
      navigation.navigate("Home", { token });
    } catch (error) {
      Alert.alert("Login failed", "Check username/password");
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Login</Text>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <Button title="Login" onPress={handleLogin} />
      <Button
        title="Register"
        onPress={() => navigation.navigate("Register")}
      />
    </View>
  );
}
