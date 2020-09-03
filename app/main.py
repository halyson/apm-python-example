import elasticapm
from time import sleep
from services import customer
from services import data_lake
from random import randint, uniform


client = elasticapm.Client(service_name="app-test", environment='development', service_version='1.0')


@elasticapm.capture_span()
def sync_customers():
    sleep(uniform(0.5, 1))
    customer_data = customer.get_customer(randint(1, 10))
    if customer_data:
        data_lake.save_customer(customer_data)
        status = 'success'
    else:
        status = 'error'
    return status


def transaction_example():

    client.begin_transaction(transaction_type="data-integration")

    status = sync_customers()

    client.end_transaction("sync-customers", status)

    #client.capture_message('Custom Data Message', custom=data)


if __name__ == "__main__":
    client.capture_message('Simple Message')

    for n in range(100):
        transaction_example()
