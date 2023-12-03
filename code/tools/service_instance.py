
__author__ = "ndansi"

import atexit
from pyVim.connect import SmartConnect, Disconnect


def connect(args):
    

    service_instance = None

    # form a connection...
    try:
        if args['disable_ssl_verification']:
            service_instance = SmartConnect(host=args['host'],
                                            user=args['user'],
                                            pwd=args['password'],
                                            port=args['port'],
                                            disableSslCertValidation=True)
        else:
            service_instance = SmartConnect(host=args['host'],
                                            user=args['user'],
                                            pwd=args['password'],
                                            port=args['port'])

        # doing this means you don't need to remember to disconnect your script/objects
        atexit.register(Disconnect, service_instance)
    except IOError as io_error:
        print(io_error)

    if not service_instance:
        raise SystemExit("Unable to connect to host with supplied credentials.")

    return service_instance
