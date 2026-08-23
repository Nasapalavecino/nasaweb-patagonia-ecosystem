import os
import json
import requests
from datetime import datetime

class CloudVideoGenerator:
    def __init__(self, reel_payload: dict):
        self.payload = reel_payload
        self.api_key = os.environ.get("VIDEO_RENDER_API_KEY", "sandbox_mock_key")
        self.api_url = "https://api.shotstack.io/edit/v1/render"

    def build_cloud_render_payload(self):
        """
        Traduce el storyboard del agente a una estructura de edición de video en la nube.
        """
        script = self.payload.get("script_structure", {})
        assets = self.payload.get("visual_assets", {})
        brand = self.payload.get("target_brand", "nasaweb.ar")

        render_spec = {
            "timeline": {
                "soundtrack": {
                    "src": "https://freesound.org/data/previews/538/538466_11861866-lq.mp3",
                    "effect": "fadeInFadeOut",
                    "volume": 0.2
                },
                "tracks": [
                    {
                        "clips": [
                            {
                                "asset": {
                                    "type": "title",
                                    "text": assets.get("on_screen_kinetic_text", "¿Tu negocio aparece en Google?"),
                                    "style": "marker",
                                    "color": "#38bdf8",
                                    "size": "large"
                                },
                                "start": 0,
                                "length": 3,
                                "effect": "zoomIn"
                            },
                            {
                                "asset": {
                                    "type": "html",
                                    "html": f"<p style='color: white; font-family: sans-serif; font-size: 28px;'>{script.get('value_3_20s')}</p>",
                                    "width": 800,
                                    "height": 600
                                },
                                "start": 3,
                                "length": 17
                            },
                            {
                                "asset": {
                                    "type": "title",
                                    "text": f"Visita {brand}",
                                    "style": "block",
                                    "color": "#ffffff",
                                    "background": "#0284c7"
                                },
                                "start": 20,
                                "length": 10
                            }
                        ]
                    }
                ]
            },
            "output": {
                "format": "mp4",
                "resolution": "sd",
                "aspectRatio": "9:16"
            }
        }
        return render_spec

    def request_video_render(self):
        print("[CloudVideoGenerator] Preparando solicitud de renderizado de video en la nube...")
        render_body = self.build_cloud_render_payload()

        if self.api_key == "sandbox_mock_key":
            mock_video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
            print(f"[CloudVideoGenerator] (Modo Sandbox) Video simulado con éxito.")
            return {
                "status": "rendered",
                "video_url": mock_video_url,
                "render_timestamp": datetime.now().isoformat()
            }

        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(self.api_url, json=render_body, headers=headers)
            if response.status_code == 201:
                data = response.json()
                video_id = data.get("response", {}).get("id")
                print(f"[CloudVideoGenerator] Render en proceso. ID de tarea: {video_id}")
                return {"status": "processing", "task_id": video_id}
            else:
                print(f"[CloudVideoGenerator] Error en la API: {response.text}")
                return {"status": "error", "message": response.text}
        except Exception as e:
            print(f"[CloudVideoGenerator] Excepción de red: {e}")
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    sample_payload = {
        "target_brand": "nasaweb.ar",
        "script_structure": {
            "value_3_20s": "Automatiza tu agencia con IA.",
            "cta_20_30s": "Entra a nasaweb.ar"
        },
        "visual_assets": {"on_screen_kinetic_text": "Creciendo en el Alto Valle"}
    }
    generator = CloudVideoGenerator(sample_payload)
    print(generator.request_video_render())
