from ncclient import manager

router = {"host": "10.10.20.181", "port": "22", "username": "cisco",
          "password": "cisco"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()
