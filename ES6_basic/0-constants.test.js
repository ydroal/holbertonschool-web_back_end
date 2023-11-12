import { taskFirst, taskNext } from './0-constants';

describe('0-constants', () => {
  describe('taskFirst', () => {
    it('should return correct string', () => {
      expect(taskFirst()).toBe('I prefer const when I can.');
    });
  });

  describe('taskNext', () => {
    it('should return correct string', () => {
      expect(taskNext()).toBe('But sometimes let is okay');
    });
  });
});

