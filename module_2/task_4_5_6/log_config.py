import logging

frt = logging.Formatter('%(asctime)s - %(levelname)s %(module)s/%(funcName)s :: %(message)s')

handler = logging.FileHandler('logs/debug.log')
handler.setFormatter(frt)

log = logging.getLogger('Debug')
log.addHandler(handler)
log.setLevel(logging.DEBUG)