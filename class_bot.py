# Logs in and signs up for classes

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from login_dict import login_dict
from class_numbers import classes_dict

# global var

driver = webdriver.Firefox()

# initial dict but will use seperate login_dict.py


def login():
    driver.get("https://my.iit.edu/cp/home/displaylogin")
    username = driver.find_element_by_xpath("//*[@id='userid']/input")
    username.send_keys(login_dict['login_id'])
    password = driver.find_element_by_xpath("//*[@id='cplogin']/input[1]")
    password.send_keys(login_dict['login_pass'])
    button = driver.find_element_by_xpath("//*[@id='cplogin']/input[4]")
    button.click()
    pass


def navigate_to_classes():
    academics_tab = driver.find_element_by_partial_link_text('Academics')
    academics_tab.click()
    class_nav = driver.find_element_by_xpath("//*[@id='channel']/tbody/tr[4]/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/a")
    class_nav.click()
    sleep(3)
    driver.switch_to_frame("content")
    term_nav = driver.find_element_by_xpath("/html/body/div[3]/form/input")
    print term_nav
    term_nav.click()
    pin_verif = driver.find_element_by_xpath('//*[@id="apin_id"]')
    pin_verif.send_keys(login_dict['pin'])
    pin_verif.submit()
    pass


def input_classes():
    class1 = driver.find_element_by_id('crn_id1')
    class2 = driver.find_element_by_id('crn_id2')
    class3 = driver.find_element_by_id('crn_id3')
    class4 = driver.find_element_by_id('crn_id4')
    class5 = driver.find_element_by_id('crn_id5')
    class1.send_keys(classes_dict['CRN1'])
    class2.send_keys(classes_dict['CRN2'])
    class3.send_keys(classes_dict['CRN3'])
    class4.send_keys(classes_dict['CRN4'])
    class5.send_keys(classes_dict['CRN5'])
    class_submit = driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
    class_submit.click()
    pass


def class_bot():
    login()
    sleep(5)
    navigate_to_classes()
    sleep(2)
    input_classes()
    pass

class_bot()
