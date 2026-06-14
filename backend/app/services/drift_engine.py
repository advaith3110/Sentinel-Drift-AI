def detect_drift(current_config, baseline_config):

    drifts = []

    for key, expected_value in baseline_config.items():

        current_value = current_config.get(key)

        if current_value != expected_value:

            drifts.append({
                "control": key,
                "expected": expected_value,
                "current": current_value,
                "status": "Drift Detected"
            })

    return drifts