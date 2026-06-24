from flask import Flask, request
import requests

INSTANCE_ID = "instance182136"
TOKEN = "vg8kbgyl555umxh8"

app = Flask(__name__)

COMANDOS = {
    "/presentarse": "👤 *¡Preséntate al clan!* 🐾\n\n📝 Copia y completa esto:\n\n👤 *Nombre:*\n🎂 *Edad:*\n📍 *Ciudad:*\n🎯 *Intereses:*",
    "/reglas": "⚙️ *Reglas oficiales del clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈* ⚙️\n\n🚫 *Cero toxicidad:* Está totalmente prohibido el acoso y la discriminación.\n\n📵 *Spam:* No hacer spam o se te llamará la atención. Primera vez recordatorio, segunda recordatorio, tercera advertencia.\n\n🤝 *Respeto:* Respetar al Staff y a todos los integrantes.\n\n🔞 *Prohibido Gore o contenido +18.*\n\n⚔️ *Peleas:* Prohibido pelear en el clan. Si hay conflicto se llevará a los involucrados a un chat privado.\n\n📣 *Prohibido promocionar otras comunidades, clanes o teams.*\n\n👋 Da la bienvenida a los nuevos integrantes.\n\n🎮 *Actividades:* No es obligatorio participar, ¡pero nos daría gusto!\n\n💬 Si te sientes incómodo/a, díselo al staff. ¡Bienvenido/a al clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈! 🐾",
    "/bienvenida": "¡Bienvenido/a al clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈! 🐱✨\n\nNos alegra un montón que estés aquí 🎉 Este es tu nuevo lugar para hacer amigos, reír, compartir y pasarla bien 💫\n\n📋 Usa /reglas para conocer las normas del clan\n👋 Usa /presentarse para que todos te conozcan\n🎯 Usa /ayuda para ver todo lo que puedes hacer aquí\n\nRecuerda: aquí todos somos familia 🐾 ¡Disfrútalo al máximo! 🔥",
    "/eventos": "📅✨ *Eventos del clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈* ✨📅\n\n🔜 Próximamente anunciaremos actividades y eventos emocionantes...\n\n¡Estate pendiente! 🐾🔥",
    "/intereses": "🎮✨ *¿De qué va el clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈?* ✨🎮\n\nSomos una comunidad apasionada por los *videojuegos* 🕹️🔥\n\n¿Tienes un juego favorito? ¡Compártelo con el clan y encuentra con quién jugar! 🐾",
    "/contacto": "🐾✨ *¡El Staff del clan 𝒦𝒾𝓉𝓉𝒾𝑒𝓈 al habla!* ✨🐾\n\n👑 *Josh* — El jefe, el mero mero, el Fundador & Admin 😎🔥\n🛡️ *Ari* — La que pone el orden y el buen rollo, Co-Admin 💅⚡\n\n¿Tienes un problema? ¡No te quedes callado/a! Escríbenos sin miedo 💬🐾\n\n_El clan es de todos y queremos que estés cómodo/a_ 🫶",
    "/ayuda": "━━━━━━━━━━━━━━━━━━\n🐾✨ *COMANDOS DEL CLAN 𝒦𝒾𝓉𝓉𝒾𝑒𝓈* ✨🐾\n━━━━━━━━━━━━━━━━━━\n\n👤 /presentarse — ¡Preséntate y que te conozcan!\n⚙️ /reglas — Las normas del clan 👀\n🎉 /bienvenida — Bienvenida para los nuevos 🐱\n📅 /eventos — Actividades y eventos próximos 🔥\n🎮 /intereses — ¿De qué va el clan?\n👑 /contacto — ¿Necesitas al staff? Aquí están\n📋 /ayuda — Estás aquí, ya sabes 😄\n\n━━━━━━━━━━━━━━━━━━\n_¡Úsalos y disfruta el clan!_ 🫶🐾\n━━━━━━━━━━━━━━━━━━",
}

def enviar_mensaje(chat_id, texto):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    payload = {"token": TOKEN, "to": chat_id, "body": texto}
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return "ok", 200
    msg = data.get("data", {})
    body = msg.get("body", "").strip().lower()
    chat_id = msg.get("from", "")
    from_me = msg.get("fromMe", False)
    if from_me:
        return "ok", 200
    respuesta = COMANDOS.get(body)
    if respuesta:
        enviar_mensaje(chat_id, respuesta)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
