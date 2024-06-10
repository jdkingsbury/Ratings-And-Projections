import os
import pytest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.create_file import main as create_file_main

def test_create_file():
    # Mock command line arguments
    sys.argv = ["create_file.py", "get_player_game_log", "json", "2544", "2023-24"]
    create_file_main()

    # Check if file was created
    file_name = "get_player_game_log_2544_2023-24.json"
    file_path = os.path.join("data", file_name)
    assert os.path.exists(file_path)

    # Clean up
    os.remove(file_path)
