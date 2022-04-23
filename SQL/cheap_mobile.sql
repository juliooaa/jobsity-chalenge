CREATE OR REPLACE VIEW "cheap_mobile" AS 
(
   SELECT DISTINCT region
   FROM
     "833201630273:glue-database-jobsity"."parquet"
   WHERE (datasource = 'cheap_mobile')
) 