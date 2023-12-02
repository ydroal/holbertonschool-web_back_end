const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise with the object when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then(response => {
        expect(response).to.deep.equal({data: 'Successful response from the API'});
        done();
      })
      .catch(error => {
        done(error);
      });
  });
});
