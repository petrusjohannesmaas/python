import paramiko
from flask import Flask, jsonify

# MikroTik SSH connection details
HOST = "192.168.88.1"
USER = "admin"
PASSWORD = "test123"
PORT = 22


# Function to run MikroTik command and return output
def run_mikrotik_command(command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, port=PORT, username=USER, password=PASSWORD)

        stdin, stdout, stderr = ssh.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for command to finish
        result = stdout.read().decode("utf-8")
        ssh.close()
        return result.strip()  # Clean up the output
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Flask App Setup
app = Flask(__name__)


# Function to format output as JSON
def format_output_to_json(output):
    lines = output.splitlines()
    data = []
    for line in lines:
        # Simple text parsing into key-value pairs, MikroTik output is formatted like that
        if "=" in line:
            key, value = line.split("=", 1)
            data.append({key.strip(): value.strip()})
    return data


# Get IP information
@app.route("/get-ip-info", methods=["POST"])
def get_ip_info():
    command = "/ip address print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


# Get interface status
@app.route("/get-interface-status", methods=["POST"])
def get_interface_status():
    command = "/interface print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


# Get firewall rules
@app.route("/get-firewall-rules", methods=["POST"])
def get_firewall_rules():
    command = "/ip firewall filter print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


# Get NAT rules
@app.route("/get-nat-rules", methods=["POST"])
def get_nat_rules():
    command = "/ip firewall nat print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


# Get routing table
@app.route("/get-routing-table", methods=["POST"])
def get_routing_table():
    command = "/ip route print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


# Get system information
@app.route("/get-system-info", methods=["POST"])
def get_system_info():
    command = "/system resource print"
    result = run_mikrotik_command(command)
    return jsonify(format_output_to_json(result))


if __name__ == "__main__":
    app.run(debug=True)
