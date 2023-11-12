import createEmployeesObject from './11-createEmployeesObject';


describe('createEmployeesObject', () => {
  it('should return a correct object', () => {
    const res = createEmployeesObject("Software", [ "Bob", "Sylvie" ]);
    expect(res).toEqual({ Software: [ 'Bob', 'Sylvie' ] });
  });
});

