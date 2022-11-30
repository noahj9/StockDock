import random
from fillpdf import fillpdfs
from pathlib import Path
import shutil 
import PyPDF2
from datetime import datetime

def execute(docket,contact):
    res =['',docket.get("date").strftime("%Y-%m-%d"),docket.get("date_required").strftime("%Y-%m-%d"),docket.get("customer_name"),contact.get("name"),contact.get("phone"),contact.get("email"),
          docket.get("quote"),docket.get("deposit_amount"),docket.get("quantity_1"),docket.get("description_1"),docket.get("finished_size_1"),docket.get("stock_1"),
          docket.get("run_quantity_1"),docket.get("sheet_size_1"),docket.get("run_size_1"),docket.get("inks_1"),docket.get("instructions_1"),docket.get("bindery_1"),
          docket.get("price_comission_1"),docket.get("file_1"),docket.get("shipping_1"),docket.get("quantity_2"),docket.get("description_2"),docket.get("finished_size_2"),
          docket.get("stock_2"),docket.get("run_quantity_2"),docket.get("sheet_size_2"),docket.get("run_size_2"),docket.get("inks_2"),docket.get("instructions_2"),
          docket.get("bindery_2"),docket.get("price_comission_2"),docket.get("file_2"),docket.get("shipping_2"),docket.get("quantity_3"),docket.get("description_3"),
          docket.get("finished_size_3"),docket.get("stock_3"),docket.get("run_quantity_3"),docket.get("sheet_size_3"),docket.get("run_size_3"),docket.get("inks_3"),
          docket.get("instructions_3"),docket.get("bindery_3"),docket.get("price_comission_3"),docket.get("file_3"),docket.get("shipping_3"),docket.get("reception_notes"),
          docket.get("customer_PO"),docket.get("flexibility"),docket.get("machine_1"),docket.get("proof_1"),docket.get("terms"),docket.get("deposit"),docket.get("rep"),
          docket.get("csr"),docket.get("machine_2"),docket.get("proof_2"),docket.get("machine_3"),docket.get("proof_3")] 
    
    path = Path(__file__).parent.resolve()
    
    key = keygen()
    
    copy(path,key)
    
    data_dict = generateDataDict(path,res)
    
    fill(data_dict,path,key)
    
    return str(path)+"\\filled"+key+".pdf"

def copy(path,key):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')

    fileReader = PyPDF2.PdfFileReader(fileRead)
    fileReader.numPages
    fileWriter=PyPDF2.PdfWriter()
    
    for pageNum in range(fileReader.numPages):
        fileReader.getPage(pageNum)
    with open(str(path)+"\\filled"+key+".pdf",'wb') as f:
        fileWriter.write(f)
    fileRead.close()

def generateDataDict(path,res):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')
    data_dict = fillpdfs.get_form_fields(fileRead)
    c = 0
    for i in data_dict:
        data_dict[i] = res[c]
        c+=1
    fileRead.close()
    return data_dict
    

def fill(data_dict,path,key):
    fileRead = open(str(path)+"\\docket_template.pdf",'rb')
    fileWrite = open(str(path)+"\\filled"+key+".pdf",'wb')
    fillpdfs.write_fillable_pdf(fileRead,fileWrite,data_dict,flatten=False)
    fileWrite.close()
    fileRead.close()
    
def keygen():
    p1 = str(random.randint(1,1000))
    p2 = str(random.randint(1,1000))
    key = p1+p2
    return key
