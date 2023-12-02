function getPaymentTokenFromAPI(success) {
  if (success) {
    return new Promise((resolve) => {
      const res = {data: 'Successful response from the API' }
      resolve(res);
    });
  }
}

module.exports = getPaymentTokenFromAPI;
