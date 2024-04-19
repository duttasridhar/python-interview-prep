# Python Interview Preparation

Thanks for interviewing at Averlon.
To make sure that we can use our time best in the interviews,
we'd like to have you do some setup on your laptop in advance.

First, _clone_ or _download_ this repository to your computer
via the links on the right
(creating a fork of the repository is not necessary).

Note, we will be working with **Python 3** (Python 3.6 or later).
See the [RealPython installation guide], if you haven't installed Python 3 yet.

We'll create a [virtual environment] with [venv]
and install some Python packages

**Create a new virtual environment** called `interview_env` and _activate_ it.

```bash
$ python3 -m venv ./interview_env
$ source ./interview_env/bin/activate
```

The `activate` script is for Bash and Zsh on Mac or Linux.
For other shells, such as Fish or Csh, see the [venv] documentation.

On Windows (assuming `cmd.exe`):

```batch
> python3 -m venv .\interview_env
> .\interview_env\Scripts\activate
```

Next, **install some requirements** into the activated virtual environment:

```bash
(interview_env) $ pip install -r interview_requirements.txt
```

Finally, in that activated virtual environment, verify that the script runs properly:

```bash
(interview_env) $ python verify.py
<version>
```

[RealPython installation guide]: https://realpython.com/installing-python/
[virtual environment]: https://realpython.com/python-virtual-environments-a-primer/
[venv]: https://docs.python.org/3/library/venv.html
