from base.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skippBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')
    yesBtn = "android:id/button1"
    allowBtn = "com.android.packageinstaller:id/permission_allow_button"
    skipBtn = "com.baidu.homework:id/adx_splash_skip_text"


    def check_cancelBtn(self):
        logging.info('==========check_cancelBtn=========')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('=========check skipBtn=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('====check_market_ad====')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def skipWelcome(self):
        self.driver.find_element_by_id(self.yesBtn).click()
        self.driver.find_element_by_id(self.allowBtn).click()
        self.driver.find_element_by_id(self.allowBtn).click()
        try:
            self.driver.find_element_by_id(self.skipBtn).click()
        except:
            pass


#if __name__ == '__main__':

    #com=Common()
   #com.skipWelcome()
    # com=Common(driver)
    # com.check_cancelBtn()
    # # com.check_skipBtn()
    # com.swipeLeft()
    # com.getScreenShot('startApp')







