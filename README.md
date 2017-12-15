#### General info

This repositorium contains automated tests for Twitter webpage (https://twitter.com/). Three features are being tested:
- sending a tweet
- searching for people to follow
- following people 

#### Project organization

`/twitter_tests
    /assets - place non-code files used in your tests here.
    /configs - location of config files.
	/data - data files (like CSV files) goes here.
	/reference-screenshots - if enabled, reference screenshots are placed here.
	/reports - test result XML files will go here when you run tests.
	/screenshots - screenshots taken on test failures will go here.
	/tests - top level package for your test code.
		/flows - high level reuseable multipage flows.
		/models - data models go here. (like DataBase ORM code)
		/pages - Your page objects go here.
		/support - reuseable support utility functions go here.
		/testdata - custom code for working with test data.
		/tests - Your high level tests will go here.`

#### Requirements
* Python 3.4+
* Pip 9+
* Chrome 62+

#### How to run tests
1. Clone this repository `git clone https://github.com/szymonjan/twitter_tests.git`
2. Install all required packages `pip install -r requirements.txt`
3. Istall modified WTFramework `pip install git+https://github.com/szymonjan/wtframework_mod.git`
4. Run tests `python runtests.py`