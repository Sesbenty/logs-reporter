def test_merge_result(handler_report):
    result1 = {
        "/admin/dashboard/": {
            "DEBUG": 5,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/reviews/": {
            "DEBUG": 1,
            "INFO": 2,
            "WARNING": 3,
            "ERROR": 4,
            "CRITICAL": 5,
        },
    }
    result2 = {
        "/api/v1/payments/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/reviews/": {
            "DEBUG": 5,
            "INFO": 4,
            "WARNING": 3,
            "ERROR": 2,
            "CRITICAL": 1,
        },
    }
    merge = {
        "/admin/dashboard/": {
            "DEBUG": 5,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/reviews/": {
            "DEBUG": 6,
            "INFO": 6,
            "WARNING": 6,
            "ERROR": 6,
            "CRITICAL": 6,
        },
        "/api/v1/payments/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
    }
    assert merge == handler_report.merge_results([result1, result2])


def test_worker(handler_report, logs_file):
    res = {
        "/api/v1/checkout/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/users/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 1,
            "CRITICAL": 0,
        },
        "/api/v1/orders/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/payments/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/auth/login/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
    }

    assert handler_report.worker(logs_file) == res
