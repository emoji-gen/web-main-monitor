# -*- coding: utf-8 -*-

import os

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ---------------------------------------------------------

class Inspector:
    site_url = 'https://emoji-gen.ninja'
    locale_prefixes = ('/', '/en', '/ko', '/zh-Hans', '/zh-Hant')

    def inspect(cls):
        options = Options()
        options.binary_location = os.getenv('GOOGLE_CHROME_SHIM')
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)
        try:
            for locale_prefix in cls.locale_prefixes:
                cls._inspect_home_by_path(driver, path=locale_prefix)
        finally:
            driver.quit()


    def _inspect_home_by_path(cls, driver, *, path='/'):
        driver.get(cls.site_url + path)
        driver.find_element_by_css_selector('.App')
        driver.find_element_by_css_selector('.Header')
        driver.find_element_by_css_selector('.Home')
        driver.find_element_by_css_selector('.Result')
        driver.find_element_by_css_selector('.Generator')
        driver.find_element_by_css_selector('.RecentlyLog')
        driver.find_element_by_css_selector('.Footer')
