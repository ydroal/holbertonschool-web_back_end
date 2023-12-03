const expect = require('chai').expect;
const request = require('request');

describe('get request to root', () => {
  it('returns status code 200', (done) => {
    request.get('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns correct message', (done) => {
    request.get('http://localhost:7865', (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('get request to cart page with parameter', () => {
  it('returns status code 200', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns correct message', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns status code 404', (done) => {
    request.get('http://localhost:7865/cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('post request to login page', () => {
  it('returns status code 200 and correct message', (done) => {
    const testReq = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: true,
      body: {
        userName: "Betty"
      }
    };

    request.post(testReq, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});

describe('get request to available_payments page', () => {
  it('returns correct message', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      const res = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
      expect(JSON.parse(body)).to.deep.equal(res);
      done();
    });
  });
});

