insert into public.user_tokens(user_id, user_state)
values($1,$2)
on conflict(user_id)
do 
update set  user_state = $2,
            updated=now()