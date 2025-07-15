from flask import Flask, render_template, request, redirect, url_for,jsonify


from app import masa_reset, raporlayici, veritabani # app klasöründeki modüller

app = Flask(__name__)
  # veritabani eklendi

@app.route('/siparisler')
def siparisler():
    df = veritabani.tum_siparisleri_getir()
    return render_template(
        'siparisler.html',
        siparis_html=df.to_html(classes='table table-striped', index=False)
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/garson')
def garson():
    return render_template('garson.html')

@app.route('/yemek')
def yemek():
    return render_template('yemek.html')

"""@app.route('/siparisler')
def siparisler():
    siparis_df = raporlayici.siparis_raporu()
    return render_template(
        'siparisler.html',
        siparis_html=siparis_df.to_html(classes='table table-striped', index=False)
    )
"""
@app.route('/rapor')
def rapor():
    siparis_df = raporlayici.siparis_raporu()
    performans_df = raporlayici.performans_raporu()

    return render_template(
        'rapor.html',
        siparis_html=siparis_df.to_html(classes='table table-striped', index=False),
        performans_html=performans_df.to_html(classes='table table-striped', index=False)
    )

@app.route('/garson_ilgi', methods=['POST'])
def garson_ilgi():
    data = request.json
    masa_no = data.get('masa_no')
    garson_id = data.get('garson_id')
    ilgi_suresi = data.get('ilgi_suresi')  # saniye cinsinden
    
    if not all([masa_no, garson_id, ilgi_suresi]):
        return jsonify({'error': 'Eksik veri'}), 400
    
    veritabani.garson_ilgi_suresi_ekle(masa_no, garson_id, ilgi_suresi)
    
    return jsonify({'message': 'İlgi süresi kaydedildi'}), 200


@app.route('/masa_reset', methods=['GET', 'POST'])
def masa_reset_route():
    if request.method == 'POST':
        masa_no = request.form.get('masa_no')
        if masa_no:
            masa_reset.masa_reset(int(masa_no))
        else:
            masa_reset.masa_reset()
        return redirect(url_for('index'))
    return render_template('masa_reset.html')

if __name__ == '__main__':
    app.run(debug=True)
