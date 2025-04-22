def calculate_average_hours(volunteer_list):
    """Calculate average hours; returns 0 if list is empty."""
    # Avoid division by zero
    if not volunteer_list:
        return 0

    total = 0
    for v in volunteer_list:
        total += v["Hours"]
    # Use volunteer_list, not undefined volunteer
    avg = total / len(volunteer_list)
    return avg  # return avg, not avrg


def filter_by_city(data, city):
    """Return list of records where City matches (case-insensitive)."""
    result = []
    for row in data:
        # Call city.lower() correctly and compare
        if row["City"].lower() == city.lower():
            # Append to list, not add()
            result.append(row)
    return result


def load_data(file_path):
    """Load CSV-like data into a list of dicts."""
    records = []
    # Use the passed-in file_path, not undefined 'file'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Skip header
    for line in lines[1:]:
        parts = line.strip().split(',')
        # Expecting at least 5 columns
        if len(parts) < 5:
            continue
        record = {
            "Volunteer_ID": parts[0],
            "Name": parts[1],
            "City": parts[2],
            "Hours": int(parts[3]),   
            "Date": parts[4]
        }
        records.append(record)
    return records


if __name__ == "__main__":
    # Use the correct variable name when calling load_data
    file_path = "volunteer_data.csv"
    try:
        records = load_data(file_path)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        exit(1)
    except ValueError as e:
        print(f"Error parsing data: {e}")
        exit(1)

    delhi_volunteers = filter_by_city(records, "Delhi")
    avg_hours = calculate_average_hours(delhi_volunteers)
    print("Average hours (Delhi):", avg_hours)
