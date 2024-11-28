def get_response(text):
    text = text.lower()
    if 'tipos de mouse' in text or 'qué tipos de mouse' in text or 'qué mouses tienes':
        return 'Hay varios tipos de mouses, como óptico, láser, trackball, y más. ¿Cuál te interesa?'
    elif 'características de mouse' in text or 'qué características tiene un mouse' in text or 'cuáles son las características de un mouse':
        return 'Los mouses pueden tener distintas características como DPI ajustable, botones programables, etc. ¿Qué característica te interesa?'
    elif 'precio de mouse' in text or 'cuánto cuesta un mouse' in text or 'cuáles son los precios de los mouses':
        return 'Los precios varían según el modelo y las características. ¿Qué tipo de mouse te interesa?'
    elif 'óptico' in text:
        return 'Un mouse óptico utiliza un LED para detectar el movimiento. Son precisos y comunes.'
    elif 'láser' in text:
        return 'Un mouse láser utiliza un láser para detectar el movimiento. Son más precisos que los ópticos y funcionan en más superficies.'
    elif 'trackball' in text:
        return 'Un mouse trackball tiene una bola que el usuario manipula para mover el cursor. Es ideal para espacios reducidos.'
    elif 'dpi' in text or 'sensibilidad' in text:
        return 'DPI (puntos por pulgada) mide la sensibilidad del mouse. Un DPI más alto significa mayor sensibilidad.'
    elif 'botones programables' in text or 'botones configurables' in text:
        return 'Los mouses con botones programables permiten asignar funciones específicas a cada botón. Son ideales para juegos y productividad.'
    else:
        return 'Lo siento, no entendí tu mensaje. ¿Puedes ser más específico? Puedes preguntar sobre tipos de mouses, características, precios, y más.'

