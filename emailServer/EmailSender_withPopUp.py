from socket import *
from Tkinter import *

def quitTkinter():
   quit()
   master.quit

def sendMessage():
    # Get the entered data
    sender = '<'+(e1.get())+'>\r\n'
    recipient = '<'+(e2.get())+'>\r\n'
    subject =(e3.get())+'\r\n'
    msg = '\r\n'+(e4.get())
    endmsg = '\r\n.\r\n'
    # Close the window
    master.destroy()

    # Choose a mail server (e.g. Google mail server) and call it mailserver.
    mailserver = 'ALT2.ASPMX.L.GOOGLE.COM'
    port = 25

    # Create socket called clientSocket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # and establish a connection with the mailserver
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024)
    print recv       # Must have line break here, else syntax is wrong (spacing)
    if recv[:3] != '220':
        print '220 reply not received from server.'

    # Send HELO command.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand)

    # Get back and print the response
    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '250':
        print '250 reply not received from server.'

    # Send MAIL FROM command and print server response.
    mailFrom = sender #'<kbehraki@wellesley.edu>\r\n'
    clientSocket.send("MAIL FROM: "+mailFrom)
         # Copied directly from above to print
    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '250':
        print '250 reply not received from server.'

    # Send RCPT TO command and print server response.
    mailTo =  recipient   # '<kbehraki@wellesley.edu>\r\n'
    clientSocket.send("RCPT TO: "+mailTo)
         # Copied directly from above to print
    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '250':
        print '250 reply not received from server.'


    # Send DATA command and print server response.
    dataCommand = "DATA\r\n"
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '354':
        print '354 reply not received from server.'

    # Send message data.
    messageData = msg
        # Message ends with a single period.
    markEnding = endmsg

    FROM = sender
    TO = recipient

    clientSocket.send("FROM: "+FROM+"TO: "+TO+"SUBJECT: "+subject+messageData+markEnding)

    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '250':
        print '250 reply not received from server'


    # Send QUIT command and get server response.
    quitCommand = "QUIT\r\n"
    print quitCommand
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    print recv1
    if recv1[:3] != '221':
        print '221 reply not received from server'

    print '\r\nMessage  has been sent!\r\n'
    quit()


master = Tk()
Label(master, text="FROM: ").grid(row=0)
Label(master, text="TO: ").grid(row=1)
Label(master, text="SUBJECT: ").grid(row=2)
Label(master, text="MESSAGE: ").grid(row=4)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(rows=4, column=1, rowspan=4, columnspan=5)

Button(master, text='Send', command=sendMessage).grid(row=10, column=0, sticky=W, pady=10)
Button(master, text='Quit', command=quitTkinter).grid(row=10, column=1, sticky=W, pady=10)

mainloop( )
