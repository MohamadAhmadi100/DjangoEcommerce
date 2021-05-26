import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connection.channel()
ch2.queue_declare(queue='first')


def callback(ch, method, properties, body):
    print(f'Received {body}')


ch2.basic_consume(queue='first', on_message_callback=callback, auto_ack=True)
print('waiting for message...press ctrl+c to exit')
ch2.start_consuming()
