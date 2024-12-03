WITH f_r as (
    SELECT * FROM
{{ ref('fct_reviews') }}
),

l_c as (
    SELECT * FROM
{{ ref("dim_listings_cleansed") }})


SELECT * FROM
f_r
INNER JOIN l_c
USING(listing_id)
WHERE l_c.created_at >= f_r.review_date 

