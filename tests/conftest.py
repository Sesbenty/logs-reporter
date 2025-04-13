from pathlib import Path
import pytest
from reports.handler_report import Handler

@pytest.fixture
def handler_report():
    return Handler()

@pytest.fixture
def logs_file():
    logs = """2025-03-27 12:36:45,000 INFO django.request: GET /api/v1/checkout/ 201 OK [192.168.1.62]
    2025-03-27 12:35:19,000 WARNING django.security: SuspiciousOperation: Invalid HTTP_HOST header
    2025-03-27 12:10:18,000 DEBUG django.db.backends: (0.43) SELECT * FROM 'cart' WHERE id = 11;
    2025-03-27 12:26:18,000 WARNING django.security: ConnectionError: Failed to connect to payment gateway
    2025-03-27 12:20:50,000 DEBUG django.db.backends: (0.14) SELECT * FROM 'reviews' WHERE id = 76;
    2025-03-27 12:33:05,000 ERROR django.request: Internal Server Error: /api/v1/users/ [192.168.1.39] - PermissionDenied: User does not have permission
    2025-03-27 12:29:35,000 INFO django.request: GET /api/v1/orders/ 204 OK [192.168.1.67]
    2025-03-27 12:06:15,000 WARNING django.security: IntegrityError: duplicate key value violates unique constraint
    2025-03-27 12:10:49,000 CRITICAL django.core.management: OSError: No space left on device
    2025-03-27 12:42:07,000 INFO django.request: GET /api/v1/users/ 201 OK [192.168.1.22]
    2025-03-27 12:44:47,000 INFO django.request: GET /api/v1/payments/ 204 OK [192.168.1.57]
    2025-03-27 12:05:14,000 INFO django.request: GET /api/v1/auth/login/ 200 OK [192.168.1.28]
    2025-03-27 12:18:30,000 CRITICAL django.core.management: ValueError: Invalid input data"""
    
    file_path = Path("logs.log")
    file_path.write_text(logs)

    yield file_path.resolve()

    file_path.unlink()
    

