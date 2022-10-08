create table members(
		id integer primary key autoincrement,
		id_member int unique,
		username varchar(255)
);

create table tasks(
		id integer primary key autoincrement,
		message varchar(255),
		author int,
		foreign key(author) references members(id)
);

insert into members (id_member, username) values (234623543, 'andy');
insert into tasks (message, author) values ('Хуй', 1);