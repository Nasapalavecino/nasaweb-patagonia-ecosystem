import os
import json
from datetime import datetime

class MediaRenderer:
    def __init__(self, reel_payload: dict):
        self.payload = reel_payload
        self.output_dir = "output_media"
        os.makedirs(self.output_dir, exist_ok=True)

    def render_storyboard_spec(self):
        """
              Genera la especificación técnica de renderizado y simula 
              la creación de los recursos visuales para el Reel.
              """
        brand = self.payload.get("target_brand", "nasaweb.ar")
        topic = self.payload.get("topic", "Automatización con IA")
        script = self.payload.get("script_structure", {})
        assets = self.payload.get("visual_assets", {})

        print(f"[MediaRenderer] Procesando storyboard para {brand}...")
        print(f"[MediaRenderer] Tema: {topic}")

        # Estructura del guion técnico por segundos para la edición automática
        storyboard_frames = [{
            "second": "0-3s (Gancho)",
            "visual": assets.get("background_media_prompt"),
            "overlay_text": assets.get("on_screen_kinetic_text"),
            "audio_voiceover": script.get("hook_0_3s")
        }, {
            "second": "3-20s (Valor)",
            "visual": "B-roll dinámico con transiciones rápidas y métricas en pantalla",
            "overlay_text": "Soluciones digitales para el Alto Valle",
            "audio_voiceover": script.get("value_3_20s")
        }, {
            "second": "20-30s (CTA)",
            "visual": "Pantalla final con branding de la agencia y URL interactiva",
            "overlay_text": f"Entra a {brand}",
            "audio_voiceover": script.get("cta_20_30s")
        }]

        # Guardar especificación como artefacto JSON listo para renderizadores de video (FFmpeg / MoviePy)
        filename = f"{self.output_dir}/storyboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_package = {
            "render_status": "ready_for_video_compilation",
            "target_brand": brand,
            "resolution": "1080x1920 (Vertical 9:16)",
            "framerate": 30,
            "storyboard": storyboard_frames,
            "caption": self.payload.get("caption_and_seo")
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(output_package, f, ensure_ascii=False, indent=4)

        print(f"[MediaRenderer] Storyboard compilado con éxito en: {filename}")
        return output_package

if __name__ == "__main__":
    # Prueba unitaria local del renderer
    sample_payload = {
        "target_brand": "nasaweb.ar",
        "topic": "SEO y Automatización",
        "visual_assets": {
            "background_media_prompt": "Toma aérea de Cipolletti",
            "on_screen_kinetic_text": "¿Tu negocio aparece en Google?"
        },
        "script_structure": {
            "hook_0_3s": "Estás perdiendo clientes.",
            "value_3_20s": "Automatiza con IA.",
            "cta_20_30s": "Visita nasaweb.ar"
        },
        "caption_and_seo": {"instagram_caption": "Creciendo en la Patagonia 🚀"}
    }
    renderer = MediaRenderer(sample_payload)
    renderer.render_storyboard_spec()
