import sys
from .db_operations import connect_to_database
from .data_retrieval import retrieval_function_mapping

def retrieve_data(retrieval_function_identifier, *args):
    conn = connect_to_database()
    if not conn:
        raise Exception("Database connection failed")

    try:
        if retrieval_function_identifier in retrieval_function_mapping:
            retrieval_function = retrieval_function_mapping[retrieval_function_identifier]
            data = retrieval_function(conn, *args)
            return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

if __name__ == "__main__":

    def main():
        if len(sys.argv) < 2:
            print("Usage: python retrieve_data.py <retrieval_function> <arg1> <arg2> ...")
            sys.exit(1)

        retrieval_function_identifier = sys.argv[1]
        args = sys.argv[2:]

        try:
            result = retrieve_data(retrieval_function_identifier, *args)
            print(result)

        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit(1)

    main()
