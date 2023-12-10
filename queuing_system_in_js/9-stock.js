import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    Id: 1, 
    name: 'Suitcase 250', 
    price: 50, 
    stock: 4
  },
  {
    Id: 2, 
    name: 'Suitcase 450', 
    price: 100, 
    stock: 10
  },
  {
    Id: 3, 
    name: 'Suitcase 650', 
    price: 350, 
    stock: 2
  },
  {
    Id: 4, 
    name: 'Suitcase 1050', 
    price: 550, 
    stock: 5
  }
]

function getItemById(id) {
  return listProducts.find((element) => element.Id === id);
}

// redis
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

async function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client);

  try {
    await setAsync(`item.${itemId}`, stock - 1);
  } catch(err) {
      console.log(err);
  }
}

async function getCurrentReservedStockById (itemId) {
  const getAsync = promisify(client.get).bind(client);

  try {
    const stock = await getAsync(`item.${itemId}`);
    return stock;
    } catch(err) {
        console.log(err);
    } 
}

// express
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const stock= await getCurrentReservedStockById(itemId);
  const currentQuantity = stock !== null ? parseInt(stock) : item.stock;
  res.json({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const stock = await getCurrentReservedStockById(itemId);
  const stockInt = stock !== null ? parseInt(stock) : item.stock;
  
  if (stockInt <= 0) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
  } else {
    await reserveStockById(itemId, parseInt(stockInt));
    res.json({ status: 'Reservation confirmed', itemId: itemId });
    return;
  }
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
