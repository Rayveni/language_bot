update public.user_tokens
set user_token = $2,
    user_state=null,
    updated=now()   
where user_state= $1