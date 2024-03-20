import sys
from pathlib import Path
from .db_operations import connect_to_database
from .json_reader import read_json_file
from .data_insertion import insert_function_mapping


# NOTE: This function inserts data into the database based on the function identifier and the data provided
def insert_data(function_identifier, data):
    conn = connect_to_database()
    if conn is None:
        print("Database connection failed")
        return

    try:
        if function_identifier in insert_function_mapping:
            insertion_function = insert_function_mapping[function_identifier]
            insertion_function(conn, data)
        else:
            raise ValueError(f"Function identifier '{function_identifier}' not recognized.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


# NOTE: This is a simple command-line interface to the insert_data function
#      It is not part of the main application and is only used for testing
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <json_file_path> <table_name>")
        sys.exit(1)

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
        sys.exit(1)

    insert_data(function_identifier, data)
