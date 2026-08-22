import json
from datetime import datetime

class FirebaseConnector:
    def __init__(self, project_id="nasaweb-patagonia-db"):
        self.project_id = project_id
        self.database_url = f"https://{project_id}-default-rtdb.firebaseio.com/"

    def push_agent_log(self, agent_name, status, payload):
        log_packet = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "status": status,
            "details": payload
        }
        # Simulación de envío a Firebase Realtime Database
        print(f"[Firebase Sync] Log enviado para {agent_name} -> {status}")
        return log_packet
