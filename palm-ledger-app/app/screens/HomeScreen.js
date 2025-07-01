import React, { useEffect, useState } from "react";
import { View, Text, Button, FlatList } from "react-native";
import { getTransactions } from "../services/api";

export default function HomeScreen({ route, navigation }) {
  const { token } = route.params;
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const res = await getTransactions(token);
    setTransactions(res.data);
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 22 }}>Transactions</Text>
      <FlatList
        data={transactions}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={{ marginVertical: 8, padding: 10, borderWidth: 1 }}>
            <Text>{item.name}</Text>
            <Text>
              ₦{item.amount} x {item.quantity}
            </Text>
            <Text>{item.description}</Text>
          </View>
        )}
      />
      <Button
        title="Add Transaction"
        onPress={() => navigation.navigate("AddTransaction", { token })}
      />
    </View>
  );
}
