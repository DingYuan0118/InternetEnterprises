from enterprise_list import ENTERPRISE_LIST

def add_enterprise(enterprise_name, enterprise_code):
    if enterprise_name in ENTERPRISE_LIST:
        return
    else:
        ENTERPRISE_LIST[enterprise_name] = enterprise_code