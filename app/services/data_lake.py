from time import sleep
from random import uniform
import elasticapm


@elasticapm.capture_span()
def save_customer(customer: dict):
    print('-- Save Customer:', customer)
    sleep(uniform(0.5, 1))
    return True
