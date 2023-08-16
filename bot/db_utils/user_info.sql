select user_token
       ,google_spreadsheet
from public.user_tokens
where user_id=$1
	