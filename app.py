from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'bhavya.mettupalli@gmail.com'
app.config['MAIL_PASSWORD'] = 'tklr mnnz lsrz rcwe'

app.config['SECRET_KEY'] = 'csac jsnaco6465c 4ssd64c'

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if not all([name, email, subject, message]):
        return jsonify({'error': 'Missing data!'}), 400

    try:
        # Send email
        msg = Message(subject=f"New Contact Form Submission: {subject}",
                      sender=email,
                      recipients=['bhavya.mettupalli@gmail.com'])  # Your email here
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return jsonify({'success': 'Message sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
