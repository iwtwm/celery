from celery import Celery

from branch_dictionary import branch_coverage
from unittest.mock import Mock, patch

# Function to print branch coverage
def print_branch_coverage():
    print("\nBranch Coverage:\n")
    s = ""
    for key, value in branch_coverage.items():
        s += f"{key} is covered: {value}\n"
    print(s)

def run_handle_conf_update(app):
    app.amqp._handle_conf_update("task_routes")
    app.amqp._handle_conf_update()

def run_worker_main(app):
    with patch.object(Celery, 'start', return_value=None) as mock_start:
        try:
            app.worker_main(argv=None)
        except ValueError:
            pass
        try:
            app.worker_main(argv=['TestValue'])
        except ValueError:
            pass
        app.worker_main(argv=['worker'])

# Function to run all tests and print coverage
def run_coverage():
    app = Celery()

    run_handle_conf_update(app)
    run_worker_main(app)
    
    print_branch_coverage()

if __name__ == '__main__':
    run_coverage()