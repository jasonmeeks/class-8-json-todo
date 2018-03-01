# Python / JSON TODOs

# Install

```bash
$ mkvirtualenv todos -p /usr/bin/python3
$ pip install -r requirements.txt
```

# Usage

**General:**

```bash
$ python main.py --help
$ python main.py --debug
```

**List todos**
```bash
$ python main.py list 
$ python main.py list -s pending
$ python main.py list -s done
$ python main.py list -s all
```


**Create todos**
```bash
$ python main.py create "My TODO Task"
$ python main.py create "My TODO Task" -d "Much description, wow"
$ python main.py create "My TODO Task" -d "Much description, wow" -p "2018-03-05"
$ python main.py create "My TODO Task" -d "Much description, wow" -p "2018-03-05 19:25:33"
```

**Complete task**
```bash
$ python main.py complete "My TODO Task"
$ python main.py complete 1  # by order/id
```

### Student's Tasks

##### Create tasks Invalid Due Dates

**Test:** `test_create_new_task_invalid_due_date`

```bash
$ py.test tests.py --tb=short -k invalid_due_date
```

##### List tasks with invalid status

**Test:** `test_list_invalid_status_task`

```bash
$ py.test tests.py --tb=short -k status_task

```

##### Complete tasks by ID

**Test:** `test_complete_task_by_id`

```bash
$ py.test tests.py --tb=short -k task_by_id

```

##### Raise if the task is already done

**Test:** `test_complete_task_already_done`

```bash
$ py.test tests.py --tb=short -k task_already_done

```

##### Raise if the task doesn't exist

**Test:** `test_complete_task_doesnt_exist_fails`

```bash
$ py.test tests.py --tb=short -k doesnt_exist

```
