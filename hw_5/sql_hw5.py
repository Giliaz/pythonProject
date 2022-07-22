from flask import Flask, render_template
from webargs import fields
from webargs.flaskparser import use_kwargs

from hw_5.sql_handler import execute_query

app = Flask(__name__)


# choice page
@app.route('/')
def index():
    return '<h3>Start page (tap choice): <a href = "genres_sales">genres_sales</a> (?genre=..) </h3>'


# country sales
@app.route('/genres_sales')
@use_kwargs({"genre": fields.Str(load_default=''), }, location="query")
def get_country_sales(genre):
    query = f"SELECT g.Name, BillingCity AS City, SUM(Quantity) AS Total_Tracks " \
            f"FROM invoices as i " \
            f"INNER JOIN invoice_items as i2 on i.InvoiceId = i2.InvoiceId " \
            f"INNER JOIN tracks as t on i2.TrackId = t.TrackId " \
            f"INNER JOIN genres as g on t.GenreId = g.GenreId " \
            f"WHERE g.Name LIKE '{genre}' " \
            f"GROUP BY BillingCity " \
            f"ORDER BY SUM(Quantity) DESC " \
            f"LIMIT 1; "

    records = [('Genre music', 'City of best sales', 'Sales(tracks)')]
    records.extend(execute_query(query))

    if (len(records) < 2) & (genre != ''):
        return f'<h3>genres_sales(?genre=..)<br><font color="red">Genre is not correct or not find in database...</color>{render_template("table_from_list.html", csv=records)}</h3>'
    else:
        return f'<h3>genres_sales(?genre=..)</h3>{render_template("table_from_list.html", csv=records)}'



if __name__ == '__main__':
    app.run(debug=True)