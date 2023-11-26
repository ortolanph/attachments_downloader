MESSAGE_INSERT = "insert into message (message_id) values (?);"

MESSAGE_LIST_ALL_IDS = "select message_id from message;"

MESSAGE_SELECT_BATCH = "select message_id from message where message_processed = 0 limit ?;"
