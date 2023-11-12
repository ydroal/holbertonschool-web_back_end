import getFullBudgetObject from './9-getFullBudget';
import getBudgetObject from './7-getBudgetObject';

jest.mock('./7-getBudgetObject', () => ({
  __esModule: true, 
  default: jest.fn(),
}));

describe('getFullBudgetObject', () => {
  it('should return a full budget object', () => {
    const income = 1000;
    const gdp = 5000;
    const capita = 2000;

    // return valueのセット
    getBudgetObject.mockReturnValue({ income, gdp, capita });

    const fullBudget = getFullBudgetObject(income, gdp, capita);

    expect(getBudgetObject).toHaveBeenCalledWith(income, gdp, capita);

    expect(fullBudget.getIncomeInDollars(income)).toBe(`$${income}`);

    expect(fullBudget.getIncomeInEuros(income)).toBe(`${income} euros`);
  });
});
