import getNeighborhoodsList from './2-arrow';

describe('2-arrow', () => {
  it('should return correct list', () => {
    const neighborhoodsList = new getNeighborhoodsList();
    const res = neighborhoodsList.addNeighborhood('Noe Valley');
    expect(res).toEqual(['SOMA', 'Union Square', 'Noe Valley']);
  });
});
