<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova-AI Powerhouse | Command Engine</title>
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #151c2e;
            --accent-color: #00d2ff;
            --green-glow: #00ff87;
            --text-color: #e2e8f0;
            --subtext-color: #94a3b8;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            max-width: 800px;
            width: 100%;
        }

        .header-card {
            background: var(--card-bg);
            border: 1px solid #2a354d;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
            margin-bottom: 20px;
        }

        h1 { color: var(--accent-color); margin: 0 0 6px 0; font-size: 1.6rem; }
        p.subtitle { color: var(--subtext-color); margin: 0 0 12px 0; font-size: 0.85rem; }

        .status-badge {
            display: inline-block;
            background: rgba(0, 255, 135, 0.15);
            color: var(--green-glow);
            border: 1px solid var(--green-glow);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid #2a354d;
            border-radius: 10px;
            padding: 12px;
            text-align: center;
        }

        .card h3 { margin: 0 0 5px 0; font-size: 0.75rem; color: var(--subtext-color); }
        .card .value { font-size: 1.2rem; font-weight: bold; color: var(--accent-color); }

        .chat-card {
            background: var(--card-bg);
            border: 1px solid #2a354d;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .chat-box {
            height: 280px;
            background: #0b0f19;
            border: 1px solid #2a354d;
            border-radius: 8px;
            padding: 12px;
            overflow-y: auto;
            margin-bottom: 12px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .msg {
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 0.9rem;
            line-height: 1.4;
            max-width: 85%;
        }

        .msg.ai {
            background: rgba(0, 210, 255, 0.1);
            border: 1px solid var(--accent-color);
            align-self: flex-start;
            color: #e2e8f0;
        }

        .msg.user {
            background: #0072ff;
            align-self: flex-end;
            color: white;
        }

        .quick-queries {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            margin-bottom: 12px;
            padding-bottom: 4px;
        }

        .chip {
            background: #1e293b;
            border: 1px solid #334155;
            color: var(--subtext-color);
            padding: 6px 10px;
            border-radius: 15px;
            font-size: 0.75rem;
            white-space: nowrap;
            cursor: pointer;
        }

        .chip:hover { border-color: var(--accent-color); color: white; }

        .input-row { display: flex; gap: 8px; }

        input {
            flex: 1;
            padding: 10px;
            background: #0b0f19;
            border: 1px solid #2a354d;
            color: white;
            border-radius: 6px;
            font-size: 0.9rem;
        }

        button {
            padding: 10px 18px;
            background: linear-gradient(90deg, #00d2ff, #0072ff);
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
        }

        .voice-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .voice-btn {
            background: rgba(0, 255, 135, 0.2);
            border: 1px solid var(--green-glow);
            color: var(--green-glow);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header-card">
            <h1>Nova-AI Powerhouse</h1>
            <p class="subtitle">Super Intelligence Core Municipal Allocation Engine</p>
            <span class="status-badge">AI Predictive Core Active</span>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Housing Available</h3>
                <div class="value">1,248</div>
            </div>
            <div class="card">
                <h3>Taxpayer Savings</h3>
                <div class="value">$350M+</div>
            </div>
            <div class="card">
                <h3>Efficiency Rate</h3>
                <div class="value">99.4%</div>
            </div>
        </div>

        <div class="chat-card">
            <div class="voice-bar">
                <h3 style="margin: 0; color: var(--subtext-color); font-size: 0.9rem;">Intelligence Command Console</h3>
                <button class="voice-btn" onclick="testAudio()">🔊 Voice Audio: ACTIVE</button>
            </div>
            
            <div class="chat-box" id="chatBox">
                <div class="msg ai">
                    <strong>Nova-AI Core:</strong> Strategic engine online. Ask any question regarding Rocky Mount, hospital bed impacts, or taxpayer savings.
                </div>
            </div>

            <div class="quick-queries">
                <div class="chip" onclick="quickAsk('How many hospital beds are saved in Rocky Mount?')">Hospital Beds</div>
                <div class="chip" onclick="quickAsk('If we house ten thousand homeless people, how much money will be saved?')">10,000 People Savings</div>
                <div class="chip" onclick="quickAsk('How many vacant homes do we have in Rocky Mount North Carolina?')">Rocky Mount Homes</div>
            </div>

            <div class="input-row">
                <input type="text" id="userInput" placeholder="Ask any question in plain English..." onkeydown="if(event.key==='Enter') sendQuery()">
                <button onclick="sendQuery()">Execute</button>
            </div>
        </div>
    </div>

    <script>
        let synth = window.speechSynthesis;

        function testAudio() {
            speakDirective("Voice synthesizer operational. Nova AI core online.");
        }

        async function sendQuery() {
            const input = document.getElementById('userInput');
            const query = input.value.trim();
            if (!query) return;

            addMessage(query, 'user');
            input.value = '';

            const loadingId = 'loading-' + Date.now();
            addLoadingMessage("Processing query...", loadingId);

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });
                const data = await res.json();
                
                removeMessage(loadingId);
                addMessage(data.response, 'ai');
                speakDirective(data.response);
            } catch (err) {
                removeMessage(loadingId);
                let fallback = "Tactical Data: Transitioning unsheltered individuals saves $35,000 per person annually in municipal and hospital costs.";
                addMessage(fallback, 'ai');
                speakDirective(fallback);
            }
        }

        function quickAsk(text) {
            document.getElementById('userInput').value = text;
            sendQuery();
        }

        function addMessage(text, sender) {
            const chatBox = document.getElementById('chatBox');
            const msgDiv = document.createElement('div');
            msgDiv.className = `msg ${sender}`;
            msgDiv.innerHTML = sender === 'ai' ? `<strong>Nova-AI Core:</strong> ${text}` : text;
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function addLoadingMessage(text, id) {
            const chatBox = document.getElementById('chatBox');
            const msgDiv = document.createElement('div');
            msgDiv.className = 'msg ai';
            msgDiv.id = id;
            msgDiv.innerHTML = `<strong>Nova-AI Core:</strong> <em>${text}</em>`;
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function removeMessage(id) {
            const el = document.getElementById(id);
            if (el) el.remove();
        }

        function speakDirective(text) {
            if ('speechSynthesis' in window) {
                synth.cancel();
                let cleanText = text.replace(/<[^>]*>?/gm, '');
                let utterance = new SpeechSynthesisUtterance(cleanText);
                utterance.pitch = 0.8;
                utterance.rate = 0.95;

                let voices = synth.getVoices();
                let selectedVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Male') || v.name.includes('David') || v.name.includes('Google US')));
                if (selectedVoice) utterance.voice = selectedVoice;

                synth.speak(utterance);
            }
        }
    </script>

</body>
</html>
