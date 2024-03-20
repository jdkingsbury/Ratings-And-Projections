import sys
from .db_operations import connect_to_database
from .data_retrieval import retrieval_function_mapping
from stats.stats_calculations import calculation_function_mapping

# Note: This function retrieves data from the database and then calculates a result based on the retrieved data
def retrieve_and_calculate_data(retrieval_function_identifier, calculation_function_identifier, *args):
    conn = connect_to_database()
    if not conn:
        raise Exception("Database connection failed")

    try:
        if retrieval_function_identifier in retrieval_function_mapping:
            retrieval_function = retrieval_function_mapping[retrieval_function_identifier]
            data = retrieval_function(conn, *args)

            if calculation_function_identifier in calculation_function_mapping:
                calculation_function = calculation_function_mapping[calculation_function_identifier]
                result = calculation_function(data)
                return result
            else:
                raise ValueError(f"Calculation function identifier '{calculation_function_identifier}' not recognized.")
        else:
            raise ValueError(f"Retrieval function identifier '{retrieval_function_identifier}' not recognized.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()


# NOTE: This is a simple command-line interface to the retrieve_and_calculate_data function
#      It is not part of the main application and is only used for testing
if __name__ == "__main__":
    def main():
        if len(sys.argv) < 4:
            print("Usage: python -m db.retrieve_data <retrieval_function> <calculation_function> <args>")
            sys.exit(1)

        retrieval_function_identifier = sys.argv[1]
        calculation_function_identifier = sys.argv[2]
        args = sys.argv[3:]

        try:
            result = retrieve_and_calculate_data(retrieval_function_identifier, calculation_function_identifier, *args)
            print(f"Calculation Result: {result}")
        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit(1)

    main()
