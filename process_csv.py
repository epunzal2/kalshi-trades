import csv

def process_settlement_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        return [
            {
                "type": row[0],
                "Original_Date": row[1],
                "Market_Ticker": row[2],
                "Result": row[3],
                "Profit_In_Dollars": float(row[4]),
                "Yes_Contracts_Owned": int(row[5]),
                "Yes_Contracts_Average_Price_In_Cents": float(row[6]),
                "No_Contracts_Owned": int(row[7]),
                "No_Contracts_Average_Price_In_Cents": float(row[8]),
            }
            for row in csv.reader(file) if len(row) >= 9
        ]

def calculate_settlement_profit(row):
    # simple settlement calculation for now
    if row["Result"] == "yes":
        # contract_return - (what I paid for the contracts)
        return (
            row["Yes_Contracts_Owned"]
            - (
                (row["Yes_Contracts_Owned"] * row["Yes_Contracts_Average_Price_In_Cents"])
                + (row["Yes_Contracts_Owned"] * row["Yes_Contracts_Average_Price_In_Cents"])
            )
        )
    else:
        return (
            row["No_Contracts_Owned"]
            - (
                (row["Yes_Contracts_Owned"] * row["Yes_Contracts_Average_Price_In_Cents"])
                + (row["Yes_Contracts_Owned"] * row["Yes_Contracts_Average_Price_In_Cents"])
            )
        )

