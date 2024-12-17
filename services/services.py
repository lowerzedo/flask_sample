import json

def get_course(**kwargs):
    with open('responses/course.json') as f:
        data = json.load(f)

    return data


def get_module_desc(**kwargs):
    with open('responses/module_desc.json') as f:
        data = json.load(f)

    return data


def get_module_version(**kwargs):
    with open('responses/module_version.json') as f:
        data = json.load(f)

    return data


def get_pm_version(**kwargs):
    with open('responses/pm_version.json') as f:
        data = json.load(f)

    return data


def get_program_map(**kwargs):
    with open('responses/program_map.json') as f:
        data = json.load(f)

    return data


