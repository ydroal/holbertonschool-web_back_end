import { createClient } from 'redis';

const client = createClient();

async function connectToServer() {
  client.on('error', (err) => console.log('Redis client not connected to the server:', err));

  try {
    await client.connect();
    console.log('Redis client connected to the server')
  } catch (err) {
  }
}

connectToServer();
