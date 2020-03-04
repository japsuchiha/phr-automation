import time
import sys
import math
from config import username
from config import password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path=r'C:/Users/jpnts/Downloads/chromedriver_win32/chromedriver.exe')
print(sys.argv)
# driver = webdriver.Chrome()
driver.get("https://phr.umd.edu/phrtimeentry/timeentry?action=ddmenu&view=menu&currentpayperiod=201905")
print(driver.window_handles)
elem = driver.find_element_by_id("username")
elem.send_keys(username)
time.sleep(3)
passw = driver.find_element_by_id("password")
passw.send_keys(password)
log = driver.find_element_by_name("_eventId_proceed")
log.send_keys(Keys.ENTER)
time.sleep(5)
print(driver.window_handles)
curr = driver.window_handles[0]
frame = driver.find_element_by_id("duo_iframe")
driver.switch_to.frame(frame)
time.sleep(5)
print(driver.window_handles)
auth = driver.find_element_by_class_name("auth-button")
auth.send_keys(Keys.ENTER)
driver.switch_to.default_content()
time.sleep(5)
link = driver.find_elements_by_tag_name('a')
link[0].send_keys(Keys.ENTER)
time.sleep(5)
links = driver.find_elements_by_tag_name('a')
print(driver.window_handles)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
links[5].send_keys(Keys.ENTER)
time.sleep(5)
pay = driver.find_elements_by_tag_name('a')
pay[1].send_keys(Keys.ENTER)
num = [4,3,2]
goal = sys.argv[1]
n3 = n2 = 0
n4 = int(goal)/4
rem = int(goal)%4
wk1 = []
if rem == 1:
    n4 = n4-1
    wk1.append(3)
    wk1.append(2)
elif rem == 3:
    wk1.append(3)
elif rem == 2:
    wk1.append(2)

for i in range(math.floor(n4)):
    wk1.append(4)
print(wk1)

days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for i in range(len(wk1)):
    hrs = "wk1{}HrsIn1".format(days[i])
    mins = "wk1{}MinsIn1".format(days[i])
    print(hrs)
    name = "{}".format(hrs)
    namem = "{}".format(mins)
    hr = driver.find_element_by_name(str(name))
    min = driver.find_element_by_name(str(namem))
    hr.send_keys("10")
    min.send_keys("00")
    hrso = "wk1{}HrsOut1".format(days[i])
    minso = "wk1{}MinsOut1".format(days[i])
    name = "{}".format(hrso)
    namem = "{}".format(minso)
    hr = driver.find_element_by_name(str(name))
    min = driver.find_element_by_name(str(namem))
    hrto = (wk1[i] + 10)-12
    print(hrto)
    if hrto == 0:
       hr.send_keys("12"); 
    hr.send_keys("0{}".format(hrto))
    min.send_keys("00")

goal = sys.argv[2]
n3 = n2 = 0
n4 = int(goal)/4
rem = int(goal)%4
wk1 = []
if rem == 1:
    n4 = n4-1
    wk1.append(3)
    wk1.append(2)
elif rem == 3:
    wk1.append(3)
elif rem == 2:
    wk1.append(2)

for i in range(math.floor(n4)):
    wk1.append(4)
print(wk1)

for i in range(len(wk1)):
    hrs = "wk2{}HrsIn1".format(days[i])
    mins = "wk2{}MinsIn1".format(days[i])
    print(hrs)
    name = "{}".format(hrs)
    namem = "{}".format(mins)
    hr = driver.find_element_by_name(str(name))
    min = driver.find_element_by_name(str(namem))
    hr.send_keys("10")
    min.send_keys("00")
    hrso = "wk2{}HrsOut1".format(days[i])
    minso = "wk2{}MinsOut1".format(days[i])
    name = "{}".format(hrso)
    namem = "{}".format(minso)
    hr = driver.find_element_by_name(str(name))
    min = driver.find_element_by_name(str(namem))
    hrto = (wk1[i] + 10)-12
    print(hrto)
    if hrto == 0:
       hr.send_keys("12"); 
    hr.send_keys("0{}".format(hrto))
    min.send_keys("00")
