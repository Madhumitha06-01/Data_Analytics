SELECT TOP (1000) [SNO]
      ,[CODE]
      ,[ITEMNAME]
      ,[SUMMARY]
      ,[IMAGE_URL]
      ,[MRP]   
      
  FROM [webdata].[dbo].[vissco]
  --- select mrp by use max
  select ITEMNAME, MAX(MRP)
  from  webdata..vissco
 -- where ITEMNAME like '%Dyna%'
 -- where MRP is not null
   where MRP is  null
  group by ITEMNAME 
  -- join a table1& 2
  select *
  from webdata..vissco vis
 join webdata..vissco1 co
 on vis.ITEMNAME = co.ITEMNAME
    --- select table 1
	SELECT TOP (1000) [ITEMNAME]
      ,[MRP]
      ,[SUMMARY]
  FROM [webdata].[dbo].[vissco1]
  -- select table 2
  SELECT TOP (1000) [SNO]
      ,[CODE]
      ,[ITEMNAME]
      ,[SUMMARY]
      ,[IMAGE_URL]
      ,[MRP]
  FROM [webdata].[dbo].[vissco]
	-- sum the value
SELECT 
    ITEMNAME,
    SUM(CONVERT(int, MRP)) AS TotalMRP
FROM 
    [webdata].[dbo].[vissco]
WHERE 
    ISNUMERIC(MRP) = 1
GROUP BY 
    ITEMNAME;



	