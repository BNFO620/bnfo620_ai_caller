import re
from models import Interval


def parse_interval(interval: str | None) -> Interval:

    if not interval:
        return Interval(None, None, interval)

    interval = interval.replace("–", "-")
    # TODO: add annotations for the regex pattern
    is_match = re.match(r"\s*(-?\d+(?:\.\d+)?)\s*-\s*(-?\d+(?:\.\d+)?)\s*$", interval)

    if not is_match:
        return Interval(None, None, interval)

    return Interval(float(is_match.group(1)), float(is_match.group(2)), interval)
