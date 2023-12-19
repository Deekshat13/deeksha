*** Settings ***
Library           RequestsLibrary

*** Variables ***
${BASE_URL}       http://127.0.0.1:5000
&{HEADERS}        Content-Type=application/json;charset=utf-8

*** Keywords ***
Create Data
    [Arguments]    ${name}    ${department}    ${position}
    ${data}=    Create Dictionary    name=${name}    department=${department}    position=${position}
    [Return]    ${data}
    
*** Test Cases ***
Create Session
    Create Session    alias=employee_api    url=${BASE_URL}

Create Employee
    ${data}=    Create Data    John    IT    Developer
    ${response}=    Post On Session    employee_api    /employees    json=${data}    headers=${HEADERS}
    Should Be Equal As Strings    ${response.status_code}    201


Get All Employees
    ${response}=    Get On Session    employee_api    /employees
    Should Be Equal As Strings    ${response.status_code}    200
    ${employees}=    Evaluate    json.loads('''${response.content}''')
    Log    Employees: ${employees}

Get Employee by ID
    ${response}=    Get On Session    employee_api    /employees/3
    Should Be True    ${response.status_code} == 200 or ${response.status_code} == 404
    Run Keyword If    '${response.status_code}' == '200'    Log    Employee: ${response.content}

Update Employee
    ${data}=    Create Data    sindhu    HR    Manager
    ${response}=    Put On Session    employee_api    /employees/4    json=${data}    headers=${HEADERS}
    Should Be Equal As Strings    ${response.status_code}    200

Delete Employee
    ${response}=    Delete On Session    employee_api    /employees/6
    Should Be Equal As Strings    ${response.status_code}    200
    
