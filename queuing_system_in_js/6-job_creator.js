import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the test message',
};

let job = queue.create('push_notification_code', jobData).save((err) => {
  if(err) {
    console.error(err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
 });

job.on('complete', () => {
  console.log('Notification job completed');

}).on('failed', () => {
  console.log('Notification job failed');
});
