from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_cusco():
    """Test that Cusco returns the correct cultural details."""
    result = get_local_culture_info("Cusco")
    
    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert "Cuy al horno" in result["dishes"]
    assert len(result["phrases"]) > 0
    assert any("quechua" in phrase.lower() for phrase in result["phrases"])

def test_get_local_culture_info_default():
    """Test a default destination behavior."""
    result = get_local_culture_info("Tokio")
    
    assert result["status"] == "success"
    assert "Tokio" in result["destination"]
    assert "Hola" in result["phrases"]
