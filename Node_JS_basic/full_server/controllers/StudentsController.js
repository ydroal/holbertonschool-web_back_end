import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const studentsList = await readDatabase(process.argv[2]);
      let resText = 'This is the list of our students\n';

      Object.keys(studentsList).sort().forEach((key) => {
        resText += `Number of students in ${key}: ${studentsList[key].length}. List: ${studentsList[key].join(', ')}\n`;
      });

      res.send(resText);
    } catch (error) {
      res.status(500).send(`This is the list of our students\n${error.message}`);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const studentsList = await readDatabase(process.argv[2]);
      if (studentsList[major]) {
        res.send(`List: ${studentsList[major].join(', ')}`);
      }
      return;
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
