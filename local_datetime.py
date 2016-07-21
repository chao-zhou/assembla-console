from datetime import datetime
from dateutil import tz, parser


def is_today_local(date_str):
    central = to_local_time(date_str)
    local = datetime.now(tz.tzlocal())

    is_same_date = local.date() == central.date()
    return is_same_date


def to_local_time(date_str):
    date = parser.parse(date_str)
    return date.astimezone(tz.tzlocal())
