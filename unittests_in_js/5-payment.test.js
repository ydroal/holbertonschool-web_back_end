const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let spy;

  beforeEach(() => {
    // 各テストの前にconsole.logのスパイを設定
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // 各テストの後にスパイをリストア
    spy.restore();
  });

  it('function called with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 120')).to.be.true;
  });

  it('function called with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 20')).to.be.true;
  });
});
