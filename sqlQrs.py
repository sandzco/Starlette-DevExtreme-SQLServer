orderSQL='''
SELECT TOP (100) [SalesOrderNumber]
      ,[PurchaseOrderNumber]
      ,[RevisionNumber]
      ,CONVERT(varchar, OrderDate, 103) as OrderDate
      ,[Status]
      ,[AccountNumber]
      ,concat(cust.LastName, ',', cust.FirstName) as CustomerName
      ,concat(terr.Name, ' - ', terr.CountryRegionCode) as Territory
      ,[BillToAddressID]
      ,[ShipToAddressID]
      ,cast([SubTotal] as float) as SubTotal
      ,cast([TaxAmt] as float) asTaxAmt
      ,cast([Freight] as float) as Freight
      ,cast([TotalDue] as float) as TotalDue
  FROM [Sales].[SalesOrderHeader] ord
  inner join [Sales].[SalesTerritory] terr on ord.TerritoryID = terr.TerritoryID
  inner join [AdvWrks].[Person].[Person] cust on cust.BusinessEntityID = ord.CustomerID
  '''