import React, { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";
import { addTransaction } from "../services/api";

export default function AddTransactionScreen({ route, navigation }) {
  const { token } = route.params;
  const [name, setName] = useState("");
  const [amount, setAmount] = useState("");
  const [quantity, setQuantity] = useState("");
  const [description, setDescription] = useState("");

  const handleAdd = async () => {
    try {
      const data = {
        name,
        amount,
        quantity,
        description,
      };
      await addTransaction(data, token);
      Alert.alert("Success", "Transaction added");
      navigation.goBack();
    } catch (err) {
      Alert.alert("Error", "Something went wrong");
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Add Transaction</Text>
      <TextInput
        placeholder="Name"
        value={name}
        onChangeText={setName}
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Amount"
        value={amount}
        onChangeText={setAmount}
        keyboardType="numeric"
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Quantity"
        value={quantity}
        onChangeText={setQuantity}
        keyboardType="numeric"
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={setDescription}
        style={{ borderWidth: 1, marginVertical: 10 }}
      />
      <Button title="Save" onPress={handleAdd} />
    </View>
  );
}
