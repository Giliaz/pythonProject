from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from flask import Flask, render_template

from sql_handler import execute_query

app = Flask(__name__)


# choice page
@app.route('/')
def index():
    return '<h3>Start page (tap choice): <a href = "country_sales">country_sales</a> (?country=..), ' \
           '<a href = "track_id"> track_id</a> (?id=..), <a href = "time_all_tracks"> time_all_tracks</a>.</h3>'


# country sales
@app.route('/country_sales')
@use_kwargs({"country": fields.Str(load_default="%"), }, location="query")
def get_country_sales(country):
       query = f"SELECT BillingCity AS City, SUM(Quantity) AS Total_Tracks " \
              f"FROM invoices as i " \
              f"INNER JOIN invoice_items as i2 on i.InvoiceId = i2.InvoiceId " \
              f"INNER JOIN tracks as t on i2.TrackId = t.TrackId " \
              f"INNER JOIN genres as g on t.GenreId = g.GenreId " \
              f"WHERE g.Name is 'Metal' " \
              f"GROUP BY BillingCity " \
              f"ORDER BY SUM(Quantity) DESC " \
              f"LIMIT 1;



if __name__ == '__main__':
    app.run(debug=True)