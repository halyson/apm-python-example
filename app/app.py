import elasticapm
from time import sleep

client = elasticapm.Client(service_name="app-test")


@elasticapm.capture_span()
def do_thing():
    sleep(5)


def transaction_example(data: dict):

    client.begin_transaction(transaction_type="track-do-thing")

    sleep(4)
    do_thing()
    sleep(4)

    client.end_transaction("finish-do-thing", "success")

    client.capture_message(message="Connection Error", custom=data)


if __name__ == "__main__":
    client.capture_message('Simple Message')

    data = {
        'name': 'Halyson Sampaio'
    }

    client.capture_message('Custom Data Message', custom=data)

    transaction_example(data)
