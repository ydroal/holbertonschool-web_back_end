import createEmployeesObject from './11-createEmployeesObject';
import createReportObject from './12-createReportObject';


jest.mock('./11-createEmployeesObject', () => ({
  __esModule: true,
  default: jest.fn().mockReturnValue({ engineering: ['Bob', 'Jane'], marketing: ['Sylvie'] }),
}));

describe('12-createReportObject', () => {
  it('should return a object with the key allEmployees and a method property', () => {
    const employees = createEmployeesObject('engineering', ['Bob', 'Jane'], 'marketing', ['Sylvie']);
    const report = createReportObject(employees);
    expect(report.allEmployees).toEqual({ engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] });
    expect(report.getNumberOfDepartments(report.allEmployees)).toBe(2);
  });
});
