import todos

from pprint import pprint


with open('sample_todos.json', 'r') as fp:
    tasks = todos.unserialize(fp.read())

# List tasks

task_list = todos.list_tasks(tasks)
pprint(task_list)


# Create task
"""
todos.create_task(tasks, 'Take out the trash')
pprint(tasks)
"""
# Complete task
"""
new_tasks = todos.complete_task(tasks, 'Review AWS proposal')
pprint(new_tasks)
"""
