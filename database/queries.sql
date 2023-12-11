select m.message_id,
       m.message_subject,
       printf('%.2f', sum(a.attachment_size) / 1024, 2) as attachments_size
from message m
         inner join main.attachment a on m.message_id = a.message_id
group by m.message_id,
         m.message_subject,
         a.attachment_size;

select l.label_name,
       printf('%.2f', sum(a.attachment_size) / 1024, 2) as attachments_size
from attachment a
         inner join message_label ml on a.message_id = ml.message_id
         inner join label l on ml.label_id = l.label_id
group by l.label_id;

select distinct(attachment_type)
from attachment;

select *
from message;

-- Fetch message information
select message_id, message_from, message_subject, message_date
  from message
 where message_processed = 1
   and message_download = 0
 limit ?;

-- Fetch label information
select l.label_name
from label l
         inner join main.message_label ml on l.label_id = ml.label_id
where ml.message_id=?;

-- Fetch attachment information
select attachment_name, attachment_type, attachment_size
  from attachment
 where message_id=?;