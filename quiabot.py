'''
Todo:

Question types other then radio buttons

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os.path import abspath
from time import sleep

CHROMEDRIVERLOCATION = 'chromedriver'


def answers(quiaurl,quia_user,quia_password,toreturn='driver',loadper = 0.5):
	#Create webdriver
	driverlocation = abspath(CHROMEDRIVERLOCATION)
	driver = webdriver.Chrome(driverlocation)

	#driver.set_window_size(1120, 550)
	driver.get(quiaurl)

	#Find login fields
	u = driver.find_element_by_name('tag_quiz_username')
	p = driver.find_element_by_name('tag_quiz_password')
	e = driver.find_element_by_name('tagStartQuiz')

	#Log into quiz
	u.send_keys(quia_user)
	p.send_keys(quia_password)
	e.click()
	
	#Submit quiz
	driver.find_element_by_name('tag_end_quiz_one_at_a_time').click()
	sleep(loadper)
	driver.find_element_by_name('tag_final_end_quiz').click()

	toreturn = toreturn.lower()

	if toreturn == 'driver':
		return driver
	elif toreturn == 'html':
		return driver.page_source
		driver.close()

def fillinanswers(quiaurl,quia_user,quia_password,answerdriver,toreturn = 'driver',loadper = 0.5):
	#Create webdriver
	driverlocation = abspath(CHROMEDRIVERLOCATION)

	driver = webdriver.Chrome(driverlocation)
	#driver.set_window_size(1120, 550)

	driver.get(quiaurl)
	
	#Find login fields
	u = driver.find_element_by_name('tag_quiz_username')
	p = driver.find_element_by_name('tag_quiz_password')
	e = driver.find_element_by_name('tagStartQuiz')

	#Log into quiz
	u.send_keys(quia_user)
	p.send_keys(quia_password)
	e.click()

	#Find length of quiz
	l = driver.find_elements_by_xpath("//*[contains(text(), 'Question 1 of ')]")
	quizlen = int(l[0].text[13:])

	return driver
	
	#Fill in answers
	for x in xrange(quizlen):
		## Next question
		driver.find_element_by_name('tag_submit_one_at_a_time').click()
		sleep(loadper)

	#Submit quiz
	driver.find_element_by_name('tag_final_end_quiz').click()

	toreturn = toreturn.lower()

	if toreturn == 'driver':
		return driver
	elif toreturn == 'html':
		return driver.page_source
		driver.close()
	else:
		return None
