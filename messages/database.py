from flask import Flask, request, render_template
import mysql.connector
from collections import Counter

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deeksha",
    database="messages"
)
cursor = mydb.cursor()


@app.route('/user', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        source = request.form.get('source')
        message = request.form.get('message')

        sql = "INSERT INTO message_db (source, message) VALUES (%s, %s)"
        val = (source, message)
        cursor.execute(sql, val)
        mydb.commit()

    return render_template('user_input.html')


@app.route('/', methods=['GET'])
def db_service():
    summary_query = ("SELECT COUNT(DISTINCT source) AS total_unique_sources, COUNT(DISTINCT message) AS "
                     "total_unique_messages, COUNT(*) AS total_messages FROM message_db")
    cursor.execute(summary_query)
    summary_result = cursor.fetchone()

    cursor.execute("SELECT * FROM message_db")
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()

    detailed_report = []

    for row in data:
        detailed_report.append(dict(zip(columns, row)))

    cursor.execute("SELECT message FROM message_db")
    all_messages = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT source FROM message_db")
    all_senders = [row[0] for row in cursor.fetchall()]

    message_counts = Counter(all_messages)
    sender_counts = Counter(all_senders)

    max_size = 40
    min_size = 10
    message_font_sizes = {}
    sender_font_sizes = {}

    if message_counts:
        sorted_messages = sorted(message_counts, key=lambda x: message_counts[x], reverse=True)
        step_size_messages = (max_size - min_size) / len(sorted_messages)
        for i, message in enumerate(sorted_messages, start=1):
            message_font_sizes[message] = f"{int(max_size - (step_size_messages * i))}px"

    if sender_counts:
        sorted_senders = sorted(sender_counts, key=lambda x: sender_counts[x], reverse=True)
        step_size_senders = (max_size - min_size) / len(sorted_senders)
        for i, sender in enumerate(sorted_senders, start=1):
            sender_font_sizes[sender] = f"{int(max_size - (step_size_senders * i))}px"

    summary = {
        'Total Unique Sources': summary_result[0],
        'Total Unique Messages': summary_result[1],
        'Total Messages': summary_result[2],
        'Detailed Report': detailed_report,
        'Message Font Sizes': message_font_sizes,
        'Sender Font Sizes': sender_font_sizes
    }

    return render_template('index.html', summary=summary)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
