import React, { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";
import { register } from "../services/api";

export default function RegisterScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleRegister = async () => {
    try {
      const res = await register({ username, password, email });
      const token = res.data.token;
      navigation.navigate("Home", { token });
    } catch (error) {
      Alert.alert("Register failed", "Check details or username exists");
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Register</Text>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <Button title="Register" onPress={handleRegister} />
    </View>
  );
}
