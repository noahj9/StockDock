import fillpdf
from fillpdf import fillpdfs
from pathlib import Path



def execute():
    path = Path(__file__).parent.resolve()
    file = open(str(path)+"\\docket_template.pdf",'rb')
    data_dict = fillpdfs.get_form_fields(file)
    print (data_dict.keys())
    file.close()
execute()