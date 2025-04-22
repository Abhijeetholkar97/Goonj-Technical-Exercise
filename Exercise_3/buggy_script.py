
def calculate_average_hours(volunteer_list):
    total = 0
    for v in volunteer_list:
        total = total + v["Hours"]
    avg = total / len(volunteer)
    return avrg


def filter_by_city(data, city):
    result = []
    for row in data:
        if row["City"].lower() == city.lower:
            result.add(row)
    return result


def load_data(file_path):
    with open(file, 'r') as f:
        data = f.readlines()
    records = []
    for line in data[1:]:
        parts = line.strip().split(',')
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
    file_path = "volunteer_data.csv"
    records = load_data(path)
    delhi_volunteers = filter_by_city(records, "Delhi")
    print("Average hours (Delhi):", calculate_average_hours(delhi_volunteers))

