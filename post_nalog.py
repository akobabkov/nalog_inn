import requests
import status
import options

param = {
    'c': 'innMy',
    'captcha': '',
    'captchaToken': '',
    'fam': '',
    'nam': '',
    'otch': '',
    'bdate': '',
    'bplace': '',
    'doctype': '',
    'docno': '',
    'docdt': ''
}

host = 'https://service.nalog.ru/inn-proc.do'
res = requests.post(host, param)
status.http_status(res)
data = res.json()
options.response_options(param, res, data)

Q = input('press Enter to exit')
