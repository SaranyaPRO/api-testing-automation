import requests
from behave import given, when, then
from utils.data import ApiToken
import os
import json
import logging


def get_token(tokenName):
    if tokenName.lower() == "superadmin":
        token = ApiToken.superAdminToken
    elif tokenName.lower() == "user":
        token = ApiToken.userToken
    elif tokenName.lower() == "user1":
        token = ApiToken.userToken1
    elif tokenName.lower() == "user2":
        token = ApiToken.userToken2    
    return token


@given("I have a base URL {base_url} api")
def step_given(context, base_url):
    print(base_url)
    context.logger = logging.getLogger()
    print("set logger successfully")
    context.logger.info("set logger successfully")

    context.base_url = base_url
    context.logger.info("base_url : " + str(context.base_url))


@then(
    "I send a {method} request to {endpoint} with parameters with {payload} dataPath with {tokenName} token"
)
def step_POST(context, method, endpoint, payload, tokenName):
    # Get Token
    token = get_token(tokenName)

    print("Payload File name : " + payload)
    # directory of jsonFile
    json_payload_path = os.getcwd() + "/features/utils/apiJsonData/" + payload
    print("json_payload_path :", str(json_payload_path))
    context.logger.info("json_payload_path : %s", json_payload_path)

    # Endpoint
    url = context.base_url + endpoint
    print("Current EndPoint to Run : " + url)
    context.logger.info("Current EndPoint to Run : " + str(url))

    context.response = None
    # context.response = requests.get(url, params=params)
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }

    if method.lower() == "get":
        context.response = requests.get(url, headers=headers)

        # Status Code
        print("Status Code : " + str(context.response.status_code))
        context.logger.info("Status Code : " + str(context.response.status_code))

        # Response
        if str(context.response.status_code) == "200":
            context.response_json = context.response.json()
            print("Response : " + str(context.response_json))
            context.logger.info("Response : " + str(context.response_json))
        else:
            print("Response Status Code : " + str(context.response.status_code))
            context.logger.info(
                "Response Status Code : " + str(context.response.status_code)
            )

    elif method.lower() == "post":
        with open(json_payload_path) as f:
            payload = json.load(f)

        # Post
        context.response = requests.post(url, json=payload, headers=headers)

        # Status Code
        print("Status Code : " + str(context.response.status_code))
        context.logger.info("Status Code : " + str(context.response.status_code))

        # Response
        if str(context.response.status_code) == "200":
            context.response_json = context.response.json()
            print("Response : " + str(context.response_json))
            context.logger.info("Response : " + str(context.response_json))
        else:
            print("Response Status Code : " + str(context.response.status_code))
            context.logger.info(
                "Response Status Code : " + str(context.response.status_code)
            )


@then("the response status code should be {status_code} code")
def step_then(context, status_code):
    print(
        "Compare current statusCode : "
        + str(context.response.status_code)
        + " with expected statusCode : "
        + str(status_code)
    )

    context.logger.info(
        "Compare current statusCode : "
        + str(context.response.status_code)
        + " with expected statusCode : "
        + str(status_code)
    )

    assert int(context.response.status_code) == int(status_code)
