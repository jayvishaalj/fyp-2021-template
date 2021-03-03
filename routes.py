from flask import render_template, jsonify, make_response, request
import json
from bulk_layer import check_bulkiness


def routes_with_app(app, data):
    @app.route('/')
    @app.route('/dashboard.html')
    def dashboard():
        return render_template('dashboard.html', async_mode=None)

    @app.route('/testpage')
    def indexpage():
        return render_template('index.html', async_mode=None)

    @app.route('/user.html')
    def user_page():
        return render_template('user.html')

    @app.route('/ping')
    def get_ping():
        return 'ping'

    @app.route("/login/<name>")
    def index(name):
        print(request.remote_addr)
        # ' OR '1'='1
        query = "SELECT * FROM users WHERE username = '{0}'".format(name)
        print(query)
        result = data.query(sql=query, value=name)
        if(result == None):
            resp = make_response(jsonify(
                {"data": None, "message": "Your Sql Injection is Alerted to Tenent"}), 206)
            return resp
        resData = result.fetchall()
        resp = make_response(jsonify({"data": resData}), 200)
        resp = check_bulkiness(resp, 50)
        if(resp == None):
            resp = make_response(
                jsonify({"data": "ATTEMPT TO DATA LEAK DETECTED"}), 400)
        return resp

    # # serve index for all paths, so a client side router can take over
    @app.route('/<path:path>')
    def get_home_redirect(path):
        return dashboard()
