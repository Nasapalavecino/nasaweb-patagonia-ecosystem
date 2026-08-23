import json
from datetime import datetime
from agents.firebase_connector import FirebaseConnector
from agents.media_renderer import MediaRenderer

class ReelMasterAgent:
    def __init__(self, target_brand="nasaweb.ar"):
        self.agent_name = "ReelMaster"
        self.target_brand = target_brand
        self.firebase = FirebaseConnector(project_id="nasaweb-leads")

    def generate_reel_content(self, topic=None):
        if not topic:
            if "nasaweb" in self.target_brand:
                topic = "Posicionamiento web y automatización comercial para PyMEs del Alto Valle"
            else:
                topic = "Agenda de desarrollo urbano e innovación en Cipolletti"

        payload = {
            "agent": self.agent_name,
            "target_brand": self.target_brand,
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "visual_assets": {
                "background_media_prompt": "Toma dinámica en loop de comercios y paisajes urbanos del Alto Valle con interfaces digitales flotantes y métricas de conversión SEO.",
                "on_screen_kinetic_text": "¿Tu negocio en el Alto Valle sigue sin aparecer en Google?"
            },
            "script_structure": {
                "hook_0_3s": "Estás perdiendo clientes todos los días si tu comercio local no cuenta con una estructura web optimizada.",
                "value_3_20s": "En Nasaweb implementamos ecosistemas digitales y automatizaciones con IA que capturan prospectos las 24 horas, permitiéndote escalar sin depender exclusivamente de redes sociales.",
                "cta_20_30s": "Entra a nasaweb.ar, agenda tu asesoría estratégica y lleva tu marca al siguiente nivel hoy."
            },
            "caption_and_seo": {
                "instagram_caption": "El mercado digital en la Patagonia evoluciona de forma constante. Automatiza tus procesos de captación y asegura visibilidad permanente para tu PyME. 🚀",
                "hashtags": [
                    "#Cipolletti",
                    "#AltoValle",
                    "#RioNegro",
                    "#Nasaweb",
                    "#MarketingDigital",
                    "#PyMEsPatagonia",
                    "#DesarrolloWeb"
                ]
            }
        }
        return payload

    def run_reel_automation(self):
        print(f"[{self.agent_name}] Iniciando producción agéntica de contenido para {self.target_brand}...")
        payload = self.generate_reel_content()
        
        # Invocar al motor de renderizado para compilar la especificación del Storyboard
        renderer = MediaRenderer(payload)
        renderer.render_storyboard_spec()

        # Sincronización automática de datos estructurados con Firebase
        self.firebase.push_agent_log(
            agent_name=self.agent_name,
            status="success",
            payload=payload
        )
        print(f"[{self.agent_name}] Paquete audiovisual estructurado, renderizado y sincronizado en Firebase con éxito.")
        return payload

if __name__ == "__main__":
    agent = ReelMasterAgent()
    agent.run_reel_automation()utomation()
