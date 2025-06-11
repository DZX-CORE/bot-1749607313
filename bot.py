import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomBot:
    def __init__(self, token):
        self.token = token
        self.application = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("info", self.info_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Olá! Sou um bot criado pelo DZX-CORE.\n\n"
            "Comandos disponíveis:\n"
            "/start - Iniciar bot\n"
            "/help - Mostrar ajuda\n"
            "/info - Informações do bot\n\n"
            "Envie qualquer mensagem e eu responderei!"
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = """
🤖 **Ajuda do Bot**

**Comandos:**
• /start - Inicializar o bot
• /help - Mostrar esta ajuda
• /info - Informações sobre o bot

**Como usar:**
Envie qualquer mensagem de texto e eu responderei de forma inteligente.

**Funcionalidades:**
• Resposta automática a mensagens
• Comandos personalizados
• Interface amigável

Criado automaticamente pelo DZX-CORE!
        """
        await update.message.reply_text(help_text)
    
    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        info_text = f"""
📊 **Informações do Bot**

**Nome:** Bot DZX-CORE
**Versão:** 1.0.0
**Criado por:** Orquestrador DZX-CORE
**Usuário:** {update.effective_user.first_name}
**Chat ID:** {update.effective_chat.id}

**Status:** ✅ Online e funcionando
**Última atualização:** Agora

Este bot foi gerado automaticamente!
        """
        await update.message.reply_text(info_text)
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text
        
        # Respostas inteligentes baseadas na mensagem
        responses = {
            'oi': 'Olá! Como posso ajudar você?',
            'olá': 'Oi! Tudo bem? Em que posso ser útil?',
            'como está': 'Estou funcionando perfeitamente! E você?',
            'obrigado': 'De nada! Sempre à disposição!',
            'tchau': 'Até logo! Volte sempre!'
        }
        
        response = responses.get(user_message.lower(), 
                               f"Você disse: '{user_message}'. Sou um bot inteligente criado pelo DZX-CORE!")
        
        await update.message.reply_text(response)
    
    def run(self):
        print("Bot iniciando...")
        self.application.run_polling()

if __name__ == '__main__':
    import os
    
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print("Erro: BOT_TOKEN não configurado!")
        print("Configure: export BOT_TOKEN=seu_token_aqui")
        exit(1)
    
    bot = CustomBot(TOKEN)
    bot.run()
