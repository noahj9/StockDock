import random
from fillpdf import fillpdfs
from pathlib import Path
import shutil
import PyPDF2

docket = {'Clear': '1', 'Date In': '1', 'Date Required': '1', 'Customer Name': '1', 'Contact Name': '1', 'Phone': '1', 'Email': '1', 'quote number': '1',
          'Deposit Amount': '1', 'qty1': '1', 'description1': '1', 'finished size1': '1', 'stock1': '1', 'runqty1': '1', 'sheetsize1': '1', 'runsize1': '1', 'inks1': '1',
          'special instructions1': '1', 'bindery1': '1', 'price1': '1', 'file1': '1', 'shipping1': '1', 'qty2': '1', 'description2': '1', 'finished size2': '1', 'stock2': '1',
          'runqty2': '1', 'sheetsize2': '1', 'runsize2': '1', 'inks2': '1', 'special instructions2': '1', 'bindery2': '1', 'price2': '1', 'file2': '1', 'shipping2': '1', 'qty3': '1',
          'description3': '1', 'finished size3': '1', 'stock3': '1', 'runqty3': '1', 'sheetsize3': '1', 'runsize3': '1', 'inks3': '1', 'special instructions3': '1', 'bindery3': '1',
          'price3': '1', 'file3': '1', 'shipping3': '1', 'Reception Notes': '1', 'Customer PO': '1', 'Firmorflex': '1', 'Machine1': '1', 'Proof1': '1', 'Terms': '1', 'Deposits': '1',
          'Salesrep': '1', 'CSR': '1', 'Machine2': '1', 'Proof2': '1', 'Machine3': '1', 'Proof3': '1'}

def execute():
    path = Path(__file__).parent.resolve()

    key = keygen()

    copy(path,key)

    data_dict = generateDataDict(path)

    fill(data_dict,path,key)
    return str(path)+"\\docket_filled"+key+".pdf"


def copy(path,key):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')
    shutil.copyfile(str(path)+"\\docket_template.pdf",str(path)+"\\docket_filled"+key+".pdf")

    fileReader = PyPDF2.PdfFileReader(fileRead)
    fileReader.numPages
    fileWriter=PyPDF2.PdfWriter()

    for pageNum in range(fileReader.numPages):
        fileReader.getPage(pageNum)
    with open(str(path)+"\\docket_filled"+key+".pdf",'wb') as f:
        fileWriter.write(f)
    fileRead.close()

def generateDataDict(path):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')
    data_dict = fillpdfs.get_form_fields(fileRead)
    print (data_dict)
    for i in data_dict:
        data_dict[i] = docket[i]
    fileRead.close()
    return data_dict


def fill(data_dict,path,key):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')
    fileWrite = open(str(path)+"\\docket_filled"+key+".pdf",'wb')
    fillpdfs.write_fillable_pdf(fileRead,fileWrite,data_dict,flatten=False)
    fileWrite.close()
    fileRead.close()

def keygen():
    p1 = str(random.randint(1,1000))
    p2 = str(random.randint(1,1000))
    key = p1+p2
    return key

execute()
