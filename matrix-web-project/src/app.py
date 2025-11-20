from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rows_raw = request.form.get('rows', '').strip()
        cols_raw = request.form.get('cols', '').strip()
        matrix_text = request.form.get('matrix_text', '').strip()

        try:
            rows = int(rows_raw)
            cols = int(cols_raw)
        except ValueError:
            flash("Rows and columns must be integers")
            return redirect(url_for('index'))

        if not matrix_text:
            flash("Please provide matrix elements in the textarea")
            return redirect(url_for('index'))

        matrix_lines = [line.strip() for line in matrix_text.splitlines() if line.strip()]
        if len(matrix_lines) != rows:
            flash(f"Expected {rows} rows of data, but got {len(matrix_lines)}")
            return redirect(url_for('index'))

        matrix = []
        try:
            for line in matrix_lines:
                parts = line.replace(',', ' ').split()
                if len(parts) != cols:
                    raise ValueError("Column count mismatch")
                row = [int(p) for p in parts]
                matrix.append(row)
        except ValueError:
            flash("Matrix elements must be integers and match the specified columns per row")
            return redirect(url_for('index'))

        return render_template('result.html', matrix=matrix)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)