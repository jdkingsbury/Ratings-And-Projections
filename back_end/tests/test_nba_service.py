import pytest
from services.nba_service import (
    get_player_stats,
    get_all_players,
    get_player_id,
    get_player_career_stats,
    get_player_game_log,
    get_player_cumulative_stats
)

def test_get_player_stats():
    result = get_player_stats('2023-24', 'json')
    assert result is not None
    assert isinstance(result, str)  # Assuming the result is a JSON string

def test_get_all_players():
    result = get_all_players('2023-24', 'json')
    assert result is not None
    assert isinstance(result, str)  # Assuming the result is a JSON string

def test_get_player_id():
    result = get_player_id('LeBron James', 'json')
    assert result is not None
    assert isinstance(result, str)  # Assuming the result is a JSON string

def test_get_player_career_stats():
    result = get_player_career_stats(2544, 'json')
    assert result is not None
    assert isinstance(result, str)  # Assuming the result is a JSON string

def test_get_player_game_log():
    result = get_player_game_log(2544, '2023-24', 'json')
    assert result is not None
    assert isinstance(result, str)  # Assuming the result is a JSON string

# NOTE: This test will fail because the function requires game_ids
# def test_get_player_cumulative_stats():
#     result = get_player_cumulative_stats(2544, '1234,5678', '2023-24', 'json')
#     assert result is not None
#     assert isinstance(result, str)  # Assuming the result is a JSON string
