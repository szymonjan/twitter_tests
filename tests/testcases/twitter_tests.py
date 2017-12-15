# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore


from tests.pages.twitter_pages import LoginPage, MainPage
import tests.testdata.settings as data

from time import sleep
from random import randint
import unittest

class TwitterTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(data.url_address())
        #Login to a service before a test
        LoginPage(self.driver).login_to_service(data.login(), data.password())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver())

    def test_sending_tweet(self):
        main_page = MainPage(self.driver)

        # Get tweet count before message is sended
        before_count = int(main_page.get_tweet_count())

        # Send tweet with a random number
        rand_number = randint(0,9999)
        text_to_send = "tweet number: {}".format(rand_number)
        main_page.send_tweet(text_to_send)

        sleep(3)
        # Check that sended message is correct
        sended_text = main_page.get_tweet_text()
        self.assertEqual(text_to_send, sended_text)


if __name__ == '__main__':
    unittest.main()
