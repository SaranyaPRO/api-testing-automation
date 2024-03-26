Feature: Verify form Responses Api endpoints Note: it supports only GET and POST

  @gamificationapi
  Scenario Outline: Verify a inputForm Api Type of ExternalApi
    Given I have a base URL <base URL> api
    Then I send a <method> request to <endpoint> with parameters with <payload> dataPath with <tokenName> token
    Then the response status code should be <statusCode> code

    Examples: 
      | base URL                                       | method | endpoint                                                 | statusCode | payload     | tokenName |
      | https://stage-gamificationapi.theproindia.com/ | GET    | /v1/applications/projectId/62b404da22635c1c1fa248b7/1/10 |        200 | Test.json   | user1     |
      | https://stage-gamificationapi.theproindia.com/ | GET    | /v1/gameAction/application/649a8e07c05ea8224df9f5e       |        200 | Gamifi.json | user2     |
      
       
