from time import sleep
import elasticapm
from random import uniform

client = elasticapm.Client(service_name="app-test", environment='development')


@elasticapm.capture_span()
def get_customer(id: int):
    print('- Get Customer...')
    sleep(2)
    data = None
    if id == 10:
        try:
            sleep(uniform(0.5, 1))
            raise Exception("Get Customer Failed!!")
        except Exception as e:
            client.capture_exception()
    else:
        data = {
            'id': id,
            'name': 'Halyson Sampaio'
        }
    return data
