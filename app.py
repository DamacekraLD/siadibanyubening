from flask import Flask, jsonify, Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "siadibanyubening"
app.config['DEBUG'] = True

# DATA DUMMY UNTUK DOKTER
dokters = [
    {
        'id': 1,
        'nama': 'Dr. Ahmad Fauzi',
        'spesialis': 'Dokter Umum',
        'jadwal': 'Senin, Rabu, Jumat',
        'ruangan': '101',
        'notelp': '081234567890'
    },
    {
        'id': 2,
        'nama': 'Dr. Siti Nurhaliza',
        'spesialis': 'Dokter Gigi',
        'jadwal': 'Selasa, Kamis',
        'ruangan': '102',
        'notelp': '082345678901'
    },
    {
        'id': 3,
        'nama': 'Dr. Budi Santoso',
        'spesialis': 'Dokter Anak',
        'jadwal': 'Senin - Jumat',
        'ruangan': '103',
        'notelp': '083456789012'
    }
]

pasiens = [
    {
        'id': 1,
        'nama': 'Andi Wijaya',
        'umur': 30,
        'jenis_kelamin': 'Laki-laki',
        'alamat': 'Jl. Merdeka No. 10',
        'notelp': '081234567890'
    },
    {
        'id': 2,
        'nama': 'Sari Lestari',
        'umur': 25,
        'jenis_kelamin': 'Perempuan',
        'alamat': 'Jl. Sudirman No. 20',
        'notelp': '082345678901'
    },
    {
        'id': 3,
        'nama': 'Rina Susanti',
        'umur': 28,
        'jenis_kelamin': 'Perempuan',
        'alamat': 'Jl. Thamrin No. 30',
        'notelp': '083456789012'
    }
]

obats = [
    {
        "id": 1, 
        "nama_obat": "Paracetamol", 
        "kategori": "Analgesik", 
        "harga": 5000, 
        "stok": 100, 
        "supplier": 
        "Kimia Farma"},
    {
        "id": 2, 
        "nama_obat": 
        "Amoxicillin", 
        "kategori": "Antibiotik", 
        "harga": 12000, 
        "stok": 50, 
        "supplier": 
        "Dexa Medica"},
    {
        "id": 3, 
        "nama_obat": "Betadine", 
        "kategori": "Antiseptik", 
        "harga": 18000, 
        "stok": 30, 
        "supplier": "Mahakam Beta Farma"}
]



# ROUTE UNTUK WEBSITE

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/dokter', methods=["GET"])
def getdokter():
    return render_template('dokter598/data_dokter.html', dokter=dokters)

@app.route('/pasien', methods=["GET"])
def getpasien():
    return render_template('pasien616/data_pasien.html', pasien=pasiens)

@app.route('/apotek', methods=["GET"])
def getapotek():
    return render_template('apotek591/data_apotek.html', obat=obats)

# ROUTE DOKTER

@app.route('/tambahdokter', methods=['GET'])
def form_dokter():
    return render_template('dokter598/form_dokter.html', dokter=None)

@app.route('/simpan_dokter', methods=['POST'])
def simpan_dokter():
    nama = request.form['nama']
    spesialis = request.form['spesialis']
    jadwal = request.form['jadwal']
    ruangan = request.form['ruangan']
    notelp = request.form['notelp']

    new_id = max(dokter['id'] for dokter in dokters) + 1 if dokters else 1
    new_dokter = {
        'id': new_id,
        'nama': nama,
        'spesialis': spesialis,
        'jadwal': jadwal,
        'ruangan': ruangan,
        'notelp': notelp
    }
    dokters.append(new_dokter)
    flash('Data dokter berhasil disimpan!', 'success')
    return render_template('dokter598/data_dokter.html', dokter=dokters, message="Data dokter berhasil disimpan!")

@app.route('/edit_dokter/<int:id>', methods=['GET'])
def edit_dokter(id):
    dokter_obj = next((d for d in dokters if d['id'] == id), None)
    return render_template('dokter598/form_dokter.html', dokter=dokter_obj)

@app.route('/update_dokter/<int:id>', methods=['PUT'])
def update_dokter(id):
    data = request.get_json()
    for d in dokters:
        if d['id'] == id:
            d['nama'] = data.get('nama', d['nama'])
            d['spesialis'] = data.get('spesialis', d['spesialis'])
            d['jadwal'] = data.get('jadwal', d['jadwal'])
            d['ruangan'] = data.get('ruangan', d['ruangan'])
            d['notelp'] = data.get('notelp', d['notelp'])
            flash('Data dokter berhasil diperbarui!', 'success')
            return jsonify(success=True)
    return jsonify(success=False)

@app.route('/hapus_dokter/<int:id>', methods=['DELETE'])
def hapus_dokter(id):
    global dokters
    dokters = [d for d in dokters if d['id'] != id]
    flash('Data dokter berhasil dihapus!', 'success')
    return jsonify(success=True)

# ROUTE PASIEN

@app.route('/tambahpasien', methods=['GET'])
def form_pasien():
    return render_template('pasien616/form_pasien.html', pasien=None)

@app.route('/simpan_pasien', methods=['POST'])
def simpan_pasien():
    nama = request.form['nama']
    umur = int(request.form['umur'])
    jenis_kelamin = request.form['jenis_kelamin']
    alamat = request.form['alamat']
    notelp = request.form['notelp']

    new_id = max(pasien['id'] for pasien in pasiens) + 1 if pasiens else 1
    new_pasien = {
        'id': new_id,
        'nama': nama,
        'umur': umur,
        'jenis_kelamin': jenis_kelamin,
        'alamat': alamat,
        'notelp': notelp
    }
    pasiens.append(new_pasien)
    flash('Data pasien berhasil disimpan!', 'success')
    return render_template('pasien616/data_pasien.html', pasien=pasiens, message="Data pasien berhasil disimpan!")

@app.route('/edit_pasien/<int:id>', methods=['GET'])
def edit_pasien(id):
    pasien_obj = next((p for p in pasiens if p['id'] == id), None)
    return render_template('pasien616/form_pasien.html', pasien=pasien_obj)

@app.route('/update_pasien/<int:id>', methods=['PUT'])
def update_pasien(id):
    data = request.get_json()
    for p in pasiens:
        if p['id'] == id:
            p['nama'] = data.get('nama', p['nama'])
            p['umur'] = data.get('umur', p['umur'])
            p['jenis_kelamin'] = data.get('jenis_kelamin', p['jenis_kelamin'])
            p['alamat'] = data.get('alamat', p['alamat'])
            p['notelp'] = data.get('notelp', p['notelp'])
            flash('Data pasien berhasil diperbarui!', 'success')
            return jsonify(success=True)
    return jsonify(success=False)

@app.route('/hapus_pasien/<int:id>', methods=['DELETE'])
def hapus_pasien(id):
    global pasiens
    pasiens = [p for p in pasiens if p['id'] != id]
    flash('Data pasien berhasil dihapus!', 'success')
    return jsonify(success=True)

# ROUTE APOTEK

@app.route('/tambahapotek', methods=['GET'])
def form_apotek():
    return render_template('apotek591/form_apotek.html', obat=None)

@app.route('/simpan_apotek', methods=['POST'])
def simpan_apotek():
    nama_obat = request.form['nama']
    kategori = request.form['kategori']
    harga = int(request.form['harga'])
    stok = int(request.form['stok'])
    supplier = request.form['supplier']

    new_id = max(obat['id'] for obat in obats) + 1 if obats else 1
    new_obat = {
        'id': new_id,
        'nama_obat': nama_obat,
        'kategori': kategori,
        'harga': harga,
        'stok': stok,
        'supplier': supplier
    }
    obats.append(new_obat)
    flash('Data obat berhasil disimpan!', 'success')
    return render_template('apotek591/data_apotek.html', obat=obats, message="Data obat berhasil disimpan!")

@app.route('/edit_apotek/<int:id>', methods=['GET'])
def edit_apotek(id):
    obat_obj = next((o for o in obats if o['id'] == id), None)
    return render_template('apotek591/form_apotek.html', obat=obat_obj)

@app.route('/update_apotek/<int:id>', methods=['PUT'])
def update_apotek(id):
    data = request.get_json()
    for o in obats:
        if o['id'] == id:
            o['nama_obat'] = data.get('nama', o['nama_obat'])
            o['kategori'] = data.get('kategori', o['kategori'])
            o['harga'] = data.get('harga', o['harga'])
            o['stok'] = data.get('stok', o['stok'])
            o['supplier'] = data.get('supplier', o['supplier'])
            flash('Data obat berhasil diperbarui!', 'success')
            return jsonify(success=True)
    return jsonify(success=False)

@app.route('/hapus_apotek/<int:id>', methods=['DELETE'])
def hapus_apotek(id):
    global obats
    obats = [o for o in obats if o['id'] != id]
    flash('Data obat berhasil dihapus!', 'success')
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()