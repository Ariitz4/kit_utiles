from src.files import save_lines, load_lines

def test_save_and_load_list(tmp_path):
    archivo = tmp_path / "lista.txt"
    lista_original = ["uno", "dos", "tres"]
    
    save_lines(archivo, lista_original)
    resultado = load_lines(archivo)
    
    assert resultado == lista_original

def test_empty_file(tmp_path):
    archivo = tmp_path / "vacio.txt"
    archivo.touch()  # crea el archivo vacío
    
    resultado = load_lines(archivo)
    
    assert resultado == []