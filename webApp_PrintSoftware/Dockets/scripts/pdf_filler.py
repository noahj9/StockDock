import random
from fillpdf import fillpdfs
from pathlib import Path
import shutil
import PyPDF2
 
docket = {'Clear': '', 'Date In': '11/11/2011', 'Date Required': '11/12/2011', 'Firm': 'yee', 'Flexible': 'T',
          'Customer Name': '1', 'Contact Name': '1', 'Phone': '1', 'Email': '1', 'quote number': '1',
          'Terms': 'COD', 'Deposits': '50%', 'Deposit Amount': '212', 'Salesrep': 'Moe', 'CSR': 'Moe',
          '0': '1212', '1': '12313', '2': '123123', 'Reception Notes': '123123', 'Customer PO': '123123'}
 
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
    print(data_dict)
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
