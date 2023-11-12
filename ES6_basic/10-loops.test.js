import appendToEachArrayValue from './10-loops';


describe('appendToEachArrayValue', () => {
  it('should return a correct list', () => {
    const res = appendToEachArrayValue(['appended', 'fixed', 'displayed'], 'correctly-');
    expect(res).toEqual([ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ]);
  });
});
