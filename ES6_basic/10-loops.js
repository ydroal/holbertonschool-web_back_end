export default function appendToEachArrayValue(array, appendString) {
  const res = [];
  for (let value of array) {
    value = appendString + value;
    res.push(value);
  }

  return res;
}
