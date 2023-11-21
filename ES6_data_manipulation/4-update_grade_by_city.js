export default function updateStudentGradeByCity(array, city, newGrades) {
  const grade = { grade: 'N/A' };

  const filterdStudent = array.filter((student) => student.location === city);
  const res = filterdStudent.map((student) => {
    newGrades.forEach((element) => {
      if (element.studentId === student.id) {
        grade.grade = element.grade;
      }
    });
    return { ...student, ...grade };
  });

  return res;
}
