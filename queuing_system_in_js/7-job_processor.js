import kue from 'kue';

const queue = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // ジョブの進行状況を50%に更新
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();  
  }
};

// 指定したキューに新しいジョブが追加されるたびに呼び出される関数を定義
queue.process('push_notification_code2', (job, done) => {
  let phoneNumber = job.data.phoneNumber;
  let message = job.data.message;
  sendNotification(phoneNumber, message, job, done);
});
