from services.services import get_course, get_module_desc, get_module_version, get_pm_version, get_program_map


def get_course_main(**kwargs):
    return get_course(**kwargs)


def get_module_desc_main(**kwargs):
    return get_module_desc(**kwargs)


def get_module_version_main(**kwargs):
    return get_module_version(**kwargs)


def get_pm_version_main(**kwargs):
    return get_pm_version(**kwargs)


def get_program_map_main(**kwargs):
    return get_program_map(**kwargs)