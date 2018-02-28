from datetime import datetime

from .exceptions import (
    InvalidTaskStatus, TaskAlreadyDoneException, TaskDoesntExistException)
from .utils import parse_date, parse_int


def new():
    pass


def create_task(tasks, name, description=None, due_on=None):
    pass


def list_tasks(tasks, status='all'):
    pass


def complete_task(tasks, name):
    pass
