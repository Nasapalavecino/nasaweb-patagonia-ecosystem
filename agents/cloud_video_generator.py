import os
from datetime import datetime
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

class CloudVideoGenerator:
    def __init__(self, reel_payload: dict):
        self.payload = reel_payload
        self.output_dir = "output_media"
        os.makedirs(self.output_dir, exist_ok=True)

    def request_video_render(self):
        print("[CloudVideoGenerator] Renderizando video real en formato vertical (9:16) con Python...")
        
        script = self.payload.get("script_structure", {})
        hook_text = script.get("hook_0_3s", "¿Tu negocio aparece en Google?")
        brand = self.payload.get("target_brand", "nasaweb.ar")

        output_filename = f"{self.output_dir}/reel_seo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"

        try:
            # Crear un clip de fondo oscuro corporativo (Vertical 9:16 -> 1080x1920 o compacto 540x960 para render rápido)
            bg = ColorClip(size=(540, 960), color=(9, 13, 22), duration=10)

            # Texto del Gancho
            txt_hook = TextClip(
                hook_text, 
                fontsize=32, 
                color='white', 
                size=(480, None), 
                method='caption',
                font='Arial-Bold'
            ).set_duration(10).set_position(('center', 'center'))

            # Componer el video
            video = CompositeVideoClip([bg, txt_hook])
            
            # Escribir el archivo MP4 usando ffmpeg integrado
            video.write_videofile(
                output_filename, 
                fps=24, 
                codec='libx264', 
                audio=False,
                logger=None
            )

            print(f"[CloudVideoGenerator] Video compilado con éxito en: {output_filename}")
            
            # Como se ejecuta en GitHub Actions, simulamos un enlace de artefacto o descarga local
            return {
                "status": "rendered_locally",
                "video_file": output_filename,
                "video_url": f"https://github.com/Nasapalecino/nasaweb-patagonia-ecosystem/raw/main/{output_filename}",
                "render_timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            print(f"[CloudVideoGenerator] Error al compilar con MoviePy: {e}")
            # Fallback seguro si falta ImageMagick en el runner de GitHub
            return {
                "status": "rendered_fallback",
                "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
                "error_note": str(e)
            }

if __name__ == "__main__":
    sample_payload = {
        "target_brand": "nasaweb.ar",
        "script_structure": {
            "hook_0_3s": "¿Por qué tu competencia aparece primera en Google y vos no?"
        }
    }
    gen = CloudVideoGenerator(sample_payload)
    gen.request_video_render()
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
