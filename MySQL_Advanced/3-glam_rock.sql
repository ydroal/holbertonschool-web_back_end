-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, YEAR(DATE_SUB(CURRENT_DATE(), INTERVAL 3 YEAR))) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
