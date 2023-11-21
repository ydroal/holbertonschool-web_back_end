export default function getStudentsByLocation(array, city) {
  const res = array.filter((student) => student.location === city);

  return res;
}
