import getSumOfHoods from './3-default-parameter.js';

describe('3-default-parameter', () => {
  it('should return correct number', () => {
    expect(getSumOfHoods(51)).toBe(159);
    expect(getSumOfHoods(52, 57)).toBe(128);
    expect(getSumOfHoods(55, 6, 46)).toBe(107);
  });
});
