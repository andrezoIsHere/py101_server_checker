class Checker:

    _address_list = []

    def __init__(self, await_time = 60):

        # Will create a directory log if it doesn't exist
        try:
            os.mkdir('log')
        except: 
            pass

        logging.basicConfig(filename=f'log/check-{uuid4()}.log',
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s')

        self.await_time = await_time

    def setList(self, new_list: list):
        if new_list:
            logging.warn("All changes are under your control. Remember that all addresses should be valid")
            self._address_list = new_list
        else:
            logging.error("The new list is clear. Nothing changed")

    def getList(self):
        return self._address_list

    # Will add address to handler
    def addAddress(self, *args):
        if len(args) == 1 and type(args[0]) == list:
            for href in args[0]:
                if href:
                    self._address_list.append(href)
                else: 
                    logging.error("You didn't enter the address for check")
        else:
            for href in args:
                if href:
                    self._address_list.append(href)
                else: 
                    logging.error("You didn't enter the address for check")
    
    # Will remove address to handler
    def removeAddress(self, href=''):
        if href:
            try:
                self._address_list.remove(href)
            except:
                logging.error("You didn't enter the address to remove")
        else:
            logging.error("You didn't enter the address to remove")

    # All another procceses will be stopped. You should use this script as subprocess
    def startHandle(self, stop_at=60, send_messages=True):

        current_point = 0
        while stop_at > current_point:
            
            for href in self._address_list:

                try:
                    response = get(href)

                    if not response.ok:
                        raise Exception()

                except Exception as exc:
                    
                    logging.error(f"The site \"{href}\" isn't working")
                    send_message.new_message(f"The site \"{href}\" isn't working")
                    break

            current_point += self.await_time
            sleep(self.await_time)

        send_message.new_message(f"The process has been finished because the time is up")

# If you use it in your project, don't forget to connect the libraries below. Example:
if __name__ == '__main__':

    # Importing all libraries
    import logging, os

    from requests import get
    from uuid import uuid4
    from time import sleep

    import send_message

    c = Checker() # Will initialize the handler

    c.addAddress('https://yandex.kz/', 'https://yandex.ru/') # Both variants will add addresses to handler
    c.addAddress(['https://google.kz', 'https://google.ru']) # It works too ;)

    c.addAddress('https://testestestestest.kz') # It doesn't exist

    c.getList() # Will return the full list of addresses

    c.startHandle() # Will start handling all addresses
    
