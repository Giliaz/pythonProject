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
    query = f"SELECT UnitPrice AS Price_Unit, count(Quantity) AS Total_Quanity,(count(Quantity) * UnitPrice) AS Total_Sales " \
            f"FROM invoice_items " \
            f"JOIN invoices i on invoice_items.InvoiceId = i.InvoiceId " \
            f"WHERE BillingCountry LIKE '{country}';"

    records = execute_query(query)
    return (f'<h3>For {country}:' if country != "%" else '<h3>For all countries:') + \
           f' Price {records[0][0]} USD, Quantity {records[0][1]} ps., Sales {records[0][2]} USD.</h3>'


# track id
@app.route('/track_id')
@use_kwargs({"id": fields.Int(missing=1, validate=[validate.Range(min=1, max=3503)]), }, location="query")
def get_track_id(id):
    query = f"SELECT tracks.Name AS Track, a3.Name AS Team, tracks.Composer AS Composers," \
                    f" a2.Title AS Album, g.Name AS Genre, mt.Name AS Media, (tracks.Milliseconds/60000) AS 'Longest(min.)', " \
                    f" (tracks.Bytes/1000000) AS 'Size(MB)', tracks.UnitPrice AS 'Price(USD)' " \
            f"FROM tracks " \
            f"JOIN playlist_track pt on tracks.TrackId = pt.TrackId, " \
                    f" playlists p join playlist_track t on p.PlaylistId = t.PlaylistId, " \
                    f" tracks t2 join genres g on g.GenreId = t2.GenreId, " \
                    f" tracks t3 join albums a on a.AlbumId = t3.AlbumId, " \
                    f" albums a2 join artists a3 on a3.ArtistId = a2.ArtistId, " \
                    f" albums a4 join media_types mt on mt.MediaTypeId = t3.MediaTypeId, " \
                    f" tracks t4 join invoice_items ii on t.TrackId = ii.TrackId, " \
                    f" invoice_items i join invoices i2 on i2.InvoiceId = i.InvoiceId, " \
                    f" invoices i3 join customers c on i3.CustomerId = c.CustomerId, " \
                    f" customers c2 join employees e on c2.SupportRepId = e.EmployeeId " \
            f"WHERE tracks.TrackId = {id} " \
            f"LIMIT 1;"

    records = execute_query(query)
    return render_template("table_from_list.html", csv=records)


@app.route('/time_all_tracks')
def get_time():
    query = f"SELECT SUM(Milliseconds)/3600000" \
            f" FROM tracks" \
            f" JOIN albums a on tracks.AlbumId = a.AlbumId;"

    return f'<h3>Total time all tracks: {execute_query(query)[0][0]} hrs.<h/3>'


if __name__ == '__main__':
    app.run(debug=True)
