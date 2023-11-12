import returnHowManyArguments from './4-rest-parameter.js';

describe('4-rest-parameter', () => {
  it('should return correct number', () => {
	  expect(returnHowManyArguments("ab", 123, 500)).toBe(3);
	  expect(returnHowManyArguments()).toBe(0);
  });
});
