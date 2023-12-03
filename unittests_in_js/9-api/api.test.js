const expect = require('chai').expect;
const request = require('request');

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

