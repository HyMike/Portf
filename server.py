from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


def writing_data(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email},{subject},{message}')


def writing_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:website>')
def page_name(website=None):
    return render_template(website)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writing_csv(data)
            return redirect('thankyou.html')
        except:
            return 'it didn\'t save correctly.'
    else:
        return 'something went wrong!'
