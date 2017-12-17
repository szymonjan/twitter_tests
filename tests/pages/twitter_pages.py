# -*- coding: utf-8 -*-
# This file contains all of the pages used in tests. Every page should consist of loctors (e.g. Xpath)
# and methods used to interact with an webpage elements.

from tests.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):

    """ This page will be used only for log in """

    #All locators are specified by XPATH and are defined  as class variables
    LOGIN_FIELD = "//input[@id='signin-email']"
    PASS_FIELD = "//input[@id='signin-password']"
    LOGIN_BTN = "//*[@class='flex-table-secondary']/button"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

        #Login form elements are located during page initailiztion.
        self.login_field = self.find_clickable_element(self.LOGIN_FIELD)
        self.pass_field = self.find_clickable_element(self.PASS_FIELD)
        self.login_btn = self.find_clickable_element(self.LOGIN_BTN)

    def login_to_service(self, login, password):
        "This method is used for login in"
        self.login_field.clear()
        self.login_field.send_keys(login)
        self.pass_field.clear()
        self.pass_field.send_keys(password)
        self.login_btn.click()

class MainPage(BasePage):

    """ This is a main page for logged in user. It displays most important
    content. """

    #All locators are specified by XPATH and are defined as the class variables
    TWEET_BOX = "//div[@id='tweet-box-home-timeline']"
    SEND_TWEET_BTN = "//button[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']/span[1]"
    TWEET_COUNT = "//span[@class='ProfileCardStats-statValue']"
    TWEETS_LIST = "//p[@class='TweetTextSize  js-tweet-text tweet-text']"
    SEARCH_FIELD = "//input[@class='search-input']"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

        self.tweet_box = self.find_clickable_element(self.TWEET_BOX)
        self.tweet_count = self.find_visible_element(self.TWEET_COUNT)
        self.search_field = self.find_clickable_element(self.SEARCH_FIELD)

    def send_tweet(self, text):
        self.tweet_box.send_keys(text)
        # The button is visible after interaction with box
        self.find_clickable_element(self.SEND_TWEET_BTN).click()

    def get_tweet_count(self):
        """ Returns a value of sended tweets """
        return self.tweet_count.text

    def get_tweet_text(self):
        """ Returns the latest tweeted tweeted message """
        return self.get_element_from_list(self.TWEETS_LIST, 0)

    def search(self, text):
        self.search_field.send_keys(text)
        self.search_field.send_keys(Keys.ENTER)


class SearchResultsPage(BasePage):

    """ This page displays results for a searched phrase """
    SEARCH_RESULTS = "//a[contains(@class,'fullname')]"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

    def get_search_results(self):
        """ Method returns a list of names that are results of searching phrase """
        return self.get_list_of_names(self.SEARCH_RESULTS)

class ProfilePage(BasePage):

    """ This page displays all information about a single twitter profile """

    FOLLOW_BTN = "//div[@data-name='Donald Tusk']//button[contains(@class, ' follow-text')]"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

    def follow_profile(self):
        follow_btn = self.find_clickable_element(self.FOLLOW_BTN)
        follow_btn.click()

class FollowedPage(BasePage):

    """ This page displays all information about a single twitter profile """

    FOLLOWED_PROFILES = "//div[@class='ProfileCard-userFields']//a[contains(@class, 'fullname')]"
    ISFOLLOWED_BTN = "//div[@data-name='Donald Tusk']//button[contains(@class, 'following-text')]"
    UNFOLLOW_BTN = "//div[@data-name='Donald Tusk']//button[contains(@class, 'unfollow-text')]"

    def __init__(self, webdriver, *args, **kwargs):
        super().__init__(webdriver, *args, **kwargs)

    def unfollow_profile(self):
        """ Unfollow profile by mowing mouse to a button then click on it """
        self.find_clickable_element(self.ISFOLLOWED_BTN).click()

    def get_followed_profiles(self):
        """ Method returns list of followed profiles names """
        return self.get_list_of_names(self.FOLLOWED_PROFILES)