const fs = require('fs');
const fsp = require('fs').promises;
const express = require('express');

const app = express();
const port = 1245;

async function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const text = await fsp.readFile(path, 'utf8');
  const data = text.split('\n');
  const students = data.slice(1).filter((line) => line.length > 0);
  let res = `Number of students: ${students.length}\n`;

  const group = students.reduce((result, line) => {
    const [firstname, , , field] = line.split(',');

    const element = result.find((s) => s.field === field);
    if (element) {
      element.count += 1;
      element.firstnames.push(firstname);
    } else {
      result.push({
        field,
        count: 1,
        firstnames: [firstname],
      });
    }
    return result;
  }, []);

  group.forEach((element) => {
    res += `Number of students in ${element.field}: ${element.count}. List: ${element.firstnames.join(', ')}\n`;
  });

  return res;
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (async (req, res) => {
  try {
    const studentsList = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${studentsList}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
}));

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});

module.exports = app;
