from datetime import datetime, timezone

# The target date and time
target_datetime_str = "1970-01-01 00:00:00.001"
target_datetime = datetime.strptime(target_datetime_str, "%Y-%m-%d %H:%M:%S.%f")
target_datetime = target_datetime.replace(tzinfo=timezone.utc)

# Convert to Unix timestamp in milliseconds
unix_timestamp_ms = int(target_datetime.timestamp() * 1000)

print(unix_timestamp_ms)
