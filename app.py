from flask import Flask, render_template, request, jsonify, send_file
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
import os
import io
from datetime import datetime
from utils.password_generator import PasswordGenerator
from utils.pdf_generator import PDFGenerator
from utils.password_rules import PLATFORM_RULES
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize generators
password_gen = PasswordGenerator()
pdf_gen = PDFGenerator()

@app.route('/')
def index():
    """Main page route"""
    platforms = list(PLATFORM_RULES.keys())
    return render_template('index.html', platforms=platforms)

@app.route('/api/generate-password', methods=['POST'])
def generate_password():
    """Generate password based on platform or custom rules"""
    try:
        data = request.get_json()
        
        platform = data.get('platform', 'custom')
        length = int(data.get('length', 12))
        include_uppercase = data.get('uppercase', True)
        include_lowercase = data.get('lowercase', True)
        include_numbers = data.get('numbers', True)
        include_symbols = data.get('symbols', True)
        difficulty = data.get('difficulty', 'medium')
        
        # Validate inputs
        if length < 4 or length > 128:
            return jsonify({'error': 'Password length must be between 4 and 128 characters'}), 400
        
        # Generate password
        if platform != 'custom' and platform in PLATFORM_RULES:
            password_data = password_gen.generate_platform_password(platform, length, difficulty)
        else:
            password_data = password_gen.generate_custom_password(
                length, include_uppercase, include_lowercase, 
                include_numbers, include_symbols, difficulty
            )
        
        return jsonify({
            'success': True,
            'password': password_data['password'],
            'strength': password_data['strength'],
            'rules_applied': password_data['rules'],
            'entropy': password_data['entropy']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/check-strength', methods=['POST'])
def check_strength():
    """Check password strength in real-time"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        strength_data = password_gen.calculate_strength(password)
        
        return jsonify({
            'success': True,
            'strength': strength_data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download-pdf', methods=['POST'])
def download_pdf():
    """Generate and download password PDF report"""
    try:
        data = request.get_json()
        
        pdf_data = {
            'password': data.get('password', ''),
            'platform': data.get('platform', 'Custom'),
            'rules': data.get('rules', []),
            'strength': data.get('strength', {}),
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'entropy': data.get('entropy', 0)
        }
        
        # Generate PDF
        pdf_buffer = pdf_gen.generate_password_report(pdf_data)
        
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f'password_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/platforms')
def get_platforms():
    """Get available platforms and their rules"""
    return jsonify({
        'platforms': PLATFORM_RULES
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
