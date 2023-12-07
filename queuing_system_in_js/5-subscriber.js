import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', (err) => console.log('Redis client not connected to the server:', err));
subscriber.on('connect', () => console.log('Redis client connected to the server'));

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  } else console.log(message);
});
