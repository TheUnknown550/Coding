import React from 'react';
import {StyleSheet, Text, View} from 'react-native';

export default function App(){
  return(
    <View style = {BG.Heading}>
      <Text style = {text.Heading}>First Header</Text>
      <Text style = {text.SubHead}> Sub Heading this is jus tto make it longer to test it can can enter and it can.</Text>
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
  },
  SubHead:{
    flex: 18,
    fontSize: 16
  }
})