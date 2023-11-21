export default function getStudentIdsSum(array) {
  return array.reduce((total, student) => total + student.id, 0);
}
