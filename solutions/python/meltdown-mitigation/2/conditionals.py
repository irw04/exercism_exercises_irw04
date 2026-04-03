"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if float(temperature) < 800.00 and 500.00 < float(neutrons_emitted) and (float(temperature) * float(neutrons_emitted)) < 500000.00:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ((voltage * current) / theoretical_max_power) *100

    if efficiency >= 80:
        return "green"
    elif 60 <= efficiency:
        return "orange"
    elif 30 <= efficiency:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second

    if value < (threshold * .9):
        return "LOW"
    elif (threshold * .9) <= value <= (threshold * 1.1):
        return "NORMAL"
    else: 
        return "DANGER"  
