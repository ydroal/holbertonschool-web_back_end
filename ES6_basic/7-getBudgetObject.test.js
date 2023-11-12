import getBudgetObject from './7-getBudgetObject';

describe('getBudgetObject', () => {
  it('should return correct object', () => {
    expect.assertions(1);
    const test = getBudgetObject(400, 700, 900);
    expect(test).toStrictEqual({ income: 400, gdp: 700, capita: 900 });
  });
});
