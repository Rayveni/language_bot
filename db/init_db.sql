create table if not exists public.user_tokens(
	user_id int primary key,
	user_state varchar(40),
	user_token text,
	google_spreadsheet varchar(100),	
	created timestamp not null default current_timestamp,
	updated timestamp not null default current_timestamp
);