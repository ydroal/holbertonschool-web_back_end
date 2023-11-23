export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || !startString) return '';

  let newStr = '';
  for (let str of set) {
    if (str && str.startsWith(startString)) {
      str = `${str.replace(startString, '')}-`;
      newStr = newStr.concat(str);
    }
  }
  const lastChar = newStr.slice(-1);
  if (lastChar === '-') newStr = newStr.slice(0, -1);

  return newStr;
}
