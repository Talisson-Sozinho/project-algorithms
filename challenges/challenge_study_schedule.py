def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time:
        return None

    count = 0

    for check_in, check_out in permanence_period:
        if (
            type(check_out) != int
            or type(check_in) != int
            or check_in > check_out
            or check_in < 0
            or check_out < 0
        ):
            return None

        if check_in <= target_time <= check_out:
            count += 1

    return count
