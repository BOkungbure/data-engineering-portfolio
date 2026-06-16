select
    game_name,
    developer,
    release_date,
    positive_ratings,
    negative_ratings,
    positive_ratings + negative_ratings as total_ratings,
    round(
    (cast(positive_ratings as numeric) / nullif(positive_ratings + negative_ratings, 0) * 100), 2
        ) as approval_pct,
    price
from {{ ref('stg_games') }}
where price > 0