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
