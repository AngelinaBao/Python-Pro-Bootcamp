class Question:
    def __init__(self, question, index):
        self.text = question[index]["text"]
        self.answer = question[index]["answer"]