# bamboozled

Tired of manually clocking in and out from bamboo HR webpage? This tool is for you.

The scripts use the germanium library (https://germaniumhq.com/) to automate clock-in/out operations.

This tool is designed to run every day from Monday to Friday twice a day: once in the morning to clock in, once in the evening to clock out. Some simple randomness is added so that the clock in/out operation will not be performed always at the same time.

Please use this wisely and with integrity. The purpose of the tool is to avoid the bother of manually clocking in and out, and the chances of forgetting to do so. It is NOT intended to cheat on your daily hours.

Currently it is tested with Chrome on Mac OS. 

### Initial set-up

If using Anaconda, if needed you can create a new environment with:

`$ conda create -n my_env python=3.7`

and then activate it with:

`$ source activate my_env`

Wether creating a new environment or not, install the requirements:

`$ pip install -r requirements.txt`

### About the log in credentials and other constants

Add to your _~/.bash_profile_ two environment variables:

BAMBOO_USR='your_username' 

BAMBOO_PWD='your_pwd'

(and if necessary run `$ source ~/.bash_profile`).

Look in the _constants.py_ file, and change what's necessary for your needs.

**important:** Change the bamboo url string with the correct link for your organization.

### On setting up the cron job (on Mac OS)

Modify the cron.txt file accordingly with the path to your scripts.

To set up a cron job from cron.txt:

`$ crontab cron.txt`

To remove current cron settings:

`$ crontab -r`

To list currently scheduled jobs:

`$ crontab -l`

**Note:** In the current version, there might be issues in getting the environment variables by using _os.getenv()_. If so,
you can hard-code your credentials... making sure not to push them.

#### A note on cron.txt:

_* * * * * /path/to/python /path/to/script.py_

The dots have the following meaning (from left to right):

- minutes (0-59)
- hour (0-23)
- day of the month (1-31)
- month (1-12)
- day of the week (0-7, where 7==0==Sunday)

Hence to schedule a job at 10:30 am monday to friday:

30 10 * * 1,2,3,4,5 /path/to/python /path/to/script.py (also 1-5 should work)

The /path/to/python is optional if one just wants to use the default root.
It is necessary if one wants to use a specific version or environment.

### Direct use

The script could be also called directly. For a test run, Ii the root folder just run:

`$ python bamboozled.py`

Or run the clock-in/out scripts directly with:

`python clock_in.py` (or clock_out.py)

However, given that by default there is a random wait from 0 to 20 minutes, this won't be executed immediately.
