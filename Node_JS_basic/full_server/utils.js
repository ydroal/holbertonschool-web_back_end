const fs = require('fs');
const fsp = require('fs').promises;

export default async function readDatabase(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const text = await fsp.readFile(path, 'utf8');
  const data = text.split('\n');
  const students = data.slice(1).filter((line) => line.length > 0);

  const res = {};

  students.forEach((line) => {
    const [firstname, , , field] = line.split(',');
    if (!res[field]) {
      res[field] = [];
    }
    res[field].push(firstname);
  });

  return res;
}
