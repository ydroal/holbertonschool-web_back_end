import kue from 'kue';

const queue = kue.createQueue();

// 指定したキューに新しいジョブが追加されるたびに呼び出される関数を定義
queue.process('push_notification_code', (job, done) => {
  let phoneNumber = job.data.phoneNumber;
  let message = job.data.message;
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  sendNotification(phoneNumber, message);
  done();
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
