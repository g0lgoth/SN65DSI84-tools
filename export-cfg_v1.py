import os
import xlsxwriter

def read_input(doc):
	with open(doc) as input_list:
	    input_list = input_list.readlines()
	    # j'enlève le saut de page
	    input_list[1] = input_list[1].rstrip("\n")
	    adresses_list = input_list[1].split(" ")
	    input_list[4] = input_list[4].rstrip("\n")
	    values_list = input_list[4].split(" ")	    
	return adresses_list, values_list

# création de l'excel avec la mise en forme spécifique
def excel_creation(general_path):
    # se place au chemin qu'on lui donne 
    excel_directory_move = os.chdir(general_path)
    # 
    wb = xlsxwriter.Workbook('cfg_input.xlsx')
    worksheet = wb.add_worksheet()
    wrap_format = wb.add_format({'text_wrap': True}) # permet de sauter des lignes dans une cellule
    cell_format_title = wb.add_format({'bold': True})
    cell_format_title.set_font_size(13)
    cell_format_title.set_align('center')
    cell_format_title.set_align('vcenter')
    worksheet.set_column('A:A', 40)
    worksheet.write(0,0,"Adress", cell_format_title)
    worksheet.set_column('B:B', 40)
    worksheet.write(0,1,"Values", cell_format_title)
    return wb, worksheet, wrap_format

def writing(value1, value2, wb, worksheet, wrap_format):
    cell_format_folder = wb.add_format({})
    cell_format_folder.set_align('vcenter')
    cell_format_folder.set_align('center')
    cell_format = wb.add_format({})
    x=1
    for i, j in zip(value1, value2):
    	worksheet.write(x, 0, i)
    	worksheet.write(x, 1, j, wrap_format)
    	x += 1
    wb.close()

def main():
	# on obtient le chemin d'où le code est lancé
	general_path = os.path.abspath(os.getcwd())
	input_document="cfg_input.txt"
	adresses_input, values_input = [], []
	adresses_input, values_input = read_input(input_document)
	print(adresses_input,"\n", values_input)
	wb, worksheet, wrap_format = excel_creation(general_path)
	writing(adresses_input, values_input, wb, worksheet, wrap_format)

if __name__ == "__main__":
    main()