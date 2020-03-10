from google.cloud import pubsub_v1

project_id = ""
subscription_name = ""
timeout = 5.0  # "How long the subscriber should listen for
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_name
)

def callback(message):
    print("Received message: {}".format(message))
    message.ack()

streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=callback
)
print("Listening for messages on {}..\n".format(subscription_path))

try:
    streaming_pull_future.result(timeout=timeout)
except:  # noqa
    streaming_pull_future.cancel()
