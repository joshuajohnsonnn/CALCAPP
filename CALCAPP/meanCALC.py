# Now this is for Mean---------------------------------------------------------------
from __future__ import annotations


def mean_numbers(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def quartiles_iqr(values: list[float]) -> tuple[float, float, float]:
    """Return (Q1, Q3, IQR) using the median-of-halves method."""
    if len(values) < 4:
        # Not enough data for meaningful IQR-based anomaly detection.
        return (0.0, 0.0, 0.0)

    xs = sorted(values)
    n = len(xs)

    # Split into lower/upper halves (exclude median when n is odd)
    mid = n // 2
    lower = xs[:mid]
    upper = xs[mid:] if n % 2 == 0 else xs[mid + 1 :]

    def median(arr: list[float]) -> float:
        m = len(arr) // 2
        if len(arr) % 2 == 0:
            return (arr[m - 1] + arr[m]) / 2
        return arr[m]

    q1 = median(lower)
    q3 = median(upper)
    iqr = q3 - q1
    return q1, q3, iqr


def detect_anomalies_iqr(values: list[float], k: float = 1.5) -> list[float]:
    q1, q3, iqr = quartiles_iqr(values)
    if iqr == 0:
        return []

    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr

    return [v for v in values if v < lower_bound or v > upper_bound]


def compute_mean_with_anomaly_handling(values: list[float]) -> None:
    mean_all = mean_numbers(values)
    print(f"The mean of the numbers is: {mean_all}")

    anomalies = detect_anomalies_iqr(values)
    if not anomalies:
        print("No anomalies detected using the IQR (1.5x) rule.")
        return

    print("Anomalies detected (IQR rule):")
    print("  ", anomalies)

    while True:
        resp = input("Do you want to remove anomalies and recompute the mean? (y/n): ").strip().lower()
        if resp in {"y", "yes"}:
            anomaly_set = set(anomalies)
            filtered = [v for v in values if v not in anomaly_set]

            if not filtered:
                print("After removing anomalies, no data remains; cannot recompute mean.")
                return

            mean_filtered = mean_numbers(filtered)
            print(f"The mean after removing anomalies is: {mean_filtered}")
            return
        if resp in {"n", "no"}:
            print("Keeping anomalies. Mean remains unchanged.")
            return
        print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    # Input from the user (terminal)
    numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))

    # Calculate mean with anomaly detection/handling
    compute_mean_with_anomaly_handling(numbers)

