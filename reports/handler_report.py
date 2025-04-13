import re
from reports.ireport import IReport


class Handler(IReport):
    def __init__(self):
        self.pattern = re.compile(r"/\S+/")
        self.level_counts_template = {
            "DEBUG": 0,
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        }

    def worker(self, path: str):
        handlers = {}
        with open(path, "r") as file:
            for line in file:
                if "django.request" not in line:
                    continue
                level = line.split()[2]
                match = re.search(self.pattern, line)
                if match is None:
                    continue
                handler = match.group(0)
                if handler not in handlers:
                    handlers[handler] = self.level_counts_template.copy()

                handlers[handler][level] += 1
        return handlers

    def merge_results(self, results: list[dict]):
        merge = {}
        for result in results:
            for handler, values in result.items():
                if handler not in merge:
                    merge[handler] = values
                else:
                    for level, value in values.items():
                        merge[handler][level] += value
        return merge

    def make_report(self, result: dict):
        total_counts = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
        print(
            "HANDLER"
            + " " * 18
            + "".join(f"{head:<12}" for head in total_counts.keys())
        )

        for handler, value in sorted(result.items(), key=lambda x: x[0]):
            for level, count in value.items():
                total_counts[level] += count
            print(f"{handler:<25}" + "".join([f"{x:<12}" for x in value.values()]))

        print("_" * 80)
        print(" " * 25 + "".join([f"{x:<12}" for x in total_counts.values()]))
        print(f"Total requests: {sum([x for x in total_counts.values()])}")
