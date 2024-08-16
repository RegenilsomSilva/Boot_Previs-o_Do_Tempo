
import speech_recognition as sr
import os


print('Inicializa o reconhecedor')
def audio_para_texto(caminho_audio):
    # Inicializa o reconhecedor
    recognizer = sr.Recognizer()

    # Abre o arquivo de áudio
    print('Função que abre o arquivo de áudio....')
    with sr.AudioFile(caminho_audio) as source:
        audio = recognizer.record(source)  # Lê o áudio do arquivo

    try:
        # Usa o Google Web Speech API para reconhecer o áudio
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Texto reconhecido: ", texto)
        print(os.linesep)
        return texto
    except sr.UnknownValueError:
        print("O Google Web Speech API não conseguiu entender o áudio.")
    except sr.RequestError as e:
        print(f"Não foi possível requisitar resultados do serviço do Google; {e}")

# Exemplo de uso
caminho_do_audio = "teste023.waptt"
audio_para_texto(caminho_do_audio)
