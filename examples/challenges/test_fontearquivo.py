from FonteArquivo import FonteArquivo
import pytest

fa = None

@pytest.fixture(scope='module')
def fa():
    print('*****SETUP*****')
    fa = FonteArquivo("./estudantes.csv")
    yield fa
    print('******TEARDOWN******')
    fa.fecharArquivo()

def test_open_file_to_read(fa):
    assert fa.possuiDados() == True

def test_read_next_file_line(fa):
    assert fa.proximoDado() == "\ufeffNome;Matematica;Historia;Geografia"

def test_close_file_to_read(fa):
    fa.fecharArquivo()
    with pytest.raises(ValueError, match=r"I/O operation on closed file."):fa.reader.read()
    
    



