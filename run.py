from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock database
parts_db = {
    "C180": {
        "1998": [
            {
                "id": "MB-1998-C180-001",
                "name": "طقم تيل فرامل امامي",
                "description": "قطع أصلية من المصنع - رقم القطعة: A12345678B",
                "price": 45000,
                "origin": "ألمانيا",
                "category": "فرامل",
                "images": ["brake-pads-1.jpg", "brake-pads-2.jpg"],
                "3d_model": "brake_assembly.glb"
            },
            # More parts...
            {
                "id": 2,
                "name": "فلتر زيت محرك",
                "description": "فلتر زيت محرك اصلي لمرسيدس 1990-1999",
                "price": "320 د.ج",
                "origin": "ألمانيا",
                "category": "فلتر",
                "images": ["images/filtro.png"],
                "badge": "جديد"
            },
            {
                "id": 3,
                "name": "شمعة احتراق",
                "description": "شمعة احتراق اصلية لمعظم موديلات مرسيدس 1990-1999",
                "price": "280 د.ج",
                "origin": "اليابان",
                "category": "شمعة",
                "images": ["images/buji.png"],
                "badge": None
            },
            {
                "id": 4,
                "name": "سير المكينة",
                "description": "سير مكينة اصلي لمرسيدس C180 موديل 1998",
                "price": "380 د.ج",
                "origin": "ألمانيا",
                "category": "سير",
                "images": ["images/crua.png"],
                "badge": "عرض خاص"
            }
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_parts():
    data = request.json
    model = data.get('model')
    year = data.get('year')
    
    results = parts_db.get(model, {}).get(year, [])
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)