#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(response.body).reduce((usersCompletedTasks, todo) => {
      if (todo.completed) {
        if (usersCompletedTasks[todo.userId]) {
          usersCompletedTasks[todo.userId] += 1;
        } else {
          usersCompletedTasks[todo.userId] = 1;
        }
      }
      return usersCompletedTasks;
    }, {}));
  }
});
