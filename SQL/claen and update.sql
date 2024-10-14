SELECT TOP (1000) [UniqueID ] 
      ,[ParcelID]
      ,[LandUse]
      ,[PropertyAddress]
      ,[SaleDate]
      ,[SalePrice]
      ,[LegalReference]
      ,[SoldAsVacant]
      ,[OwnerName]
      ,[OwnerAddress]
      ,[Acreage]
      ,[TaxDistrict]
      ,[LandValue]
      ,[BuildingValue]
      ,[TotalValue]
      ,[YearBuilt]
      ,[Bedrooms]
      ,[FullBath]
      ,[HalfBath]
  FROM [webdata].[dbo].[newtable]
  --order by
  select * from webdata ..newtable
  order by ParcelID

  --join
  Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress,b.PropertyAddress)
From webdata.dbo.newtable a
JOIN webdata.dbo.newtable b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null
  
  -- Breaking out a string
  Select PropertyAddress
From webdata.dbo.newtable
--Where PropertyAddress is null
--order by ParcelID

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 ) as Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress)) as Address

From webdata.dbo.newtable
--- add the changes into the original table
-- Add the first new column

--the column was added
ALTER TABLE newtable
ADD PropertySplitAddress NVARCHAR(255);
--update
UPDATE newtable 
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1)
WHERE CHARINDEX(',', PropertyAddress) > 0;
--- new column city
ALTER TABLE newtable
ADD PropertySplitCity NVARCHAR(255);
--update
UPDATE newtable 
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))
WHERE CHARINDEX(',', PropertyAddress) > 0;
 select * from newtable 

