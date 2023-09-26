#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const taskCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskCompleted[todo.userId]) {
        taskCompleted[todo.userId] = 1;
      } else {
        taskCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(taskCompleted);
});
