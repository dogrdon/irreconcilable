drop table if exists terms; 
create table terms (
    term_id integer primary key autoincrement,
    term_text text not null
);

drop table if exists uris;
create table uris (
    uri_id integer primary key autoincrement,
    uri text not null,
    uri_term integer, 
    FOREIGN KEY(uri_term) REFERENCES terms(term_id)
);
