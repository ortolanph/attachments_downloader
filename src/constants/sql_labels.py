LABEL_EXIST = "select count(*) as exist_label from label where label_id = ?;"

LABEL_INSERT = "insert into label (label_id, label_name) values (?, ?)"

LABEL_ASSOCIATION_EXIST = ("select count(*) as exist_association "
                           "from message_label "
                           "where label_id = ? and message_id = ?;")

LABEL_ASSOCIATION_INSERT = "insert into message_label (message_id, label_id) values (?, ?)"
