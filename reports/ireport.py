from abc import abstractmethod


class IReport:
    @abstractmethod
    def worker(self, path: str):
        raise NotImplementedError

    @abstractmethod
    def merge_results(self, results):
        raise NotImplementedError

    @abstractmethod
    def make_report(self, result):
        raise NotImplementedError
