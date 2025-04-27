from flask import Flask, render_template, request, redirect, url_for
from your_script import run_automation  # you'll wrap your big script inside a function called `run_automation`

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_sheet_id = request.form.get('source_sheet_id')
        target_sheet_id = request.form.get('target_sheet_id')

        # Call your main automation function
        run_automation(source_sheet_id, target_sheet_id)

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return "✅ Your sheets have been processed! Check the target Google Sheet."

if __name__ == '__main__':
    app.run(debug=True)
