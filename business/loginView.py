import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    username_type=(By.ID,'com.baidu.homework:id/passport_phone_number_input_edit')
    password_type=(By.ID,'com.baidu.homework:id/passport_password_input_view')
    userBtn=(By.ID,'com.baidu.homework:id/tv_phone_enter')
    passwordBtn=(By.ID,'com.baidu.homework:id/tv_password_login')

    tip_commit=(By.ID,'com.tal.kaoyan:id/tip_commit')

    button_mysefl=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    RightButton=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logoutBtn=(By.ID,'com.tal.kaoyan:id/setting_logout_text')




    def login_action(self,username,password):
        self.skipWelcome()

        logging.info('============login_action==============')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)
        self.driver.find_element(*self.userBtn).click()

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.passwordBtn).click()

        logging.info('login finished!')

    def check_account_alert(self):
        logging.info('=====check_account_alert====')
        try:
            element=self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.click()

    def check_loginStatus(self):
        logging.info('====check_loginStatus======')
        self.check_market_ad()
        self.check_account_alert()

        try:

            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('=====logout_action======')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
    l=LoginView()
    l.login_action("16604688441","111111")