export default function createEmployeesObject(departmentName, employees) {
  const res = {
    [departmentName]: employees,
  };
  return res;
}
