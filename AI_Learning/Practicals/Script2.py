import csv

def analyze_csv(file_path):
    data = {}

    # Read csv file using 
    with open(file_path, mode='r') as file:
        reader: csv.DictReader[str] = csv.DictReader(file)

        # Initialize dictionary for numeric columns
        for field in reader.fieldnames:
            data[field] = []

        # Calculate the data

        for row in reader:
            for field in row:
                try:
                    value = float(row[field])
                    data[field].append(value)
                except ValueError:
                    pass

    # Calculate sun ans mean
    print("\n CSV Anylsis report")
    for field, values in data.items():
        if values:
            total = sum(values)
            mean = total / len(values)
            print(f"\n column: {field}")
            print(f"Sum: {total}")
            print(f"Mean: {mean}")
        else:
            print(f"\n column: {field} (No Numeric Data)")

file_path = "text_script2.csv"
analyze_csv(file_path)
