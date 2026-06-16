select
    appid,
    name as game_name,
    cast(release_date as date) as release_date,
    developer,
    cast(positive_ratings as int) as positive_ratings,
    cast(negative_ratings as int) as negative_ratings,
    cast(price as float) as price
from {{ ref('raw_data') }}