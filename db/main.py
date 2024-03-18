import sys
from pathlib import Path
from .db_operations import connect_to_database
from .json_reader import read_json_file
from .data_insertion import function_mapping


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <json_file_path> <table_name>")
        return

    function_identifier = sys.argv[1]
    args = sys.argv[2:]
    args_string = "_".join(map(str, args))
    current_script_path = Path(__file__).parent
    json_file_name = f"{function_identifier}_{args_string}.json"
    json_file_path = current_script_path / f"../data/{json_file_name}"
    absolute_json_file_path = json_file_path.resolve()

    data = read_json_file(absolute_json_file_path)

    if data is None:
        print(f"Error: File {json_file_path} not found")
        return

    conn = connect_to_database()

    if conn is not None and function_identifier in function_mapping:
        insertion_function = function_mapping[function_identifier]
        insertion_function(conn, data)
        conn.close()
    else:
        print(f"Function identifier '{function_identifier}' not recognized.")


if __name__ == "__main__":
    main()
