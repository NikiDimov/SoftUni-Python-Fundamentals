class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []
while not command == "Stop":
    information = command.split()
    email = Email(information[0], information[1], information[2])
    emails.append(email)
    command = input()

sent_emails = [int(index)for index in input().split(", ")]
for i in range(len(emails)):
    if i in sent_emails:
        emails[i].send()
        print(emails[i].get_info())
    else:
        print(emails[i].get_info())

