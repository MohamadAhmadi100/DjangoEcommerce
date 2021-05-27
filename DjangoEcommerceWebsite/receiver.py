import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connection.channel()
ch2.queue_declare(queue='second', durable=True)


def callback(ch, method, properties, body):
    print(f'Received {body}')
    time.sleep(2)
    print('Done')
    ch2.basic_ack(delivery_tag=method.delivery_tag)


ch2.basic_qos(prefetch_count=1)
ch2.basic_consume(queue='second', on_message_callback=callback)
print('waiting for message...press ctrl+c to exit')
ch2.start_consuming()
