import random
import math
import statistics


def generate_random_values(sample_size=100, lower_bound=1, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(sample_size)]


def compute_statistical_metrics(numeric_data):
    average = statistics.mean(numeric_data)  # Среднее арифметическое
    middle_value = statistics.median(numeric_data)  # Медиана
    sample_deviation = statistics.stdev(numeric_data)  # Стандартное отклонение
    sum_square_root = math.sqrt(sum(numeric_data))  # Квадратный корень из суммы
    rounded_root = round(sum_square_root, 2)  # Округление до 2 знаков

    return average, middle_value, sample_deviation, rounded_root


random_sample = generate_random_values()# Список из 100 случ. чисел

avg, med, stdev, root_sum = compute_statistical_metrics(random_sample)# Статистика

print(f"Среднее: {avg:.2f}, Медиана: {med}, Стандартное отклонение: {stdev:.2f}, Корень из суммы: {root_sum}")