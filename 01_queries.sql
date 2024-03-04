select id, title, user_id 
	from tasks
	where user_id = 8;

select * 
	from tasks t 
	where status_id in (
	select id from status s 
	where name = 'new'
	);

update tasks set status_id = 2
	where id = 39;

insert into users (fullname, email) 
	values ('Bimba Lazy', 'l@zy.com')
	
select fullname from users u
	where id not in (
	select user_id from tasks
	);

insert into tasks (title, description, status_id, user_id)
	values ('GH', 'go home', 1, 8);

select *
	from tasks 
	where status_id in (
	select id from status s 
	where name <> 'completed'
	);

delete from tasks where id = 78;

select * from users u 
	where email like '%za%';

update users set fullname = 'Dimon Demon'
	where id = 5;

select status_id, count(id) from tasks
	group by status_id;

select t.id, t.title, t.description, t.status_id, t.user_id, u.fullname, u.email
	from tasks t
	join users u on t.user_id = u.id 
	where email like '%.net';

insert into tasks (title, description, status_id, user_id)
	values ('CP','', 1, 6);

select *
	from tasks t 
	where description is null or description = '';

select u.fullname, t.id as task_id, t.title, t.description, t.status_id
	from tasks t
	join users u on t.user_id = u.id 
	where t.status_id in (
	 	select id from status s
	 		where s.name = 'in progress')
	order by u.fullname;

select u.id, u.fullname, u.email, count(t.id) 
	from users u 
	left join tasks t on u.id = t.user_id
	group by u.id 
	order by u.id asc;


	


	

