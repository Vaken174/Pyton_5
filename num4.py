import random
from datetime import datetime, timedelta
from array import array


def get_random_date_in_range(range_start, range_end):
    date_range = range_end - range_start
    random_day_offset = random.randint(0, date_range.days)
    return range_start + timedelta(days=random_day_offset)


def create_random_dates_array(dates_count=10):
    """Генерирует массив случайных дат за последние 5 лет"""
    current_date = datetime.now()
    five_years_ago = current_date - timedelta(days=5 * 365)

    timestamp_array = array('l')

    for _ in range(dates_count):
        random_date = get_random_date_in_range(five_years_ago, current_date)
        timestamp_array.append(int(random_date.timestamp()))

    return timestamp_array


def compute_date_intervals(timestamps_array):
    day_differences = []
    for idx in range(len(timestamps_array) - 1):
        first_date = datetime.fromtimestamp(timestamps_array[idx])
        second_date = datetime.fromtimestamp(timestamps_array[idx + 1])

        date_interval = abs(second_date - first_date)
        day_differences.append(date_interval.days)

        print(f"Интервал между {first_date.date()} и {second_date.date()}: {date_interval.days} дней")

    return day_differences


date_timestamps = create_random_dates_array()

print("\nИнтервалы между соседними датами:")
date_intervals = compute_date_intervals(date_timestamps)