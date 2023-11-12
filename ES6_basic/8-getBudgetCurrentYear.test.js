import getBudgetForCurrentYear from './8-getBudgetCurrentYear';

describe('8-getBudgetCurrentYear', () => {
  it('should return correct object', () => {
    const currentYear = new Date().getFullYear();
    const res = getBudgetForCurrentYear(2100, 5200, 1090);
    expect(res).toEqual({
      [`income-${currentYear}`]: 2100, 
      [`gdp-${currentYear}`]: 5200, 
      [`capita-${currentYear}`]: 1090
    });
  });
});
