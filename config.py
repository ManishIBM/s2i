
JENKINS_INFO = {"url": "https://sys-abell-team-jenkins.swg-devops.com/job/$build_info$",
           "user": "pureauto@us.ibm.com",
           "token": "1106e0de4c15e4fd92fcfababec8ff9de8",
                "pipeline":"hci_pipeline_temp",
                "build_id":"9"}

EXCEL_INFO = {"xls_name":['HCI_Automation_Summary.xlsx','SDS_Automation_Summary.xlsx'],
              "sheet_name":['BVT', 'FVT'],
              "SerialNo": 0,
              "suites": 1,
              "scenarios": 2,
              "header_row": 1,
              "first_row": 3}

URLS={
    "url_result": JENKINS_INFO['url']+'/testReport/api/json',
    "url_home": JENKINS_INFO['url']+'/api/json',
    "jobs": 'https://sys-abell-team-jenkins.swg-devops.com/api/json?tree=jobs[name]',
    "builds": 'https://sys-abell-team-jenkins.swg-devops.com/job/$job$/api/json?tree=builds[displayName,number]&pretty=true'
}

GIT_INFO = {'suite_url':'https://raw.github.ibm.com/ProjectAbell/Automation/master/jenkins/test_suites_info.json',
            'user': "pureauto@us.ibm.com",
            "token": "def59229cbfae5a03276aaf59c9ae4bdd403911b"}