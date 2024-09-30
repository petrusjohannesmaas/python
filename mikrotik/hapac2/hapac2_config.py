import paramiko
from flask import Flask, jsonify, request

# MikroTik SSH connection details
HOST = "192.168.88.1"
USER = "admin"
PASSWORD = "test123"
PORT = 22


# Function to run commands on MikroTik router
def run_mikrotik_command(commands):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, port=PORT, username=USER, password=PASSWORD)

        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            stdout.channel.recv_exit_status()  # Wait for command to finish
            error = stderr.read().decode("utf-8")
            if error:
                raise Exception(f"Error executing command: {error}")

        ssh.close()
        return "Commands executed successfully"

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Flask App Setup
app = Flask(__name__)


# Bridge setup
@app.route("/setup-bridge", methods=["POST"])
def setup_bridge():
    commands = [
        "/interface bridge add name=bridge1",
        "/interface bridge port add interface=ether2 bridge=bridge1",
        "/ip address add address=192.168.88.1/24 interface=bridge1",
        "/ip pool add name=dhcp_pool ranges=192.168.88.2-192.168.88.254",
        "/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1",
        "/ip dhcp-server add name=dhcp_server interface=bridge1 address-pool=dhcp_pool lease-time=30m disabled=no",
    ]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


# WAN setup
@app.route("/setup-wan", methods=["POST"])
def setup_wan():
    commands = [
        "/ip dhcp-client add disabled=no interface=ether1",
        "/interface pppoe-client add disabled=no interface=ether1 user=me password=123 add-default-route=yes use-peer-dns=yes",
    ]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


# Ping Google
@app.route("/ping-test", methods=["POST"])
def ping_test():
    commands = ["/ping 8.8.8.8 count=4"]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


# User management
@app.route("/setup-user", methods=["POST"])
def setup_user():
    commands = [
        "/user add name=jupyter password=testing123 group=full",
        "/user remove admin",
    ]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


# Disable services
@app.route("/disable-services", methods=["POST"])
def disable_services():
    commands = [
        "/ip proxy set enabled=no",
        "/ip socks set enabled=no",
        "/ip upnp set enabled=no",
        "/ip cloud set ddns-enabled=no update-time=no",
    ]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


# Firewall and NAT setup
@app.route("/setup-firewall", methods=["POST"])
def setup_firewall():
    commands = [
        "/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade",
        "/ip firewall nat add chain=dstnat protocol=tcp port=3389 in-interface=ether1 action=dst-nat to-address=192.168.88.254",
        "/ip firewall filter add chain=forward action=fasttrack-connection connection-state=established,related",
        "/ip firewall filter add chain=forward action=accept connection-state=established,related",
        "/ip firewall filter add chain=forward action=drop connection-state=invalid",
        "/ip firewall filter add chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface=ether1 comment='Drop WAN access to LAN'",
    ]
    result = run_mikrotik_command(commands)
    return jsonify({"message": result})


if __name__ == "__main__":
    app.run(debug=True)
