const fs = require('fs');
const path = require('path');
const readJsonFile = require('../db/readJson');

describe('readJsonFile', () => {
  const testFilePath = path.join(__dirname, 'testData.json');
  const validJsonData = [
    {
      "SEASON_ID": "22023",
      "Player_ID": 2544,
      "Game_ID": "0022301195",
      "GAME_DATE": "APR 14, 2024",
      "MATCHUP": "LAL @ NOP",
      "WL": "W",
      "MIN": 38,
      "FGM": 11,
      "FGA": 20,
      "FG_PCT": 0.55,
      "FG3M": 0,
      "FG3A": 2,
      "FG3_PCT": 0.0,
      "FTM": 6,
      "FTA": 6,
      "FT_PCT": 1.0,
      "OREB": 2,
      "DREB": 9,
      "REB": 11,
      "AST": 17,
      "STL": 5,
      "BLK": 1,
      "TOV": 4,
      "PF": 0,
      "PTS": 28,
      "PLUS_MINUS": 19
    }
  ];

  beforeAll(() => {
    fs.writeFileSync(testFilePath, JSON.stringify(validJsonData), 'utf-8');
  });

  afterAll(() => {
    fs.unlinkSync(testFilePath);
  });

  it('should read and parse a valid JSON file', () => {
    const data = readJsonFile(testFilePath);
    expect(data).toEqual(validJsonData);
  });

  it('should throw an error if the file does not exist', () => {
    const invalidFilePath = 'nonexistent.json';
    expect(() => readJsonFile(invalidFilePath)).toThrow();
  });

  it('should throw an error if the file contains invalid JSON', () => {
    const invalidJsonFilePath = path.join(__dirname, 'invalidData.json');
    fs.writeFileSync(invalidJsonFilePath, 'invalid json', 'utf-8');

    expect(() => readJsonFile(invalidJsonFilePath)).toThrow();

    fs.unlinkSync(invalidJsonFilePath);
  });
});
