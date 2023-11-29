from src.controller.message_controller import MessageController

if __name__ == '__main__':
    print("Step 2 - Fetching message data")
    message_controller = MessageController()

    messages = message_controller.load_next_messages()

    for message_id in messages:
        gmail_message = message_controller.fetch_message(message_id)

        print("Getting message headers")
        payload_headers = gmail_message["payload"]["headers"]
        print("Getting label ids")
        label_ids = gmail_message["labelIds"]
        print("Getting payload pars")
        attachments = gmail_message["payload"]["parts"]

        print("Updating message data")
        message_controller.update_message_data(message_id, payload_headers)
