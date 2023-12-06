import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setHash(hashKey) {
  const hash = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  };
  
  for (const property in hash) {
    client.hset(hashKey, property, hash[property], redis.print);
  }
  
  client.hgetall(hashKey, (err, reply) => {
    if (err) console.log('Error:', err);
    else console.log(reply);
  });
}

setHash('HolbertonSchools');
