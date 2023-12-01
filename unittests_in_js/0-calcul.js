function calculateNumber(a, b) {
  const aRounded = Math.round(a);
  const bRounded = Math.round(b);

  return aRounded + bRounded;
}

module.exports = calculateNumber;

