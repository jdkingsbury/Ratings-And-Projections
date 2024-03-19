import sys
from .db_operations import connect_to_database
from .data_retrieval import retrieval_function_mapping
from ..stats.stats_calculations import calculation_function_mapping


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python retrieve_data.py <retrieval_function> <calculation_function> [args]"
        )
        return

    retrieval_function_identifier = sys.argv[1]
    calculation_function_identifier = sys.argv[2]
    args = sys.argv[3:]

    conn = connect_to_database()

    if conn and retrieval_function_identifier in retrieval_function_mapping:
        data = retrieval_function_mapping[retrieval_function_identifier](conn, *args)

        if data and calculation_function_identifier in calculation_function_mapping:
            result = calculation_function_mapping[calculation_function_identifier](data)
            print(f"Calculation Result: {result}")
        else:
            print(
                f"Calculation function identifier '{calculation_function_identifier}' not recognized."
            )

        conn.close()
    else:
        print(
            f"Retrieval function identifier '{retrieval_function_identifier}' not recognized or connection failed."
        )


if __name__ == "__main__":
    main()
