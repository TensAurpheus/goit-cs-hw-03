create table if not exists users(
	id SERIAL primary key,
	fullname VARCHAR(100),
	email VARCHAR(100) unique not null
);

create table if not exists status(
	id SERIAL primary key,
	name varchar(50) unique not null
);

create table if not exists tasks(
	id SERIAL primary key,
	title varchar(100),
	description text,
	status_id integer,
	user_id integer,
	foreign key (status_id) references status(id),
	foreign key (user_id) references users(id)
		on delete cascade
);


