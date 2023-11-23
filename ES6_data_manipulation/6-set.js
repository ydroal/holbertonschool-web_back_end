export default function setFromArray(array) {
  const resSet = new Set();
  array.forEach((e) => {
    resSet.add(e);
  });
  return resSet;
}
