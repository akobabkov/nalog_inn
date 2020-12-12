def http_status(res):
    status = res.status_code
    if status == 200:
        print('Готов к работе, сейчас отдам данные :)')
    else:
        print('Что-то пошло не так... HTTP код ', status)
    return
