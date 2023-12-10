import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const client = createClient();
const queue = kue.createQueue();
let reservationEnabled = true;

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');
  reserveSeat(50);
});

async function reserveSeat (number) {
  const setAsync = promisify(client.set).bind(client);
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const getAsync = promisify(client.get).bind(client);
  return await getAsync('available_seats');
}

// express
const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if(err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
   });

   job.on('complete', () => {
     console.log(`Seat reservation job ${job.id} completed`);
   
   }).on('failed', (errorMessage) => {
     console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
   });
});


app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats === 0) {
      reservationEnabled = false;
    } else if (currentSeats > 0 && reservationEnabled) {
      await reserveSeat(currentSeats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
