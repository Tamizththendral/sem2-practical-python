
class Password:
    def __init__(self, password):
        self.password = password
        self.pw = []  
    def check(self):
        self.pw.clear()
        if len(self.password) < 8:
            self.pw.append("Password must contain at least 8 characters.")
        if self.password[0].islower():
            print('first letter of the password must be uppercase letter')
        if not any(char.isdigit() for char in self.password):
            self.pw.append("Password must contain at least one digit.")
        if not any(char.isupper() for char in self.password):
            self.pw.append("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in self.password):
            self.pw.append("Password must contain at least one lowercase letter.")
        special_characters = "!@#$%^&*(),.?\":{}|<>"
        if not any(char in special_characters for char in self.password):
            self.pw.append("Password must contain at least one special character.")
        if len(self.pw) == 0:
            self.pw.append("Your password is valid.")
    def displaycheck(self):
        for i in self.pw:
            print(i)
password = input("Enter the password: ")
password_validator = Password(password)
password_validator.check() 
password_validator.displaycheck() 

class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.sentences = []
    def split_into_sentences(self):
        sentence_endings = ['.', '?', '!']
        sentence = ''
        for char in self.text:
            sentence += char
            if char in sentence_endings:
                self.sentences.append(sentence.strip())
                sentence = ''
    def process_sentences(self):
        for sentence in self.sentences:
            sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace())
            words = sentence.split()
            word_count = len(words)
            print(f'Sentence: "{sentence}", Word Count: {word_count}')
    def display_sentences(self):
        for sentence in self.sentences:
            print(sentence)
input_text = input("Enter a paragraph of text: ")
text_processor = TextProcessor(input_text)
text_processor.split_into_sentences()
text_processor.display_sentences()
text_processor.process_sentences()
