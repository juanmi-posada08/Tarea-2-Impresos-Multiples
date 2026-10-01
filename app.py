from flask import Flask, jsonify, request

app = Flask(__name__)

VERSION_VIGENTE = 3


@app.route("/instruccion/<title>/<int:version>")
def evaluate_instruction(title, version):
    role = request.args.get("role", "lectura")

    if version < VERSION_VIGENTE:
        status = "version obsoleta"
    elif role == "lectura":
        status = "vigente, solo lectura"
    elif role == "edicion":
        status = "vigente, edicion habilitada"
    else:
        status = "rol no reconocido"

    return jsonify({
        "instruccion": title,
        "version": version,
        "rol": role,
        "estado": status
    })


if __name__ == "__main__":
    app.run(debug=True)

# Verificado por sistema Key-2026