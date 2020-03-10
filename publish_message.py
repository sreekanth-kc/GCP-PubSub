from google.cloud import pubsub_v1

project_id = ""
topic_name = ""

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_name)

for n in range(1, 10):
    data = u"Message number {}".format(n)
    data = data.encode("utf-8")
    future = publisher.publish(topic_path, data=data)
    print(future.result())

print("Published messages.")
