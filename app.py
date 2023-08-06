import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

PRIVATE_REPO_URL = os.environ.get("PRIVATE_REPO_URL")
PRIVATE_REPO_TOKEN = os.environ.get("PRIVATE_REPO_TOKEN")
KOYEB_DEPLOYMENT_PATH = os.environ.get("KOYEB_DEPLOYMENT_PATH")

@app.route('/deploy', methods=['POST'])
def deploy_to_koyeb():
    try:
        subprocess.run(["/bin/bash", "deploy_script.sh"])
        
        return jsonify({"message": "Deployed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
