name = f"SELECT BillingCity AS City, SUM(Quantity) AS Total_Tracks " \
       f"FROM invoices as i " \
       f"INNER JOIN invoice_items as i2 on i.InvoiceId = i2.InvoiceId " \
       f"INNER JOIN tracks as t on i2.TrackId = t.TrackId " \
       f"INNER JOIN genres as g on t.GenreId = g.GenreId " \
       f"WHERE g.Name is 'Metal' " \
       f"GROUP BY BillingCity " \
       f"ORDER BY SUM(Quantity) DESC " \
       f"LIMIT 1;