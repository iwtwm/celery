from celery import Celery

from branch_dictionary import branch_coverage

# Function to print branch coverage
def print_branch_coverage():
    print("\nBranch Coverage:\n")
    s = ""
    for key, value in branch_coverage.items():
        s += f"{key} is covered: {value}\n"
    print(s)

# Function to run tests and print coverage
def run_coverage():
    app = Celery()

    # run first and second branch of _verify_seconds
    try:
        app.amqp._verify_seconds(-2147483648 - 1, "TestValue")
    except ValueError as e:
        e.__traceback__ = None
    app.amqp._verify_seconds(-2147483648, "TestValue")

    print_branch_coverage()

if __name__ == '__main__':
    run_coverage()