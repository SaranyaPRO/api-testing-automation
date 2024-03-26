Feature: Verify form Responses Api endpoints Note: it supports only GET and POST

  @ApiTesting
  Scenario Outline: Verify a inputForm Api Type of ExternalApi
    Given I have a base URL <base URL> api
    Then I send a <method> request to <endpoint> with parameters with <payload> dataPath with <tokenName> token
    Then the response status code should be <statusCode> code

    Examples: 
      | base URL                                         | method | endpoint                                                                  | statusCode | payload                                  | tokenName  |
      | https://stage-gpmd-formbuilder.theproindia.com   | GET    | /Form/f0be559b-ed15-434a-a33b-0326ad49ea26                                |        401 | None                                     | user       |
      | https://stage-gpmd-formresponses.theproindia.com | POST   | /FormResponse/getResponsesWithFilter/530f70d7-53e4-40b7-a49c-2b1b1b062ada |        401 | formResponse_GetResponsesWithFilter.json | user       |
      | https://stage-gpmd-dashboard.theproindia.com     | GET    | /Project/daf160e5-7e70-493a-ac67-ca1cc0e43762                             |        200 | None                                     | superadmin |
