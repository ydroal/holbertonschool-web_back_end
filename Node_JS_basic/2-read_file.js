const fs = require('fs');

function countStudents(path) {
  if (!(fs.existsSync(path))) {
    throw new Error('Cannot load the database');
  }

  const text = fs.readFileSync(path, 'utf8');
  if (!text) throw new Error('Cannot load the database');

  const data = text.split('\n');
  const students = data.slice(1).filter((line) => line.length > 0);
  console.log(`Number of students: ${students.length}`);

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
    console.log(`Number of students in ${element.field}: ${element.count}. List: ${element.firstnames.join(', ')}`);
  });
}

module.exports = countStudents;
