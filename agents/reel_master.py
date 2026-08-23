import json
from datetime import datetime
from agents.firebase_connector import FirebaseConnector

class ReelMasterAgent:
    def __init__(self, target_brand="nasaweb.ar"):
        self.agent_name = "ReelMaster"
        self.target_brand = target_brand
        self.firebase = FirebaseConnector(project_id="nasaweb-leads")

    def generate_reel_content(self, topic=None):
        if not topic:
            topic = "SEO local explicado fácil: Cómo hacer que Google recomiende tu negocio en el Alto Valle"

        payload = {
            "agent": self.agent_name,
            "target_brand": self.target_brand,
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "production_sheet": {
                "format": "Reel / TikTok Vertical (9:16)",
                "estimated_duration": "30 segundos",
                "hook_0_3s": {
                    "visual": "Primer plano dinámico, señalando a la pantalla con texto cinético grande.",
                    "spoken_text": "¿Por qué cuando alguien busca lo que vendés en Google, el que aparece siempre es tu competencia?"
                },
                "value_3_20s": {
                    "visual": "B-roll rápido de la pantalla del celular mostrando mapas y resultados de búsqueda local en Cipolletti y el Alto Valle.",
                    "spoken_text": "Tranquilo, el SEO no es chino básico. Explicado fácil: es preparar tu sitio web para que Google entienda exactamente qué hacés y en qué zona estás. Si lo hacés bien, Google te recomienda solo y gratis a los clientes que ya te están buscando con la billetera en la mano."
                },
                "cta_20_30s": {
                    "visual": "Pantalla final con branding de Nasaweb y URL limpia.",
                    "spoken_text": "Entra a nasaweb.ar, agendá una asesoría y pongamos tu negocio en la primera página."
                }
            },
            "caption_and_seo": {
                "instagram_caption": "El posicionamiento SEO no tiene por qué ser un misterio técnico. Si tenés un comercio o PyME en la Patagonia, aparecer en Google de forma orgánica es la clave para recibir consultas todos los días sin depender de la suerte. 🚀 Escribinos o entrá a nasaweb.ar para potenciar tu visibilidad.",
                "hashtags": [
                    "#Cipolletti",
                    "#AltoValle",
                    "#RioNegro",
                    "#Nasaweb",
                    "#SEOlocal",
                    "#PyMEsPatagonia",
                    "#MarketingDigital"
                ]
            }
        }
        return payload

    def run_reel_automation(self):
        print(f"[{self.agent_name}] Iniciando producción de guion comercial para {self.target_brand}...")
        payload = self.generate_reel_content()
        
        # Sincronización automática de la hoja de producción con Firebase
        self.firebase.push_agent_log(
            agent_name=self.agent_name,
            status="ready_to_record",
            payload=payload
        )
        print(f"[{self.agent_name}] Guion comercial optimizado y sincronizado en Firebase con éxito.")
        return payload

if __name__ == "__main__":
    agent = ReelMasterAgent()
    agent.run_reel_automation()
