create table message
(
    message_id        text not null primary key,
    message_from      text,
    message_subject   text,
    message_date      text,
    message_language  text,
    message_processed int default 0,
    message_download  int default 0
);

create table label
(
    label_id   text not null primary key,
    label_name text not null
);

create table message_label
(
    id         integer not null primary key autoincrement,
    message_id text    not null,
    label_id   text    not null
);

create table attachment
(
    attachment_id   text not null primary key,
    message_id      text not null,
    attachment_name text not null,
    attachment_type text not null,
    attachment_data text not null,
    attachment_size real not null,
    downloaded      int default 0
);
