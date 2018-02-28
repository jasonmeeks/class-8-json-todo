
"""
main.py list -f done|pending|all(D)

main.py create -t [TASK NAME] -d [DESCRIPTION] -p [PENDING DUE DATE]

main.py complete id -t [TASK NAME]

Homework:
* Add the "filter by date" functionality to list
"""
import os
import json
import click

import todos


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('-f', '--data-file', default='todo_data.json')
@click.pass_context
def cli(ctx, debug, data_file):
    data_file_path = os.path.abspath(data_file)
    ctx.obj['data_file'] = data_file
    ctx.obj['data_file_path'] = data_file_path

    if not os.path.exists(data_file_path):
        with open(data_file_path, 'w') as fp:
            tasks = todos.new()
            fp.write(json.dumps(tasks))
    elif os.path.isdir(data_file_path):
        ctx.fail('Data file {} is a directory'.format(data_file))

    with open(data_file_path, 'r') as fp:
        # Task 1: Check the format of file and prevent:
        # json.decoder.JSONDecodeError
        ctx.obj['json_data'] = json.loads(fp.read())

    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
@click.option(
    '-s', '--status',
    type=click.Choice(['all', 'pending', 'done']), default='pending')
@click.pass_context
def list(ctx, status):
    tasks = todo.list_tasks(ctx.obj['json_data'], status=status)
    for task in tasks:
        pass


@cli.command()
def create(ctx):
    click.echo('Creating')


sample = [
    {
        'task': 'Email team updates',
        'description': (
            'The email must contain the latest changes and planned '
            'actions for the following weeks'),
        'due_on': '2018-03-01T09:00:00',
        'status': 'pending'
    }
]

if __name__ == '__main__':
    # cli(obj={})
