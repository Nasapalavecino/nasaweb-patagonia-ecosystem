import json
from datetime import datetime
from agents.firebase_connector import FirebaseConnector
from agents.cloud_video_generator import CloudVideoGenerator

class ReelMasterAgent:
    def __init__(self, target_brand="nasaweb.ar"):
        self.agent_name = "ReelMaster"
        self.target_brand = target_brand
        self.firebase = FirebaseConnector(project_id="nasaweb-leads")

    def generate_reel_content(self, topic=None):
        if not topic:
            topic = "SEO explicado fácil: Cómo hacer que Google recomiende tu negocio local en el Alto Valle"

        payload = {
            "agent": self.agent_name,
            "target_brand": self.target_brand,
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "visual_assets": {
                "background_media_prompt": "Toma dinámica de un celular mostrando búsquedas locales en Google y comercios activos en el Alto Valle.",
                "on_screen_kinetic_text": "¿Por qué tu competencia aparece primera en Google y vos no?"
            },
            "script_structure": {
                "hook_0_3s": "¿Por qué cuando alguien busca lo que vendés en Google, el que aparece siempre es tu competencia?",
                "value_3_20s": "Tranquilo, el SEO no es chino básico. Explicado fácil: es preparar tu sitio web para que Google entienda exactamente qué hacés y en qué zona estás, como Cipolletti o el Alto Valle. Si lo hacés bien, Google te recomienda solo y gratis a los clientes que ya te están buscando con la billetera en la mano.",
                "cta_20_30s": "Entra a nasaweb.ar, agendá una asesoría y pongamos tu negocio en la primera página."
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
        print(f"[{self.agent_name}] Iniciando producción agéntica de contenido para {self.target_brand}...")
        payload = self.generate_reel_content()
        
        # Invocar al generador en la nube
        video_gen = CloudVideoGenerator(payload)
        render_result = video_gen.request_video_render()
        
        payload["rendered_video_output"] = render_result

        # Sincronización automática con Firebase
        self.firebase.push_agent_log(
            agent_name=self.agent_name,
            status="success",
            payload=payload
        )
        print(f"[{self.agent_name}] Guion de SEO sencillo y sincronización completados con éxito.")
        return payload

if __name__ == "__main__":
    agent = ReelMasterAgent()
    agent.run_reel_automation()
