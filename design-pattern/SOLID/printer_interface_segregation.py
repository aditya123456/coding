from abc import  ABC, abstractmethod

class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):

    def print(self, document):
        print(f"Printing {document} in black and white")

    def fax(self, document):
        raise NotImplemented("Fax is not supported")

    def scan(self, document):
        raise NotImplemented("Scan is not supported")

class ModernPrinter(Printer):

    def print(self, document):
        print(f"Printing {document} in color..")

    def fax(self, document):
        print("Faxing document")

    def scan(self, document):
        print("Scaning document")


class PrinterIS(ABC):

    @abstractmethod
    def print(self, document):
        pass

class FaxIS(ABC):

    @abstractmethod
    def fax(self, document):
        pass


class ScannerIS(ABC):

    @abstractmethod
    def scan(self, document):
        pass

class NewPrinter(PrinterIS, FaxIS, ScannerIS):

    def print(self, document):
        print(f"Printing {document} in color..")

    def fax(self, document):
        print("Faxing document")

    def scan(self, document):
        print("Scanning document")

