"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    if temperature < 800:
        if neutrons_emitted > 500:
            if temperature * neutrons_emitted < 500000:
                return True
    return False

def reactor_efficiency(voltage, current, theorhetical_max_power): 
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    percentage_value = (generated_power / theorhetical_max_power) * 100
    if percentage_value < 30:
        return "black"
    elif 60 > percentage_value >= 30:
        return "red"
    elif 80 > percentage_value >= 60:
        return "orange"
    else:
        return "green"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    temp_x_npps = temperature * neutrons_produced_per_second
    if (.9 * threshold) > temp_x_npps:
        return "LOW"
    elif (.9 * threshold) < temp_x_npps:
        if (1.1 * threshold) >= temp_x_npps:
            return "NORMAL"
        return "DANGER"
    else:
        return "DANGER"