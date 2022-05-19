import React from 'react';
import {StyleSheet, Text, View} from 'react-native';

export default function App(){
  return(
    <View style = {BG.Heading}>
      <Text style = {text.Heading}>This is the first message</Text>
    </View>
  )
}

const BG = StyleSheet.create({
  Heading:{
    flex: 1,
    backgroundColor: '#FC0'
  }
})

const text = StyleSheet.create({
  Heading:{
    flex: 1,
    fontSize: 26,
    textAlign: 'center'
  }
})