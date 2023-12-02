const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('in the case of sum', () => {
    it('Should round the two numbers, and add a from b', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      expect(calculateNumber('SUM', 0.1, 0.3)).to.equal(0);
    });
  });

  describe('in the case of subtract', () => {
    it('Should round the two numbers, and subtract b from a', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      expect(calculateNumber('SUBTRACT', 0.1, 0.3)).to.equal(0);
    });
  });

  describe('in the case of divide', () => {
    it('Should round the two numbers, and divide a with b', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('Should return "Error" if division by zero', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });
});

