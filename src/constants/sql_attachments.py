ATTACHMENT_EXIST = "select count(*) as exist_attachment from attachment where message_id = ?;"

ATTACHMENT_INSERT = ("insert into attachment "
                     "(attachment_id, "
                     "message_id, "
                     "attachment_name, "
                     "attachment_type, "
                     "attachment_data, "
                     "attachment_size) "
                     "values (?, ?, ?, ?, ?, ?)")

ATTACHMENT_BY_MESSAGE_ID = ("select attachment_id, attachment_name, attachment_type, attachment_data, attachment_size "
                            "from attachment "
                            "where message_id=?;")
