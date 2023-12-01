const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('in the case of sum', () => {
    it('Should round the two numbers, and add a from b', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      assert.strictEqual(calculateNumber('SUM', 0.1, 0.3), 0);
    });
  });

  describe('in the case of subtract', () => {
    it('Should round the two numbers, and subtract b from a', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      assert.strictEqual(calculateNumber('SUBTRACT', 0.1, 0.3), 0);
    });
  });

  describe('in the case of divide', () => {
    it('Should round the two numbers, and divide a with b', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('Should return "Error" if division by zero' , () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
