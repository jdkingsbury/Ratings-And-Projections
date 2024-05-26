const { insertPlayerGameLog } = require('./insertQueries');

// NOTE: Map the data type to the corresponding insert function
const insertFunctionMap = {
  player_game_log: insertPlayerGameLog,
};

module.exports = insertFunctionMap;
