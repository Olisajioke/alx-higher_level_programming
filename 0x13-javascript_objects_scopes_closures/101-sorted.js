#!/usr/bin/node
const myDict = require('./101-data').dict;

const totalEntries = Object.entries(myDict);
const valuesArr = Object.values(myDict);
const uniqueValues = [...new Set(valuesArr)];
const updatedDict = {};
for (const index in uniqueValues) {
  const innerList = [];
  for (const key in totalEntries) {
    if (totalEntries[key][1] === uniqueValues[index]) {
      innerList.unshift(totalEntries[key][0]);
    }
  }
  updatedDict[uniqueValues[index]] = innerList;
}
console.log(updatedDict);
