import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='second', durable=True)
message = 'This is Testing'
for n in range(1, 20):
    channel.basic_publish(exchange='', routing_key='second', body=f'num {n}',
                          properties=pika.BasicProperties(delivery_mode=2,))
    print(n)

connection.close()
