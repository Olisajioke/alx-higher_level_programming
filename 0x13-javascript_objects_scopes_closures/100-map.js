#!/usr/bin/node
const { list } = require('./100-data');
console.log('Initial List:', list);
const newList = list.map((value, index) => value * index);
console.log('New List:', newList);
