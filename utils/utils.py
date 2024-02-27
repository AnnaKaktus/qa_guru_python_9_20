import requests
import allure
import curlify
import logging
from selene import browser
from allure_commons.types import AttachmentType

BASE_URL = "https://demowebshop.tricentis.com/"


def send_request(url, **kwargs):
    url = BASE_URL + url
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(
            body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt"
        )
        logging.info(curlify.to_curl(response.request))
        return response


def remove_product():
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()
