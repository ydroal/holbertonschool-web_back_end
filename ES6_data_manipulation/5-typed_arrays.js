export default function createInt8TypedArray(length, position, value) {
  if (value < -128 || value > 127) {
    throw new RangeError('Position outside range');
  }
  if (position > length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  view[position] = value;

  return new DataView(buffer);
}
