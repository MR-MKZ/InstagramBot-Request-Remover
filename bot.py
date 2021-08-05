from selenium import webdriver
from time import sleep
from info import user, passwd


class Bot():
    def __init__(self):
        self.login(user, passwd)

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagram.com')
        sleep(2)
        username_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_input.send_keys(password)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        self.driver.get(
            'https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(3)
        #number_of_clicks = 0
        #while number_of_clicks < 6:
            #self.driver.find_element_by_xpath(
                #'/html/body/div[1]/section/main/div/article/main/button').click()
            #sleep(1)
            #number_of_clicks += 1
        list_of_usernames = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_usernames.append(names.text)
        for i in list_of_usernames:
            self.driver.get(f'https://instagram.com/{i}')
            sleep(1)
            # REQUESTED
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[1]').click()
            sleep(2)
            # UNFOLLOW
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[1]').click()


def main():
    myBot = Bot()


if __name__ == '__main__':
    main()
