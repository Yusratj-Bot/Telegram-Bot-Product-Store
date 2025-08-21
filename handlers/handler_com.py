from handlers.handler import Handler


class CommandHandler(Handler):
    # class that handles commands like /start, /help ...
    def __init__(self, bot):
        super().__init__(bot)

    def _on_start_button_click(self, msg) -> None:
        self.bot.send_message(msg.chat.id,
                              'Hello! Waiting for other commands',
                              reply_markup=self.keyboards.start_menu()
                              )

    def _show_catalog(self, msg) -> None:
        products = self.DB.select_all_products()
        if not products:
            self.bot.send_message(msg.chat.id, "Каталог пуст.")
            return

        response = "Каталог товаров:\n\n"
        for product in products:
            response += f"- {product.name} ({product.price} руб.)\n"

        self.bot.send_message(msg.chat.id, response)

    def handle(self) -> None:
        #  '/start' input event handler
        @self.bot.message_handler(commands=['start'])
        def handle(msg) -> None:
            if msg.text == '/start':
                self._on_start_button_click(msg)

        @self.bot.message_handler(commands=['catalog'])
        def handle_catalog(msg) -> None:
            self._show_catalog(msg)
