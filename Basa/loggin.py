def logging(some):
    log = open('log.txt', 'a', encoding='utf-8')
    log.write(f'{str(some)}\n')
    log.close()