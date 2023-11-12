import concatArrays from './5-spread-operator.js';

describe('concatArrays', () => {
  test('Console log should have been called with the correct values', () => {
    const logSpy = jest.spyOn(console, 'log');

    concatArrays(['a', 'b'], ['c', 'd'], 'Hello');
    expect(logSpy).toHaveBeenCalled();
    expect(logSpy.mock.calls[0]).toEqual([
      ['a', 'b', 'c', 'd', 'H', 'e', 'l', 'l', 'o']
    ]);

    logSpy.mockRestore();
  });
});

