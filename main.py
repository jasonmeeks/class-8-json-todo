
"""
Usage:
main.py list -s done|pending|all(D)

main.py create [TASK NAME] -d [DESCRIPTION] -p [PENDING DUE DATE]

main.py complete id | [TASK NAME]

Homework:
* Add the "filter by date" functionality to list
"""
import os
import json
import click

import todos


def _debug(msg):
    ctx = click.get_current_context()
    if ctx.obj['debug']:
        click.echo(msg)


def _json_dumps(obj):
    ctx = click.get_current_context()
    return json.dumps(obj, indent=ctx.obj['indent'])


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('-i', '--indent', type=int, default=2)
@click.option('-f', '--data-file', default='todo_data.json')
@click.pass_context
def cli(ctx, debug, indent, data_file):
    ctx.obj['debug'] = debug
    ctx.obj['indent'] = indent
    _debug('Debug mode is %s' % ('on' if debug else 'off'))

    data_file_path = os.path.abspath(data_file)
    ctx.obj['data_file'] = data_file
    ctx.obj['data_file_path'] = data_file_path

    if not os.path.exists(data_file_path):
        with open(data_file_path, 'w') as fp:
            _debug('Task file created: {}'.format(data_file_path))
            tasks = todos.new()
            fp.write(_json_dumps(tasks))
    elif os.path.isdir(data_file_path):
        ctx.fail('Data file {} is a directory'.format(data_file))

    with open(data_file_path, 'r') as fp:
        # Task 1: Check the format of file and prevent:
        # json.decoder.JSONDecodeError
        ctx.obj['json_data'] = todos.unserialize(fp.read())
        _debug('Read tasks from task file {}'.format(data_file_path))


@cli.command()
@click.option(
    '-s', '--status',
    type=click.Choice(['all', 'pending', 'done']), default='pending')
@click.pass_context
def list(ctx, status):
    tasks = todos.list_tasks(ctx.obj['json_data'], status=status)
    summary = todos.summary(ctx.obj['json_data'])
    click.echo('{} tasks. {} pending. {} done.'.format(
        summary['total'], summary['pending'], summary['done']))

    print('-' * 60)
    tpl = "{:>10} | {:^30} | {:>10}"
    print(tpl.format('|        #', 'Task', 'Status       |'))
    print('-' * 60)
    for task in tasks:
        idx, name, due_on, status = task
        print(tpl.format(idx, name, status))

    print('-' * 60)


@cli.command()
@click.argument('name')
@click.option('-d', '--description')
@click.option('-p', '--due-on', help='Date Formats: 2018-01-01 19:30:51')
@click.pass_context
def create(ctx, name, description, due_on):
    tasks = ctx.obj['json_data']
    todos.create_task(
        tasks, name, description=description, due_on=due_on)

    serialized = todos.serialize(tasks)
    with open(ctx.obj['data_file_path'], 'w') as fp:
        fp.write(_json_dumps(serialized))


@cli.command()
@click.argument('name')
@click.pass_context
def complete(ctx, name):
    new_tasks = todos.complete_task(ctx.obj['json_data'], name)

    serialized = todos.serialize(new_tasks)
    with open(ctx.obj['data_file_path'], 'w') as fp:
        fp.write(_json_dumps(serialized))
    click.echo("Task {}. Done!".format(name))


if __name__ == '__main__':
    cli(obj={})
