CREATE OR REPLACE VIEW "most_appearing_regions" AS 
(
   SELECT *
   FROM
     (
      WITH
        most_commonly AS (
         SELECT
           region
         , "count"(*) qtd
         FROM
           "833201630273:glue-database-jobsity"."parquet"
         GROUP BY 1
         ORDER BY 2 DESC
      ) 
,       trips_filter_turin_prague AS (
         SELECT *
         FROM
           "833201630273:glue-database-jobsity"."parquet"
         WHERE (region IN ('Turin', 'Prague'))
      ) 
,       last_event AS (
         SELECT "max"(datetime) max_datetime
         FROM
           trips_filter_turin_prague
      ) 
      SELECT t.*
      FROM
        (trips_filter_turin_prague t
      INNER JOIN last_event l ON (t.datetime = l.max_datetime))
   ) 
) 