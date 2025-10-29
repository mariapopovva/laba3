from flask import Flask, request, jsonify
from service import add_income, add_expense


app = Flask(__name__)
BALANCE = 0.0


@app.post("/income")
def income():
    global BALANCE
    amount = float(request.json.get("amount", 0))
    BALANCE = add_income(BALANCE, amount)
    return jsonify({"balance": BALANCE})


@app.post("/expense")
def expense():
    global BALANCE
    amount = float(request.json.get("amount", 0))
    BALANCE = add_expense(BALANCE, amount)
    return jsonify({"balance": BALANCE})


@app.get("/balance")
def balance():
    return jsonify({"balance": BALANCE})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)