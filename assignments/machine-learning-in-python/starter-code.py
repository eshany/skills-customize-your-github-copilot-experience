# Machine Learning in Python - Starter Code

from statistics import mean

# Sample data: [hours_studied, sleep_hours, exam_score]
DATA = [
    [1, 6, 58],
    [2, 6, 62],
    [3, 7, 68],
    [4, 7, 72],
    [5, 8, 78],
    [6, 8, 84],
]


def prepare_data(rows):
    """Split rows into features (X) and target values (y)."""
    x_values = []
    y_values = []
    for row in rows:
        x_values.append(row[:-1])
        y_values.append(row[-1])
    return x_values, y_values


def predict_with_simple_rule(features):
    """A simple baseline rule students can improve."""
    predictions = []
    for hours_studied, sleep_hours in features:
        prediction = 40 + (6 * hours_studied) + (2 * sleep_hours)
        predictions.append(prediction)
    return predictions


def mean_absolute_error(actual, predicted):
    errors = [abs(a - p) for a, p in zip(actual, predicted)]
    return mean(errors)


def main():
    x_values, y_values = prepare_data(DATA)

    print(f"Total samples: {len(DATA)}")
    print(f"First feature row: {x_values[0]}")
    print(f"First label: {y_values[0]}")

    predictions = predict_with_simple_rule(x_values)
    mae = mean_absolute_error(y_values, predictions)

    print("\nPredictions:", predictions)
    print(f"Mean Absolute Error: {mae:.2f}")


if __name__ == "__main__":
    main()
