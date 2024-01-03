#!/usr/bin/node
// Task Tracker

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const finishedTasks = {};
  body.forEach((task) => {
    if (task.completed) {
      if (!finishedTasks[task.userId]) {
        finishedTasks[task.userId] = 1;
      } else {
        finishedTasks[task.userId] += 1;
      }
    }
  });
  console.log(finishedTasks);
});
