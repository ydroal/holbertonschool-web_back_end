import kue from 'kue';

const queue = kue.createQueue();

function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');
  
  jobs.forEach(element => {
    // job.save() を呼び出す前に job オブジェクトを定義
    const job = queue.create('push_notification_code_3', element);
    job.save(err => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);

    }).on('failed', error => {
      console.log(`Notification job ${job.id} failed`, error);

    }).on('progress', progress => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
