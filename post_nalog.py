import requests
import status

param = {
    'c': 'innMy',
    'captcha': '',
    'captchaToken': '',
    'fam': '',
    'nam': '',
    'otch': '',
    'bdate': '',
    'bplace': '',
    'doctype': '21',
    'docno': '',
    'docdt': ''
}

host = 'https://service.nalog.ru/inn-proc.do'
res = requests.post(host, param)
status.http_status(res)
res = res.json()
if 'inn' in res:
    print('Пользователь ' + param['fam'] + ' имеет ИНН: ' + res['inn'])
elif 'fam' in res['ERRORS']:
    print(res['ERRORS'].get('fam'))
elif 'nam' in res['ERRORS']:
    print(res['ERRORS'].get('nam'))
elif 'otch' in res['ERRORS']:
    print(res['ERRORS'].get('otch'))
elif 'bdate' in res['ERRORS']:
    print(res['ERRORS'].get('bdate'))
elif 'doctype' in res['ERRORS']:
    print(res['ERRORS'].get('doctype'))
elif 'docno' in res['ERRORS']:
    print(res['ERRORS'].get('docno'))
else:
    print('ИНН не найден!')

Q = input('press Enter to exit')
