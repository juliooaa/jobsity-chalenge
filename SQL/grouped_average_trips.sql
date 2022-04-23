CREATE OR REPLACE VIEW "grouped_average_trips_per_region" AS 
(
   SELECT *
   FROM
     (
      WITH
        trips_grouped AS (
         SELECT
           origin_coord
         , destination_coord
         , datetime
         , "max"("region") region
         , "max"("datasource") datasource
         FROM
           "833201630273:glue-database-jobsity"."parquet"
         GROUP BY 1, 2, 3
      ) 
,       weekly_average AS (
         SELECT
           region
         , EXTRACT(WEEK FROM datetime) week
         , "count"(*) qtd
         FROM
           trips_grouped
         GROUP BY 1, 2
      ) 
      SELECT *
      FROM
        weekly_average
      ORDER BY week ASC
   ) 
) 