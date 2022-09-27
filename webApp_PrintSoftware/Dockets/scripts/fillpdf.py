import fillpdf

def execute():
    
    data_dict = fillpdf.get_form_fields("Print Docket Frontside-090222.pdf")
    print (data_dict)
    

execute()