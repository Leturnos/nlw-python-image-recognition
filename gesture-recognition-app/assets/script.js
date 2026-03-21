document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  const canvasCtx = canvas.getContext('2d');
  
  const qualitySlider = document.getElementById('quality-slider');
  const qualityValue = document.getElementById('quality-value');
  const drawLandmarksCb = document.getElementById('draw-landmarks-cb');
  const fpsCounter = document.getElementById('fps-counter');
  const gestureContainer = document.getElementById('gesture-container');
  const gestureImage = document.getElementById('gesture-image');

  let ws;
  let sending = false;
  let lastSent = 0;
  const targetFps = 30;
  const minIntervalMs = 1000 / targetFps;

  function connectWS() {
    const proto = (location.protocol === 'https:') ? 'wss' : 'ws';
    ws = new WebSocket(`${proto}://${location.host}/ws`);

    ws.onmessage = (ev) => {
      try {
        const msg = JSON.parse(ev.data);

        if (msg.image) {
          const img = new Image();
          img.onload = () => {
            canvasCtx.clearRect(0, 0, canvas.width, canvas.height);
            canvasCtx.drawImage(img, 0, 0, canvas.width, canvas.height);
          };
          img.src = 'data:image/jpeg;base64,' + msg.image;
        }

        if (msg.fps) {
          fpsCounter.textContent = `FPS: ${msg.fps}`;
        }
        
        if (msg.gesture_image) {
            gestureImage.src = msg.gesture_image;
        } else {
            gestureImage.src = '';
        }

        if (msg.labels && msg.labels.length > 0) {
            gestureContainer.innerHTML = msg.labels.map(l => 
                `<p>${l.hand}: ${l.gesture} (${l.prob}%)</p>`
            ).join('');
        } else {
            gestureContainer.innerHTML = '';
        }

      } catch (e) {
        console.error('Error processing message', e);
      }
    };

    ws.onclose = () => {
      console.log('WebSocket closed, reconnecting...');
      setTimeout(connectWS, 1000);
    };

    ws.onerror = (err) => {
      console.error('WebSocket error:', err);
      ws.close();
    };
  }

  async function startCam() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 }, audio: false });
      video.srcObject = stream;
      await video.play();

      // Set canvas size to match video
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
    } catch(e) {
      console.error('Error starting camera', e);
      alert('Could not start camera. Please grant permission and ensure it is not in use.');
    }
  }

  function loop(now) {
    requestAnimationFrame(loop);
    if (!ws || ws.readyState !== 1) return;
    if (!video.videoWidth || !video.videoHeight) return;
    if (sending) return;
    if (now - lastSent < minIntervalMs) return;

    sending = true;
    lastSent = now;

    // Draw video to an offscreen canvas to get the data
    const offscreenCanvas = document.createElement('canvas');
    offscreenCanvas.width = video.videoWidth;
    offscreenCanvas.height = video.videoHeight;
    const offscreenCtx = offscreenCanvas.getContext('2d');
    offscreenCtx.drawImage(video, 0, 0, offscreenCanvas.width, offscreenCanvas.height);
    
    const quality = parseFloat(qualitySlider.value);
    const dataUrl = offscreenCanvas.toDataURL('image/jpeg', quality);
    const image = dataUrl.split(',')[1];
    const draw_landmarks = drawLandmarksCb.checked;

    try {
      ws.send(JSON.stringify({ image, draw_landmarks }));
    } finally {
      sending = false;
    }
  }

  // --- Event Listeners ---
  qualitySlider.addEventListener('input', () => {
    qualityValue.textContent = `${Math.round(qualitySlider.value * 100)}%`;
  });

  // --- Main ---
  (async () => {
    connectWS();
    await startCam();
    requestAnimationFrame(loop);
  })();

});
