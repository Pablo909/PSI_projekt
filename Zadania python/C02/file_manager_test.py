import file_manager


plik = file_manager.FileManager("tekst")
print(plik.read_file())
plik.update_file(" - update test")
print(plik.read_file())
