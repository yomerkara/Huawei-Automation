import pandas as pd
from user_input import ask_user_questions

# Define sector-specific orders
output_file = "output.xlsx"
    
sector1_order = ['A', 'B']
sector2_order = ['A', 'D', 'B', 'E']
sector3_order = ['A', 'D', 'G', 'B', 'E', 'H']
sector4_order = ['A', 'D', 'G', 'J', 'B', 'E', 'H', 'K']

# Define custom sorting functions for each sector
def get_custom_order_function(order):
    def custom_order(item):
        last_char = item[-1] if isinstance(item, str) and len(item) > 0 else ''
        return order.index(last_char) if last_char in order else len(order)
    return custom_order

sector_sort_functions = {
    "1": get_custom_order_function(sector1_order),
    "2": get_custom_order_function(sector2_order),
    "3": get_custom_order_function(sector3_order),
    "4": get_custom_order_function(sector4_order)
}

def filter_excel_with_answers(user_answers):
    sourceFile = r"./output.xlsx"
    cddSheetName = "3G_CDD"
    ipSheetName = "IP_PLAN"
    
    # Load the Excel file
    df = pd.read_excel(sourceFile, sheet_name=cddSheetName)
    df2 = pd.read_excel(sourceFile, sheet_name=ipSheetName)
    
    # Apply filters from user answers
    for key, value in user_answers.items():
        if key == "saha_kodu":
            df = df[df["NodeB Name"] == value]
            df2 = df2[df2["SITE"] == value[1:]]
        elif key == "sector_number":
            # Get the sort function based on the sector number
            if df.empty:  # Exit early if no data is left
                print("No data left after filtering.")
                break  # Exit the function if no data remains
            sort_function = sector_sort_functions.get(value)
            if sort_function:
                # Check if 'Cell Name' exists in the DataFrame
                if 'Cell Name' in df.columns:
                    print(f"Sorting 'Cell Name' with sector number {value}...")
                    # Apply the sorting function
                    try:
                        # Apply the sorting function to get sort indices
                        sort_indices = df['Cell Name'].apply(sort_function)
                        print(f"Sorting indices before sorting:\n{sort_indices}")

                        # Sort the indices and get valid index positions
                        sorted_indices = sort_indices.argsort()
                        print(f"Sorted indices:\n{sorted_indices}")

                        # Check if sorted_indices are still valid for the current DataFrame
                        if sorted_indices.max() < len(df):
                            df_sorted = df.iloc[sorted_indices].reset_index(drop=True)
                            df = df_sorted  # Update df with sorted data
                        else:
                            print("Warning: Some indices are out of bounds after sorting.")
                            return  # Exit if any indices are out of bounds
                    except Exception as e:
                        print(f"Error occurred during sorting: {e}")
                else:
                    print("Warning: 'Cell Name' column not found.")
                    return  # Exit if 'Cell Name' does not exist
            else:
                print(f"Warning: No sort function defined for sector {value}")

    # Display filtered data
    print("\nFiltered Excel Data:\n", df)
    print("\nFiltered Excel Data:\n", df2)

    # Optionally, save the filtered data to a new Excel file
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name="3G_CDD", index=False)
        df2.to_excel(writer, sheet_name="IP_PLAN", index=False)

