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
    query = f"SELECT BillingCountry, UnitPrice AS Price_Unit, COUNT(Quantity) AS Total_Quantity,(COUNT(Quantity) * UnitPrice) AS Total_Sales " \
            f"FROM invoice_items as i1 " \
            f"JOIN invoices as i2 on i1.InvoiceId = i2.InvoiceId " \
            f"WHERE BillingCountry LIKE '{country}' " \
            f"GROUP BY BillingCountry;"

    records = [('Country', 'Price', 'Quantity', 'Sales')]
    records.extend(execute_query(query))
    return render_template("table_from_list.html", csv=records)


# track id
@app.route('/track_id')
@use_kwargs({"id": fields.Int(missing=1, validate=[validate.Range(min=1, max=3503)]), }, location="query")
def get_track_id(id):
    query = f"SELECT t.TrackId, t.Name AS Track, a.Title AS Album, a2.Name AS Team, t.Composer AS Composers, " \
            f"g.Name AS Genre, GROUP_CONCAT(pl.Name) AS Play_Lists, mt.Name AS Media_Type, " \
            f"t.Milliseconds/60000 AS Track_Time, t.Bytes/1000000 AS Track_Size, t.UnitPrice AS Price " \
            f"FROM tracks as t " \
            f"JOIN albums as a on t.AlbumId = a.AlbumId " \
            f"JOIN artists as a2 on a.ArtistId = a2.ArtistId " \
            f"JOIN genres as g on t.GenreId = g.GenreId " \
            f"JOIN media_types as mt on t.MediaTypeId = mt.MediaTypeId " \
            f"JOIN playlist_track as plt on t.TrackId = plt.TrackId " \
            f"JOIN playlists as pl on plt.PlaylistId = pl.PlaylistId " \
            f"WHERE t.TrackId LIKE {id};"

    records = [('TrackId', 'Track', 'Album', 'Team', 'Composers', 'Genre',
                     'Play_Lists', 'Media_Type', 'Time(min)','Size(mb)', 'Price')]
    records.extend(execute_query(query))
    return render_template("table_from_list.html", csv=records)


@app.route('/time_all_tracks')
def get_time():
    query = f"SELECT SUM(Milliseconds)/3600000 " \
            f"FROM tracks as t " \
            f"JOIN albums as a on t.AlbumId = a.AlbumId;"

    return f'<h3>Total time all tracks: {execute_query(query)[0][0]} hrs.<h/3>'


if __name__ == '__main__':
    app.run(debug=True)
