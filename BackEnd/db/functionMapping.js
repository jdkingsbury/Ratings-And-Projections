const { insertPlayerGameLog } = require("./insertQueries");
const { retrievePlayerGameLog } = require("./retrieveQueries");

// NOTE: Map the data type to the corresponding insert function
const insertFunctionMap = {
  'player_game_log': insertPlayerGameLog,
};

// NOTE: Map the data type to the corresponding retrieve function
const retrieveFunctionMap = {
  'player_game_log': retrievePlayerGameLog,
};

module.exports = { 
  insertFunctionMap, 
  retrieveFunctionMap,
};
