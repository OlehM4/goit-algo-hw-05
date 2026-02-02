import sys
from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    parts = line.strip().split()
    return {
      "date": parts[0],
      "time": parts[1],
      "level": parts[2],
      "message": " ".join(parts[3:])  
    }


def load_logs(file_path: str) -> list:
    log_list = []
    with open(file_path, "r") as file_log:
        for logs in file_log:
           parse_log = parse_log_line(logs)
           log_list.append(parse_log)
    return log_list


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    count_log = defaultdict(int)
    for log in logs:
        level = log.get("level")
        if level:
            count_log[level] += 1
    return dict(count_log)


def display_log_counts(counts: dict):    
    message = "Рівень логування | Кількість\n-----------------|----------\n"
    for level, value in counts.items():
        message += f"{level:<17}| {value}\n"
    return message


def dict_to_string(logs: list) -> str:
    for log in logs:
        print(" ".join(v for v in log.values()))
   

def main():
    file_log_path = Path("logs.txt")
    logs = load_logs(file_log_path)
    
    try:
        if len(sys.argv) >= 2:
            print(display_log_counts(count_logs_by_level(logs)))
            
        if len(sys.argv) >= 3:
            level = sys.argv[2]
            print(f"Деталі логів для рівня '{level.upper()}':")
            dict_to_string(filter_logs_by_level(logs, level))
    except Exception as e:
        return e

if __name__ == "__main__":
    main()