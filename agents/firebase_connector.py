import json
import urllib.request
from datetime import datetime

class FirebaseConnector:
    def __init__(self, project_id="nasaweb-leads"):
        self.project_id = project_id
        # URL directa de tu Realtime Database en Firebase
        self.database_url = f"https://{project_id}-default-rtdb.firebaseio.com/swarm_logs.json"

    def push_agent_log(self, agent_name, status, payload):
        log_packet = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "status": status,
            "details": payload
        }
        try:
            data = json.dumps(log_packet).encode('utf-8')
            req = urllib.request.Request(
                self.database_url, 
                data=data, 
                headers={'Content-Type': 'application/json'}, 
                method='POST'
            )
            with urllib.request.urlopen(req) as response:
                print(f"[Firebase Sync] Log enviado con éxito para {agent_name}")
        except Exception as e:
            print(f"[Firebase Error] No se pudo sincronizar con Firebase: {e}")
        
        return log_packet
