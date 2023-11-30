ATTACHMENT_EXIST = "select count(*) as exist_attachment from attachment where attachment_id = ?;"

ATTACHMENT_INSERT = ("insert into attachment "
                "(attachment_id, "
                "message_id, "
                "attachment_name, "
                "attachment_type, "
                "attachment_data, "
                "attachment_size) "
                "values (?, ?, ?, ?, ?, ?)")
