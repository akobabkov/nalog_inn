# данный кусок логики мне не очень нравится :(
def response_options(param, res, data):
    if 'code' in data:
        if data['code'] == 1:
            print('Пользователь ' + param['fam'] + ' имеет ИНН: ' + data['inn'])
        else:
            print('ИНН не найден!')
    elif 'ERROR' in data:
        if 'fam' in data['ERRORS']:
            print(data['ERRORS'].get('fam'))
        elif 'nam' in data['ERRORS']:
            print(data['ERRORS'].get('nam'))
        elif 'otch' in data['ERRORS']:
            print(data['ERRORS'].get('otch'))
        elif 'bdate' in data['ERRORS']:
            print(data['ERRORS'].data('bdate'))
        elif 'doctype' in data['ERRORS']:
            print(data['ERRORS'].get('doctype'))
        elif 'docno' in res['ERRORS']:
            print(data['ERRORS'].get('docno'))
    else:
        print('Что-то неизвестное: ' + data)
    return
