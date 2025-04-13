import argparse
import os
import sys
from concurrent.futures import Future, ProcessPoolExecutor

from reports.handler_report import Handler
from reports.ireport import IReport

reports_handler: dict[str, type[IReport]] = {"handlers": Handler}


def map_reduce(reporter: IReport, files: list[str]):
    if len(files) == 1:
        result = reporter.worker(files[0])
        reporter.make_report(result)
        return

    futures: list[Future] = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        for file in files:
            futures.append(executor.submit(reporter.worker, file))

    results = []
    for future in futures:
        results.append(future.result())

    result = reporter.merge_results(results)
    reporter.make_report(result)


def main():
    parser = argparse.ArgumentParser(
        prog="Log Reporter",
        description="",
    )

    parser.add_argument("files", nargs="*", type=str, help="List files logs")
    parser.add_argument("--report", type=str, help="Type report")
    args = parser.parse_args()

    error = False

    files: list[str] = args.files
    report: str = args.report

    for file in files:
        if not os.path.isfile(file):
            print(f"File not exist: {file}")
            error = True

    if report not in reports_handler:
        print(f"Type report {report} not registered")
        error = True

    if error:
        sys.exit(1)

    reporter = reports_handler[report]()
    map_reduce(reporter, files)


if __name__ == "__main__":
    main()
