const request = require('supertest');
const express = require('express');
const fetchRoutes = require('../routes/fetch');

const app  = express();
app.use('/fetch', fetchRoutes);


/**
 * @test {GET /fetch/:functionName}
 * @description Test the /fetch/:functionName endpoint.
 */

describe('GET /fetch/:functionName', () => {
  test('Should return a file if it exists', async () => {
    const response = await request(app)
      .get('/fetch/get_player_game_log')
      .query({ player_id: 2544, season_year: '2023-24', output_format: 'json' });

    expect(response.status).toBe(200);
  });

  test('Should execute Python script and return the generated file', async () => {
    const response = await request(app)
      .get('/fetch/get_player_game_log')
      .query({ player_id: 2544, season_year: '2023-24', output_format: 'json' });
    expect(response.status).toBe(200);
  });
});

