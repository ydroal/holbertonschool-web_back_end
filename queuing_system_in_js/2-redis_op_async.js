import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const asyncGet = promisify(client.get).bind(client);;

  try {
    const reply = await asyncGet(schoolName); 
  } catch (err) {
    console.log('Error:', err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
