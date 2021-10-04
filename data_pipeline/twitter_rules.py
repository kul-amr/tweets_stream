import requests
from config import *
from twitter_conn import *
import json


def get_rules():
    response = requests.get(TWITTER_RULE_URL, auth=bearer_oauth)

    if response.status_code != 200:
        raise Exception(
            "Error in fetching rules (HTTP {}):{}".format(response.status_code, response.text)
        )

    print(json.dumps(response.json()))
    return response.json()


def set_rules():
    # job_rule = [
    #     {"value": "(software engineer OR software developer OR data engineer OR fullstack engineer "
    #               "OR fullstack developer OR frontend developer OR frontend engineer OR backend engineer"
    #               "OR backend developer OR devops engineer OR ios engineer OR andriod engineer"
    #               "OR cloud engineer) (hiring OR recruit OR work)"
    #               "-consult -embedded has:links lang:en -is:reply"}
    # ]

    job_rule = [
        {"value": "(software OR data OR fullstack "
                  "OR frontend OR backend OR systems "
                  "OR devops OR ios OR andriod OR cloud "
                  "OR AI OR ML OR artificial intelligence OR machine learning) (hiring OR recruit OR work)"
                  "(context:66.961961812492148736 OR context:66.850073441055133696 OR context:66.847544972781826048 "
                  "OR context:66.849075881653846016) "
                  "-consult -embedded has:links lang:en -is:reply"}
    ]
    # 961961812492148736 - Recruitment
    # 850073441055133696 - job search
    # 847544972781826048 - careers
    # 849075881653846016 Startups

    payload = {"add": job_rule}
    response = requests.post(
        TWITTER_RULE_URL,
        auth=bearer_oauth,
        json=payload
    )

    if response.status_code != 201:
        raise Exception(
            "Error in adding rules (HTTP {}):{}".format(response.status_code, response.text)
        )
    else:
        print(json.dumps(response.json()))


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    rule_ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": rule_ids}}
    response = requests.post(
        TWITTER_RULE_URL,
        auth=bearer_oauth,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(
            "Error in deleting rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    else:
        print(json.dumps(response.json()))


r = get_rules()
delete_all_rules(r)
set_rules()
get_rules()
