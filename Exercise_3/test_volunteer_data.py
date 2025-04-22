import pytest
from correct_script import calculate_average_hours, filter_by_city, load_data

DATA_FILE = "volunteer_data.csv"


def test_load_data_count():
    """All 5 rows (after header) should be loaded."""
    records = load_data(DATA_FILE)
    assert len(records) == 5


def test_filter_by_city_delhi_and_average():
    """Delhi should have 2 volunteers with average hours 3.0."""
    records = load_data(DATA_FILE)
    delhi = filter_by_city(records, "Delhi")
    assert len(delhi) == 2
    # 4 and 2 hours → avg = 3.0
    assert calculate_average_hours(delhi) == pytest.approx(3.0)


def test_filter_by_city_mumbai_and_average():
    """Mumbai should have 2 volunteers with average hours 4.5."""
    records = load_data(DATA_FILE)
    mumbai = filter_by_city(records, "mumbai")  # lowercase input
    assert len(mumbai) == 2
    # 3 and 6 hours → avg = 4.5
    assert calculate_average_hours(mumbai) == pytest.approx(4.5)


def test_filter_by_city_bangalore_and_average():
    """Bangalore should have 1 volunteer with 5 hours."""
    records = load_data(DATA_FILE)
    bengaluru = filter_by_city(records, "Bangalore")
    assert len(bengaluru) == 1
    assert calculate_average_hours(bengaluru) == pytest.approx(5.0)


def test_filter_nonexistent_city_empty():
    """Filtering a city not in the data should return an empty list."""
    records = load_data(DATA_FILE)
    nowhere = filter_by_city(records, "Nowhere")
    assert nowhere == []
