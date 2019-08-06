import os
import time
import random

import constants
from bamboozled import Bamboozled

# random sleep not to clock-in/out always at the same time
secs = int(random.random()*constants.MAX_SLEEP)
time.sleep(secs)

# getenv might give troubles with cron jobs. If so, hard-code defaults
usr = os.getenv(constants.BAMBOO_USR, "my_username")
pwd = os.getenv(constants.BAMBOO_ENV, "my_password")

b = Bamboozled(constants.BROWSER, usr, pwd)

# open web-page, log-in, and clock in
b.open_bamboo()
b.standard_log_in()
b.clock_in()
