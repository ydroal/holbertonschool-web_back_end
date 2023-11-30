const http = require('http');
const fs = require('fs');
const fsp = require('fs').promises;

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

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students');
    try {
      const studentsList = await countStudents(process.argv[2]);
      res.end(`This is the list of our students\n${studentsList}`);
    } catch (error) {
      res.end(error.message);
    }
  }
});

const port = 1245;
app.listen(port);

module.exports = app;
