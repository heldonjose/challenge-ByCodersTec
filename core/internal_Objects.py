class ImportLine():
    def __init__(self, line):
        self.type = line[0:1]
        self.date = line[1:9]
        self.value = line[9:19]
        self.document_owner = line[19:30]
        self.number_card = line[31:42]
        self.hour = line[42:48]
        self.name_owner = line[48:62]
        self.name_store = line[62:81]

    def __str__(self):
        return '{}-{}-{}'.format(self.document_recipient, self.name_ower, self.date)
