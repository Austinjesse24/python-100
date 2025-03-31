import React from 'react';
import { View, Text, Button } from 'react-native';

const App = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Hello, React Native! 🚀</Text>
      <Button title="Click Me" onPress={() => alert('Button Pressed!')} />
    </View>
  );
};

export default App;
 