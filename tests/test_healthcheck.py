import logging as logger
from woocommerce import API


def test_framework_healthcheck():
    logger.info('just checking framework is wired correctly')


def test_woo_commerce():
    wcapi = API(
        url="http://localhost/testsite/wp-json/wc/v3/",
        consumer_key="ck_193946c3c441358f82d409aa49a4437e70fab5e6",
        consumer_secret="cs_abeca33e603806408753d245c95cdbf29f3b8181",
        version="wc/v3"
    )
    response = wcapi.get("products")
    print(response.json())
