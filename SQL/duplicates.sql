--Find a duplicates
WITH RowNumCTE AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY sno, summary
            ORDER BY summary
        ) AS row_num
    FROM care
)  -- Ensure this closing parenthesis matches the opening parenthesis

SELECT *
FROM RowNumCTE
WHERE row_num > 1
ORDER BY summary;

-- Remove the duplicates
BEGIN TRANSACTION;

WITH RowNumCTE AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY sno, summary
            ORDER BY summary
        ) AS row_num
    FROM care
)

DELETE FROM RowNumCTE
WHERE row_num > 1;

-- If everything is fine, commit the transaction
COMMIT;

-- If something goes wrong, uncomment the next line to roll back
-- ROLLBACK;
select * from care