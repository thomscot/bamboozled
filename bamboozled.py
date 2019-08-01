import os
from time import sleep

from germanium.util import wait
from germanium.static import S, Link, click, open_browser, close_browser, go_to, type_keys, Css, Button

import constants


class Bamboozled:
	"""
	To log in on bamboo and automate clock in/out operations etc.
	Attributes:
				browser: str, the browser to be used, eg "chrome"
				user: str, username on bamboo
				pwd: str, password
	"""

	def __init__(self, browser, user, pwd):
		self.browser = browser
		self.user = user
		self.pwd = pwd


	def open_bamboo(self):
		"""
		Open the browser and navigate to bamboo log in page
		"""
		open_browser(self.browser)
		go_to(constants.BAMBOO_LOGIN)

	def standard_log_in(self):
		"""
		Log in bamboo hr by standard log in, that is, not the "log in with Google". 
		Note: Using Google seems more complicated. Besides, if using 2FA hings get very tricky.
		One could use backup codes: read it from file, use it, when using last one log in to google,
		generate new ones, download and substitute the backup codes file with new one... jeez.
		"""
		
		# Click the link for standard log-in (not google log-in)
		link = S(Link(constants.STANDARD_LOGIN))
		click(link)

		# go to the user_id field and type user
		id_field = S(constants.LOGIN_ID, strategy="css")
		click(id_field)
		type_keys(self.user)
		wait(Css('div.progress').not_exists) # wait for the domain check
		
		# go to password field and type the password
		pwd_field = S(constants.PWD_ID, strategy="css")
		click(pwd_field)
		type_keys(self.pwd)
		
		# click the log in button
		log_in = S(Button(constants.LOGIN_BTN))
		click(log_in)

	@staticmethod
	def clock_in():
		"""
		Click the clock_in button (assume is logged in) and close the browser
		"""

		# TODO: Handle exception if no button is found (eg, already clocked-in)
		clock_in = S(Button(constants.CLOCK_IN_BTN))
		click(clock_in)
		close_browser()

	@staticmethod
	def clock_out():
		"""
		Click the clock_out button (assume is logged in) and close the browser
		"""

		# TODO: Handle exception if no button is found (eg, already clocked-in)
		clock_out = S(Button(constants.CLOCK_OUT_BTN))
		click(clock_out)
		close_browser()


	def test_run(self, sleep_time):
		"""
		A test run to check that everything is working fine:
		Open browser, navigate to bamboo, log in, clock-in, wait a few seconds (just to be able to see what happens), 
		and repeat for the clock-out operation.
		
		:param: sleep_time: int, number of seconds to sleep between clock-in/out
		"""

		self.open_bamboo()
		self.standard_log_in()
		self.clock_in()

		sleep(sleep_time)

		self.open_bamboo()
		self.standard_log_in()
		self.clock_out()



if __name__ == "__main__":

	usr = os.getenv(constants.BAMBOO_USR, "my_username")
	pwd = os.getenv(constants.BAMBOO_ENV, "my_password")

	b = Bamboozled(constants.BROWSER, usr, pwd)

	b.test_run(5)




