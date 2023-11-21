export default function getListStudentIds(array) {
  if (!Array.isArray(array)) return [];

  const res = array.map((student) => student.id);

  return res;
}
