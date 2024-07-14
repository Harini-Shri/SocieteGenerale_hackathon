from flask import Flask, request, render_template, redirect, url_for
import asset_management
import resource_monitoring
import lifecycle_management
import predictive_maintenance
import cost_management
import train_model

app = Flask(__name__)

@app.route('/')
def index():
    assets = asset_management.get_assets()
    return render_template('index.html', assets=assets)

@app.route('/add_asset', methods=['POST'])
def add_asset():
    name = request.form['name']
    asset_type = request.form['type']
    purchase_date = request.form['purchase_date']
    warranty_period = int(request.form['warranty_period'])
    status = request.form['status']
    asset_management.add_asset(name, asset_type, purchase_date, warranty_period, status)
    return redirect(url_for('index'))

@app.route('/delete_asset/<int:asset_id>', methods=['POST'])
def delete_asset_route(asset_id):
    asset_management.delete_asset(asset_id)
    return redirect(url_for('index'))

@app.route('/predict_maintenance', methods=['POST'])
def predict_maintenance_route():
    asset_id = int(request.form['asset_id'])
    days_since_last_maintenance = int(request.form['days_since_last_maintenance'])
    prediction = predictive_maintenance.predict_from_input(asset_id, days_since_last_maintenance)
    
    return redirect(url_for('predict_maintenance_success', asset_id=asset_id, prediction=prediction))

@app.route('/predict_maintenance_success')
def predict_maintenance_success():
    asset_id = request.args.get('asset_id')
    prediction = request.args.get('prediction')
    return render_template('predict_maintenance_success.html', asset_id=asset_id, prediction=prediction)

@app.route('/train_model')
def train_model_route():
    train_model.train_model()
    return redirect(url_for('train_model_success'))

@app.route('/train_model_success')
def train_model_success():
    return render_template('train_model_success.html', message="Model trained successfully!")

@app.route('/add_maintenance', methods=['POST'])
def add_maintenance():
    asset_id = int(request.form['asset_id'])
    details = request.form['details']
    cost = float(request.form['cost'])
    cost_management.add_maintenance_cost(asset_id, details, cost)
    return redirect(url_for('index'))

@app.route('/update_status', methods=['POST'])
def update_status():
    asset_id = int(request.form['asset_id'])
    status = request.form['status']
    lifecycle_management.update_asset_status(asset_id, status)
    return redirect(url_for('index'))

@app.route('/asset_details/<int:asset_id>')
def asset_details(asset_id):
    total_cost = cost_management.get_total_cost(asset_id)
    maintenance_prediction = predictive_maintenance.predict_maintenance(asset_id)
    return render_template('asset_details.html', asset_id=asset_id, total_cost=total_cost, maintenance_prediction=maintenance_prediction)

@app.route('/lifecycle_management')
def lifecycle_management_route():
    lifecycle_data = lifecycle_management.get_lifecycle_data()
    return render_template('lifecycle_management.html', lifecycle_data=lifecycle_data)

if __name__ == '__main__':
    app.run(debug=True)
