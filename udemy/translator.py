from translate import Translator
translator = Translator(to_lang='ja')
try: 
    with open('./translator.txt', mode='r') as my_file: #make sure to have correct file path
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt',mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('get your file path')