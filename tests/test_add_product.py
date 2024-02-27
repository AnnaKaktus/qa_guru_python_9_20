import os
import allure
from selene import browser, have
from dotenv import load_dotenv
from tests.conftest import BASE_URL
from utils.utils import send_request, remove_product

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


@allure.title("Adding with params")
def test_add_product_to_cart_with_params():
    response = send_request(
        "login", data={"Email": {login}, "Password": {password}}, allow_redirects=False
    )
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = send_request(
        "addproducttocart/details/72/1",
        data={
            "product_attribute_72_5_18": 53,
            "product_attribute_72_6_19": 54,
            "product_attribute_72_3_20": 57,
            "product_attribute_72_8_30": 93,
            "addtocart_72.EnteredQuantity": 1,
        },
        allow_redirects=False,
        cookies={"NOPCOMMERCE.AUTH": cookies},
    )
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element(".product-name").should(have.text("Build your own cheap computer"))
    remove_product()


@allure.title("Adding without params")
def test_add_product_to_cart_without_params():
    response = send_request(
        "login", data={"Email": {login}, "Password": {password}}, allow_redirects=False
    )
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = send_request(
        "addproducttocart/catalog/31/1/1", cookies={"NOPCOMMERCE.AUTH": cookies}
    )
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("14.1-inch Laptop"))
    remove_product()
