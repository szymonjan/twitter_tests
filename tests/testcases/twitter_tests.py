# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore
from wtframework.wtf.utils.wait_utils import do_until

from tests.pages.twitter_pages import LoginPage, MainPage, SearchResultsPage, \
    ProfilePage, FollowedPage
import tests.testdata.settings as data

from random import randint
from time import sleep
import unittest


class TwitterTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(data.url_address())
        # Login to a service before a test
        LoginPage(self.driver).login_to_service(data.login(), data.password())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver())

    def test_sending_tweet(self):
        # Main page object initialization
        main_page = MainPage(self.driver)

        # Send tweet with a random number
        rand_number = randint(0, 9999)
        text_to_send = "tweet number: {}".format(rand_number)
        main_page.send_tweet(text_to_send)

        # Check that sended tweet is correct
        # Do_until is a retry wrapper that'll keep performing the assertion until it succeeds.
        # If not it raise an error message
        sended_tweet = main_page.get_tweet_text
        do_until(lambda: self.assertEqual(text_to_send, sended_tweet),
                 message="Text is incorrect!")

    def test_profile_searching(self):
        # Search for 'Andrzej Duda' phrase
        MainPage(self.driver).search("Andrzej Duda")

        # Find if the searched phrase is in the results
        search_results_list = SearchResultsPage(self.driver).get_search_results()
        do_until(lambda: self.assertIn("Andrzej Duda", search_results_list),
                 message="Text wasn't found!")

    def test_following_profile(self):
        # Go directly to Donald Tusk profile and follow
        self.driver.get("https://twitter.com/eucopresident")
        ProfilePage(self.driver).follow_profile()

        # Go to the user's followed profile page and check if Donald Tusk
        # is being followed
        sleep(2)  # I know it's ugly :P
        self.driver.get("https://twitter.com/usertest344/following")
        followed_profiles_list = FollowedPage(self.driver).get_followed_profiles()
        do_until(lambda: self.assertIn("Donald Tusk", followed_profiles_list),
                 message="Profile wasn't found!")

        # Clean up by unfollowing Donald Tusk profile
        FollowedPage(self.driver).unfollow_profile()


if __name__ == '__main__':
    unittest.main()
