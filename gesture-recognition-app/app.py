import json
import time
from fasthtml.common import *
from core.processor import GestureProcessor
from core.utils import decode_image, encode_image

app, rt = fast_app(hdrs=(
    Link(rel='stylesheet', href='/assets/style.css'),
    Script(src='/assets/script.js'),
))
processor = GestureProcessor()

# To track FPS per connection, we'd normally use a session or context, 
# but for simplicity in this single-user-focused app, let's use a class to track it.
class FPSTracker:
    def __init__(self, alpha=0.9):
        self.prev_time = time.time()
        self.fps = 0
        self.alpha = alpha

    def update(self):
        curr = time.time()
        instant_fps = 1 / (curr - self.prev_time) if curr > self.prev_time else 0
        self.prev_time = curr

        self.fps = self.alpha * self.fps + (1 - self.alpha) * instant_fps
        return int(self.fps)

fps_tracker = FPSTracker()

@rt("/")
def get():
    return Title("Gesture Recognition — AI Hand Gesture Recognition"), Main(
        Header(
            H1("Gesture Recognition App"),
            P("Intelligent Hand Gesture Recognition System", cls="subtitle")
        ),
        Div(
            Div(
                Video(id="video", autoplay=True, playsinline=True, style="display:none"),
                Canvas(id="canvas"),
                Div("FPS: 0", id="fps-counter", cls="fps-badge"),
                cls="vision-card"
            ),
            Div(
                Div(
                    H3("Image Quality Control"),
                    Div(
                        Input(type="range", id="quality-slider", min="0.1", max="1.0", step="0.05", value="0.5"),
                        Span("50%", id="quality-value"),
                        cls="quality-control"
                    ),
                    H3("Settings"),
                    Div(
                        Label(Input(type="checkbox", id="draw-landmarks-cb", checked=True), " Draw Hand Landmarks"),
                        cls="settings-control"
                    ),
                    H3("Live Feed Data"),
                    Div(id="gesture-container"),
                    cls="info-card"
                ),
                Div(
                    H3("Detected Gesture"),
                    Div(Img(id="gesture-image"), cls="gesture-preview-box"),
                    cls="info-card"
                ),
                cls="sidebar-info"
            ),
            cls="main-content"
        ),
        cls="app-container"
    )

@app.ws("/ws")
async def ws(image: str, draw_landmarks: bool, send):
    img = decode_image(image)
    if img is not None:
        processed_img, labels, gesture_image = processor.process_frame(img, draw_landmarks)
        fps = fps_tracker.update()
        await send(json.dumps({
            "image": encode_image(processed_img),
            "labels": labels,
            "gesture_image": gesture_image,
            "fps": fps
        }))

serve()
