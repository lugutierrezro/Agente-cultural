def get_local_culture_info(destination: str) -> dict:
    """Return typical dishes, customs, and useful phrases for a given destination.

    This is intentionally simple for an introductory laboratory.
    """
    destination_normalized = destination.lower().strip()

    dishes = []
    customs = []
    phrases = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        dishes.extend(["Cuy al horno", "Chiri Uchu", "Sopa de Quinua", "Pachamanca"])
        customs.extend([
            "Masticar hojas de coca o tomar mate de coca para el mal de altura.",
            "Respetar las ofrendas a la Pachamama (Madre Tierra)."
        ])
        phrases.extend([
            "Allin p'unchay (Buenos días en quechua).",
            "Sulpayki (Gracias en quechua).",
            "¿Imayna kashanki? (¿Cómo estás?)"
        ])
    elif "lima" in destination_normalized:
        dishes.extend(["Ceviche", "Lomo Saltado", "Ají de Gallina", "Causa Limeña"])
        customs.extend([
            "El tráfico puede ser pesado, salir con anticipación.",
            "La comida marina se consume tradicionalmente de día."
        ])
        phrases.extend([
            "¡Qué paja! (¡Qué genial!).",
            "Habla causa (Hola amigo)."
        ])
    else:
        # Default fallback
        dishes.extend(["Platos típicos locales del mercado principal."])
        customs.extend(["Saludar amablemente", "Dejar propina del 10% si el servicio fue bueno."])
        phrases.extend(["Hola", "Gracias", "Por favor", "¿Cuánto cuesta?"])

    return {
        "status": "success",
        "destination": destination,
        "dishes": dishes,
        "customs": customs,
        "phrases": phrases,
    }
