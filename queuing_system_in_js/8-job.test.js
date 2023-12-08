import kue from 'kue';
import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';


const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('should throw Error when argument(jobs) is not an array', () => {
    const arg = 'hello';
    expect(() => createPushNotificationsJobs(arg, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should adds new job when being passed an array', () => {
    const mockJobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];
    createPushNotificationsJobs(mockJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(mockJobs[1]);
  });
});

