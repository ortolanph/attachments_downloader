MESSAGE_INSERT = "insert into message (message_id) values (?);"

MESSAGE_LIST_ALL_IDS = "select message_id from message;"

MESSAGE_SELECT_BATCH = "select message_id from message where message_processed = 0 limit ?;"

MESSAGE_SELECT_BATCH_PROCESSED = ("select message_id, message_from, message_subject, message_date "
                                  "from message "
                                  "where message_processed = 1 "
                                  "and message_download = 0 "
                                  "limit ?;")

MESSAGE_UPDATE = ("update message "
                  "set message_from=?, "
                  "message_subject=?, "
                  "message_date=? "
                  "where message_id = ?;")

MESSAGE_MARK_AS_PROCESSED = "update message set message_processed = 1 where message_id = ?"
