# coding: utf-8
# @Time    : 2017/5/3 20:28
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : ustc_cas.py

class USTCCas():
    cas_host = "https://passport.ustc.edu.cn/serviceValidate?ticket=%s&service=%s"

    ticket = None
    service = None
    err_msg = None

    def api_url(self):
        return self.cas_host % (self.ticket, self.service)

    def __init__(self, ticket, service):
        self.ticket = ticket
        self.service = service

    def get_ustc_id(self):
        import requests
        import re
        try:
            r = requests.get(self.api_url())
            if r and r.status_code == 200:
                res = r.text
            else:
                return False
            if "authenticationSuccess" in res:
                regex = r'<cas:user>(.*)</cas:user>'
                p = re.compile(regex)
                m = p.search(res)
                if m:
                    return m.group(1).upper()
                else:
                    return False
            else:
                return False
        except:
            return False